from snowflake.snowpark.functions import col

class ObjectExist:
    
    def __init__(self,session):
        self.session = session
        self.database_view = "INFORMATION_SCHEMA.DATABASES"
        self.schema_view = "INFORMATION_SCHEMA.SCHEMATA"
        self.table_view = "INFORMATION_SCHEMA.TABLE"


    
    def db_exist(self,db_name):
        df = self.session.table(self.database_view).filter(col("database_name") == db_name )
        res = df.collect()
        if len(res) == 0:
            return False
        elif len(res) > 0:
            return True
        
    def schema_exist(self,db_name,schema_name):
        if self.db_exist(db_name):
            df = self.session.table(self.schema_view).filter((col("catalog_name") == db_name) and (col("schema_name") == schema_name))
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
            if le