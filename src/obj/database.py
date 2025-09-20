import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../processing'))



from vars.gvobject import Config as cfg , Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from vars.obj.database.gvdatabase import DatabaseTag as tags
from dep import deploy
from setup import privilege 
from .baseobj import BaseObject 


class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.is_new_database(session=instance.parent.session, database_name=value)
        if ( vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__) 
            and not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
            and not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__)
            ):
            instance._name = value


    def __delete__(self,instance):
        del instance._name

class DataRetentionTimeInDays:
    def __get__(self,instance,owner):
        return instance._data_retention_time_in_days
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._data_retention_time_in_days = value
        else:
            vv.is_positive_number(value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_between(value,tags.min_allowed_value().get(tags.DATA_RETENTION_TIME_IN_DAYS),tags.max_allowed_value().get(tags.DATA_RETENTION_TIME_IN_DAYS),instance.parent.__class__.__name__,self.__class__.__name__)
            instance._data_retention_time_in_days = value

    
    def __delete__(self,instance):
        del instance._data_retention_time_in_days

class MaxDataExtensionTimeInDays:
    def __get__(self,instance,owner):
        return instance._max_data_extension_time_in_days
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._max_data_extension_time_in_days = value
        else:
            vv.is_positive_number(value,instance.parent.__class__.__name__,self.__class__.__name__)
            vv.is_between(value,tags.min_allowed_value().get(tags.MAX_DATA_EXTENSION_TIME_IN_DAYS),tags.max_allowed_value().get(tags.MAX_DATA_EXTENSION_TIME_IN_DAYS),instance.parent.__class__.__name__,self.__class__.__name__)    
            instance._max_data_extension_time_in_days = value

    def __delete__(self,instance):
        del instance._max_data_extension_time_in_days


class ExternalVolume:
    def __get__(self,instance,owner):
        return instance._external_volume
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._external_volume = value
        else:
            vo.is_valid_external_volume(session=instance.parent.session,external_volume_identifier=value,object_type=self.__class__.__name__)
            instance._external_volume=value

    def __delete__(self,instance):
        del instance._external_volume

class Catalog:
    def __get__(self,instance,owner):
        return instance._catalog
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._catalog=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vo.is_valid_catalog(session=instance.parent.session,catalog_identifier=value,object_type=self.__class__.__name__)
            instance._catalog=value

    def __delete__(self,instance):
        del instance._catalog


class ReplaceInvalidCharacters:
    def __get__(self,instance,owner):
        return instance._replace_invalid_characters
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._replace_invalid_characters = value
        elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._replace_invalid_characters = value

    def __delete__(self,instance):
        del instance._replace_invalid_characters


class DefaultDdlCollation:
    def __get__(self,instance,owner):
        return instance._default_ddl_collation
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._default_ddl_collation=value
        else:
            vv.is_valid_collation_specifier(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,valid_specifiers=tags.allowed_value_list().get(tags.DEFAULT_DDL_COLLATION))
            instance._default_ddl_collation = f"'{value}'"

    def __delete__(self,instance):
        del instance._default_ddl_collation


class LogLevel:
    def __get__(self,instance,owner):
        return instance._log_level
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._log_level=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.LOG_LEVEL),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._log_level = f"'{value}'"

    def __delete__(self,instance):
        del instance._log_level

class TraceLevel:
    def __get__(self,instance,owner):
        return instance._trace_level
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._trace_level=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.TRACE_LEVEL),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._trace_level = f"'{value}'"

    def __delete__(self,instance):
        del instance._trace_level

class StorageSerializationPolicy:
    def __get__(self,instance,owner):
        return instance._storage_serialization_policy
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._storage_serialization_policy = value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.STORAGE_SERIALIZATION_POLICY),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._storage_serialization_policy = value

    def __delete__(self,instance):
        del instance._storage_serialization_policy


class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._comment = value
        else:
            instance._comment = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._comment

class DatabaseAttrs:
    def __init__(self,parent):
        self.parent = parent

    name = Name()

    data_retention_time_in_days = DataRetentionTimeInDays()

    max_data_extension_time_in_days = MaxDataExtensionTimeInDays()

    external_volume = ExternalVolume()

    catalog = Catalog()

    replace_invalid_characters = ReplaceInvalidCharacters()

    default_ddl_collation = DefaultDdlCollation()

    log_level=LogLevel()
    trace_level=TraceLevel()

    storage_serialization_policy = StorageSerializationPolicy()

    comment = Comment()


