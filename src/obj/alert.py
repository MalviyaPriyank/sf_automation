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
        vo.schema_exist(session=instance.parent.session,database_name=instance._database,schema_name=value)
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
        instance.parent.logger.info(f"inside schedule setting : {value}")
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vv.is_valid_cron(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        instance._schedule = f"'{value}'"

    
    def __delete__(self,instance):
        del instance._schedule

class Iff:
    def __get__(self,instance,owner):
        return instance._iff
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._iff=value  

    def __delete__(self,instance):
        del instance._iff

class Then:
    def __get__(self,instance,owner):
        return instance._action_type
    
    def __set__(self,instance,value):
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
        if instance._action_type.upper()=="SQL":
            vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._action_sql = value

    def __delete__(self,instance):
        del instance._action_sql

class IntegrationName:
    def __get__(self,instance,owner):
        return instance._integration_name
    
    def __set__(self,instance,value):
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
        if instance._action_type.upper()=="INTEGRATION":
            vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._email_address = f"'{value}'"

    def __delete__(self,instance):
        del instance._email_address

class EmailSubject:
    def __get__(self,instance,owner):
        return instance._email_subject
    
    def __set__(self,instance,value):
        if instance._action_type.upper()=="INTEGRATION":
            vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._email_subject = f"'{value}'"

    def __delete__(self,instance):
        del instance._email_subject

class EmailContent:
    def __get__(self,instance,owner):
        return instance._email_content
    
    def __set__(self,instance,value):
        if instance._action_type.upper()=="INTEGRATION":
            vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._email_content = f"'{value}'"

    def __delete__(self,instance):
        del instance._email_content

class Warehouse:
    def __get__(self,instance,owner):
        return instance._warehouse
    
    def __set__(self,instance,value):
        vo.warehouse_exist(session=instance.parent.session,warehouse_name=value)
        instance._warehouse = f"'{value}'"

    def __delete__(self,instance):
        del instance._warehouse

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = f"'{value}'"

    def __delete__(self,instance):
        del instance._comment

class AlertAttrs:
    def __init__(self,parent):
        self.parent = parent

    database=Database()
    schema=Schema()
    name = Name()
    iff=Iff()
    then=Then()
    warehouse=Warehouse()
    schedule = Schedule()
    comment=Comment()



class Alerts(BaseObject):
    def __init__(self, session, user_id, logger):
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


    def set_create_alert_qry(self):
        self.logger.info("Creating query")
        self.qry = f"""CREATE OR REPLACE ALERT {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} """
        self.logger.info(f"Initial query : {self.qry}")
        if self.attr.warehouse != "NONE":
            self.qry=self.qry + f""" {tags.WAREHOUSE} = {self.attr.warehouse} """
        self.qry=self.qry + f""" 
                            SCHEDULE = {self.attr.schedule} 
                            IF 
                            ( 
                                EXISTS
                                (
                                {self.attr.iff}
                                )
                            )   
                            """
        self.qry=self.qry + f" {tags.THEN} " +self.attr.then

    def create_alert(self):
        self.execute_final_query()

class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        alert_inst=Alerts(session=session,
                         user_id=user_id,
                         logger=logger)
        logger=logger.getChild(__name__)
        
        logger.info(f"Operating on {alert_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        alert_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info('set database')
        if tags.DATABASE in kwargs.keys():
            alert_inst.set_database(kwargs[tags.DATABASE])
        else:
            alert_inst.set_database('NONE')

        logger.info('set schema')
        if tags.SCHEMA in kwargs.keys():
            alert_inst.set_schema(kwargs[tags.SCHEMA])
        else:
            alert_inst.set_schema('NONE')

        logger.info("set name")
        if tags.NAME in kwargs.keys():
            alert_inst.set_name(kwargs[tags.NAME])
        else:
            alert_inst.set_name('NONE')

        logger.info("set iff")
        if tags.IF in kwargs.keys():
            alert_inst.set_iff(kwargs[tags.IF])
        else:
            alert_inst.set_iff('NONE')

        logger.info("set then")
        if tags.THEN in kwargs.keys():
            alert_inst.set_then(kwargs[tags.THEN])
        else:
            alert_inst.set_then('NONE')

        logger.info("set warehouse")
        if tags.WAREHOUSE in kwargs.keys():
            alert_inst.set_warehouse(kwargs[tags.WAREHOUSE])
        else:
            alert_inst.set_warehouse('NONE')

        logger.info("set schedule")
        if tags.SCHEDULE in kwargs.keys():
            alert_inst.set_schedule(kwargs[tags.SCHEDULE])
        else:
            alert_inst.set_schedule('NONE')

        logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            alert_inst.set_comment(kwargs[tags.COMMENT])
        else:
            alert_inst.set_comment('NONE')

        logger.info('prepare query')
        alert_inst.set_create_alert_qry()
        
        logger.info('execute query')
        alert_inst.create_alert()


        #logger.info('create deployment entry')
        #alert_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
