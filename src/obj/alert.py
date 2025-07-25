import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../processing'))



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
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if ( vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__) 
              and not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
              and not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__)
            ):
            vo.is_new_alert(session=instance.parent.session,database=instance._database,schema=instance._schema,alert_name=value)
            instance._name = value

    def __delete__(self,instance):
        del instance._name


class Schedule:
    def __get__(self,instance,owner):
        return instance._schedule
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
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

class ActionType:
    def __get__(self,instance,owner):
        return instance._action_type
    
    def __set__(self,instance,value):
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

class AlertAttrs:
    def __init__(self,parent):
        self.parent = parent

    database=Database()
    schema=Schema()
    name = Name()
    schedule = Schedule()
    iff=Iff()
    action_type=ActionType()
    action_sql=ActionSql()
    integration_name=IntegrationName()
    email_address=EmailAddress()
    email_subject=EmailSubject()
    email_content=EmailContent()
    warehouse=Warehouse()


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

    def set_schedule(self,value):
        self.attr.schedule=value
    
    def set_iff(self,value):
        self.attr.iff=value

    def set_action_type(self,value):
        self.attr.action_type=value

    def set_action_sql(self,value):
        self.attr.action_sql=value

    def set_integration_name(self,value):
        self.attr.integration_name=value

    def set_email_address(self,value):
        self.attr.email_address=value

    def set_email_subject(self,value):
        self.attr.email_subject=value

    def set_email_content(self,value):
        self.attr.email_content=value

    def set_warehouse(self,value):
        self.attr.warehouse=value


    def set_create_alert_qry(self):
        self.qry = f"""CREATE ALERT {self.attr.database}.{self.attr.schema}.{self.attr.name} """
        if self.attr.warehouse != "NONE":
            self.qry=self.qry + f""" WAREHOUSE = {self.attr.warehouse} """
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
        if self.attr.action_type.upper()=="SQL":
            self.qry=self.qry+ f""" THEN {self.attr.action_sql} ;"""
        elif self.attr.action_type.upper()=="INTEGRATION":
            self.qry=self.qry + f""" THEN CALL SYSTEM$SEND_EMAIL({self.attr.integration_name},{self.attr.email_address},{self.attr.email_subject},{self.attr.email_content} ) ;"""
    
    def prepare_query(self):
        self.execute_final_query()


    def create_deployment_entry(self):
        deploy_inst = deploy.Deploy(self.session)
        deploy_inst.insert_into_deployment_script_table(obj_qry=self.qry,user_id=self.user_id)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database('NA')
        deploy_inst.set_object_schema('NA')
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()
    '''
    def grant_default_privileges(self):
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges[self.__class__.__name__.upper()]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = self.__class__.__name__.upper(),object_identifier=self.attr.name,role = role)
    '''

    def create_alert(self):
        self.session.sql(self.qry).collect()

    def create_object(self,*largs,**kwargs):
        self.logger.info(f'dictionary passed {kwargs}')

        self.logger.info('set database')
        self.set_database(kwargs[tags.DATABASE])

        self.logger.info('set schema')
        self.set_schema(kwargs[tags.SCHEMA])

        self.logger.info('set name')
        self.set_name(kwargs[tags.NAME])

        self.logger.info('set schedule')
        self.set_schedule(kwargs[tags.SCHEDULE])

        self.logger.info('set _if_tag')
        self.set_iff(kwargs[tags.IF])

        self.logger.info('set _action_type')
        self.set_action_type(kwargs[tags.ACTION_TYPE])

        self.logger.info('set _action_sql')
        self.set_action_sql(kwargs[tags.ACTION_SQL])

        self.logger.info('set _integration_name')
        self.set_integration_name(kwargs[tags.INTEGRATION_NAME])

        self.logger.info('set _email_address')
        self.set_email_address(kwargs[tags.EMAIL_ADDRESS])

        self.logger.info('set _email_subject')
        self.set_email_subject(kwargs[tags.EMAIL_SUBJECT])

        self.logger.info('set _email_content')
        self.set_email_content(kwargs[tags.EMAIL_CONTENT])

        self.logger.info('prepare query')
        self.prepare_query()
        
        self.logger.info('execute query')
        self.create_alert()

        self.logger.info('create deployment entry')
        self.create_deployment_entry()
