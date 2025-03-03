import sys
import os 
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__),'../../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../processing'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../deploy'))

from vars.gvobject import Config as cfg,Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from processing.stage import Stage
from dep.deploy import Deploy
from setup import privilege

class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        #if vo.database_exist(value):
        instance._database  = value

    def __delete__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        #if vo.schema_exist(instance._database,value):
        instance._schema = value

    def __delete__(self,instance):
        del instance._schema

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)        
        instance._name = value

    def __delete__(self,instance):
        del instance._name

class ColumnNameList:
    def __get__(self,instance,owner):
        return instance._column_name_list
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
        else:
            instance._column_name_list = value

    def __delete__(self,instance):
        del instance._column_name_list

class ColumnTypeList:
    def __get__(self,instance,owner):
        return instance._column_type_list
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
        else:
            instance._column_type_list = value

    def __delete__(self,instance):
        del instance._column_type_list


class TableAttrs:
    def __init__(self,parent):
        self.parent = parent

    database = Database()

    schema = Schema()

    name = Name()

    column_name_list = ColumnNameList()

    column_type_list = ColumnTypeList()

class BaseTable:
    def __init__(self,session,root,user_id,logger):
        self.attr = TableAttrs(self)
        self.session = session 
        self.root = root
        self.user_id = user_id
        self.logger = logger

    def set_database(self,database):
        self.attr.database = database

    def set_schema(self,schema):
        self.attr.schema = schema

    def set_name(self,name):
        self.attr.name = name

    def set_qualified_name(self):
        self.qualified_name=f"{self.attr.database}.{self.attr.schema}.{self.attr.name}"

    def set_column_name_list(self,ddl_df):
        self.attr.column_name_list = ddl_df["Column_Name"].to_list()

    def set_column_type_list(self,ddl_df):
        self.attr.column_type_list = ddl_df["Column_Type"].to_list()
