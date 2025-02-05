from snowflake.snowpark.functions import col

class Table:
    def __init__(self,session):
        self.view = "INFORMATION_SCHEMA.TABLE"
        self.session = session

    def table_exist(self,db_name,schema_name,table_name):
        df = self.session.table(self.view).filter((col("table_catalog") == db_name) and (col("table_schema") == schema_name) and (col("table_name") == table_name))
        res = df.collect()
        if len(res) == 0:
            return False
        elif len(res) > 0:
            return True