import pyodbc
import pandas as pd
from src.exception.operationexception import NoCDCRecordsFound

OPERATION_MAP = {
    1: "DELETE",
    2: "INSERT",
    3: "UPDATE_BEFORE",
    4: "UPDATE_AFTER"
}
class SqlServerOperations:
    def __init__(self,logger,connection):
        self.conn=connection
        self.logger=logger.getChild(self.__class__.__name__)
        self.cursor=connection.cursor()

    def __execute_query_and_get_result(self,qry,**kwargs):
        if 'DATABASE' in kwargs:
            db_name=kwargs['DATABASE']
            self.cursor.execute(qry,(db_name),)
        elif 'FROM_LSN' in kwargs:
            from_lsn=kwargs['FROM_LSN']
            to_lsn=kwargs['TO_LSN']
            self.logger.info(f"FROM_LSN : {from_lsn}")
            self.cursor.execute(qry,from_lsn,to_lsn)
            rows = self.cursor.fetchall()
            columns=[col[0] for col in self.cursor.description]
            return rows,columns
        else:
            self.cursor.execute(qry)
        result=self.cursor.fetchone()
        return result
    
    def __execute_query_and_commit(self,qry):
        self.cursor.execute(qry)
        self.cursor.commit()

    def __get_capture_instance_of_a_table(self,table):
        qry=f"""
        SELECT 
        capture_instance
        FROM 
        cdc.change_tables
        WHERE
        source_object_id = OBJECT_ID('{table}');
        """
        res=self.__execute_query_and_get_result(qry=qry)
        return res[0]
    
    def __get_minimum_lsn_of_table(self,table):
        capture_instance=self.__get_capture_instance_of_a_table(table)
        qry=f"""
        SELECT 
        sys.fn_cdc_get_min_lsn('{capture_instance}')
        """
        res=self.__execute_query_and_get_result(qry=qry)
        return res[0]
    
    def __get_current_lsn(self):
        qry=f"""
        SELECT
        sys.fn_cdc_map_time_to_lsn('largest less than or equal', GETDATE())
        """
        res=self.__execute_query_and_get_result(qry=qry)
        return res[0]
    
    def __use_database(self,db):
        qry=f"USE {db};"
        self.__execute_query_and_commit(qry=qry)
    
    def get_incremental_data(self,table_name,**kwargs):
        if 'FROM_LSN' in kwargs:
            self.logger.info(f" CDC Record exist , last LSN recorded : {kwargs['FROM_LSN']}")
            from_lsn=kwargs['FROM_LSN']
            from_lsn = SqlServerOperations.convert_to_binary(from_lsn)
        else:
            self.logger.info(f"first time CDC getting minimum LSN of {table_name}")
            from_lsn=self.__get_minimum_lsn_of_table(table=table_name)
        to_lsn=self.__get_current_lsn()
        self.logger.info("after current_lsn")
        capture_instance=self.__get_capture_instance_of_a_table(table=table_name)
        qry=f"""
        SELECT
        *
        FROM
        cdc.fn_cdc_get_all_changes_{capture_instance}(?, ?, 'all')
        ORDER BY __$start_lsn, __$seqval
        """
        self.logger.info("sending qry for execution")
        res,columns=self.__execute_query_and_get_result(qry=qry,**{'FROM_LSN':from_lsn,'TO_LSN':to_lsn})
        self.logger.info(f" incremental records : {res}")
        if len(res)==0:
            raise NoCDCRecordsFound(server='MSSQL',object_name={table_name})
        else:
            records = [dict(zip(columns, row)) for row in res]
            df = pd.DataFrame(records)
            df["operation"] = df["__$operation"].map(OPERATION_MAP)
            return df,from_lsn,to_lsn
    
    @staticmethod
    def convert_to_binary(val):
        return bytes.fromhex(val)


    def enable_cdc_on_database(self,db):
        self.logger.info(f"Enabling CDC on {db}")
        self.__use_database(db)
        cdc_query="EXEC sys.sp_cdc_enable_db;"
        self.__execute_query_and_commit(qry=cdc_query)
        self.logger.info(f"CDC Enabled succesfully")
        return f"CDC Enabled successfully on {db} database."
    
class SqlServerConnection:
    def __init__(self,logger):
        self.logger=logger.getChild(self.__class__.__name__)

    def __connect_to_database(self):
        connection_string = (
            "Driver={ODBC Driver 18 for SQL Server};"
            "Server=tcp:gyrusdev.database.windows.net,1433;"
            "Database=GyrusExperiment;"
            "Uid=priyank;"
            "Pwd=GyrusDev@0522;"
            "Encrypt=yes;"
            "TrustServerCertificate=no;"
            "Connection Timeout=30;"
        )
        conn=pyodbc.connect(connection_string)
        self.logger.info("SQL Server connection successful")
        return conn
    
    def get_sql_server_connection(self):
        return self.__connect_to_database()
    
'''
Sample queyr for CDC
DECLARE @from_lsn binary(10);
DECLARE @to_lsn   binary(10);

-- Get min LSN for the capture instance (usually dbo_customer)
SET @from_lsn = sys.fn_cdc_get_min_lsn('dbo_customer');

-- Get current maximum LSN as of now
SET @to_lsn = sys.fn_cdc_map_time_to_lsn('largest less than or equal', GETDATE());

SELECT
    *
FROM
    cdc.fn_cdc_get_all_changes_dbo_customer(@from_lsn, @to_lsn, 'all')
ORDER BY 
    __$start_lsn,
    __$seqval;

'''
    

    



    