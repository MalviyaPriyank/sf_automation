import sys 
import os

from snowflake.snowpark.functions import col
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from vars.gvinformationschema import InformationSchema,Table
class Tables:
    def __init__(self,session):
        self.col = Table().columns
        self.session = session

    def is_existing_table(self,db_name,schema_name,table_name):
        df = self.session.table(self.col._view).filter((col(self.col._table_catalog) == db_name) and (col(self.col._table_schema) == schema_name) and (col(self.col._table_name) == table_name))
        res = df.collect()
        if len(res) == 0:
            return False
        elif len(res) > 0:
            return True
        
    def is_new_table(self,db_name,schema_name,table_name):
        df = self.session.table(self.col._view).filter((col(self.col._table_catalog) == db_name) and (col(self.col._table_schema) == schema_name) and (col(self.col._table_name) == table_name))
        res = df.collect()
        if len(res) == 0:
            return True
        elif len(res) > 0:
            return False