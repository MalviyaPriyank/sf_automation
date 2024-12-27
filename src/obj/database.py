import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../../vars/global'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))


from global_vars import Database as dbgv
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
        if vv.is_between(value,0,90):
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
            instance._replace_invalid_characters = value
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

class DatabaseAttrs:
    name = Name()
    name_tag = NameTag()

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

    storage_serialization_policy = StorageSerializationPolicy()
    storage_serialization_policy_tag = StorageSerializationPolicyTag()

    comment = Comment()
    comment_tag = CommentTag()


class Database:
    def __init__(self):
        self.attr = DatabaseAttrs()
        self.session = 'session'
        self.qry = ""

    def set_name(self,name):
        self.attr.name = name

    def set_name_tag(self,name_tag):
        self.attr.name_tag = name_tag

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

    def set_storage_serialization_policy(self,storage_serialization_policy):
        self.attr.storage_serialization_policy = storage_serialization_policy

    def set_storage_serialization_policy_tag(self,storage_serialization_policy_tag):
        self.attr.storage_serialization_policy_tag = storage_serialization_policy_tag

    def set_comment(self,comment):
        self.attr.comment = comment

    def set_comment_tag(self,comment_tag):
        self.attr.comment_tag = comment_tag


    def set_object_properties_flag(self):
        self.flag_dic = {}

        if self.attr.name != "NONE":
            self.flag_dic[dbgv._name_tag] = 1
        else:
            self.flag_dic[dbgv._name_tag] = 0

        if self.attr.data_retention_time_in_days != "NONE":
            self.flag_dic[dbgv._data_retention_time_in_days_tag] = 1
        else:
            self.flag_dic[dbgv._data_retention_time_in_days_tag] = 0

        if self.attr.max_data_extension_time_in_days != "NONE":
            self.flag_dic[dbgv._max_data_extension_time_in_days_tag] = 1
        else:
            self.flag_dic[dbgv._max_data_extension_time_in_days_tag] = 0

        if self.attr.external_volume != "NONE":
            self.flag_dic[dbgv._external_volume_tag] = 1
        else:
            self.flag_dic[dbgv._external_volume_tag] = 0

        if self.attr.catalog != "NONE":
            self.flag_dic[dbgv._catalog_tag] = 1
        else:
            self.flag_dic[dbgv._catalog_tag] = 0

        if self.attr.default_ddl_collation != "NONE":
            self.flag_dic[dbgv._default_ddl_collation_tag] = 1
        else:
            self.flag_dic[dbgv._default_ddl_collation_tag] = 0

        if self.attr.storage_serialization_policy != "NONE":
            self.flag_dic[dbgv._storage_serialization_policy_tag] = 1
        else:
            self.flag_dic[dbgv._storage_serialization_policy_tag] = 0

        if self.attr.comment != "NONE":
            self.flag_dic[dbgv._comment_tag] = 1
        else:
            self.flag_dic[dbgv._comment_tag] = 0

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
                if prop == dbgv._data_retention_time_in_days_tag:
                    self.qry = f" {self.qry} {self.attr.data_retention_time_in_days_tag} = {self.attr.data_retention_time_in_days} "
                if prop == dbgv._max_data_extension_time_in_days_tag:
                    self.qry = f" {self.qry} {self.attr.max_data_extension_time_in_days_tag} = {self.attr.max_data_extension_time_in_days} "
                if prop == dbgv._external_volume_tag:
                    self.qry = f" {self.qry} {self.attr.external_volume_tag} = {self.attr.external_volume} "
                if prop == dbgv._catalog_tag:
                    self.qry = f" {self.qry} {self.attr.catalog_tag} = {self.attr.catalog} "
                if prop == dbgv._default_ddl_collation_tag:
                    self.qry = f" {self.qry} {self.attr.default_ddl_collation_tag} = {self.attr.default_ddl_collation} "
                if prop == dbgv._storage_serialization_policy_tag:
                    self.qry = f" {self.qry} {self.attr.storage_serialization_policy_tag} = {self.attr.storage_serialization_policy} "
                if prop == dbgv._comment_tag:
                    self.qry = f" {self.qry} {self.attr.comment_tag} = {self.attr.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()


def main(**kwargs):
    database = Database()
    
    database.set_name(kwargs[dbgv._name_tag])
    database.set_name_tag(dbgv._name_tag)

    database.set_data_retention_time_in_days(kwargs[dbgv._data_retention_time_in_days_tag])
    database.set_data_retention_time_in_days_tag(dbgv._data_retention_time_in_days_tag)

    database.set_max_data_extension_time_in_days(kwargs[dbgv._max_data_extension_time_in_days_tag])
    database.set_max_data_extension_time_in_days_tag(dbgv._max_data_extension_time_in_days_tag)

    database.set_external_volume(kwargs[dbgv._external_volume_tag])
    database.set_external_volume_tag(dbgv._external_volume_tag)

    database.set_catalog(kwargs[dbgv._catalog_tag])
    database.set_catalog_tag(dbgv._catalog_tag)

    database.set_default_ddl_collation(kwargs[dbgv._default_ddl_collation_tag])
    database.set_default_ddl_collation_tag(dbgv._default_ddl_collation_tag)

    database.set_storage_serialization_policy(kwargs[dbgv._storage_serialization_policy_tag])
    database.set_storage_serialization_policy_tag(dbgv._storage_serialization_policy_tag)

    database.set_comment(kwargs[dbgv._comment_tag])
    database.set_comment_tag(dbgv._comment_tag)

    database.prepare_query()

    return database.qry
