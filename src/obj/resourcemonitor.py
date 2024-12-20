
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../../vars'))

from resourcemonitor_global_vars import *

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
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
        if value == None:
            instance._credit_quota = None
        elif type(value) == int:
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
        if value not in _allowed_values_frequency:
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
        if instance._frequency is None:
            raise ValueError
        elif value == None:
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

class Triggers:
    def __get__(self,instance,owner):
        return instance._triggers
    
    def __set__(self,instance,threshold,action):
        if action not in _allowed_actions_triggers:
            raise ValueError
        else:
            instance._triggers = f" ON {threshold} DO {action}"
    
    def __delete__(self,instance):
        del instance._triggers

class TriggersTag:
    def __get__(self,instance,owner):
        return instance._triggers_tag
    
    def __set__(self,instance,value):
        instance._triggers_tag = value
    
    def __delete__(self,instance):
        del instance._triggers_tag



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
    triggers = Triggers()
    triggers_tag = TriggersTag()


class ResourceMonitor:
    def __init__(self,session):
        self.attr = ResourceMonitorAttrs()
        self.session = session
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
    
    def set_triggers(self,threshold,action):
        self.attr.triggers = threshold,action
    
    def set_triggers_tag(self,triggers_tag):
        self.attr.triggers_tag = triggers_tag


    def set_object_properties_flag(self):
        self.flag_dic = {}
        if self.attr.name is not None:
            self.flag_dic['name'] = 1
        else:
            self.flag_dic['name'] = 0

        if self.attr.credit_quota is not None:
            self.flag_dic['credit_quota'] = 1
        else:
            self.flag_dic['credit_quota'] = 0

        if self.attr.frequency is not None:
            self.flag_dic['frequency'] = 1
        else:
            self.flag_dic['frequency'] = 0

        if self.attr.start_timestamp is not None:
            self.flag_dic['start_timestamp'] = 1
        else:
            self.flag_dic['start_timestamp'] = 0

        if self.attr.end_timestamp is not None:
            self.flag_dic['end_timestamp'] = 1
        else:
            self.flag_dic['end_timestamp'] = 0

        if self.attr.notify_users is not None:
            self.flag_dic['notify_users'] = 1
        else:
            self.flag_dic['notify_users'] = 0
        
        if self.attr.triggers is not None:
            self.flag_dic['triggers'] = 1
        else:
            self.flag_dic['triggers'] = 0


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
                if prop == 'credit_quota':
                    self.qry = f" {self.qry} {self.attr.credit_quota_tag}  = {self.attr.credit_quota} "
                if prop == 'frequency':
                    self.qry = f" {self.qry} {self.attr.frequency_tag} = {self.attr.frequency} "
                if prop == 'start_timestamp':
                    self.qry = f" {self.qry} {self.attr.start_timestamp_tag} = {self.attr.start_timestamp} "
                if prop == 'end_timestamp':
                    self.qry = f" {self.qry} {self.attr.end_timestamp_tag} = {self.attr.end_timestamp} "
                if prop == 'notify_users':
                    self.qry = f" {self.qry} {self.attr.notify_users_tag} = {self.attr.notify_users} "
                if prop == 'triggers':
                    self.qry = f" {self.qry} {self.attr.triggers_tag} = {self.attr.triggers} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_resource_monitor_qry()
        self.add_properties_to_query()


def main(session,**kwargs):
    rm = ResourceMonitor()

    rm.set_name(kwargs[_name_tag])
    rm.set_name_tag(_name_tag)
    rm.set_credit_quota(kwargs[_credit_quota_tag])
    rm.set_credit_quota_tag(_credit_quota_tag)
    rm.set_frequency(kwargs[_frequency_tag])
    rm.set_frequency_tag(_frequency_tag)
    rm.set_start_timestmap(kwargs[_start_timestamp_tag])
    rm.set_start_timestamp_tag(_start_timestamp_tag)
    rm.set_end_timestamp(kwargs[_end_timestamp_tag])
    rm.set_end_timestamp_tag(_end_timestamp_tag)
    rm.set_notify_users(kwargs[_notify_users_tag])
    rm.set_notify_users_tag(_notify_users_tag)
    rm.set_triggers(kwargs[_triggers_tag])
    rm.set_triggers_tag(_triggers_tag)

    rm.prepare_query()

    return rm.qry
