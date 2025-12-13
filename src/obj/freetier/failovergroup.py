import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from src.obj.baseobj import BaseObject
from vars.obj.failovergroup.gvfailovergroup import FailoverGroupTag as tags
from validation.validatevalue import ValidateValue as vv
from src.usr.user import ChatHistory

class Name:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
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
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

        instance._name = value

    def __delete__(self, instance):
        del instance._name


class ObjectTypes:
    def __get__(self, instance, owner):
        return instance._object_types

    def __set__(self, instance, value):
        instance._object_types=value
        

    def __delete__(self, instance):
        del instance._object_types


class AllowedDatabases:
    def __get__(self, instance, owner):
        return instance._allowed_databases

    def __set__(self, instance, value):
        instance._allowed_databases=value

    def __delete__(self, instance):
        del instance._allowed_databases


class AllowedShares:
    def __get__(self, instance, owner):
        return instance._allowed_shares

    def __set__(self, instance, value):
        instance._allowed_shares=value

    def __delete__(self, instance):
        del instance._allowed_shares


class AllowedIntegrationTypes:
    def __get__(self, instance, owner):
        return instance._allowed_integration_types

    def __set__(self, instance, value):
        instance._allowed_integration_types=value

    def __delete__(self, instance):
        del instance._allowed_integration_types


class ReplicationSchedule:
    def __get__(self, instance, owner):
        return instance._replication_schedule

    def __set__(self, instance, value):
        instance._replication_schedule = value

    def __delete__(self, instance):
        del instance._replication_schedule

class FailoverGroupAttrs:
    name = Name()
    object_types = ObjectTypes()
    allowed_databases = AllowedDatabases()
    allowed_shares = AllowedShares()
    allowed_integration_types = AllowedIntegrationTypes()
    replication_schedule = ReplicationSchedule()



class FailoverGroup(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = FailoverGroupAttrs()
        self.session = session
        self.logger = logger.getChild(self.__class__.__name__)
        self.user_id = user_id


    def set_name(self, val=None): self.attr.name = val
    def set_object_types(self, val=None): self.attr.object_types = val
    def set_allowed_databases(self, val=None): self.attr.allowed_databases = val
    def set_allowed_shares(self, val=None): self.attr.allowed_shares = val
    def set_allowed_accounts(self, val=None): self.attr.allowed_accounts = val
    def set_replication_schedule(self, val=None): self.attr.replication_schedule = val


    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(tag, attr):
            self.flag_dic[tag] = 1 if getattr(self.attr, attr) != "NONE" else 0

        set_flag(tags.OBJECT_TYPES, "object_types")
        set_flag(tags.ALLOWED_DATABASES, "allowed_databases")
        set_flag(tags.ALLOWED_SHARES, "allowed_shares")
        set_flag(tags.ALLOWED_ACCOUNTS, "allowed_accounts")
        set_flag(tags.REPLICATION_SCHEDULE, "replication_schedule")

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, val in self.flag_dic.items() if val == 1]


    def set_create_failover_group_qry(self):
        self.qry = f"CREATE FAILOVER GROUP {self.attr.name[0]}"

    def add_properties_to_query(self):
        for prop in self.property_lst:
            if prop == tags.OBJECT_TYPES:
                self.qry += f" {self.attr.object_types}"
            if prop == tags.ALLOWED_DATABASES:
                self.qry += f" {self.attr.allowed_databases}"
            if prop == tags.ALLOWED_SHARES:
                self.qry += f" {self.attr.allowed_shares}"
            if prop == tags.ALLOWED_ACCOUNTS:
                self.qry += f" {self.attr.allowed_accounts}"
            if prop == tags.REPLICATION_SCHEDULE:
                self.qry += f" {self.attr.replication_schedule}"


    def alter_object(self):
        for prop in self.property_lst:
            if prop == tags.REPLICATION_SCHEDULE:
                self.qry = f"ALTER FAILOVER GROUP {self.attr.name[0]} SET {self.attr.replication_schedule}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER FAILOVER GROUP {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming failover group {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == 'TRUE':
            self.set_create_failover_group_qry()
            self.add_properties_to_query()
        elif self.is_create == 'FALSE':
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=FailoverGroup(session=session,
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

        logger.info("set object_types")
        if tags.OBJECT_TYPES in kwargs.keys():
            obj_inst.set_object_types(kwargs[tags.OBJECT_TYPES])
        else:
            obj_inst.set_object_types('NONE')

        logger.info("set allowed_databases")
        if tags.ALLOWED_DATABASES in kwargs.keys():
            obj_inst.set_allowed_databases(kwargs[tags.ALLOWED_DATABASES])
        else:
            obj_inst.set_allowed_databases('NONE')

        logger.info("set allowed_shares")
        if tags.ALLOWED_SHARES in kwargs.keys():
            obj_inst.set_allowed_shares(kwargs[tags.ALLOWED_SHARES])
        else:
            obj_inst.set_allowed_shares('NONE')

        logger.info("set allowed_accounts")
        if tags.ALLOWED_ACCOUNTS in kwargs.keys():
            obj_inst.set_allowed_accounts(kwargs[tags.ALLOWED_ACCOUNTS])
        else:
            obj_inst.set_allowed_accounts('NONE')

        logger.info("set replication_schedule")
        if tags.REPLICATION_SCHEDULE in kwargs.keys():
            obj_inst.set_replication_schedule(kwargs[tags.REPLICATION_SCHEDULE])
        else:
            obj_inst.set_replication_schedule('NONE')


        logger.info('prepare query')
        obj_inst.prepare_query()

        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                        object_identifier=obj_inst.attr.name[0],
                                        qry=obj_inst.qry)

    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()

