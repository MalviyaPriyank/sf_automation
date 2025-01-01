import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../../vars/global'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))


from global_vars import ResourceMonitor as gv
from validatevalue import ValidateValue as vv

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        if value == "NONE" :
            raise KeyError
        elif not vv.starts_with_alphabet(value):
            raise ValueError
        elif not vv.is_enclosed_in_double_quotes(value):
            if vv.has_space(value):
                raise ValueError
            if vv.has_special_characters(value):
                raise ValueError
            else:
                instance._name = value

    def __delete__(self,instance):
        del instance._name

class NameTag:
    def __get__(self,instance,owner):
        return instance._name_tag
    
    def __set__(self,instance,value):
        instance._name_tag = value

    def __delete__(self,instance):
        del instance._name_tag

class CreditQuota:
    def __get__(self,instance,owner):
        return instance._credit_quota
    
    def __set__(self,instance,value):
        if  vv.is_positive_number(value):
            instance._credit_quota = value
        else:
            raise KeyError
    
    def __delete__(self,instance):
        del instance._credit_quota

class CreditQuotaTag:
    def __get__(self,instance,owner):
        return instance._credit_quota_tag
    
    def __set__(self,instance,value):
        instance._credit_quota_tag = value
    
    def __delete__(self,instance):
        del instance._credit_quota_tag


class Frequency:
    def __get__(self,instance,owner):
        return instance._frequency
    
    def __set__(self,instance,value):
        if value not in gv._allowed_values_frequency:
            raise ValueError
        else:
            instance._frequency = value
    
    def __delete__(self,instance):
        del instance._frequency

class FrequencyTag:
    def __get__(self,instance,owner):
        return instance._frequency_tag
    
    def __set__(self,instance,value):
        instance._frequency_tag = value
    
    def __delete__(self,instance):
        del instance._frequency_tag

class StartTimestamp:
    def __get__(self,instance,owner):
        return instance._start_timestamp
    
    def __set__(self,instance,value):
        if instance._frequency == "NONE":
            raise ValueError
        elif value == "NONE":
            instance._start_timestamp = 'IMMEDIATELY'
        else:
            instance._start_timestamp = value
    
    def __delete__(self,instance):
        del instance._start_timestamp

class StartTimestampTag:
    def __get__(self,instance,owner):
        return instance._start_timestamp_tag
    
    def __set__(self,instance,value):
        instance._start_timestamp_tag = value
    
    def __delete__(self,instance):
        del instance._start_timestamp_tag

class EndTimestamp:
    def __get__(self,instance,owner):
        return instance._end_timestamp
    
    def __set__(self,instance,value):
        instance._end_timestamp = value
    
    def __delete__(self,instance):
        del instance._end_timestamp

class EndTimestampTag:
    def __get__(self,instance,owner):
        return instance._end_timestamp_tag
    
    def __set__(self,instance,value):
        instance._end_timestamp_tag = value
    
    def __delete__(self,instance):
        del instance._end_timestamp_tag


class NotifyUsers:
    def __get__(self,instance,owner):
        return instance._notify_users
    
    def __set__(self,instance,value):
        if vv.has_space(value):
            if vv.is_enclosed_in_double_quotes(value):
                instance._notify_users = value
            else:
                raise KeyError
        elif vv.has_special_characters(value):
            if vv.is_enclosed_in_double_quotes(value):
                instance._notify_users = value
            else:
                raise KeyError
        else:
            instance._notify_users = value
    
    def __delete__(self,instance):
        del instance._notify_users


class NotifyUsersTag:
    def __get__(self,instance,owner):
        return instance._notify_users_tag
    
    def __set__(self,instance,value):
        instance._notify_users_tag = value
    
    def __delete__(self,instance):
        del instance._notify_users_tag

class TriggersOn:
    def __get__(self,instance,owner):
        return instance._triggers_on
    
    def __set__(self,instance,value):
        if vv.is_positive_number(value):
            instance._triggers_on = value
        else:
            raise ValueError
        
    
    def __delete__(self,instance):
        del instance._triggers_on

class TriggersOnTag:
    def __get__(self,instance,owner):
        return instance._triggers_on_tag
    
    def __set__(self,instance,value):
        instance._triggers_on_tag = value
    
    def __delete__(self,instance):
        del instance._triggers_on_tag

class Do:
    def __get__(self,instance,owner):
        return instance._do
    
    def __set__(self,instance,value):
        if value not in gv._allowed_values_do:
            raise ValueError
        else:
            instance._do = value
    
    def __delete__(self,instance):
        del instance._do

class DoTag:
    def __get__(self,instance,owner):
        return instance._do_tag
    
    def __set__(self,instance,value):
        instance._do_tag = value
    
    def __delete__(self,instance):
        del instance._do_tag


