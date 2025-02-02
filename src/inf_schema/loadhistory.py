
import sys
import os

from snowflake.snowpark.functions import col
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))

from validation.validateobject import ValidateObject


class LoadHistory:
    def __init__(self,session):
        self.view = "INFORMATION_SCHEMA.LOAD_HISTORY"
        self.session = session

    def get_load_status_of_table(self,database_name,schema_name,table_name):
        if ValidateObject.schema_exist(database_name=database_name,schema_name=schema_name):
            df = self.session.table(self.view).filter((col("schema_name") == schema_name) and (col("table_name") == table_name )).select(col("status"))
            res = df.collect()
            return res[0][0]
        

    

