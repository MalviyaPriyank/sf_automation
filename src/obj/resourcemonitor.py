import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))

from vars.gvobject import ResourceMonitor as gv
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo


class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.is_new_resource_monitor(session=instance.parent.session,resource_monitor_name=value)
        if ( vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__) 
            and not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
            and not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__)
            ):
            instance._name = value

    def __delete__(self,instance):
        del instance._name

class CreditQuota:
    def __get__(self,instance,owner):
        return instance._credit_quota
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._credit_quota=value
        else:
            vv.is_positive_number(value)
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
            vv.is_allowed_value(value=value,allowed_list=gv._allowed_values_frequency,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
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

class Triggers:
    def __get__(self,instance,owner):
        return instance._triggers
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._triggers=value
        else:
            vv.is_allowed_value(value=value.upper(),allowed_list=gv._allowed_values_triggers,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._triggers=value
        
    def __delete__(self,instance):
        del instance._triggers

class Threshold:
    def __get__(self,instance,owner):
        return instance._threshold
    
    def __set__(self,instance,value):
        if instance._triggers!="NONE":
            vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            if instance._triggers=="SINGLE":
                vv.is_positive_number(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                instance._threshold=value
            elif instance._triggers=="MULTIPLE":
                vv.is_list(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                instance._threshold=value
        elif instance._triggers=="NONE":
            instance._threshold="NONE"
        
    def __delete__(self,instance):
        del instance._threshold

class Action:
    def __get__(self,instance,owner):
        return instance._action
    
    def __set__(self,instance,value):
        if instance._triggers!="NONE":
            vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            if instance._triggers=="SINGLE":
                vv.is_positive_number(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                instance._action=value
            elif instance._triggers=="MULTIPLE":
                vv.is_list(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,*[],**{"MUST_BE_OF_LENGTH":len(instance._threshold)})
                instance._action=value
        elif instance._triggers=="NONE":
            instance._action="NONE"

        
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


class ResourceMonitor:
    def __init__(self,session,user_id,logger):
        self.session = session
        self.qry = ""
        self.user_id=user_id
        self.logger=logger
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

        set_flag(gv._name_tag,"_name")
        set_flag(gv._credit_quota_tag,"_credit_quota")
        set_flag(gv._frequency_tag,"_frequency")
        set_flag(gv._start_timestamp_tag,"_start_timestamp")
        set_flag(gv._end_timestamp_tag,"_end_timestamp")
        set_flag(gv._notify_users_tag,"_notify_users")
        set_flag(gv._triggers_tag,"_triggers")
        set_flag(gv._threshold_tag,"_threshold")
        set_flag(gv._action_tag,"_action")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_resource_monitor_qry(self):
        self.qry = f"CREATE OR REPLACE RESOURCE MONITOR {self.attr.name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            self.qry = f"{self.qry} WITH "
            for prop in self.property_lst:
                if prop == gv._credit_quota_tag:
                    self.qry = f" {self.qry} {gv._credit_quota_tag}  = {self.attr.credit_quota} "
                if prop == gv._frequency_tag:
                    self.qry = f" {self.qry} {gv._frequency_tag} = {self.attr.frequency} "
                if prop == gv._start_timestamp_tag:
                    self.qry = f" {self.qry} {gv._start_timestamp_tag} = {self.attr.start_timestamp} "
                if prop == gv._end_timestamp_tag:
                    self.qry = f" {self.qry} {gv._end_timestamp_tag} = {self.attr.end_timestamp} "
                if prop == gv._notify_users_tag:
                    self.qry = f" {self.qry} {gv._notify_users_tag} = {self.attr.notify_users} "
                if prop == gv._triggers_tag:
                    self.qry=f" {self.qry} TRIGGERS "
                    if gv._triggers_tag.upper()=="SINGLE":
                        self.qry = f" {self.qry} ON {self.attr.threshold} DO {self.attr.action} "
                    if gv._triggers_tag.upper()=="MULTIPLE":
                        for i in range(0,len(self.attr.threshold)):
                            self.qry=f" {self.qry} ON {self.attr.threshold[i]} DO {self.attr.action[i]} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_resource_monitor_qry()
        self.add_properties_to_query()

    def create_resource_monitor(self):
        self.session.sql(self.qry)


    def create_object(session,**kwargs):
        rm = ResourceMonitor(session) 
        rm.validate_user()
        rm.set_name(kwargs[gv._name_tag])
        rm.set_credit_quota(kwargs[gv._credit_quota_tag])
        rm.set_frequency(kwargs[gv._frequency_tag])
        rm.set_start_timestmap(kwargs[gv._start_timestamp_tag])
        rm.set_end_timestamp(kwargs[gv._end_timestamp_tag])
        rm.set_notify_users(kwargs[gv._notify_users_tag])
        rm.set_triggers(kwargs[gv._triggers_tag])
        rm.set_threshold(kwargs[gv._threshold_tag])
        rm.set_action(kwargs[gv._action_tag])
        rm.prepare_query()
        rm.create_resource_monitor()
