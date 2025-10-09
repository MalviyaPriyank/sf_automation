import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.replicationgroup.gvreplicationgroup import ReplicationGroupTag as tags

class RGName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class RGObjectTypes:
    def __get__(self, instance, owner):
        return instance._object_types
    def __set__(self, instance, value):
        # expects list or comma-separated strings
        if isinstance(value, list):
            instance._object_types = f"OBJECT_TYPES = ({', '.join(value)})"
        else:
            instance._object_types = f"OBJECT_TYPES = ({value})"
    def __delete__(self, instance):
        del instance._object_types

class RGAllowedDatabases:
    def __get__(self, instance, owner):
        return instance._allowed_databases
    def __set__(self, instance, value):
        if isinstance(value, list):
            instance._allowed_databases = f"ALLOWED_DATABASES = ({', '.join(value)})"
        else:
            instance._allowed_databases = f"ALLOWED_DATABASES = ({value})"
    def __delete__(self, instance):
        del instance._allowed_databases

class RGAllowedShares:
    def __get__(self, instance, owner):
        return instance._allowed_shares
    def __set__(self, instance, value):
        if isinstance(value, list):
            instance._allowed_shares = f"ALLOWED_SHARES = ({', '.join(value)})"
        else:
            instance._allowed_shares = f"ALLOWED_SHARES = ({value})"
    def __delete__(self, instance):
        del instance._allowed_shares

class RGAllowedIntegrationTypes:
    def __get__(self, instance, owner):
        return instance._allowed_integration_types
    def __set__(self, instance, value):
        if isinstance(value, list):
            instance._allowed_integration_types = f"ALLOWED_INTEGRATION_TYPES = ({', '.join(value)})"
        else:
            instance._allowed_integration_types = f"ALLOWED_INTEGRATION_TYPES = ({value})"
    def __delete__(self, instance):
        del instance._allowed_integration_types

class RGAllowedAccounts:
    def __get__(self, instance, owner):
        return instance._allowed_accounts
    def __set__(self, instance, value):
        if isinstance(value, list):
            instance._allowed_accounts = f"ALLOWED_ACCOUNTS = ({', '.join(value)})"
        else:
            instance._allowed_accounts = f"ALLOWED_ACCOUNTS = ({value})"
    def __delete__(self, instance):
        del instance._allowed_accounts

class RGReplicationSchedule:
    def __get__(self, instance, owner):
        return instance._replication_schedule
    def __set__(self, instance, value):
        instance._replication_schedule = f"REPLICATION_SCHEDULE = '{value}'"
    def __delete__(self, instance):
        del instance._replication_schedule

class RGIgnoreEditionCheck:
    def __get__(self, instance, owner):
        return instance._ignore_edition_check
    def __set__(self, instance, value):
        # expects Boolean or "TRUE"/"FALSE"
        if isinstance(value, bool):
            val = "TRUE" if value else "FALSE"
        else:
            val = value
        instance._ignore_edition_check = f"IGNORE EDITION CHECK = {val}"
    def __delete__(self, instance):
        del instance._ignore_edition_check

class RGErrorIntegration:
    def __get__(self, instance, owner):
        return instance._error_integration
    def __set__(self, instance, value):
        instance._error_integration = f"ERROR_INTEGRATION = {value}"
    def __delete__(self, instance):
        del instance._error_integration

class RGTagClause:
    def __get__(self, instance, owner):
        return instance._tag_clause
    def __set__(self, instance, value):
        # expects dict of tag_name: tag_value
        if isinstance(value, dict):
            clause = ", ".join(f"{k} = '{v}'" for k, v in value.items())
        else:
            # single tag, e.g. {"k":"v"}
            k, v = next(iter(value.items()))
            clause = f"{k} = '{v}'"
        instance._tag_clause = f"TAG ({clause})"
    def __delete__(self, instance):
        del instance._tag_clause

class ReplicationGroupAttrs:
    name = RGName()
    object_types = RGObjectTypes()
    allowed_databases = RGAllowedDatabases()
    allowed_shares = RGAllowedShares()
    allowed_integration_types = RGAllowedIntegrationTypes()
    allowed_accounts = RGAllowedAccounts()
    replication_schedule = RGReplicationSchedule()
    ignore_edition_check = RGIgnoreEditionCheck()
    error_integration = RGErrorIntegration()
    tag_clause = RGTagClause()

