from snowflake.snowpark.functions import col
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from vars.gvinformationschema import Schema

class Schemata:
    def __init__(self,session):
        self.col = Schema().columns
        self.session = session

    def is_existing_schema(self,db_name,schema_name):
        df = self.session.table(self.col._view).filter((col(self.col.catalog_name) == db_name) and (col(self.col.schema_name) == schema_name))
        res = df.collect()
        if len(res) == 0:
            return False
        elif len(res) > 0:
            return True
        
    def is_new_schema(self,db_name,schema_name):
        df = self.session.table(self.col._view).filter((col(self.col.catalog_name) == db_name) and (col(self.col.schema_name) == schema_name))
        res = df.collect()
        if len(res) == 0:
            return True
        elif len(res) > 0:
            return False
