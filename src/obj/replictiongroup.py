import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))

from .baseobj import BaseObject
from vars.obj.replicationgroup.gvreplicationgroup import ReplicationGroupTag as tags
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from exception.valueexception import InvalidObjectTypeForAllowedDatabases

class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)

    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_database(session=instance.parent.session, database_name=name)
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
                vo.database_exist(session=instance.parent.session,database_name=old_name)
                vo.is_new_database(session=instance.parent.session,database_name=new_name)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to


class ObjectTypes:
    def __get__(self, instance, owner):
        return instance._object_types
    
    def __set__(self, instance, value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        for object in value:
            vv.is_allowed_value(value=object,
                                allowed_list=tags.allowed_value_list().get('OBJECT_TYPES'),
                                object_type=instance.parent.__class__.__name__,
                                attr_name=self.__class__.__name__)
        instance._object_types=value

    def __delete__(self, instance):
        del instance._object_types

class AllowedDatabases:
    def __get__(self, instance, owner):
        return instance._allowed_databases
    def __set__(self, instance, value):
        if 'DATABASES' not in instance._object_types:
            raise InvalidObjectTypeForAllowedDatabases(attr_name=self.__class__.__name__,object_name=instance.parent.__class__.__name__)
        if value=="NONE":
            instance._allowed_databases=value
        else:
            for db in value:
                vo.database_exist(session=instance.parent.session,
                                  database_name=db)
            instance._allowed_databases=value

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
        self.logger = logger.getChild(self.__class__.__name__)
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


class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        obj_inst=ReplicationGroup(session=session,
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

        logger.info("set allowed_integration_types")
        if tags.ALLOWED_INTEGRATION_TYPES in kwargs.keys():
            obj_inst.set_allowed_integration_types(kwargs[tags.ALLOWED_INTEGRATION_TYPES])
        else:
            obj_inst.set_allowed_integration_types('NONE')

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

        logger.info("set ignore_edition_check")
        if tags.IGNORE_EDITION_CHECK in kwargs.keys():
            obj_inst.set_ignore_edition_check(kwargs[tags.IGNORE_EDITION_CHECK])
        else:
            obj_inst.set_ignore_edition_check('NONE')

        logger.info("set error_integration")
        if tags.ERROR_INTEGRATION in kwargs.keys():
            obj_inst.set_error_integration(kwargs[tags.ERROR_INTEGRATION])
        else:
            obj_inst.set_error_integration('NONE')

        logger.info("set tag_clause")
        if tags.TAG_CLAUSE in kwargs.keys():
            obj_inst.set_tag_clause(kwargs[tags.TAG_CLAUSE])
        else:
            obj_inst.set_tag_clause('NONE')

        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
