import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../processing'))



from vars.gvobject import Alert as gv, Config as cfg , Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from dep import deploy
from setup import privilege 
from processing.stage import Stage

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if ( vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__) 
              and not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
              and not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__)
            ):
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
        return instance._allowed_recipients
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._allowed_recipients=value  

    def __delete__(self,instance):
        del instance._allowed_recipients

class Then:
    def __get__(self,instance,owner):
        return instance._default_recipients
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._default_recipients = value

    def __delete__(self,instance):
        del instance._default_recipients

class AlertAttrs:
    def __init__(self,parent):
        self.parent = parent

    name = Name()
    schedule = Schedule()
    iff=Iff()
    then=Then()


class Alerts:
    def __init__(self,session,user_id):
        self.session = session
        self.user_id = user_id
        self.qry = ""
        self.attr = AlertAttrs(self)

    def set_name(self, value):
        self.attr.name = value

    def set_schedule(self,value):
        self.attr.schedule=value
    
    def set_iff(self,value):
        self.attr.iff=value

    def set_then(self,value):
        self.attr.then=value


    def set_create_alert_qry(self):
        self.qry = f"""CREATE ALERT {self.attr.name} 
        WAREHOUSE='WH_XSMALL' 
        SCHEDULE={self.attr.schedule} 
        IF( EXISTS
            (
            SELECT DISTINCT cfa."Loyalty_Number"
            FROM DB_DEV_SNOWCHAIN.SCH_SNOWCHAIN.CUSTOMER_FLIGHT_ACTIVITY cfa
            LEFT JOIN DB_DEV_SNOWCHAIN.SCH_SNOWCHAIN.CUStOMERS cst
            ON cst."customer_id" = cfa."Loyalty_Number"
            WHERE cst."customer_id" IS NULL
            AND cfa."Loyalty_Number" IS NOT NULL
            ) 
        ) 
        THEN 
        CALL SYSTEM$SEND_EMAIL('NOT_INT_EMAIL','snowchain123@gmail.com','ALERT {self.attr.name}','Referential integrity breached')
        """
    
    def prepare_query(self):
        self.session.sql("USE DATABASE DB_DEV_SNOWCHAIN").collect()
        self.session.sql("USE SCHEMA SCH_SNOWCHAIN").collect()
        self.set_create_alert_qry()


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

        self.set_name(kwargs[gv._name_tag])
        self.set_schedule(kwargs[gv._schedule_tag])
        self.set_iff(kwargs[gv._if_tag])
        self.set_then(kwargs[gv._then_tag])
        self.prepare_query()
        self.create_alert()
        self.create_deployment_entry()
