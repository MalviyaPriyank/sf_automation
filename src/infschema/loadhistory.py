
import sys
import os

from snowflake.snowpark.functions import col
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))

from validation.validateobject import ValidateObject as vo
from validation.validatevalue import ValidateValue as vv


class Database:
    def __get__(self,instance,owner):
        return instance._database

    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if vo.database_exist(database_name=value):
            instance._database = value

    def __delete__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema

    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if vo.schema_exist(instance._database,schema_name=value):
            instance._schema = value

    def __delete__(self,instance):
        del instance._schema

class LoadHistoryAttr:
    database = Database()
    schema = Schema()



class LoadHistory:
    def __init__(self,session):
        self.view = "INFORMATION_SCHEMA.LOAD_HISTORY"
        self.attr = LoadHistoryAttr()
        self.session = session

    def set_database(self,value):
        self.attr.database = value

    def set_schema(self,value):
        self.attr.schema = value

    def get_load_status_of_table(self,database_name,schema_name,table_name):
        self.set_database(database_name)
        self.set_schema(schema_name)
        df = self.session.table(self.view).filter((col("schema_name") == schema_name.upper()) and (col("table_name") == table_name.upper())).select(col("status"))
        res = df.collect()
        return res[0][0]