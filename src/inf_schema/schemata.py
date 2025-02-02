import sys
import os

from snowflake.snowpark.functions import col
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))

from validation.validateobject import ValidateObject

class Schema:
    def __init__(self,session):
        self.view = "INFORMATION_SCHEMA.SCHEMATA"
        self.session = session

    def schema_exist(self,db_name,schema_name):
        if ValidateObject.database_exist(db_name):
            df = self.session.table(self.view).filter((col("catalog_name") == db_name) and (col("schema_name") == schema_name))
            res = df.collect()
            if len(res) == 0:
                return False
            elif len(res) > 0:
                return True
    
