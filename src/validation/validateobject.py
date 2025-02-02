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
    def __init__(self):
        self.database_tag = 'DATABASE'
        self.schema_tag = 'SCHEMA'


    @classmethod
    def object_exist(self,**kwargs):
        if kwargs['OBJECT_TYPE'] == self.database_tag:
            if Databases.db_exist(db_name= kwargs[self.database_tag]):
                return True
            else:
                raise ObjectDoesNotExist(self.database_tag,kwargs[self.database_tag])
        elif kwargs['OBJECT_TYPE'] == self.schema_tag:
            if Schema.schema_exist(db_name= kwargs[self.database_tag], schema_name= kwargs[self.schema_tag]):
                return True
            else:
                raise ObjectDoesNotExist(self.schema_tag,kwargs[self.schema_tag])
