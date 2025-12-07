import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../processing'))

import logging
logger = logging.getLogger('Alert logs')

from vars.gvobject import Config as cfg 
from vars.obj.alert.gvalert import AlertTag as tags
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from dep import deploy
from .baseobj import BaseObject 
from src.usr.user import ChatHistory

class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.database_exist(session=instance.parent.session, database_name=value)
        instance._database = value

    def __delete__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.schema_exist(session=instance.parent.session,database_name=instance._database,schema_name=value)
        instance._schema = value

    def __delete__(self,instance):
        del instance._schema

class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)

    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
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
                vo.alert_exist(session=instance.parent.session,
                               object_type=instance.parent.__class__.__name__,
                               database=instance._database,
                               schema=instance._schema,
                               alert_name=old_name)
                vo.is_new_alert(session=instance.parent.session,
                                database=instance._database,
                                schema=instance._schema,
                                alert_name=new_name)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to


class Schedule:
    def __get__(self,instance,owner):
        return instance._schedule
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        instance.parent.logger.info(f"inside schedule setting : {value}")
        vv.is_valid_cron(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        instance._schedule = f"'{value}'"

    
    def __delete__(self,instance):
        del instance._schedule

class Iff:
    def __get__(self,instance,owner):
        return instance._iff
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._iff=value  

    def __delete__(self,instance):
        del instance._iff

class Then:
    def __get__(self,instance,owner):
        return instance._action_type
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        instance._action_type=value  

    def __delete__(self,instance):
        del instance._action_type

class ActionSql:
    def __get__(self,instance,owner):
        return instance._action_sql
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if instance._action_type.upper()=="SQL":
            vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._action_sql = value

    def __delete__(self,instance):
        del instance._action_sql

class IntegrationName:
    def __get__(self,instance,owner):
        return instance._integration_name
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if instance._action_type.upper()=="INTEGRATION":
            vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vo.integration_exist(session=instance.parent.session,integration_name=value)
            instance._integration_name = f"'{value}'"

    def __delete__(self,instance):
        del instance._integration_name

class EmailAddress:
    def __get__(self,instance,owner):
        return instance._email_address
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if instance._action_type.upper()=="INTEGRATION":
            vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._email_address = f"'{value}'"

    def __delete__(self,instance):
        del instance._email_address

class EmailSubject:
    def __get__(self,instance,owner):
        return instance._email_subject
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if instance._action_type.upper()=="INTEGRATION":
            vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._email_subject = f"'{value}'"

    def __delete__(self,instance):
        del instance._email_subject

class EmailContent:
    def __get__(self,instance,owner):
        return instance._email_content
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if instance._action_type.upper()=="INTEGRATION":
            vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._email_content = f"'{value}'"

    def __delete__(self,instance):
        del instance._email_content

class Warehouse:
    def __get__(self,instance,owner):
        return instance._warehouse
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        vo.warehouse_exist(session=instance.parent.session,warehouse_name=value)
        instance._warehouse = f"'{value}'"

    def __delete__(self,instance):
        del instance._warehouse

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        instance._comment = f"'{value}'"

    def __delete__(self,instance):
        del instance._comment

class AlertAttrs:
    def __init__(self,parent):
        self.parent = parent

    database=Database() #required
    schema=Schema() #required
    name = Name() #required
    iff=Iff() #required
    then=Then() #required
    warehouse=Warehouse()
    schedule = Schedule()
    comment=Comment()



class Alerts(BaseObject):
    def __init__(self, session, user_id, logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger)
        self.attr=AlertAttrs(self)

    def set_database(self, value):
        self.attr.database = value

    def set_schema(self, value):
        self.attr.schema = value

    def set_name(self, value):
        self.attr.name = value

    def set_iff(self,value):
        self.attr.iff=value
    
    def set_then(self,value):
        self.attr.then=value

    def set_warehouse(self,value):
        self.attr.warehouse=value

    def set_schedule(self,value):
        self.attr.schedule=value

    def set_comment(self,value):
        self.attr.comment=value

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.WAREHOUSE,"_warehouse")
        set_flag(tags.SCHEDULE,"_schedule")
        set_flag(tags.COMMENT,"_comment")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_qry(self):
        self.qry = f"CREATE OR REPLACE ALERT {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} "


    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.WAREHOUSE:
                    self.qry = f" {self.qry} {tags.WAREHOUSE} = {self.attr.warehouse} "
                if prop == tags.SCHEDULE:
                    self.qry = f" {self.qry} {tags.SCHEDULE} = {self.attr.schedule} "
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "

        self.qry = self.qry + f"""
        IF 
        ( 
            EXISTS
            (
            {self.attr.iff}
            )
        )   
        """
        self.qry=self.qry + f" {tags.THEN} " +self.attr.then

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

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=Alerts(session=session,
                         user_id=user_id,
                         logger=logger)
        
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info(f'set database {kwargs[tags.DATABASE]}')
        if tags.DATABASE in kwargs.keys():
            obj_inst.set_database(kwargs[tags.DATABASE])
        else:
            obj_inst.set_database('NONE')

        obj_inst.logger.info(f'set schema {kwargs[tags.SCHEMA]}')
        if tags.SCHEMA in kwargs.keys():
            obj_inst.set_schema(kwargs[tags.SCHEMA])
        else:
            obj_inst.set_schema('NONE')

        obj_inst.logger.info(f"set name {kwargs[tags.NAME]}")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        obj_inst.logger.info(f"set iff {kwargs[tags.IF]}")
        if tags.IF in kwargs.keys():
            obj_inst.set_iff(kwargs[tags.IF])
        else:
            obj_inst.set_iff('NONE')

        obj_inst.logger.info(f"set then {kwargs[tags.THEN]}")
        if tags.THEN in kwargs.keys():
            obj_inst.set_then(kwargs[tags.THEN])
        else:
            obj_inst.set_then('NONE')

        obj_inst.logger.info(f"set warehouse {kwargs[tags.WAREHOUSE]}")
        if tags.WAREHOUSE in kwargs.keys():
            obj_inst.set_warehouse(kwargs[tags.WAREHOUSE])
        else:
            obj_inst.set_warehouse('NONE')

        obj_inst.logger.info(f"set schedule {kwargs[tags.SCHEDULE]}")
        if tags.SCHEDULE in kwargs.keys():
            obj_inst.set_schedule(kwargs[tags.SCHEDULE])
        else:
            obj_inst.set_schedule('NONE')

        obj_inst.logger.info(f"set comment {kwargs[tags.COMMENT]}")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')
        
        obj_inst.prepare_query()

        obj_inst.logger.info('execute query')
        obj_inst.execute_final_query()

        obj_inst.logger.info('write to git')
        obj_inst.write_file_to_git(object_name=obj_inst.attr.name[0],
                                   object_type=obj_inst.__class__.__name__,
                                   object_database=obj_inst.attr.database,
                                   object_schema=obj_inst.attr.schema)
        
        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                           object_identifier=obj_inst.attr.name[0],
                                           qry=obj_inst.qry)

        #logger.info('create deployment entry')
        #alert_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