class ReplicationGroup(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = ReplicationGroupAttrs()
        self.session = session
        self.logger = logger
        self.user_id = user_id

    # setter methods
    def set_name(self, val=None): self.attr.name = val
    def set_object_types(self, val=None): self.attr.object_types = val
    def set_allowed_databases(self, val=None): self.attr.allowed_databases = val
    def set_allowed_shares(self, val=None): self.attr.allowed_shares = val
    def set_allowed_integration_types(self, val=None): self.attr.allowed_integration_types = val
    def set_allowed_accounts(self, val=None): self.attr.allowed_accounts = val
    def set_replication_schedule(self, val=None): self.attr.replication_schedule = val
    def set_ignore_edition_check(self, val=None): self.attr.ignore_edition_check = val
    def set_error_integration(self, val=None): self.attr.error_integration = val
    def set_tag_clause(self, val=None): self.attr.tag_clause = val

    def set_object_properties_flag(self):
        self.flag_dic = {}
        def set_flag(tag, attrname):
            self.flag_dic[tag] = 1 if getattr(self.attr, attrname, "NONE") != "NONE" else 0

        set_flag(tags.OBJECT_TYPES, "object_types")
        set_flag(tags.ALLOWED_DATABASES, "allowed_databases")
        set_flag(tags.ALLOWED_SHARES, "allowed_shares")
        set_flag(tags.ALLOWED_INTEGRATION_TYPES, "allowed_integration_types")
        set_flag(tags.ALLOWED_ACCOUNTS, "allowed_accounts")
        set_flag(tags.REPLICATION_SCHEDULE, "replication_schedule")
        set_flag(tags.IGNORE_EDITION_CHECK, "ignore_edition_check")
        set_flag(tags.ERROR_INTEGRATION, "error_integration")
        set_flag(tags.TAG_CLAUSE, "tag_clause")

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_replication_group_qry(self):
        self.qry = f"CREATE REPLICATION GROUP {self.attr.name[0]}"

    def add_properties_to_query(self):
        for prop in self.property_lst:
            if prop == tags.OBJECT_TYPES:
                self.qry += f" {self.attr.object_types}"
            if prop == tags.ALLOWED_DATABASES:
                self.qry += f" {self.attr.allowed_databases}"
            if prop == tags.ALLOWED_SHARES:
                self.qry += f" {self.attr.allowed_shares}"
            if prop == tags.ALLOWED_INTEGRATION_TYPES:
                self.qry += f" {self.attr.allowed_integration_types}"
            if prop == tags.ALLOWED_ACCOUNTS:
                self.qry += f" {self.attr.allowed_accounts}"
            if prop == tags.REPLICATION_SCHEDULE:
                self.qry += f" {self.attr.replication_schedule}"
            if prop == tags.IGNORE_EDITION_CHECK:
                self.qry += f" {self.attr.ignore_edition_check}"
            if prop == tags.ERROR_INTEGRATION:
                self.qry += f" {self.attr.error_integration}"
            if prop == tags.TAG_CLAUSE:
                self.qry += f" {self.attr.tag_clause}"

    def alter_object(self):
        for prop in self.property_lst:
            # handle various SET or UNSET or ADD/REMOVE etc
            if prop == tags.REPLICATION_SCHEDULE:
                self.qry = f"ALTER REPLICATION GROUP {self.attr.name[0]} SET {self.attr.replication_schedule}"
                self.execute_final_query()
            if prop == tags.ERROR_INTEGRATION:
                self.qry = f"ALTER REPLICATION GROUP {self.attr.name[0]} SET {self.attr.error_integration}"
                self.execute_final_query()
            # more conditions for OBJECT_TYPES, ALLOWED_DATABASES, ALLOWED_SHARES, ADD/REMOVE accounts, rename, tags
            if prop == tags.TAG_CLAUSE:
                self.qry = f"ALTER REPLICATION GROUP {self.attr.name[0]} {self.attr.tag_clause}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER REPLICATION GROUP {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming replication group {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_replication_group_qry()
            self.add_properties_to_query()
        else:
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        self.logger.info(f"Operating on {self.__class__.__name__}, create flag: {kwargs.get(tags.IS_CREATE)}")
        self.is_create = kwargs.get(tags.IS_CREATE)
        self.set_name(kwargs.get(tags.NAME))
        self.set_object_types(kwargs.get(tags.OBJECT_TYPES))
        self.set_allowed_databases(kwargs.get(tags.ALLOWED_DATABASES))
        self.set_allowed_shares(kwargs.get(tags.ALLOWED_SHARES))
        self.set_allowed_integration_types(kwargs.get(tags.ALLOWED_INTEGRATION_TYPES))
        self.set_allowed_accounts(kwargs.get(tags.ALLOWED_ACCOUNTS))
        self.set_replication_schedule(kwargs.get(tags.REPLICATION_SCHEDULE))
        self.set_ignore_edition_check(kwargs.get(tags.IGNORE_EDITION_CHECK))
        self.set_error_integration(kwargs.get(tags.ERROR_INTEGRATION))
        self.set_tag_clause(kwargs.get(tags.TAG_CLAUSE))

        self.prepare_query()
        self.execute_final_query()
