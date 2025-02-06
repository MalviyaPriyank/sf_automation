from snowflake.snowpark.functions import col
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from vars.gvinformationschema import InformationSchema,Database,Schema


class ObjectExist:
    
    def __init__(self,session):
        self.session = session
        self.database_view = InformationSchema._database_view
        self.db_col = Database().columns
        self.schema_view = InformationSchema._schema_view
        self.schema_col = Schema().columns
        self.table_view = InformationSchema._table_view


    
    def db_exist(self,db_name):
        df = self.session.table(self.database_view).filter(col(self.db_col.database_name) == db_name )
        res = df.collect()
        if len(res) == 0:
            return False
        elif len(res) > 0:
            return True
        
    def schema_exist(self,db_name,schema_name):
        if self.db_exist(db_name):
            df = self.session.table(self.schema_view).filter((col(self.schema_col.catalog_name) == db_name) and (col(self.schema_col.schema_name) == schema_name))
            res = df.collect()
            if len(res) == 0:
                return False
            elif len(res) > 0:
                return True
        else:
            return False
        
    def table_exist(self,db_name,schema_name,table_name):
        if self.schema_exist(db_name= db_name, schema_name= schema_name):
            df = self.session.table(self.table_view).filter((col("table_catalog") == db_name) and (col("table_schema") == schema_name) and (col("table_name") == table_name))
            res = df.collect()
            if len(res) == 0:
                return False
            elif len(res) > 0:
                return True
        else:
            return False