class ResourceMonitorAttrs:
    name = Name()
    name_tag = NameTag()
    credit_quota = CreditQuota()
    credit_quota_tag = CreditQuotaTag()
    frequency = Frequency()
    frequency_tag = FrequencyTag()
    start_timestamp = StartTimestamp()
    start_timestamp_tag = StartTimestampTag()
    end_timestamp = EndTimestamp()
    end_timestamp_tag = EndTimestampTag()
    notify_users = NotifyUsers()
    notify_users_tag = NotifyUsersTag()
    triggers_on = TriggersOn()
    triggers_on_tag = TriggersOnTag()
    do = Do()
    do_tag = DoTag()


class ResourceMonitor:
    def __init__(self):
        self.attr = ResourceMonitorAttrs()
        self.session = 'session'
        self.qry = ""

    def set_name(self,name):
        self.attr.name = name 

    def set_name_tag(self,name_tag):
        self.attr.name_tag = name_tag

    def set_credit_quota(self,credit_quota):
        self.attr.credit_quota = credit_quota

    def set_credit_quota_tag(self,credit_quota_tag):
        self.attr.credit_quota_tag = credit_quota_tag

    def set_frequency(self,frequency):
        self.attr.frequency = frequency

    def set_frequency_tag(self,frequency_tag):
        self.attr.frequency_tag = frequency_tag

    def set_start_timestmap(self,start_timestamp):
        self.attr.start_timestamp = start_timestamp

    def set_start_timestamp_tag(self,start_timestamp_tag):
        self.attr.start_timestamp_tag = start_timestamp_tag

    def set_end_timestamp(self,end_timestamp):
        self.attr.end_timestamp = end_timestamp

    def set_end_timestamp_tag(self,end_timestamp_tag):
        self.attr.end_timestamp_tag = end_timestamp_tag

    def set_notify_users(self,notify_users):
        self.attr.notify_users = notify_users

    def set_notify_users_tag(self,notify_users_tag):
        self.attr.notify_users_tag = notify_users_tag
    
    def set_triggers_on(self,triggers_on):
        self.attr.triggers_on = triggers_on
    
    def set_triggers_on_tag(self,triggers_on_tag):
        self.attr.triggers_on_tag = triggers_on_tag

    def set_do(self,do):
        self.attr.do = do
    
    def set_do_tag(self,do_tag):
        self.attr.do_tag = do_tag

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
        set_flag(gv._triggers_on_tag,"_triggers_on")
        set_flag(gv._do_tag,"_do")


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
                    self.qry = f" {self.qry} {self.attr.credit_quota_tag}  = {self.attr.credit_quota} "
                if prop == gv._frequency_tag:
                    self.qry = f" {self.qry} {self.attr.frequency_tag} = {self.attr.frequency} "
                if prop == gv._start_timestamp_tag:
                    self.qry = f" {self.qry} {self.attr.start_timestamp_tag} = {self.attr.start_timestamp} "
                if prop == gv._end_timestamp_tag:
                    self.qry = f" {self.qry} {self.attr.end_timestamp_tag} = {self.attr.end_timestamp} "
                if prop == gv._notify_users_tag:
                    self.qry = f" {self.qry} {self.attr.notify_users_tag} = {self.attr.notify_users} "
                if prop == gv._triggers_on_tag:
                    self.qry = f" {self.qry} {self.attr.triggers_on_tag} = {self.attr.triggers_on} "
                if prop == gv._do_tag:
                    self.qry = f" {self.qry} {self.attr.do_tag} = {self.attr.do} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_resource_monitor_qry()
        self.add_properties_to_query()


def main(**kwargs):
    rm = ResourceMonitor()

    rm.set_name(kwargs[gv._name_tag])
    rm.set_name_tag(gv._name_tag)

    rm.set_credit_quota(kwargs[gv._credit_quota_tag])
    rm.set_credit_quota_tag(gv._credit_quota_tag)

    rm.set_frequency(kwargs[gv._frequency_tag])
    rm.set_frequency_tag(gv._frequency_tag)

    rm.set_start_timestmap(kwargs[gv._start_timestamp_tag])
    rm.set_start_timestamp_tag(gv._start_timestamp_tag)

    rm.set_end_timestamp(kwargs[gv._end_timestamp_tag])
    rm.set_end_timestamp_tag(gv._end_timestamp_tag)

    rm.set_notify_users(kwargs[gv._notify_users_tag])
    rm.set_notify_users_tag(gv._notify_users_tag)

    rm.set_triggers_on(kwargs[gv._triggers_on_tag])
    rm.set_triggers_on_tag(gv._triggers_on_tag)

    rm.set_do(kwargs[gv._do_tag])
    rm.set_do_tag(gv._do_tag)

    rm.prepare_query()

    return rm.qry
