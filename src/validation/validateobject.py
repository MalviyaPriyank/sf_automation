import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../inf_schema'))

from inf_schema.databases import Databases

from exception.objectexception import ( 
    ObjectDoesNotExist
)


class ValidateObject:
    def __init__(self):
        pass


    @staticmethod
    def database_exist(self,db_name):
        if Databases.db_exist(db_name= db_name):
            return True
        else:
            raise ObjectDoesNotExist('DATABASE',db_name)
