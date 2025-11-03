import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))

from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from vars.obj.resourcemonitor.gvresourcemonitor import ResourceMonitorTag as tags
from .baseobj import BaseObject 

class Name:   
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)
    
    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_resource_monitor(session=instance.parent.session,resource_monitor_name=name)
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
                vo.resource_monitor_exist(session=instance.parent.session,resource_monitor_name=old_name)
                vo.is_new_resource_monitor(session=instance.parent.session,resource_monitor_name=new_name)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"


    def __del__(self,instance):
        del instance._name
        del instance._rename_to


class CreditQuota:
    def __get__(self,instance,owner):
        return instance._credit_quota
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._credit_quota=value
        else:
            vv.is_positive_number(value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._credit_quota = value
    
    def __delete__(self,instance):
        del instance._credit_quota

class Frequency:
    def __get__(self,instance,owner):
        return instance._frequency
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._frequency=value
        else:
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.FREQUENCY),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._frequency=value

    def __delete__(self,instance):
        del instance._frequency

class StartTimestamp:
    def __get__(self,instance,owner):
        return instance._start_timestamp
    
    def __set__(self,instance,value):
        instance._start_timestamp="IMMEDIATELY"
    
    def __delete__(self,instance):
        del instance._start_timestamp

class EndTimestamp:
    def __get__(self,instance,owner):
        return instance._end_timestamp
    
    def __set__(self,instance,value):
        instance._end_timestamp = value
    
    def __delete__(self,instance):
        del instance._end_timestamp


class NotifyUsers:
    def __get__(self,instance,owner):
        return instance._notify_users
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._notify_users=value
        else:
            for names in value:
                vo.user_exist(session=instance.parent.session,user_name=names)
            instance._notify_users=f"({value})"
    
    def __delete__(self,instance):
        del instance._notify_users

class Threshold:
    def __get__(self,instance,owner):
        return instance._threshold
    
    def __set__(self,instance,value):
        instance._threshold=[]
        vv.is_positive_number(value=value,
                                 object_type=instance.parent.__class__.__name__,
                                 attr_name=self.__class__.__name__)
        instance._threshold.append(value)
        
    def __delete__(self,instance):
        del instance._threshold

class Triggers:
    def __get__(self,instance,owner):
        return instance._triggers
    
    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside triggers to set: {value}")
        if value=="NONE":
            instance._triggers="NONE"
        else:
            instance._triggers="TRUE"
        
    def __delete__(self,instance):
        del instance._action

class Action:
    def __get__(self,instance,owner):
        return instance._action
    
    def __set__(self,instance,value):
        instance._action=[]
        vv.is_allowed_value(value=value,
                            allowed_list=tags.allowed_value_list().get(tags.ACTION),
                            object_type=instance.parent.__class__.__name__,
                            attr_name=self.__class__.__name__)
        instance._action.append(value)
        
    def __delete__(self,instance):
        del instance._action

class ResourceMonitorAttrs:
    def __init__(self,parent):
        self.parent = parent
        
    name = Name()
    credit_quota = CreditQuota()
    frequency = Frequency()
    start_timestamp = StartTimestamp()
    end_timestamp = EndTimestamp()
    notify_users = NotifyUsers()
    triggers = Triggers()
    threshold=Threshold()
    action=Action()


