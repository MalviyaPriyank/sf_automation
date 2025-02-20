import sys 
import os

from snowflake.snowpark.functions import col
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from vars.gvinformationschema import Database

class Databases:
    def __init__(self,session):
        self.col = Database().columns
        self.session = session

    def use_database(self,db_name):
        self.session.sql(f'USE DATABASE {db_name}').collect()

    def get_database_owner(self,db_name):
        self.use_database('DB_CONFIG')
        df = self.session.table(self.col._view).filter(col(self.col.database_name) == f'{db_name}').select(col(self.col.database_owner))
        res = df.collect()
        return res[0][0]
    
    def get_created(self,db_name):
        self.use_database('DB_CONFIG')
        df = self.session.table(self.col._view).filter(col(self.col.database_name) == f'{db_name}').select(col(self.col.created))
        res = df.collect()
        return res[0][0]
    
    def get_type_of_db(self,db_name):
        self.use_database('DB_CONFIG')
        df = self.session.table(self.col._view).filter(col(self.col.database_name) == f'{db_name}').select(col(self.col.type))
        res = df.collect()
        return res[0][0]
    
    def get_retention_time_of_db(self,db_name):
        self.use_database('DB_CONFIG')
        df = self.session.table(self.col._view).filter(col(self.col.database_name) == f'{db_name}').select(col(self.col.retention_time))
        res = df.collect()
        return res[0][0]
    
    def is_existing_database(self,db_name):
        self.use_database('DB_CONFIG')
        df = self.session.table(self.col._view).filter(col(self.col.database_name) == f'{db_name}'.upper())
        res = df.collect()

        if len(res) == 0:
            return False
        elif len(res) > 0:
            return True
        
    def is_new_database(self,db_name):
        self.use_database('DB_CONFIG')
        df = self.session.table(self.col._view).filter(col(self.col.database_name) == f'{db_name}'.upper())
        res = df.collect()
        if len(res) == 0:
            return True
        elif len(res) > 0:
            return False