import sys
import os

from snowflake.snowpark.functions import col
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from vars.gvinformationschema import InformationSchema,Database,Schema


class NewObject:
    
    def __init__(self,session):
        self.session = session
        self.database_view = InformationSchema._database_view
        self.db_col = Database().columns
        self.schema_view = InformationSchema._schema_view
        self.schema_col = Schema().columns
        self.table_view = InformationSchema._table_view


    
    def is_new_db(self,db_name):
        df = self.session.table(self.database_view).filter(col(self.db_col.database_name) == db_name )
        res = df.collect()
        if len(res) == 0:
            return True
        elif len(res) > 0:
            return False