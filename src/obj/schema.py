import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.gvobject import Schema as gv,Config as cfg, Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy
from validation.validateobject import ValidateObject as vo
from setup import privilege
from .baseobj import BaseObject 
from vars.obj.schema.gvschema import SchemaTag as tags

class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.database_exist(session=instance.parent.session, database_name=value)
        instance._database = value
    
    def __delete__(self,instance):
        del instance._database

class Name:   
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)
    
    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_schema(session=instance.parent.session,
                             database_name=instance._database,
                             schema_name=name)
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
                vo.schema_exist(session=instance.parent.session,
                                database_name=instance._database,
                                schema_name=old_name)
                vo.is_new_schema(session=instance.parent.session,
                                 database_name=instance._database,
                                 schema_name=new_name)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"


    def __del__(self,instance):
        del instance._name
        del instance._rename_to


    def __delete__(self,instance):
        del instance._name
        del instance._rename_to

class WithManagedAccess:
    def __get__(self,instance,owner):
        return instance._with_managed_access
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._with_managed_access="NONE"
        else:
            vv.is_bool(value=value, object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._with_managed_access = value
    
    def __delete__(self,instance):
        del instance._with_managed_access

class DataRetentionTimeInDays:
    def __get__(self,instance,owner):
        return instance._data_retention_time_in_days
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._data_retention_time_in_days = value
        else:
            vv.is_positive_number(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_between(value,tags.min_allowed_value().get(tags.DATA_RETENTION_TIME_IN_DAYS),tags.max_allowed_value().get(tags.DATA_RETENTION_TIME_IN_DAYS),instance.parent.__class__.__name__,self.__class__.__name__)
            instance._data_retention_time_in_days = value
    
    def __delete__(self,instance):
        del instance._data_retention_time_in_days

class MaxDataExtensionTimeInDays:
    def __get__(self,instance,owner):
        return instance._max_data_extension_time_in_days
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance.parent.logger.info("setting as none") 
            instance._max_data_extension_time_in_days = value
        else:
            instance.parent.logger.info("checking for positive number") 
            vv.is_positive_number(value,instance.parent.__class__.__name__,self.__class__.__name__)
            instance.parent.logger.info("checking for range number") 
            vv.is_between(value,tags.min_allowed_value().get(tags.MAX_DATA_EXTENSION_TIME_IN_DAYS),tags.max_allowed_value().get(tags.MAX_DATA_EXTENSION_TIME_IN_DAYS),instance.parent.__class__.__name__,self.__class__.__name__)
            instance._max_data_extension_time_in_days = value

    def __delete__(self,instance):
        del instance._max_data_extension_time_in_days

class ExternalVolume:
    def __get__(self,instance,owner):
        return instance._external_volume
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._external_volume=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vo.is_valid_external_volume(session=instance.parent.session,external_volume_identifier=value,object_type=instance.parent.__class__.__name__)
            instance._external_volume = value

    def __delete__(self,instance):
        del instance._external_volume

class Catalog:
    def __get__(self,instance,owner):
        return instance._catalog
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._catalog = value
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
            instance._replace_invalid_characters = "FALSE"
        else: 
            vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__)
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
            instance._default_ddl_collation = value

    def __delete__(self,instance):
        del instance._default_ddl_collation

class LogLevel:
    def __get__(self,instance,owner):
        return instance._log_level
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._log_level = value
        else:
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.LOG_LEVEL),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._log_level = value

    def __delete__(self,instance):
        del instance._log_level

class TraceLevel:
    def __get__(self,instance,owner):
        return instance._trace_level
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._trace_level = value
        else:
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.TRACE_LEVEL),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._trace_level = value

    def __delete__(self,instance):
        del instance._trace_level

class StorageSerializationPolicy:
    def __get__(self,instance,owner):
        return instance._storage_serialization_policy
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._storage_serialization_policy = value
        else:
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.STORAGE_SERIALIZATION_POLICY),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._storage_serialization_policy = value

    def __delete__(self,instance):
        del instance._storage_serialization_policy

class ClassificationProfile:
    def __get__(self,instance,owner):
        return instance._classification_profile
    
    def __set__(self,instance,value):
        instance._classification_profile = "NONE"

    def __delete__(self,instance):
        del instance._classification_profile

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = f'"{value}"'
    
    def __delete__(self,instance):
        del instance._comment


class SchemaAttrs:
    def __init__(self,parent):
        self.parent = parent

    database = Database()
        
    name = Name()
    with_managed_access = WithManagedAccess()
    data_retention_time_in_days = DataRetentionTimeInDays()
    max_data_extension_time_in_days = MaxDataExtensionTimeInDays()
    external_volume = ExternalVolume()
    catalog = Catalog()
    replace_invalid_characters = ReplaceInvalidCharacters()
    default_ddl_collation = DefaultDdlCollation()
    log_level = LogLevel()
    trace_level = TraceLevel()
    storage_serialization_policy = StorageSerializationPolicy()
    classification_profile = ClassificationProfile()
    comment = Comment()

