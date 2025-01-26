import sys
import os 
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../processing'))

#from global_vars import Table as gv
from validatevalue import ValidateValue as vv
from session import Session
from stage import Stage


class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
        else:
            instance._database = value

    def __delete__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
        else:
            instance._schema = value

    def __delete__(self,instance):
        del instance._schema

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
        else:
            instance._name = value

    def __delete__(self,instance):
        del instance._name

class TableType:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
        else:
            instance._name = value

    def __delete__(self,instance):
        del instance._name


class FilePath:
    def __get__(self,instance,owner):
        return instance._file_path
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
        else:
            instance._file_path = value

    def __delete__(self,instance):
        del instance._file_path

class TableDf:
    def __get__(self,instance,owner):
        return instance._table_ddl_df
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
        else:
            instance._table_ddl_df = value

    def __delete__(self,instance):
        del instance._table_ddl_df

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

    database = Database()

    schema = Schema()

    name = Name()

    table_type = TableType()

    file_path = FilePath()

    table_ddl_df = TableDf()

    column_name_list = ColumnNameList()

    column_type_list = ColumnTypeList()

class Table:

    def __init__(self,session):
        self.attr = TableAttrs()
        self.session = session 

    def set_database(self,database):
        self.attr.database = database

    def set_schema(self,schema):
        self.attr.schema = schema

    def set_name(self,name):
        self.attr.name = name

    def set_file_path(self,file_path):
        self.attr.file_path = file_path

    def set_table_ddl_df(self,table_ddl_df):
        self.attr.table_ddl_df = table_ddl_df

    def set_column_name_list(self):
        self.attr.column_name_list = self.get_column_in_a_list('COLUMN_NAME')

    def set_column_type_list(self):
        self.attr.column_type_list = self.get_column_in_a_list('COLUMN_TYPE')


    def read_table_ddl_file(self):
        table_ddl_df = pd.read_csv(self.attr.file_path)
        return table_ddl_df
        
    def get_column_in_a_list(self,column_name):
        return self.attr.table_ddl_df[column_name]
    
    def get_create_table_query(self):
        qry = f"CREATE TABLE {self.attr.database}.{self.attr.schema}.{self.attr.name} ("

        for i in range(0,len(self.attr.column_name_list)):
            qry = qry + f" {self.attr.column_name_list[i]} {self.attr.column_type_list[i]} "

        qry = qry + " ) "

    def create_table(self):
        qry = self.get_create_table_query()
        self.session.execute_qry(qry)


    def create_table_using_files_from_stage(root,database,schema):
        tbl = Table()
        tbl.set_database(database)
        tbl.set_schema(schema)
        stg = Stage(root,"DB_CONFIG","SCH_CONFIG")
        stg.set_stage('STG_INT_CONFIG')
        stg.set_stage_reference()
        file_lst = stg.get_list_of_files_from_stage()
        for files in file_lst:
            files = stg.remove_stage_name_from_file_path(files)
            stg.download_file_from_stage(files,"./DDL/")
        
        for files in file_lst:
            tbl_file = pd.read_csv(f"./DDL/{files}")


    def create_object(session,**kwargs):
        tbl = Table()
    
        session.get_root_object()
        
        tbl.set_database(kwargs['database'])

        tbl.set_schema(kwargs['schema'])

        tbl.set_name(kwargs['name'])

        tbl.set_file_path(kwargs['file_path'])

        table_ddl_df = tbl.read_table_ddl_file()
        tbl.set_table_ddl_df(table_ddl_df)

        tbl.set_column_name_list()

        tbl.set_column_type_list()

        tbl.create_table()

        
