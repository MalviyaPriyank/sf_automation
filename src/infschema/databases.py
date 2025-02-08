from snowflake.snowpark.functions import col
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from vars.gvinformationschema import InformationSchema,Database

class Databases:
    def __init__(self,session):
        self.view = InformationSchema._database_view
        self.col = Database().columns
        self.session = session


    def get_owner_of_db(self,db_name):
        df = self.session.table(self.view).filter(col(self.col.name) == f'{db_name}').select(col(self.col.database_owner))
        res = df.collect()
        return res[0][0]
    
    def get_type_of_db(self,db_name):
        df = self.session.table(self.view).filter(col(self.col.name) == f'{db_name}').select(col(self.col.type))
        res = df.collect()
        return res[0][0]
    
    def get_retention_time_of_db(self,db_name):
        df = self.session.table(self.view).filter(col(self.col.name) == f'{db_name}').select(col(self.col.retention_time))
        res = df.collect()
        return res[0][0]
    