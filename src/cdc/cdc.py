import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from src.vars.cdc.gvcdc import CdcMSSqlServer as mssql
from datetime import datetime

class CDC:
    def __init__(self,session,logger):
        self.session=session
        self.logger=logger.getChild(self.__class__.__name__)
    
    def __insert_new_record(self,table,object_name,database_name,lsn):
        current_time=datetime.now()
        qry=f"""
        INSERT
        INTO 
        {table}
        values(
            '{object_name}',
            '{database_name}',
            '{lsn}',
            '{current_time}'
        )
        """
        self.logger.info(f" executing  : {qry}")
        self.session.sql(qry).collect()
        self.logger.info(f"CDC Operation logged successfully")
    
    def log_cdc(self,server,**kwargs):
        if server =='MSSQL':
            self.logger.info(f" logging CDC for MSSQL")
            ddl_dtls=mssql()
            table=ddl_dtls._table
            self.logger.info(f" table : {table}")
            object_name=kwargs['OBJECT']
            self.logger.info(f" OBJECT : {object_name}")
            database=kwargs['DATABASE']
            self.logger.info(f" DATABASE : {database}")
            lsn=kwargs['LSN']
            self.logger.info(f" LSN : {lsn}")
            self.__insert_new_record(
                table=table,
                object_name=object_name,
                database_name=database,
                lsn=lsn
            )

    def get_latest_identifier(self,server,object_name,database_name):
        if server=='MSSQL':
            ddl_dtls=mssql()
            qry=f"""
            SELECT
            TOP 1
            {ddl_dtls.attr._lsn}
            from 
            {ddl_dtls._table}
            WHERE
            {ddl_dtls.attr._database_name}='{database_name}'
            and
            {ddl_dtls.attr._object_name}='{object_name}'
            ORDER BY 
            {ddl_dtls.attr._load_timestamp} DESC
            """
            self.logger.info(f" Getting last cdc details of {object_name} in {database_name} for {server} ")
            self.logger.info(f" qry : {qry}")
            res=self.session.sql(qry).collect()
            lst=[item for sublist in res for item in sublist]
            self.logger.info(f" LST : {lst}")
            return lst
            
            
