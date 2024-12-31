
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../../vars/global'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))


from global_vars import Schema as gv
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
        if vv.is_between(value,0,90):
            instance._data_retention_time_in_days = value
        else:
            raise ValueError
    
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
        if vv.is_positive_number(value):
            instance._max_data_extension_time_in_days = value
        else:
            raise ValueError

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
        elif vv.is_bool(value):
            instance._replace_invalid_characters = value
        else:
            raise ValueError

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
        elif value not in gv._allowed_values_log_level:
            raise ValueError
        else:
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
        elif value not in gv._allowed_values_trace_level:
            raise ValueError
        else:
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

class Tag:
    def __get__(self,instance,owner):
        return instance._tag
    
    def __set__(self,instance,value):
        instance._tag = value
    
    def __delete__(self,instance):
        del instance._tag

class TagTag:
    def __get__(self,instance,owner):
        return instance._tag_tag
    
    def __set__(self,instance,value):
        instance._tag_tag = value
    
    def __delete__(self,instance):
        del instance._tag_tag

class SchemaAttrs:
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

    tag = Tag()
    tag_tag = TagTag()


class Schema:
    def __init__(self):
        self.attr = SchemaAttrs()
        self.session = 'session'
        self.qry = ""

    def set_name(self,name):
        self.attr.name = name

    def set_name_tag(self,name_tag):
        self.attr.name_tag = name_tag

    def set_with_managed_access(self,with_managed_access):
        self.attr.with_managed_access = with_managed_access

    def set_with_managed_access_tag(self,with_managed_access_tag):
        self.attr.with_managed_access_tag = with_managed_access_tag

    def set_data_retention_time_in_days(self,data_retention_time_in_days):
        self.attr.data_retention_time_in_days = data_retention_time_in_days

    def set_data_retention_time_in_days_tag(self,data_retention_time_in_days_tag):
        self.attr.data_retention_time_in_days_tag = data_retention_time_in_days_tag
     
    def set_max_data_extension_time_in_days(self,max_data_extension_time_in_days):
        self.attr.max_data_extension_time_in_days = max_data_extension_time_in_days

    def set_max_data_extension_time_in_days_tag(self,max_data_extension_time_in_days_tag):
        self.attr.max_data_extension_time_in_days_tag = max_data_extension_time_in_days_tag

    def set_external_volume(self,external_volume):
        self.attr.external_volume = external_volume

    def set_external_volume_tag(self,external_volume_tag):
        self.attr.external_volume_tag = external_volume_tag

    def set_catalog(self,catalog):
        self.attr.catalog = catalog

    def set_catalog_tag(self,catalog_tag):
        self.attr.catalog_tag = catalog_tag

    def set_replace_invalid_characters(self,replace_invalid_characters):
        self.attr.replace_invalid_characters = replace_invalid_characters

    def set_replace_invalid_characters_tag(self,replace_invalid_characters_tag):
        self.attr.replace_invalid_characters_tag = replace_invalid_characters_tag

    def set_default_ddl_collation(self,default_ddl_collation):
        self.attr.default_ddl_collation = default_ddl_collation

    def set_default_ddl_collation_tag(self,default_ddl_collation_tag):
        self.attr.default_ddl_collation_tag = default_ddl_collation_tag

    def set_log_level(self,log_level):
        self.attr.log_level = log_level

    def set_log_level_tag(self,log_level_tag):
        self.attr.log_level_tag = log_level_tag

    def set_trace_level(self,trace_level):
        self.attr.trace_level = trace_level

    def set_trace_level_tag(self,trace_level_tag):
        self.attr.trace_level_tag = trace_level_tag

    def set_storage_serialization_policy(self,storage_serialization_policy):
        self.attr.storage_serialization_policy = storage_serialization_policy

    def set_storage_serialization_policy_tag(self,storage_serialization_policy_tag):
        self.attr.storage_serialization_policy_tag = storage_serialization_policy_tag

    def set_classification_profile(self,classification_profile):
        self.attr.classification_profile = classification_profile

    def set_classification_profile_tag(self,classification_profile_tag):
        self.attr.classification_profile_tag = classification_profile_tag

    def set_comment(self,comment):
        self.attr.comment = comment

    def set_comment_tag(self,comment_tag):
        self.attr.comment_tag = comment_tag

    def set_tag(self,tag):
        self.attr.tag = tag

    def set_tag_tag(self,tag_tag):
        self.attr.tag_tag = tag_tag


    def set_object_properties_flag(self):
        self.flag_dic = {}

        if self.attr.name != "NONE":
            self.flag_dic[gv._name_tag] = 1
        else:
            self.flag_dic[gv._name_tag] = 0

        if self.attr.with_managed_access != "NONE":
            self.flag_dic[gv._with_managed_access_tag] = 1
        else:
            self.flag_dic[gv._with_managed_access_tag] = 0

        if self.attr.data_retention_time_in_days != "NONE":
            self.flag_dic[gv._data_retention_time_in_days_tag] = 1
        else:
            self.flag_dic[gv._data_retention_time_in_days_tag] = 0

        if self.attr.max_data_extension_time_in_days != "NONE":
            self.flag_dic[gv._max_data_extension_time_in_days_tag] = 1
        else:
            self.flag_dic[gv._max_data_extension_time_in_days_tag] = 0

        if self.attr.external_volume != "NONE":
            self.flag_dic[gv._external_volume_tag] = 1
        else:
            self.flag_dic[gv._external_volume_tag] = 0

        if self.attr.catalog != "NONE":
            self.flag_dic[gv._catalog_tag] = 1
        else:
            self.flag_dic[gv._catalog_tag] = 0

        if self.attr.replace_invalid_characters != "NONE":
            self.flag_dic[gv._replace_invalid_characters_tag] = 1
        else:
            self.flag_dic[gv._replace_invalid_characters_tag] = 0

        if self.attr.default_ddl_collation != "NONE":
            self.flag_dic[gv._default_ddl_collation_tag] = 1
        else:
            self.flag_dic[gv._default_ddl_collation_tag] = 0

        if self.attr.log_level != "NONE":
            self.flag_dic[gv._log_level_tag] = 1
        else:
            self.flag_dic[gv._log_level_tag] = 0

        if self.attr.trace_level != "NONE":
            self.flag_dic[gv._trace_level_tag] = 1
        else:
            self.flag_dic[gv._trace_level_tag] = 0

        if self.attr.storage_serialization_policy != "NONE":
            self.flag_dic[gv._storage_serialization_policy_tag] = 1
        else:
            self.flag_dic[gv._storage_serialization_policy_tag] = 0

        if self.attr.classification_profile != "NONE":
            self.flag_dic[gv._classification_profile_tag] = 1
        else:
            self.flag_dic[gv._classification_profile_tag] = 0

        if self.attr.comment != "NONE":
            self.flag_dic[gv._comment_tag] = 1
        else:
            self.flag_dic[gv._comment_tag] = 0

        if self.attr.tag != "NONE":
            self.flag_dic[gv._tag_tag] = 1
        else:
            self.flag_dic[gv._tag_tag] = 0

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
                if prop == gv._tag_tag:
                    self.qry = f" {self.qry} {self.attr.tag_tag} = {self.attr.tag} "


    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()


def main(**kwargs):
    schema = Schema()

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

    schema.set_tag(kwargs[gv._tag_tag])
    schema.set_tag_tag(gv._tag_tag)

    schema.prepare_query()

    return schema.qry
