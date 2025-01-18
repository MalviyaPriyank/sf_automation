import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../../vars/global'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))


from global_vars import Database as gv
from validatevalue import ValidateValue as vv
from valueexception import IsARequiredAttribute

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        if value == "NONE" :
            raise IsARequiredAttribute(instance.parent.__class__.__name__,self.__class__.__name__)
        elif ( vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__) 
              and not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
              and not vv.has_special_characters(value,instance.parent.__class__.__name__,self.__class__.__name__)
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

class DataRetentionTimeInDays:
    def __get__(self,instance,owner):
        return instance._data_retention_time_in_days
    
    def __set__(self,instance,value):
        if vv.is_between(value,0,90,instance.parent.__class__.__name__,self.__class__.__name__):
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
        if vv.is_between(value,0,90,instance.parent.__class__.__name__,self.__class__.__name__):
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
            instance._replace_invalid_characters = value
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
    def __init__(self,parent):
        self.parent = parent

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
    def __init__(self,session):
        self.attr = DatabaseAttrs(self)
        self.session = session
        self.qry = ""

    def set_name(self, value):
        self.attr.name = value

    def set_name_tag(self, value):
        self.attr.name_tag = value

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

    def set_storage_serialization_policy(self, value):
        self.attr.storage_serialization_policy = value

    def set_storage_serialization_policy_tag(self, value):
        self.attr.storage_serialization_policy_tag = value

    def set_comment(self, value):
        self.attr.comment = value

    def set_comment_tag(self, value):
        self.attr.comment_tag = value


    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv._name_tag,"_name")
        set_flag(gv._data_retention_time_in_days_tag,"_data_retention_time_in_days")
        set_flag(gv._max_data_extension_time_in_days_tag,"_max_data_extension_time_in_days")
        set_flag(gv._external_volume_tag,"_external_volume")
        set_flag(gv._catalog_tag,"_catalog")
        set_flag(gv._replace_invalid_characters_tag,"_replace_invalid_characters")
        set_flag(gv._default_ddl_collation_tag,"_default_ddl_collation")
        set_flag(gv._storage_serialization_policy_tag,"_storage_serialization_policy")
        set_flag(gv._comment_tag,"_comment")


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
                if prop == gv._storage_serialization_policy_tag:
                    self.qry = f" {self.qry} {self.attr.storage_serialization_policy_tag} = {self.attr.storage_serialization_policy} "
                if prop == gv._comment_tag:
                    self.qry = f" {self.qry} {self.attr.comment_tag} = {self.attr.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()

    def create_database(self):
        self.session.sql(self.qry)

    def create_object(session,**kwargs):
        database = Database(session)

        database.set_name(kwargs[gv._name_tag])
        database.set_name_tag(gv._name_tag)

        database.set_data_retention_time_in_days(kwargs[gv._data_retention_time_in_days_tag])
        database.set_data_retention_time_in_days_tag(gv._data_retention_time_in_days_tag)

        database.set_max_data_extension_time_in_days(kwargs[gv._max_data_extension_time_in_days_tag])
        database.set_max_data_extension_time_in_days_tag(gv._max_data_extension_time_in_days_tag)

        database.set_external_volume(kwargs[gv._external_volume_tag])
        database.set_external_volume_tag(gv._external_volume_tag)

        database.set_catalog(kwargs[gv._catalog_tag])
        database.set_catalog_tag(gv._catalog_tag)

        database.set_replace_invalid_characters(kwargs[gv._replace_invalid_characters_tag])
        database.set_replace_invalid_characters_tag(gv._replace_invalid_characters_tag)

        database.set_default_ddl_collation(kwargs[gv._default_ddl_collation_tag])
        database.set_default_ddl_collation_tag(gv._default_ddl_collation_tag)

        database.set_storage_serialization_policy(kwargs[gv._storage_serialization_policy_tag])
        database.set_storage_serialization_policy_tag(gv._storage_serialization_policy_tag)

        database.set_comment(kwargs[gv._comment_tag])
        database.set_comment_tag(gv._comment_tag)

        database.prepare_query()
        database.create_database()

