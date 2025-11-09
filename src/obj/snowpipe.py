import sys
import os
import logging 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.gvobject import Config as cfg, Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy
from validation.validateobject import ValidateObject as vo
from setup import privilege
from .baseobj import BaseObject 
from vars.obj.snowpipe.gvsnowpipe import SnowpipeTag as tags
from src.usr.user import ChatHistory


class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.database_exist(session=instance.parent.session, database_name=value)
        instance._database = value
    
    def __delete__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.schema_exist(session=instance.parent.session, database_name=instance._database, schema_name=value)
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
            vo.is_new_pipe(session=instance.parent.session,
                           database_name=instance._database,
                           schema_name=instance._schema,
                           pipe_name=name)
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
                vo.pipe_exist(session=instance.parent.session,
                              database_name=instance._database,
                              schema_name=instance._schema,
                              pipe_name=old_name)
                vo.is_new_pipe(session=instance.parent.session,
                               database_name=instance._database,
                               schema_name=instance._schema,
                               pipe_name=new_name)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"


    def __del__(self,instance):
        del instance._name
        del instance._rename_to

class AutoIngest:
    def __get__(self,instance,owner):
        return instance._auto_ingest
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._auto_ingest=value
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._auto_ingest = value
    
    def __delete__(self,instance):
        del instance._auto_ingest

class ErrorIntegration:
    def __get__(self,instance,owner):
        return instance._error_integration
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._error_integration=value
        else:
            vo.integration_exist(session=instance.parent.session,integration_name=value)
            instance._error_integration = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._error_integration

class AwsSnsTopic:
    def __get__(self,instance,owner):
        return instance._aws_sns_topic
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._aws_sns_topic=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._aws_sns_topic = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._aws_sns_topic

class Integration:
    def __get__(self,instance,owner):
        return instance._integration
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._integration=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._integration = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._integration


class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._comment=value
        else:
            instance._comment = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._comment



class SnowpipeAttrs:
    def __init__(self,parent):
        self.parent = parent

    database = Database()
    schema = Schema()
    name = Name()
    auto_ingest = AutoIngest()
    error_integration = ErrorIntegration()
    aws_sns_topic = AwsSnsTopic()
    integration = Integration()
    comment = Comment()

