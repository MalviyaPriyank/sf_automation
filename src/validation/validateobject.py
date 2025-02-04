import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../inf_schema'))


from inf_schema.databases import Databases
from inf_schema.schemata import Schema
from exception.objectexception import ( 
    ObjectDoesNotExist
)


class ValidateObject:
    @staticmethod
    def database_exist(self,database_name):
        if Databases.db_exist(db_name= database_name):
            return True
        else:
            raise ObjectDoesNotExist('DATABASE',database_name)
        
    @staticmethod 
    def schema_exist(self,database_name,schema_name):
        if Schema.schema_exist(database_name,schema_name):
            return True
        else:
            raise ObjectDoesNotExist('SCHEMA', schema_name)
