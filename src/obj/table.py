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


class Session:
    def __get__(self,instance,owner):
        return instance._session
    
    def __set__(self,instance,value):
        instance._session = value
    
    def __delete__(self,instance):
        del instance._session

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

    session = Session()
    database = Database()

    schema = Schema()

    name = Name()

    column_name_list = ColumnNameList()

    column_type_list = ColumnTypeList()

class Table:

    def __init__(self,session,root,user_id,logger):
        self.attr = TableAttrs(self)
        self.attr.session = session 
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


    def read_table_ddl_file(self):
        table_ddl_df = pd.read_csv(self.attr.file_path)
        return table_ddl_df
        
    def get_column_in_a_list(self,column_name):
        return self.attr.table_ddl_df[column_name]
    
    def get_create_table_query(self):
        qry = f"CREATE OR REPLACE TABLE {self.attr.database}.{self.attr.schema}.{self.attr.name} ("

        for i in range(0,len(self.attr.column_name_list)):
            if i != len(self.attr.column_name_list) -1:
                qry = qry + f' "{self.attr.column_name_list[i]}" {self.attr.column_type_list[i]}, '
            else: 
                qry = qry + f' "{self.attr.column_name_list[i]}" {self.attr.column_type_list[i]} '

        qry = qry + " ) "
        return qry

    def create_table(self):
        self.qry = self.get_create_table_query()
        self.attr.session.sql(self.qry).collect()

    def grant_default_privileges(self):
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges[self.__class__.__name__.upper()]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = self.__class__.__name__.upper(),object_identifier=self.qualified_name,role = role)

    def create_table_using_files_from_stage(self,database,schema):
        self.set_database(database)
        self.set_schema(schema)
        stg = Stage(self.root,gv._config_database,gv._config_schema)
        stg.set_stage(gv._config_stage)
        stg.set_stage_reference()
        file_lst = stg.get_list_of_files_from_stage()
        file_lst = [file for file in file_lst if f"{self.attr.database}/{self.attr.schema}" in file]
        for files in file_lst:
            files = stg.remove_stage_name_from_file_path(files)
            stg.download_file_from_stage(files,"./")

        tbl_lst = []
        for files in file_lst:
            files = files.split("/")[-1]
            tbl_lst.append(files.split('.')[0])
            self.set_name(files.split('.')[0])
            tbl_ddl_data = pd.read_csv(f"{files}")
            self.set_column_name_list(tbl_ddl_data)
            self.set_column_type_list(tbl_ddl_data)
            self.logger.info(f"creating table {self.attr.name}")
            self.set_qualified_name()
            self.create_table()
            self.create_deployment_entry()
        return tbl_lst
    

    def create_deployment_entry(self):
        deploy_inst = Deploy(self.attr.session)
        self.logger.info(f"Tracking for deployment table object : {self.attr.name}")
        deploy_inst.insert_into_deployment_script_table(self.qry,self.user_id)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database(self.attr.database)
        deploy_inst.set_object_schema(self.attr.schema)
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(gv._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()
