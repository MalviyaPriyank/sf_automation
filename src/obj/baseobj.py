from abc import ABC,abstractmethod
import sys
import os 
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../git'))

from dep import deploy
from vars.gvobject import Config as cfg
from repository import Repository   
from src.validation.validateobject import ValidateObject as vo
from src.validation.validatevalue import ValidateValue as vv
from src.vars.base.basetag import BaseTag as tags

class AbstractObject(ABC):
    def __init__(self,session,user_id,logger,database_required,schema_required):
        self.session=session
        self.user_id=user_id
        self.logger=logger
        self.database_required=database_required
        self.schema_required=schema_required
        self.qry=""

    @abstractmethod
    def execute_final_query(self):
        pass


class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        if instance.parent.database_required == True:
            vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.database_exist(session=instance.parent.session, database_name=value)
            instance._database = value
        else:
            instance._database='NA'
    
    def __delete__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        if instance.parent.schema_required==True:
            vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.schema_exist(session=instance.parent.session, database_name=instance._database, schema_name=value)
            instance._schema = value
        else:
            instance._schema='NA'

    def __del__(self,instance):
        del instance._schema

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._comment


class BaseAttrs:
    def __init__(self,parent):
        self.parent=parent
    database=Database()
    schema=Schema()
    comment=Comment()

class BaseObject(AbstractObject):
    def __init__(self, session, user_id, logger,database_required,schema_required):
        super().__init__(
            session = session,
            user_id = user_id, 
            logger = logger,
            database_required=database_required,
            schema_required=schema_required
        )
        self.attr=BaseAttrs(self)
    def execute_final_query(self,**kwargs):
        self.logger.info(f" dictionary passed {kwargs}")
        if 'DATABASE' in kwargs.keys():
            self.session.sql(f"USE DATABASE {kwargs['DATABASE']}").collect()
            if 'SCHEMA' in kwargs.keys():
                self.session.sql(f"USE SCHEMA {kwargs['SCHEMA']}").collect()
        
        self.session.sql(self.qry).collect()

    def run_query(self,qry):
        self.session.sql(qry).collect()

    def set_base_attributes(self,kwargs):
        self.logger.info("Setting base attributes")

        
        self.is_create=kwargs[tags.IS_CREATE]
        
        if tags.DATABASE in kwargs.keys():
            self.set_database(kwargs[tags.DATABASE])
            self.logger.info(f"setting database for {self.__class__.__name__}")
            if self.__class__.__name__.upper()=='NETWORKRULE':
                self.run_query(qry=f"USE DATABASE {kwargs[tags.DATABASE]}")
        else:
            self.set_database('NA')
        self.logger.info(f"DATABASE : {self.attr.database}")

        if tags.SCHEMA in kwargs.keys():
            self.set_schema(kwargs[tags.SCHEMA])
            if self.__class__.__name__.upper()=='NETWORKRULE':
                self.run_query(qry=f"USE SCHEMA {kwargs[tags.SCHEMA]}")
        else:
            self.set_schema('NA')
        self.logger.info(f"SCHEMA : {self.attr.schema}")

        if tags.COMMENT in kwargs.keys():
            self.set_comment(kwargs[tags.COMMENT])
        else:
            self.set_comment('NONE')
        self.logger.info(f"COMMENT : {self.attr.comment}")

    def set_database(self,val):
        self.attr.database=val
    
    def set_schema(self,val):
        self.attr.schema=val

    def set_comment(self,val):
        self.attr.comment=val
    
    def print_query(self):
        self.logger.info(f" Query : {self.qry}")

    def print_setter(self,setter_name,value):
        self.logger.info(f" setting {setter_name} : {value}")

    def create_deployment_entry(self):
        deploy_inst = deploy.Deploy(self.session,logger=self.logger)
        self.logger.info(f"Tracking for deployment database object : {self.__class__.__name__}")
        deploy_inst.track_development(qry=self.qry,
                                      user_id=self.user_id,
                                      object_type=self.__class__.__name__,
                                      object_database=self.attr.database,
                                      object_schema=self.attr.schema,
                                      object_name=self.attr.name[0])
        
    def write_file_to_git(self):
        self.logger.info(f" BEGIN: write_file_to_git")
        commit_msg=f"Modify {self.__class__.__name__} {self.attr.name[0]} by {self.user_id}"
        self.logger.info(f"{commit_msg}")
        if self.attr.database != 'NA' and self.attr.schema != 'NA':
            filepath=f"Database/{self.attr.database.upper()}/Schemas/{self.attr.schema.upper()}/{self.__class__.__name__}/{self.attr.name[0]}.sql"
        elif self.attr.database !='NA' and self.attr.schema == 'NA':
            filepath=f"Database/{self.attr.database.upper()}/Schemas/DDL/{self.attr.name[0]}.sql"
        elif self.attr.database =='NA' and self.attr.schema != 'NA':
            filepath=f"Database/{self.attr.name[0]}/DDL/{self.attr.name[0]}.sql"
        elif self.attr.database =='NA' and self.attr.schema == 'NA':
            filepath=f"{self.__class__.__name__}/{self.attr.name[0]}/DDL/{self.attr.name[0]}.sql"
        self.logger.info(f"Writing file for {self.attr.__class__.__name__} {self.attr.name[0]} in database {self.attr.database} and schema {self.attr.schema} to repo")
        self.logger.info("Before cloning")
        repo = Repository(self.logger)
        repo.sync_repo(filepath=filepath,qry=self.qry,commit_msg=commit_msg)
        self.logger.info(f" EXIT: write_file_to_git")
    '''
    def write_file_to_git(self,object_name,object_type,object_database,object_schema):
        object_database=object_database.upper()
        object_schema=object_schema.upper()
        object_name=object_name.upper()
        self.logger.info(f" BEGIN: write_file_to_git")
        commit_msg=f"Modify {object_type} {object_name} by {self.user_id}"
        self.logger.info(f"{commit_msg}")
        if object_database != 'NA' and object_schema != 'NA':
            filepath=f"Database/{object_database}/Schemas/{object_schema}/{object_type}/{object_name}.sql"
        elif object_database !='NA' and object_schema == 'NA':
            filepath=f"Database/{object_database}/Schemas/DDL/{object_name}.sql"
        elif object_database =='NA' and object_schema != 'NA':
            filepath=f"Database/{object_name}/DDL/{object_name}.sql"
        elif object_database =='NA' and object_schema == 'NA':
            filepath=f"{object_type}/{object_name}/DDL/{object_name}.sql"
        self.logger.info(f"Writing file for {object_type} {object_name} in database {object_database} and schema {object_schema} to repo")
        self.logger.info("Before cloning")
        repo = Repository(self.logger)
        repo.sync_repo(filepath=filepath,qry=self.qry,commit_msg=commit_msg)
        self.logger.info(f" EXIT: write_file_to_git")
    '''