class Database(BaseObject):
    def __init__(self,session,user_id,logger):
        super().__init__(session, user_id, logger)
        self.attr = DatabaseAttrs(self)

    def set_name(self, value):
        self.attr.name = value

    def set_name_tag(self, value):
        self.attr.name_tag = value

    def set_data_retention_time_in_days(self, value):
        self.attr.data_retention_time_in_days = value

    def set_max_data_extension_time_in_days(self, value):
        self.attr.max_data_extension_time_in_days = value

    def set_external_volume(self, value):
        self.attr.external_volume = value


    def set_catalog(self, value):
        self.attr.catalog = value

    def set_replace_invalid_characters(self, value):
        self.attr.replace_invalid_characters = value

    def set_default_ddl_collation(self, value):
        self.attr.default_ddl_collation = value

    def set_log_level(self, value):
        self.attr.log_level = value

    def set_trace_level(self, value):
        self.attr.trace_level = value

    def set_storage_serialization_policy(self, value):
        self.attr.storage_serialization_policy = value

    def set_comment(self, value):
        self.attr.comment = value


    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.NAME,"_name")
        set_flag(tags.DATA_RETENTION_TIME_IN_DAYS,"_data_retention_time_in_days")
        set_flag(tags.MAX_DATA_EXTENSION_TIME_IN_DAYS,"_max_data_extension_time_in_days")
        set_flag(tags.EXTERNAL_VOLUME,"_external_volume")
        set_flag(tags.CATALOG,"_catalog")
        set_flag(tags.REPLACE_INVALID_CHARACTERS,"_replace_invalid_characters")
        set_flag(tags.DEFAULT_DDL_COLLATION,"_default_ddl_collation")
        set_flag(tags.LOG_LEVEL,"_log_level")
        set_flag(tags.TRACE_LEVEL,"_trace_level")
        set_flag(tags.STORAGE_SERIALIZATION_POLICY,"_storage_serialization_policy")
        set_flag(tags.COMMENT,"_comment")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"CREATE DATABASE  {self.attr.name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.DATA_RETENTION_TIME_IN_DAYS:
                    self.qry = f" {self.qry} {tags.DATA_RETENTION_TIME_IN_DAYS} = {self.attr.data_retention_time_in_days} "
                if prop == tags.MAX_DATA_EXTENSION_TIME_IN_DAYS:
                    self.qry = f" {self.qry} {tags.MAX_DATA_EXTENSION_TIME_IN_DAYS} = {self.attr.max_data_extension_time_in_days} "
                if prop == tags.EXTERNAL_VOLUME:
                    self.qry = f" {self.qry} {tags.EXTERNAL_VOLUME} = {self.attr.external_volume} "
                if prop == tags.CATALOG:
                    self.qry = f" {self.qry} {tags.CATALOG} = {self.attr.catalog} "
                if prop == tags.REPLACE_INVALID_CHARACTERS:
                    self.qry = f" {self.qry} {tags.REPLACE_INVALID_CHARACTERS} = {self.attr.replace_invalid_characters} "
                if prop == tags.DEFAULT_DDL_COLLATION:
                    self.qry = f" {self.qry} {tags.DEFAULT_DDL_COLLATION} = {self.attr.default_ddl_collation} "
                if prop == tags.LOG_LEVEL:
                    self.qry = f" {self.qry} {tags.LOG_LEVEL} = {self.attr.log_level} "
                if prop == tags.TRACE_LEVEL:
                    self.qry = f" {self.qry} {tags.TRACE_LEVEL} = {self.attr.trace_level} "
                if prop == tags.STORAGE_SERIALIZATION_POLICY:
                    self.qry = f" {self.qry} {tags.STORAGE_SERIALIZATION_POLICY} = {self.attr.storage_serialization_policy} "
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()

    def grant_default_privileges(self,*largs):
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges[self.__class__.__name__.upper()]:
                if len(largs)==0:
                    priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = self.__class__.__name__.upper(),object_identifier=self.attr.name,role = role)
                else:
                    priv_inst.grant_privilege_on_object_to_role(privilege_type=privileges, object_type=self.__class__.__name__.upper(), object_identifier='DB_CONFIG', role=role)


    def create_database(self):
        self.execute_final_query()

    def create_object(self,*largs,**kwargs):
        self.logger.info(f'dictionary passed {kwargs}')

        if len(largs) != 0:
            self.logger.info(' list args passed')
            self.qry = f"CREATE OR REPLACE DATABASE {kwargs[tags.NAME]}"
            self.logger.info('calling create database')
            self.create_database()
            self.logger.info('granting default privileges')
            self.grant_default_privileges(*['initial'])
        else:
            self.logger.info('set name')
            self.set_name(kwargs[tags.NAME])

            self.logger.info('set DATA_RETENTION_TIME_IN_DAYS')
            self.set_data_retention_time_in_days(kwargs[tags.DATA_RETENTION_TIME_IN_DAYS])

            self.logger.info('set MAX_DATA_EXTENSION_TIME_IN_DAYS')
            self.set_max_data_extension_time_in_days(kwargs[tags.MAX_DATA_EXTENSION_TIME_IN_DAYS])

            self.logger.info('set EXTERNAL_VOLUME')
            self.set_external_volume(kwargs[tags.EXTERNAL_VOLUME])

            self.logger.info('set CATALOG')
            self.set_catalog(kwargs[tags.CATALOG])

            self.logger.info('set REPLACE_INVALID_CHARACTERS')
            self.set_replace_invalid_characters(kwargs[tags.REPLACE_INVALID_CHARACTERS])

            self.logger.info('set DEFAULT_DDL_COLLATION')
            self.set_default_ddl_collation(kwargs[tags.DEFAULT_DDL_COLLATION])

            self.logger.info('set LOG_LEVEL')
            self.set_log_level(kwargs[tags.LOG_LEVEL])

            self.logger.info('set TRACE_LEVEL')
            self.set_trace_level(kwargs[tags.TRACE_LEVEL])

            self.logger.info('set STORAGE_SERIALIZATION_POLICY')
            self.set_storage_serialization_policy(kwargs[tags.STORAGE_SERIALIZATION_POLICY])

            self.logger.info('set COMMENT')
            self.set_comment(kwargs[tags.COMMENT])

            self.logger.info('preapare query')
            self.prepare_query()

            self.logger.info('execute query')
            self.create_database()

            self.logger.info('grant default priv')
            self.grant_default_privileges()
            
            self.logger.info('create deployment entry')
            self.create_deployment_entry(object_name=self.attr.name,object_type=self.__class__.__name__,object_database='NA',object_schema='NA')

            self.logger.info('writing file to git')
            self.write_file_to_git(object_name=self.attr.name,object_type=self.__class__.__name__,object_database='NA',object_schema='NA')
            