class Schema(BaseObject):
    def __init__(self, session, user_id):
        super().__init__(session, user_id)
        self.attr = SchemaAttrs(self)

    def set_database(self, value):
        self.attr.database = value

    def set_name(self, value):
        self.attr.name = value

    def set_with_managed_access(self, value):
        self.attr.with_managed_access = value

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

    def set_classification_profile(self, value):
        self.attr.classification_profile = value

    def set_comment(self, value):
        self.attr.comment = value

    def set_qualified_name(self):
        self.qualified_name = f"{self.attr.database}.{self.attr.name}"


    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.WITH_MANAGED_ACCESS,"_with_managed_access")
        set_flag(tags.DATA_RETENTION_TIME_IN_DAYS,"_data_retention_time_in_days")
        set_flag(tags.MAX_DATA_EXTENSION_TIME_IN_DAYS,"_max_data_extension_time_in_days")
        set_flag(tags.EXTERNAL_VOLUME,"_external_volume")
        set_flag(tags.CATALOG,"_catalog")
        set_flag(tags.REPLACE_INVALID_CHARACTERS,"_replace_invalid_characters")
        set_flag(tags.DEFAULT_DDL_COLLATION,"_default_ddl_collation")
        set_flag(tags.LOG_LEVEL,"_log_level")
        set_flag(tags.TRACE_LEVEL,"_trace_level")
        set_flag(tags.STORAGE_SERIALIZATION_POLICY,"_storage_serialization_policy")
        set_flag(tags.CLASSIFICATION_PROFILE,"_classification_profile")
        set_flag(tags.COMMENT,"_comment")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"CREATE OR REPLACE SCHEMA {self.attr.database}.{self.attr.name[0]} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.WITH_MANAGED_ACCESS:
                    self.qry = f" {self.qry} {tags.WITH_MANAGED_ACCESS} "
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
                if prop == tags.CLASSIFICATION_PROFILE:
                    self.qry = f" {self.qry} {tags.CLASSIFICATION_PROFILE} = {self.attr.classification_profile} "
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "

    def alter_object(self):
        for prop in self.property_lst:
            if prop == tags.WITH_MANAGED_ACCESS:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.WITH_MANAGED_ACCESS} = {self.attr.with_managed_access}"
                self.execute_final_query()
            if prop == tags.DATA_RETENTION_TIME_IN_DAYS:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.DATA_RETENTION_TIME_IN_DAYS} = {self.attr.data_retention_time_in_days}"
                self.execute_final_query()
            if prop == tags.MAX_DATA_EXTENSION_TIME_IN_DAYS:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.MAX_DATA_EXTENSION_TIME_IN_DAYS} = {self.attr.max_data_extension_time_in_days}"
                self.execute_final_query()
            if prop == tags.EXTERNAL_VOLUME:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.EXTERNAL_VOLUME} = {self.attr.external_volume}"
                self.execute_final_query()
            if prop == tags.CATALOG:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.CATALOG} = {self.attr.catalog}"
                self.execute_final_query()
            if prop == tags.REPLACE_INVALID_CHARACTERS:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.REPLACE_INVALID_CHARACTERS} = {self.attr.replace_invalid_characters}"
                self.execute_final_query()
            if prop == tags.DEFAULT_DDL_COLLATION:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.DEFAULT_DDL_COLLATION} = {self.attr.default_ddl_collation}"
                self.execute_final_query()
            if prop == tags.LOG_LEVEL:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.LOG_LEVEL} = {self.attr.log_level}"
                self.execute_final_query()
            if prop == tags.STORAGE_SERIALIZATION_POLICY:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.STORAGE_SERIALIZATION_POLICY} = {self.attr.storage_serialization_policy}"
                self.execute_final_query()
            if prop == tags.CLASSIFICATION_PROFILE:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.CLASSIFICATION_PROFILE} = {self.attr.classification_profile}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER {self.__class__.__name__}.upper() {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming {self.__class__.__name__.upper()} {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()


    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create=="TRUE":
            self.set_create_account_qry()
            self.add_properties_to_query()
        elif self.is_create=="FALSE":
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()

    def create_schema(self):
        self.session.sql(self.qry).collect()

    def create_object(self,*largs,**kwargs):
        self.logger.info(f"Operating on {self.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        self.logger.info(f'dictionary passed {kwargs}')
        self.is_create=kwargs[tags.IS_CREATE]

        self.logger.info('set database')
        self.set_database(kwargs[tags.DATABASE])
        self.logger.info('set name')
        self.set_name(kwargs[tags.NAME])
        self.logger.info('set with managed access')
        self.set_with_managed_access(kwargs[tags.WITH_MANAGED_ACCESS])
        self.logger.info('set data retention time in days')
        self.set_data_retention_time_in_days(kwargs[tags.DATA_RETENTION_TIME_IN_DAYS])
        self.logger.info('set max data extension time in days')
        self.set_max_data_extension_time_in_days(kwargs[tags.MAX_DATA_EXTENSION_TIME_IN_DAYS])
        self.logger.info('set external volume')
        self.set_external_volume(kwargs[tags.EXTERNAL_VOLUME])
        self.logger.info('set catalog')
        self.set_catalog(kwargs[tags.CATALOG])
        self.logger.info('set replace invalid characters')
        self.set_replace_invalid_characters(kwargs[tags.REPLACE_INVALID_CHARACTERS])
        self.logger.info('set default ddl collation')
        self.set_default_ddl_collation(kwargs[tags.DEFAULT_DDL_COLLATION])
        self.logger.info('set log level')
        self.set_log_level(kwargs[tags.LOG_LEVEL])
        self.logger.info('set trace level')
        self.set_trace_level(kwargs[tags.TRACE_LEVEL])
        self.logger.info('set storage serialization policy')
        self.set_storage_serialization_policy(kwargs[tags.STORAGE_SERIALIZATION_POLICY])
        self.logger.info('set classification profile')
        self.set_classification_profile(kwargs[tags.CLASSIFICATION_PROFILE])
        self.logger.info('set comment')
        self.set_comment(kwargs[tags.COMMENT])
        self.logger.info('set qualified name')
        self.set_qualified_name()
        self.logger.info('pepaer query')
        self.prepare_query()
        self.logger.info('call create schema')
        self.create_schema()
        self.logger.info(f'schema {self.attr.name} created successfully')
        #self.grant_default_privileges()
        if len(largs) == 0:
            self.create_deployment_entry(object_name=self.attr.name,object_type=self.__class__.__name__,object_database=self.attr.database,object_schema='NA')
            self.logger.info('writing file to git')
            self.write_file_to_git(object_name=self.attr.name,object_type=self.__class__.__name__,object_database=self.attr.database,object_schema='NA')


class Operation:
    @staticmethod
    def create_object(session,user_id,kwargs,*largs):
        obj_inst=Schema(session=session,
                         user_id=user_id,
                        )
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        obj_inst.logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        obj_inst.logger.info("set with_managed_access")
        if tags.WITH_MANAGED_ACCESS in kwargs.keys():
            obj_inst.set_with_managed_access(kwargs[tags.WITH_MANAGED_ACCESS])
        else:
            obj_inst.set_with_managed_access('NONE')

        obj_inst.logger.info("set data_retention_time_in_days")
        if tags.DATA_RETENTION_TIME_IN_DAYS in kwargs.keys():
            obj_inst.set_data_retention_time_in_days(kwargs[tags.DATA_RETENTION_TIME_IN_DAYS])
        else:
            obj_inst.set_data_retention_time_in_days('NONE')

        obj_inst.logger.info("set max_data_extension_time_in_days")
        if tags.MAX_DATA_EXTENSION_TIME_IN_DAYS in kwargs.keys():
            obj_inst.set_max_data_extension_time_in_days(kwargs[tags.MAX_DATA_EXTENSION_TIME_IN_DAYS])
        else:
            obj_inst.set_max_data_extension_time_in_days('NONE')

        obj_inst.logger.info("set external_volume")
        if tags.EXTERNAL_VOLUME in kwargs.keys():
            obj_inst.set_external_volume(kwargs[tags.EXTERNAL_VOLUME])
        else:
            obj_inst.set_external_volume('NONE')

        obj_inst.logger.info("set catalog")
        if tags.CATALOG in kwargs.keys():
            obj_inst.set_catalog(kwargs[tags.CATALOG])
        else:
            obj_inst.set_catalog('NONE')

        obj_inst.logger.info("set replace_invalid_characters")
        if tags.REPLACE_INVALID_CHARACTERS in kwargs.keys():
            obj_inst.set_replace_invalid_characters(kwargs[tags.REPLACE_INVALID_CHARACTERS])
        else:
            obj_inst.set_replace_invalid_characters('NONE')

        obj_inst.logger.info("set default_ddl_collation")
        if tags.DEFAULT_DDL_COLLATION in kwargs.keys():
            obj_inst.set_default_ddl_collation(kwargs[tags.DEFAULT_DDL_COLLATION])
        else:
            obj_inst.set_default_ddl_collation('NONE')

        obj_inst.logger.info("set log_level")
        if tags.LOG_LEVEL in kwargs.keys():
            obj_inst.set_log_level(kwargs[tags.LOG_LEVEL])
        else:
            obj_inst.set_log_level('NONE')

        obj_inst.logger.info("set trace_level")
        if tags.TRACE_LEVEL in kwargs.keys():
            obj_inst.set_trace_level(kwargs[tags.TRACE_LEVEL])
        else:
            obj_inst.set_trace_level('NONE')

        obj_inst.logger.info("set storage_serialization_policy")
        if tags.STORAGE_SERIALIZATION_POLICY in kwargs.keys():
            obj_inst.set_storage_serialization_policy(kwargs[tags.STORAGE_SERIALIZATION_POLICY])
        else:
            obj_inst.set_storage_serialization_policy('NONE')

        obj_inst.logger.info("set classification_profile")
        if tags.CLASSIFICATION_PROFILE in kwargs.keys():
            obj_inst.set_classification_profile(kwargs[tags.CLASSIFICATION_PROFILE])
        else:
            obj_inst.set_classification_profile('NONE')

        obj_inst.logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')


        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        
        obj_inst.logger.info('execute query')
        obj_inst.execute_final_query()

        obj_inst.logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
