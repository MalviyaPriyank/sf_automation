import sys
import os 

import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../processing'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))

from vars.gvobject import Config as cfg,Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from processing.stage import Stage
from dep.deploy import Deploy
from setup import privilege
from vars.base.basedatatypes import DataTypes
from .baseobj import BaseObject 


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

class Table(BaseObject):

    def __init__(self,session,root,user_id,logger):
        super().__init__(session=session,user_id=user_id,logger=logger)
        self.attr = TableAttrs(self)
        self.root = root

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

    def read_table_ddl_file(self):
        table_ddl_df = pd.read_csv(self.attr.file_path)
        return table_ddl_df
        
    def get_column_in_a_list(self,column_name):
        return self.attr.table_ddl_df[column_name]
    
    def get_create_table_query(self):
        qry = f"CREATE OR REPLACE TABLE {self.attr.database}.{self.attr.schema}.{self.attr.name} ("

        for i in range(0,len(self.attr.column_name_list)):
            if i != len(self.attr.column_name_list) -1:
                qry = qry + f' {self.attr.column_name_list[i]} {self.attr.column_type_list[i]}, '
            else: 
                qry = qry + f' {self.attr.column_name_list[i]} {self.attr.column_type_list[i]} '

        qry = qry + " ) "
        return qry

    def create_table(self):
        self.qry = self.get_create_table_query()
        self.session.sql(self.qry).collect()

    def grant_default_privileges(self):
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges[self.__class__.__name__.upper()]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = self.__class__.__name__.upper(),object_identifier=self.qualified_name,role = role)

    def create_table_using_files_from_stage(self,database,schema,filelist=[]):
        self.set_database(database)
        self.set_schema(schema)
        #stg = Stage(self.root,cfg._config_database,cfg._config_schema)
        #stg.set_stage(cfg._config_stage)
        #stg.set_stage_reference()
        self.logger.info('inside function')
        # file_lst = stg.get_list_of_files_from_stage()
        # self.logger.info(f'filelist received: {filelist}')
        # if filelist != []: 
        #    file_lst = [file for file in file_lst if any(file.endswith(f"{self.attr.database}/{self.attr.schema}/{inputs}") for inputs in filelist)]
        #    self.logger.info(f'filelist provided, postprocess: {file_lst}')
        # else: 
        #    file_lst = [file for file in file_lst if f"{self.attr.database}/{self.attr.schema}" in file]
        #    self.logger.info(f'filelist not provided, postprocess: {file_lst}')
            
        # for files in file_lst:
        #    files = stg.remove_stage_name_from_file_path(files)
        #    stg.download_file_from_stage(files,"tmp/")

        tbl_lst = []
        self.logger.info(f"following files in tmp {os.listdir('tmp/')}")
        for files in os.listdir('tmp/'): #file_lst:
            if files.endswith('.csv'):
                self.logger.info(f"inside file iteration for {files}")            
                #files = files.split("/")[-1]
                tbl_lst.append(files.split('.')[0])
                self.set_name(files.split('.')[0])
                tbl_ddl_data = pd.read_csv(f"tmp/{files}")
                self.logger.info("after reading file")
                self.set_column_name_list(tbl_ddl_data)
                self.set_column_type_list(tbl_ddl_data)
                #vv.is_valid_column_types(object_name=self.__class__.__name__,attribute_name='Column Type',tbl_data_typ_lst=self.attr.column_type_list,allowed_data_type_lst=DataTypes.get_allowed_data_types())
                self.logger.info(f"creating table {self.attr.name}")
                self.set_qualified_name()
                self.create_table()
                self.grant_default_privileges()
                self.create_deployment_entry(object_name=self.attr.name,object_type=self.__class__.__name__,object_database=self.attr.database,object_schema=self.attr.schema)
                self.write_file_to_git(object_name=files,object_type=self.__class__.__name__,object_database=self.attr.database,object_schema=self.attr.schema)

    def create_table_using_query(self,database,schema,table,qry):
        self.logger.info("set database")
        self.set_database(database=database)

        self.logger.info("set schema")
        self.set_schema(schema=schema)
        
        self.logger.info(f"switch to database {self.attr.database}")
        self.session.sql(f"USE DATABASE {self.attr.database}").collect()

        self.logger.info(f"switch to schema {self.attr.schema}")
        self.session.sql(f"USE SCHEMA {self.attr.schema}").collect()

        self.logger.info(f" Query : {qry}")
        self.session.sql(qry).collect()
        self.create_deployment_entry(object_name=self.attr.name,object_type=self.__class__.__name__,object_database=self.attr.database,object_schema=self.attr.schema)
        self.write_file_to_git(object_name=table,object_type=self.__class__.__name__,object_database=self.attr.database,object_schema=self.attr.schema)

