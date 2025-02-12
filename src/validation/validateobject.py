import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../inf_schema'))


from infschema.objectexist import ObjectExist
from exception.objectexception import ( 
    ObjectDoesNotExist
)


class ValidateObject:
    @staticmethod
    def database_exist(session,database_name):
        if ObjectExist.db_exist(session,db_name= database_name):
            return True
        else:
            raise ObjectDoesNotExist('DATABASE',database_name)
        
    @staticmethod 
    def schema_exist(session,database_name,schema_name):
        if ObjectExist.schema_exist(session,database_name,schema_name):
            return True
        else:
            raise ObjectDoesNotExist('SCHEMA', schema_name)
    
    @staticmethod
    def table_exist(session,database_name,schema_name,table_name):
        if ObjectExist.table_exist(session,database_name,schema_name,table_name):
            return True
        else:
            raise ObjectDoesNotExist('TABLE',table_name)
        
    @staticmethod
    def is_new_database(session,database_name):
        
        