class ResourceMonitor(BaseObject):
    def __init__(self, session, user_id, logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger)
        self.attr = ResourceMonitorAttrs(self)
    
    def validate_user(self):
        vo.is_account_admin(self.session,self.user_id,self.__class__.__name__)

    def set_name(self, value):
        self.attr.name = value

    def set_credit_quota(self, value):
        self.attr.credit_quota = value

    def set_frequency(self, value):
        self.attr.frequency = value

    def set_start_timestmap(self, value):
        self.attr.start_timestamp = value

    def set_end_timestamp(self, value):
        self.attr.end_timestamp = value

    def set_notify_users(self, value):
        self.attr.notify_users = value

    def set_triggers(self, value):
        self.attr.triggers = value

    def set_threshold(self, value):
        self.attr.threshold = value

    def set_action(self, value):
        self.attr.action = value

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.NAME,"_name")
        set_flag(tags.CREDIT_QUOTA,"_credit_quota")
        set_flag(tags.FREQUENCY,"_frequency")
        set_flag(tags.START_TIMESTAMP,"_start_timestamp")
        set_flag(tags.END_TIMESTAMP,"_end_timestamp")
        set_flag(tags.NOTIFY_USERS,"_notify_users")
        set_flag(tags.TRIGGERS,"triggers")
        set_flag(tags.THRESHOLD,"_threshold")
        set_flag(tags.ACTION,"_action")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_resource_monitor_qry(self):
        self.qry = f"CREATE OR REPLACE RESOURCE MONITOR {self.attr.name[0]} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            self.qry = f"{self.qry} WITH "
            for prop in self.property_lst:
                if prop == tags.CREDIT_QUOTA:
                    self.qry = f" {self.qry} {tags.CREDIT_QUOTA}  = {self.attr.credit_quota} "
                if prop == tags.FREQUENCY:
                    self.qry = f" {self.qry} {tags.FREQUENCY} = {self.attr.frequency} "
                if prop == tags.START_TIMESTAMP:
                    self.qry = f" {self.qry} {tags.START_TIMESTAMP} = {self.attr.start_timestamp} "
                if prop == tags.END_TIMESTAMP:
                    self.qry = f" {self.qry} {tags.END_TIMESTAMP} = {self.attr.end_timestamp} "
                if prop == tags.NOTIFY_USERS:
                    self.qry = f" {self.qry} {tags.NOTIFY_USERS} = {self.attr.notify_users} "
                if prop == tags.TRIGGERS:
                    self.qry=f" {self.qry} TRIGGERS "
                    for i in range(0,len(self.attr.action)):
                        self.qry = f" {self.qry} ON {self.attr.threshold[i]}  PERCENT DO {self.attr.action[i] } "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_resource_monitor_qry()
        self.add_properties_to_query()

    def create_resource_monitor(self):
        self.execute_final_query()


    def create_object(session,**kwargs):
        rm = ResourceMonitor(session) 
        rm.validate_user()
        rm.set_name(kwargs[tags.NAME])
        rm.set_credit_quota(kwargs[tags.CREDIT_QUOTA])
        rm.set_frequency(kwargs[tags.FREQUENCY])
        rm.set_start_timestmap(kwargs[tags.START_TIMESTAMP])
        rm.set_end_timestamp(kwargs[tags.END_TIMESTAMP])
        rm.set_notify_users(kwargs[tags.NOTIFY_USERS])
        rm.set_triggers(kwargs[tags.TRIGGERS])
        rm.set_threshold(kwargs[tags.THRESHOLD])
        rm.set_action(kwargs[tags.ACTION])
        rm.prepare_query()
        rm.create_resource_monitor()


class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        obj_inst=ResourceMonitor(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        logger.info("set credit_quota")
        if tags.CREDIT_QUOTA in kwargs.keys():
            obj_inst.set_credit_quota(kwargs[tags.CREDIT_QUOTA])
        else:
            obj_inst.set_credit_quota('NONE')

        logger.info("set frequency")
        if tags.FREQUENCY in kwargs.keys():
            obj_inst.set_frequency(kwargs[tags.FREQUENCY])
        else:
            obj_inst.set_frequency('NONE')

        logger.info("set start_timestamp")
        if tags.START_TIMESTAMP in kwargs.keys():
            obj_inst.set_start_timestmap(kwargs[tags.START_TIMESTAMP])
        else:
            obj_inst.set_start_timestmap('NONE')

        logger.info("set end_timestamp")
        if tags.END_TIMESTAMP in kwargs.keys():
            obj_inst.set_end_timestamp(kwargs[tags.END_TIMESTAMP])
        else:
            obj_inst.set_end_timestamp('NONE')

        logger.info("set notify_users")
        if tags.NOTIFY_USERS in kwargs.keys():
            obj_inst.set_notify_users(kwargs[tags.NOTIFY_USERS])
        else:
            obj_inst.set_notify_users('NONE')

        logger.info("set triggers")
        if tags.TRIGGERS in kwargs.keys():
            logger.info("setting to true")
            obj_inst.set_triggers("TRUE")
            for i in range(0,len(kwargs[tags.TRIGGERS])):
                logger.info(f"set threshold and action {kwargs[tags.TRIGGERS][i]}")
                obj_inst.set_threshold(kwargs[tags.TRIGGERS][i][tags.THRESHOLD])
                obj_inst.set_action(kwargs[tags.TRIGGERS][i][tags.ACTION])
        else:
            obj_inst.set_triggers("NONE")
            obj_inst.set_action("NONE")
            obj_inst.set_threshold("NONE")
        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry(object_name=obj_inst.attr.name[0],object_type=obj_inst.__class__.__name__,object_database='NA',object_schema='NA')
        obj_inst.write_file_to_git(object_name=obj_inst.attr.name[0],object_type=obj_inst.__class__.__name__,object_database='NA',object_schema='NA')

    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
