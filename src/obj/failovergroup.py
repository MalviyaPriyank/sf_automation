import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.failovergroup.gvfailovergroup import FailoverGroupTag as tags



class FGName:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        instance._name = value

    def __delete__(self, instance):
        del instance._name


class FGObjectTypes:
    def __get__(self, instance, owner):
        return instance._object_types

    def __set__(self, instance, value):
        # expects list like ['DATABASES','SHARES']
        if isinstance(value, list):
            instance._object_types = f"OBJECT_TYPES = ({', '.join(value)})"
        else:
            instance._object_types = f"OBJECT_TYPES = ({value})"

    def __delete__(self, instance):
        del instance._object_types


class FGAllowedDatabases:
    def __get__(self, instance, owner):
        return instance._allowed_databases

    def __set__(self, instance, value):
        # expects list of database names
        if isinstance(value, list):
            instance._allowed_databases = f"ALLOWED_DATABASES = ({', '.join(value)})"
        else:
            instance._allowed_databases = f"ALLOWED_DATABASES = ({value})"

    def __delete__(self, instance):
        del instance._allowed_databases


class FGAllowedShares:
    def __get__(self, instance, owner):
        return instance._allowed_shares

    def __set__(self, instance, value):
        if isinstance(value, list):
            instance._allowed_shares = f"ALLOWED_SHARES = ({', '.join(value)})"
        else:
            instance._allowed_shares = f"ALLOWED_SHARES = ({value})"

    def __delete__(self, instance):
        del instance._allowed_shares


class FGAllowedAccounts:
    def __get__(self, instance, owner):
        return instance._allowed_accounts

    def __set__(self, instance, value):
        if isinstance(value, list):
            instance._allowed_accounts = f"ALLOWED_ACCOUNTS = ({', '.join(value)})"
        else:
            instance._allowed_accounts = f"ALLOWED_ACCOUNTS = ({value})"

    def __delete__(self, instance):
        del instance._allowed_accounts


class FGReplicationSchedule:
    def __get__(self, instance, owner):
        return instance._replication_schedule

    def __set__(self, instance, value):
        instance._replication_schedule = f"REPLICATION_SCHEDULE = '{value}'"

    def __delete__(self, instance):
        del instance._replication_schedule


class FailoverGroupAttrs:
    name = FGName()
    object_types = FGObjectTypes()
    allowed_databases = FGAllowedDatabases()
    allowed_shares = FGAllowedShares()
    allowed_accounts = FGAllowedAccounts()
    replication_schedule = FGReplicationSchedule()



class FailoverGroup(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = FailoverGroupAttrs()
        self.session = session
        self.logger = logger
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

    def create_object(self, *largs, **kwargs):
        self.logger.info(f"Operating on {self.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        self.logger.info(f"Dictionary passed {kwargs}")
        self.is_create = kwargs[tags.IS_CREATE]

        self.set_name(kwargs[tags.NAME])
        self.set_object_types(kwargs[tags.OBJECT_TYPES])
        self.set_allowed_databases(kwargs[tags.ALLOWED_DATABASES])
        self.set_allowed_shares(kwargs[tags.ALLOWED_SHARES])
        self.set_allowed_accounts(kwargs[tags.ALLOWED_ACCOUNTS])
        self.set_replication_schedule(kwargs[tags.REPLICATION_SCHEDULE])

        self.prepare_query()
        self.execute_final_query()

class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
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
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()

