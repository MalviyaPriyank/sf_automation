
from snowflake.snowpark.functions import col

class LoadHistory:
    def __init__(self,session):
        self.view = "INFORMATION_SCHEMA.LOAD_HISTORY"
        self.session = session

    def get_load_status_of_table(self,schema_name,table_name):
        df = self.session.table(self.view).filter((col("schema_name") == schema_name) and (col("table_name") == table_name )).select(col("status"))
        res = df.collect()
        return res[0][0]

