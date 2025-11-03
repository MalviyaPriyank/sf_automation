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
from vars.obj.table.gvtable import Table as tags


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
        return (instance._name,instance._rename_to)

    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_database(session=instance.parent.session, database_name=name)
            if ( vv.starts_with_alphabet(name,instance.parent.__class__.__name__,self.__class__.__name__) 
                and not vv.has_space(name,instance.parent.__class__.__name__,self.__class__.__name__)
                and not vv.has_special_characters_except_underscore(name,instance.parent.__class__.__name__,self.__class__.__name__)
                ):
                instance._name = name
                instance._rename_to="NONE"
        else:
            instance.parent.logger.info(f" for alter operation")
            old_name=value["NAME"]
            instance.parent.logger.info(f"old name {old_name}")
            new_name=value.get("RENAME_TO","NONE")
            instance.parent.logger.info(f"new name {new_name}")
            if new_name!="NONE":
                instance.parent.logger.info(f" changing name from {old_name} to {new_name}")
                vv.required_attribute_check(old_name,instance.parent.__class__.__name__,self.__class__.__name__)
                vo.database_exist(session=instance.parent.session,database_name=old_name)
                vo.is_new_database(session=instance.parent.session,database_name=new_name)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to

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

    def __init__(self,session,user_id,logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session=session,user_id=user_id,logger=logger)
        self.attr = TableAttrs(self)

    def set_database(self,database):
        self.attr.database = database

    def set_schema(self,schema):
        self.attr.schema = schema

    def set_name(self,name):
        self.attr.name = name

    def set_qualified_name(self):
        self.qualified_name=f"{self.attr.database}.{self.attr.schema}.{self.attr.name[0]}"

    def set_column_name_list(self,value):
        self.attr.column_name_list = value

    def set_column_type_list(self,value):
        self.attr.column_type_list = value

    def read_table_ddl_file(self):
        table_ddl_df = pd.read_csv(self.attr.file_path)
        return table_ddl_df

    
    def get_create_table_query(self):
        self.qry = f"CREATE OR REPLACE TABLE {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} ("

        for i in range(0,len(self.attr.column_name_list)):
            if i != len(self.attr.column_name_list) -1:
                self.qry = self.qry + f' {self.attr.column_name_list[i]} {self.attr.column_type_list[i]}, '
            else: 
                self.qry = self.qry + f' {self.attr.column_name_list[i]} {self.attr.column_type_list[i]} '

        self.qry = self.qry + " ) "
        return self.qry

    def create_table(self):
        self.qry = self.get_create_table_query()
        self.session.sql(self.qry).collect()

    def grant_default_privileges(self):
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges[self.__class__.__name__.upper()]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = self.__class__.__name__.upper(),object_identifier=self.qualified_name,role = role)

    def create_table_using_files_from_stage(self):
        #self,database,schema,filelist=[]
        self.set_database('MY_DEV_DB')
        self.set_schema('MY_SCHEMA')
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
                #self.grant_default_privileges()
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
        self.create_deployment_entry(object_name=table,object_type=self.__class__.__name__,object_database=self.attr.database,object_schema=self.attr.schema)
        self.write_file_to_git(object_name=table,object_type=self.__class__.__name__,object_database=self.attr.database,object_schema=self.attr.schema)



class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        obj_inst=Table(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info("set database")
        if tags.DATABASE in kwargs.keys():
            obj_inst.set_database(kwargs[tags.DATABASE])
        else:
            obj_inst.set_database(kwargs[tags.DATABASE])

        logger.info("set schema")
        if tags.DATABASE in kwargs.keys():
            obj_inst.set_schema(kwargs[tags.SCHEMA])
        else:
            obj_inst.set_schema(kwargs[tags.SCHEMA])

        logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name(kwargs[tags.NAME])

        logger.info("set column")
        if tags.COLUMNS_LIST in kwargs.keys():
            obj_inst.set_column_name_list(kwargs[tags.COLUMNS_LIST])
        else:
            obj_inst.set_column_name_list("NONE")

        logger.info("set data types")
        if tags.DATA_TYPES in kwargs.keys():
            obj_inst.set_column_type_list(kwargs[tags.DATA_TYPES])
        else:
            obj_inst.set_column_type_list("NONE")

        obj_inst.set_qualified_name()
        obj_inst.get_create_table_query()
        obj_inst.session.sql(obj_inst.qry).collect()
        obj_inst.create_deployment_entry(object_name=obj_inst.attr.name[0],
                                         object_type=obj_inst.__class__.__name__,
                                         object_database=obj_inst.attr.database,
                                         object_schema=obj_inst.attr.schema)
        obj_inst.write_file_to_git(object_name=obj_inst.attr.name[0],
                                         object_type=obj_inst.__class__.__name__,
                                         object_database=obj_inst.attr.database,
                                         object_schema=obj_inst.attr.schema)


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
