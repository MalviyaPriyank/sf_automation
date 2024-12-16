
from resourcemonitorglobalvars import *

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

class NameLabel:
    def __get__(self,instance,owner):
        return instance._name_label
    
    def __set__(self,instance,value):
        instance._name_label = value

    def __delete__(self,instance):
        del instance._name_label

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

class CreditQuotaLabel:
    def __get__(self,instance,owner):
        return instance._credit_quota_label
    
    def __set__(self,instance,value):
        instance._credit_quota_label = value
    
    def __delete__(self,instance):
        del instance._credit_quota_label


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

class FrequencyLabel:
    def __get__(self,instance,owner):
        return instance._frequency_label
    
    def __set__(self,instance,value):
        instance._frequency_label = value
    
    def __delete__(self,instance):
        del instance._frequency_label

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

class StartTimestampLabel:
    def __get__(self,instance,owner):
        return instance._start_timestamp_label
    
    def __set__(self,instance,value):
        instance._start_timestamp_label = value
    
    def __delete__(self,instance):
        del instance._start_timestamp_label

class EndTimestamp:
    def __get__(self,instance,owner):
        return instance._end_timestamp
    
    def __set__(self,instance,value):
        instance._end_timestamp = value
    
    def __delete__(self,instance):
        del instance._end_timestamp

class EndTimestampLabel:
    def __get__(self,instance,owner):
        return instance._end_timestamp_label
    
    def __set__(self,instance,value):
        instance._end_timestamp_label = value
    
    def __delete__(self,instance):
        del instance._end_timestamp_label


class NotifyUsers:
    def __get__(self,instance,owner):
        return instance._notify_users
    
    def __set__(self,instance,value):
        instance._notify_users = value
    
    def __delete__(self,instance):
        del instance._notify_users


class NotifyUsersLabel:
    def __get__(self,instance,owner):
        return instance._notify_users_label
    
    def __set__(self,instance,value):
        instance._notify_users_label = value
    
    def __delete__(self,instance):
        del instance._notify_users_label

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

class TriggersLabel:
    def __get__(self,instance,owner):
        return instance._triggers_label
    
    def __set__(self,instance,value):
        instance._triggers_label = value
    
    def __delete__(self,instance):
        del instance._triggers_label



class ResourceMonitorAttrs:
    name = Name()
    name_label = NameLabel()
    credit_quota = CreditQuota()
    credit_quota_label = CreditQuotaLabel()
    frequency = Frequency()
    frequency_label = FrequencyLabel()
    start_timestamp = StartTimestamp()
    start_timestamp_label = StartTimestampLabel()
    end_timestamp = EndTimestamp()
    end_timestamp_label = EndTimestampLabel()
    notify_users = NotifyUsers()
    notify_users_label = NotifyUsersLabel()
    triggers = Triggers()
    triggers_label = TriggersLabel()


class ResourceMonitor:
    def __init__(self,session):
        self.attr = ResourceMonitorAttrs()
        self.session = session
        self.qry = ""

    def set_name(self,name):
        self.attr.name = name 

    def set_name_label(self,name_label):
        self.attr.name_label = name_label

    def set_credit_quota(self,credit_quota):
        self.attr.credit_quota = credit_quota

    def set_credit_quota_label(self,credit_quota_label):
        self.attr.credit_quota_label = credit_quota_label

    def set_frequency(self,frequency):
        self.attr.frequency = frequency

    def set_frequency_label(self,frequency_label):
        self.attr.frequency_label = frequency_label

    def set_start_timestmap(self,start_timestamp):
        self.attr.start_timestamp = start_timestamp

    def set_start_timestamp_label(self,start_timestamp_label):
        self.attr.start_timestamp_label = start_timestamp_label

    def set_end_timestamp(self,end_timestamp):
        self.attr.end_timestamp = end_timestamp

    def set_end_timestamp_label(self,end_timestamp_label):
        self.attr.end_timestamp_label = end_timestamp_label

    def set_notify_users(self,notify_users):
        self.attr.notify_users = notify_users

    def set_notify_users_label(self,notify_users_label):
        self.attr.notify_users_label = notify_users_label
    
    def set_triggers(self,threshold,action):
        self.attr.triggers = threshold,action
    
    def set_triggers_label(self,triggers_label):
        self.attr.triggers_label = triggers_label


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
                    self.qry = f" {self.qry} {self.attr.credit_quota_label}  = {self.attr.credit_quota} "
                if prop == 'frequency':
                    self.qry = f" {self.qry} {self.attr.frequency_label} = {self.attr.frequency} "
                if prop == 'start_timestamp':
                    self.qry = f" {self.qry} {self.attr.start_timestamp_label} = {self.attr.start_timestamp} "
                if prop == 'end_timestamp':
                    self.qry = f" {self.qry} {self.attr.end_timestamp_label} = {self.attr.end_timestamp} "
                if prop == 'notify_users':
                    self.qry = f" {self.qry} {self.attr.notify_users_label} = {self.attr.notify_users} "
                if prop == 'triggers':
                    self.qry = f" {self.qry} {self.attr.triggers_label} = {self.attr.triggers} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_resource_monitor_qry()
        self.add_properties_to_query()


def main(session,**kwargs):
    rm = ResourceMonitor()
    rm_labels = RML()
    rm.set_name(kwargs[rm_labels._name_label])
    rm.set_name_label(rm_labels._name_label)
    rm.set_credit_quota(kwargs[rm_labels._credit_quota_label])
    rm.set_credit_quota_label(rm_labels._credit_quota_label)
    rm.set_frequency(kwargs[rm_labels._frequency_label])
    rm.set_frequency_label(rm_labels._frequency_label)
    rm.set_start_timestmap(kwargs[rm_labels._start_timestamp_label])
    rm.set_start_timestamp_label(rm_labels._start_timestamp_label)
    rm.set_end_timestamp(kwargs[rm_labels._end_timestamp_label])
    rm.set_end_timestamp_label(rm_labels._end_timestamp_label)
    rm.set_notify_users(kwargs[rm_labels._notify_users_label])
    rm.set_notify_users_label(rm_labels._notify_users_label)
    rm.set_triggers(kwargs[rm_labels._triggers_label])
    rm.set_triggers_label(rm_labels._triggers_label)

    rm.prepare_query()

    return rm.qry