class Snowpipe(BaseObject):
    def __init__(self, session, user_id, logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger)
        self.attr = SnowpipeAttrs(self)

    def set_database(self,value):
        self.attr.database = value

    def set_schema(self,value):
        self.attr.schema = value

    def set_name(self,value):
        self.attr.name = value

    def set_copy_into(self,value):
        self.copy_into=value

    def set_auto_ingest(self,auto_ingest):
        self.attr.auto_ingest = auto_ingest

    def set_error_integration(self,error_integration):
        self.attr.error_integration = error_integration

    def set_aws_sns_topic(self,aws_sns_topic):
        self.attr.aws_sns_topic = aws_sns_topic

    def set_integration(self,integration):
        self.attr.integration = integration

    def set_comment(self,comment):
        self.attr.comment = comment

    def set_qualified_name(self):
        self.qualified_name = f"{self.attr.database}.{self.attr.schema}.{self.attr.name}"

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.AUTO_INGEST,"_auto_ingest")
        set_flag(tags.ERROR_INTEGRATION,"_error_integration")
        set_flag(tags.AWS_SNS_TOPIC,"_aws_sns_topic")
        set_flag(tags.INTEGRATION,"_integration")
        set_flag(tags.COMMENT,"_comment")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_qry(self):
        self.qry = f'CREATE OR REPLACE PIPE {self.attr.database}.{self.attr.schema}.{self.attr.name[0]}  '


    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.AUTO_INGEST:
                    self.qry = f" {self.qry} {tags.AUTO_INGEST} = {self.attr.auto_ingest} "
                if prop == tags.ERROR_INTEGRATION:
                    self.qry = f" {self.qry} {tags.ERROR_INTEGRATION} = {self.attr.error_integration} "
                if prop == tags.AWS_SNS_TOPIC:
                    self.qry = f" {self.qry} {tags.AWS_SNS_TOPIC} = {self.attr.aws_sns_topic} "
                if prop == tags.INTEGRATION:
                    self.qry = f" {self.qry} {tags.INTEGRATION} = {self.attr.integration} "
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "
        self.qry= self.qry + f" AS {self.copy_into}"

    def alter_object(self):
        for prop in self.property_lst:
            if prop == tags.AUTO_INGEST:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.AUTO_INGEST} = {self.attr.auto_ingest}"
                self.execute_final_query()
            if prop == tags.ERROR_INTEGRATION:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.ERROR_INTEGRATION} = {self.attr.error_integration}"
                self.execute_final_query()
            if prop == tags.AWS_SNS_TOPIC:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.AWS_SNS_TOPIC} = {self.attr.aws_sns_topic}"
                self.execute_final_query()
            if prop == tags.INTEGRATION:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.INTEGRATION} = {self.attr.integration}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} RENAME TO {self.attr.database}.{self.attr.schema}.{self.attr.name[1]}"
            self.logger.info(f"Renaming {self.__class__.__name__.upper()} {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()


    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create=="TRUE":
            self.set_create_qry()
            self.add_properties_to_query()
        elif self.is_create=="FALSE":
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()

    
    def pause_snowpipe(self):
        self.session.sql(f"ALTER PIPE {self.attr.database}.{self.attr.schema}.{self.attr.name} SET PIPE_EXECUTION_PAUSED=true").collect()

    def resume_snowpipe(self):
        self.session.sql(f"SELECT SYSTEM$PIPE_FORCE_RESUME('{self.attr.database}.{self.attr.schema}.{self.attr.name}')").collect()

    def create_snowpipe(self):
        self.execute_final_query()
        self.pause_snowpipe()

    def create_object(self,*largs,**kwargs):
        self.logger.info(f"Operating on {self.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        self.logger.info(f'dictionary passed {kwargs}')
        self.is_create=kwargs[tags.IS_CREATE]
        self.set_database(kwargs[tags.DATABASE])
        self.set_schema(kwargs[tags.SCHEMA])
        self.set_name(kwargs[tags.NAME])
        self.set_copy_into(kwargs[tags.COPYINTO_QUERY])
        self.set_auto_ingest(kwargs[tags.AUTO_INGEST])
        self.set_error_integration(kwargs[tags.ERROR_INTEGRATION])
        self.set_aws_sns_topic(kwargs[tags.AWS_SNS_TOPIC])
        self.set_integration(kwargs[tags.INTEGRATION])
        self.set_comment(kwargs[tags.COMMENT])
        self.set_qualified_name()
        self.prepare_query()
        self.logger.info(f"creating snowpipe : {self.attr.name}")
        self.create_snowpipe()
        self.resume_snowpipe()
        if len(largs) == 0:
            self.write_file_to_git(object_name=self.attr.name,object_type=self.__class__.__name__,object_database=self.attr.database,object_schema=self.attr.schema)



class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=Snowpipe(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info("set database")
        if tags.DATABASE in kwargs.keys():
            obj_inst.set_database(kwargs[tags.DATABASE])
        else:
            obj_inst.set_database('NONE')

        logger.info("set schema")
        if tags.SCHEMA in kwargs.keys():
            obj_inst.set_schema(kwargs[tags.SCHEMA])
        else:
            obj_inst.set_schema('NONE')

        logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        logger.info("set auto_ingest")
        if tags.AUTO_INGEST in kwargs.keys():
            obj_inst.set_auto_ingest(kwargs[tags.AUTO_INGEST])
        else:
            obj_inst.set_auto_ingest('NONE')

        logger.info("set error_integration")
        if tags.ERROR_INTEGRATION in kwargs.keys():
            obj_inst.set_error_integration(kwargs[tags.ERROR_INTEGRATION])
        else:
            obj_inst.set_error_integration('NONE')

        logger.info("set aws_sns_topic")
        if tags.AWS_SNS_TOPIC in kwargs.keys():
            obj_inst.set_aws_sns_topic(kwargs[tags.AWS_SNS_TOPIC])
        else:
            obj_inst.set_aws_sns_topic('NONE')

        logger.info("set integration")
        if tags.INTEGRATION in kwargs.keys():
            obj_inst.set_integration(kwargs[tags.INTEGRATION])
        else:
            obj_inst.set_integration('NONE')

        logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')

        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry(object_name=obj_inst.attr.name[0],
                                         object_type=obj_inst.__class__.__name__,
                                         object_database=obj_inst.attr.database,
                                         object_schema=obj_inst.attr.schema)

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry(object_name=obj_inst.attr.name[0],
                                         object_type=obj_inst.__class__.__name__,
                                         object_database=obj_inst.attr.database,
                                         object_schema=obj_inst.attr.schema)

        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                        object_identifier=obj_inst.attr.name[0],
                                        qry=obj_inst.qry)
    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
