import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))


from global_vars import Schema as gv
from validatevalue import ValidateValue as vv

class DatabaseName:
    def __get__(self,instance,owner):
        return instance._database_name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._database_name = value
    
    def __delete__(self,instance):
        del instance._database_name

class DatabaseTag:
    def __get__(self,instance,owner):
        return instance._database_tag
    
    def __set__(self,instance,value):
        instance._database_tag = value
    
    def __delete__(self,instance):
        del instance._database_tag

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__):
            if ( not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
                and not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__)
            ):
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

class WithManagedAccess:
    def __get__(self,instance,owner):
        return instance._with_managed_access
    
    def __set__(self,instance,value):
        instance._with_managed_access = value
    
    def __delete__(self,instance):
        del instance._with_managed_access

class WithManagedAccessTag:
    def __get__(self,instance,owner):
        return instance._with_managed_access_tag
    
    def __set__(self,instance,value):
        instance._with_managed_access_tag = value
    
    def __delete__(self,instance):
        del instance._with_managed_access_tag

class DataRetentionTimeInDays:
    def __get__(self,instance,owner):
        return instance._data_retention_time_in_days
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._data_retention_time_in_days = value
        elif vv.is_between(value,0,90,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._data_retention_time_in_days = value
    
    def __delete__(self,instance):
        del instance._data_retention_time_in_days

class DataRetentionTimeInDaysTag:
    def __get__(self,instance,owner):
        return instance._data_retention_time_in_days_tag
    
    def __set__(self,instance,value):
        instance._data_retention_time_in_days_tag = value
    
    def __delete__(self,instance):
        del instance._data_retention_time_in_days_tag

class MaxDataExtensionTimeInDays:
    def __get__(self,instance,owner):
        return instance._max_data_extension_time_in_days
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._max_data_extension_time_in_days = value
        elif vv.is_positive_number(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._max_data_extension_time_in_days = value

    def __delete__(self,instance):
        del instance._max_data_extension_time_in_days

class MaxDataExtensionTimeInDaysTag:
    def __get__(self,instance,owner):
        return instance._max_data_extension_time_in_days_tag
    
    def __set__(self,instance,value):
        instance._max_data_extension_time_in_days_tag = value

    def __delete__(self,instance):
        del instance._max_data_extension_time_in_days_tag

class ExternalVolume:
    def __get__(self,instance,owner):
        return instance._external_volume
    
    def __set__(self,instance,value):
        instance._external_volume = value

    def __delete__(self,instance):
        del instance._external_volume

class ExternalVolumeTag:
    def __get__(self,instance,owner):
        return instance._external_volume_tag
    
    def __set__(self,instance,value):
        instance._external_volume_tag = value

    def __delete__(self,instance):
        del instance._external_volume_tag

class Catalog:
    def __get__(self,instance,owner):
        return instance._catalog
    
    def __set__(self,instance,value):
        instance._catalog = value

    def __delete__(self,instance):
        del instance._catalog

class CatalogTag:
    def __get__(self,instance,owner):
        return instance._catalog_tag
    
    def __set__(self,instance,value):
        instance._catalog_tag = value

    def __delete__(self,instance):
        del instance._catalog_tag

class ReplaceInvalidCharacters:
    def __get__(self,instance,owner):
        return instance._replace_invalid_characters
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._replace_invalid_characters = "FALSE"
        elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._replace_invalid_characters = value

    def __delete__(self,instance):
        del instance._replace_invalid_characters

class ReplaceInvalidCharactersTag:
    def __get__(self,instance,owner):
        return instance._replace_invalid_characters_tag
    
    def __set__(self,instance,value):
        instance._replace_invalid_characters_tag = value

    def __delete__(self,instance):
        del instance._replace_invalid_characters_tag


class DefaultDdlCollation:
    def __get__(self,instance,owner):
        return instance._default_ddl_collation
    
    def __set__(self,instance,value):
        instance._default_ddl_collation = value

    def __delete__(self,instance):
        del instance._default_ddl_collation

class DefaultDdlCollationTag:
    def __get__(self,instance,owner):
        return instance._default_ddl_collation_tag
    
    def __set__(self,instance,value):
        instance._default_ddl_collation_tag = value

    def __delete__(self,instance):
        del instance._default_ddl_collation_tag

class LogLevel:
    def __get__(self,instance,owner):
        return instance._log_level
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._log_level = "OFF"
        else:
            vv.allowed_value_check(value,gv._allowed_values_log_level,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._log_level = value

    def __delete__(self,instance):
        del instance._log_level

class LogLevelTag:
    def __get__(self,instance,owner):
        return instance._log_level_tag
    
    def __set__(self,instance,value):
        instance._log_level_tag = value

    def __delete__(self,instance):
        del instance._log_level_tag

class TraceLevel:
    def __get__(self,instance,owner):
        return instance._trace_level
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._trace_level = "OFF"
        else:
            vv.allowed_value_check(value,gv._allowed_values_trace_level,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._trace_level = value

    def __delete__(self,instance):
        del instance._trace_level

class TraceLevelTag:
    def __get__(self,instance,owner):
        return instance._trace_level_tag
    
    def __set__(self,instance,value):
        instance._trace_level_tag = value

    def __delete__(self,instance):
        del instance._trace_level_tag

class StorageSerializationPolicy:
    def __get__(self,instance,owner):
        return instance._storage_serialization_policy
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._storage_serialization_policy = value
        else:
            vv.allowed_value_check(value,gv._allowed_values_storage_serialization_policy,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._storage_serialization_policy = value

    def __delete__(self,instance):
        del instance._storage_serialization_policy

class StorageSerializationPolicyTag:
    def __get__(self,instance,owner):
        return instance._storage_serialization_policy_tag
    
    def __set__(self,instance,value):
        instance._storage_serialization_policy_tag = value

    def __delete__(self,instance):
        del instance._storage_serialization_policy_tag

class ClassificationProfile:
    def __get__(self,instance,owner):
        return instance._classification_profile
    
    def __set__(self,instance,value):
        instance._classification_profile = value

    def __delete__(self,instance):
        del instance._classification_profile

class ClassificationProfileTag:
    def __get__(self,instance,owner):
        return instance._classification_profile_tag
    
    def __set__(self,instance,value):
        instance._classification_profile_tag = value

    def __delete__(self,instance):
        del instance._classification_profile_tag

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = value
    
    def __delete__(self,instance):
        del instance._comment

class CommentTag:
    def __get__(self,instance,owner):
        return instance._comment_tag
    
    def __set__(self,instance,value):
        instance._comment_tag = value
    
    def __delete__(self,instance):
        del instance._comment_tag



class SchemaAttrs:
    def __init__(self,parent):
        self.parent = parent

    database_name = DatabaseName()
    database_tag = DatabaseTag()
        
    name = Name()
    name_tag = NameTag()

    with_managed_access = WithManagedAccess()
    with_managed_access_tag = WithManagedAccessTag()

    data_retention_time_in_days = DataRetentionTimeInDays()
    data_retention_time_in_days_tag = DataRetentionTimeInDaysTag()

    max_data_extension_time_in_days = MaxDataExtensionTimeInDays()
    max_data_extension_time_in_days_tag = MaxDataExtensionTimeInDaysTag()

    external_volume = ExternalVolume()
    external_volume_tag = ExternalVolumeTag()

    catalog = Catalog()
    catalog_tag = CatalogTag()

    replace_invalid_characters = ReplaceInvalidCharacters()
    replace_invalid_characters_tag = ReplaceInvalidCharactersTag()

    default_ddl_collation = DefaultDdlCollation()
    default_ddl_collation_tag = DefaultDdlCollationTag()

    log_level = LogLevel()
    log_level_tag = LogLevelTag()

    trace_level = TraceLevel()
    trace_level_tag = TraceLevelTag()

    storage_serialization_policy = StorageSerializationPolicy()
    storage_serialization_policy_tag = StorageSerializationPolicyTag()

    classification_profile = ClassificationProfile()
    classification_profile_tag = ClassificationProfileTag()

    comment = Comment()
    comment_tag = CommentTag()



class Schema:
    def __init__(self,session):
        self.attr = SchemaAttrs(self)
        self.session = session
        self.qry = ""

    def set_database_name(self, value):
        self.attr.database_name = value

    def set_database_tag(self, value):
        self.attr.database_tag = value  

    def set_name(self, value):
        self.attr.name = value

    def set_name_tag(self, value):
        self.attr.name_tag = value

    def set_with_managed_access(self, value):
        self.attr.with_managed_access = value

    def set_with_managed_access_tag(self, value):
        self.attr.with_managed_access_tag = value

    def set_data_retention_time_in_days(self, value):
        self.attr.data_retention_time_in_days = value

    def set_data_retention_time_in_days_tag(self, value):
        self.attr.data_retention_time_in_days_tag = value

    def set_max_data_extension_time_in_days(self, value):
        self.attr.max_data_extension_time_in_days = value

    def set_max_data_extension_time_in_days_tag(self, value):
        self.attr.max_data_extension_time_in_days_tag = value

    def set_external_volume(self, value):
        self.attr.external_volume = value

    def set_external_volume_tag(self, value):
        self.attr.external_volume_tag = value

    def set_catalog(self, value):
        self.attr.catalog = value

    def set_catalog_tag(self, value):
        self.attr.catalog_tag = value

    def set_replace_invalid_characters(self, value):
        self.attr.replace_invalid_characters = value

    def set_replace_invalid_characters_tag(self, value):
        self.attr.replace_invalid_characters_tag = value

    def set_default_ddl_collation(self, value):
        self.attr.default_ddl_collation = value

    def set_default_ddl_collation_tag(self, value):
        self.attr.default_ddl_collation_tag = value

    def set_log_level(self, value):
        self.attr.log_level = value

    def set_log_level_tag(self, value):
        self.attr.log_level_tag = value

    def set_trace_level(self, value):
        self.attr.trace_level = value

    def set_trace_level_tag(self, value):
        self.attr.trace_level_tag = value

    def set_storage_serialization_policy(self, value):
        self.attr.storage_serialization_policy = value

    def set_storage_serialization_policy_tag(self, value):
        self.attr.storage_serialization_policy_tag = value

    def set_classification_profile(self, value):
        self.attr.classification_profile = value

    def set_classification_profile_tag(self, value):
        self.attr.classification_profile_tag = value

    def set_comment(self, value):
        self.attr.comment = value

    def set_comment_tag(self, value):
        self.attr.comment_tag = value


    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv._name_tag,"_name")
        set_flag(gv._with_managed_access_tag,"_with_managed_access")
        set_flag(gv._data_retention_time_in_days_tag,"_data_retention_time_in_days")
        set_flag(gv._max_data_extension_time_in_days_tag,"_max_data_extension_time_in_days")
        set_flag(gv._external_volume_tag,"_external_volume")
        set_flag(gv._catalog_tag,"_catalog")
        set_flag(gv._replace_invalid_characters_tag,"_replace_invalid_characters")
        set_flag(gv._default_ddl_collation_tag,"_default_ddl_collation")
        set_flag(gv._log_level_tag,"_log_level")
        set_flag(gv._trace_level_tag,"_trace_level")
        set_flag(gv._storage_serialization_policy_tag,"_storage_serialization_policy")
        set_flag(gv._classification_profile_tag,"_classification_profile")
        set_flag(gv._comment_tag,"_comment")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"CREATE SCHEMA  {self.attr.name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gv._with_managed_access_tag:
                    self.qry = f" {self.qry} {self.attr.with_managed_access_tag} = {self.attr.with_managed_access} "
                if prop == gv._data_retention_time_in_days_tag:
                    self.qry = f" {self.qry} {self.attr.data_retention_time_in_days_tag} = {self.attr.data_retention_time_in_days} "
                if prop == gv._max_data_extension_time_in_days_tag:
                    self.qry = f" {self.qry} {self.attr.max_data_extension_time_in_days_tag} = {self.attr.max_data_extension_time_in_days} "
                if prop == gv._external_volume_tag:
                    self.qry = f" {self.qry} {self.attr.external_volume_tag} = {self.attr.external_volume} "
                if prop == gv._catalog_tag:
                    self.qry = f" {self.qry} {self.attr.catalog_tag} = {self.attr.catalog} "
                if prop == gv._replace_invalid_characters_tag:
                    self.qry = f" {self.qry} {self.attr.replace_invalid_characters_tag} = {self.attr.replace_invalid_characters} "
                if prop == gv._default_ddl_collation_tag:
                    self.qry = f" {self.qry} {self.attr.default_ddl_collation_tag} = {self.attr.default_ddl_collation} "
                if prop == gv._log_level_tag:
                    self.qry = f" {self.qry} {self.attr.log_level_tag} = {self.attr.log_level} "
                if prop == gv._trace_level_tag:
                    self.qry = f" {self.qry} {self.attr.trace_level_tag} = {self.attr.trace_level} "
                if prop == gv._storage_serialization_policy_tag:
                    self.qry = f" {self.qry} {self.attr.storage_serialization_policy_tag} = {self.attr.storage_serialization_policy} "
                if prop == gv._classification_profile_tag:
                    self.qry = f" {self.qry} {self.attr.classification_profile_tag} = {self.attr.classification_profile} "
                if prop == gv._comment_tag:
                    self.qry = f" {self.qry} {self.attr.comment_tag} = {self.attr.comment} "


    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()

    def create_schema(self):
        self.session.sql(f"USE {self.attr.database_tag} {self.attr.database_name}").collect()
        self.session.sql(self.qry).collect()

    def create_object(session,**kwargs):
        schema = Schema(session)

        schema.set_database_name(kwargs[gv._database_tag])
        schema.set_database_tag(gv._database_tag)

        schema.set_name(kwargs[gv._name_tag])
        schema.set_name_tag(gv._name_tag)

        schema.set_with_managed_access(kwargs[gv._with_managed_access_tag])
        schema.set_with_managed_access_tag(gv._with_managed_access_tag)

        schema.set_data_retention_time_in_days(kwargs[gv._data_retention_time_in_days_tag])
        schema.set_data_retention_time_in_days_tag(gv._data_retention_time_in_days_tag)

        schema.set_max_data_extension_time_in_days(kwargs[gv._max_data_extension_time_in_days_tag])
        schema.set_max_data_extension_time_in_days_tag(gv._max_data_extension_time_in_days_tag)

        schema.set_external_volume(kwargs[gv._external_volume_tag])
        schema.set_external_volume_tag(gv._external_volume_tag)

        schema.set_catalog(kwargs[gv._catalog_tag])
        schema.set_catalog_tag(gv._catalog_tag)

        schema.set_replace_invalid_characters(kwargs[gv._replace_invalid_characters_tag])
        schema.set_replace_invalid_characters_tag(gv._replace_invalid_characters_tag)

        schema.set_default_ddl_collation(kwargs[gv._default_ddl_collation_tag])
        schema.set_default_ddl_collation_tag(gv._default_ddl_collation_tag)

        schema.set_log_level(kwargs[gv._log_level_tag])
        schema.set_log_level_tag(gv._log_level_tag)

        schema.set_trace_level(kwargs[gv._trace_level_tag])
        schema.set_trace_level_tag(gv._trace_level_tag)

        schema.set_storage_serialization_policy(kwargs[gv._storage_serialization_policy_tag])
        schema.set_storage_serialization_policy_tag(gv._storage_serialization_policy_tag)

        schema.set_classification_profile(kwargs[gv._classification_profile_tag])
        schema.set_classification_profile_tag(gv._classification_profile_tag)

        schema.set_comment(kwargs[gv._comment_tag])
        schema.set_comment_tag(gv._comment_tag)


        schema.prepare_query()
        schema.create_schema()
