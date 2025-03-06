import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../processing'))



from vars.gvobject import Database as gv, Config as cfg , Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from dep import deploy
from setup import privilege 


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
        if value == "NONE":
            instance._data_retention_time_in_days = value
        else:
            vv.is_positive_number(value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_between(value,gv._min_allowed_value_data_retention_time_in_days,gv._max_allowed_value_data_retention_time_in_days,instance.parent.__class__.__name__,self.__class__.__name__)
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
        else:
            vv.is_positive_number(value,instance.parent.__class__.__name__,self.__class__.__name__)
            vv.is_between(value,gv._min_allowed_value_max_data_extension_time_in_days,gv._max_allowed_value_max_data_extension_time_in_days,instance.parent.__class__.__name__,self.__class__.__name__)    
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
        if value=="NONE":
            instance._external_volume = value
        else:
            vo.is_valid_external_volume(session=instance.parent.session,external_volume_identifier=value,object_type=self.__class__.__name__)
            instance._external_volume=value

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
        if value=="NONE":
            instance._catalog=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vo.is_valid_catalog(session=instance.parent.session,catalog_identifier=value,object_type=self.__class__.__name__)
            instance._catalog=value

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
        if value=="NONE":
            instance._default_ddl_collation=value
        else:
            vv.is_valid_collation_specifier(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,valid_specifiers=gv._allowed_collation_specifiers)
            instance._default_ddl_collation = f"'{value}'"

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
        if value=="NONE":
            instance._log_level=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_allowed_value(value=value,allowed_list=gv._allowed_values_log_level,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
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
            vv.is_allowed_value(value=value,allowed_list=gv._allowed_values_trace_level,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
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
            vv.is_allowed_value(value=value,allowed_list=gv._allowed_values_storage_serialization_policy,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
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
        if value == 'NONE':
            instance._comment = value
        else:
            instance._comment = f"'{value}'"
    
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

    log_level=LogLevel()
    trace_level=TraceLevel()

    storage_serialization_policy = StorageSerializationPolicy()
    storage_serialization_policy_tag = StorageSerializationPolicyTag()

    comment = Comment()
    comment_tag = CommentTag()


class Database:
    def __init__(self,session,user_id,logger):
        self.session = session
        self.user_id = user_id
        self.qry = ""
        self.logger = logger
        self.attr = DatabaseAttrs(self)

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

    def set_log_level(self, value):
        self.attr.log_level = value

    def set_trace_level(self, value):
        self.attr.trace_level = value

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
        set_flag(gv._log_level_tag,"_log_level")
        set_flag(gv._trace_level_tag,"_trace_level")
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
                if prop == gv._log_level_tag:
                    self.qry = f" {self.qry} {gv._log_level_tag} = {self.attr.log_level} "
                if prop == gv._trace_level_tag:
                    self.qry = f" {self.qry} {gv._trace_level_tag} = {self.attr.trace_level} "
                if prop == gv._storage_serialization_policy_tag:
                    self.qry = f" {self.qry} {self.attr.storage_serialization_policy_tag} = {self.attr.storage_serialization_policy} "
                if prop == gv._comment_tag:
                    self.qry = f" {self.qry} {self.attr.comment_tag} = {self.attr.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()

    def create_deployment_entry(self):
        deploy_inst = deploy.Deploy(self.session)
        self.logger.info(f"Tracking for deployment database object : {self.attr.name}")
        deploy_inst.insert_into_deployment_script_table(obj_qry=self.qry, user_id=self.user_id)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database('NA')
        deploy_inst.set_object_schema('NA')
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()

    def grant_default_privileges(self,*largs):
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges[self.__class__.__name__.upper()]:
                if len(largs)==0:
                    priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = self.__class__.__name__.upper(),object_identifier=self.attr.name,role = role)
                else:
                    priv_inst.grant_privilege_on_object_to_role(privilege_type=privileges, object_type=self.__class__.__name__.upper(), object_identifier='DB_CONFIG', role=role)


    def create_database(self):
        self.session.sql(self.qry).collect()

    def create_object(self,*largs,**kwargs):
        if len(largs) != 0:
            self.qry = f"CREATE DATABASE {kwargs[gv._name_tag]}"
            self.create_database()
            self.grant_default_privileges(*['initial'])
        else:
            self.set_name(kwargs[gv._name_tag])
            self.set_name_tag(gv._name_tag)

            self.set_data_retention_time_in_days(kwargs[gv._data_retention_time_in_days_tag])
            self.set_data_retention_time_in_days_tag(gv._data_retention_time_in_days_tag)

            self.set_max_data_extension_time_in_days(kwargs[gv._max_data_extension_time_in_days_tag])
            self.set_max_data_extension_time_in_days_tag(gv._max_data_extension_time_in_days_tag)

            self.set_external_volume(kwargs[gv._external_volume_tag])
            self.set_external_volume_tag(gv._external_volume_tag)

            self.set_catalog(kwargs[gv._catalog_tag])
            self.set_catalog_tag(gv._catalog_tag)

            self.set_replace_invalid_characters(kwargs[gv._replace_invalid_characters_tag])
            self.set_replace_invalid_characters_tag(gv._replace_invalid_characters_tag)

            self.set_default_ddl_collation(kwargs[gv._default_ddl_collation_tag])
            self.set_default_ddl_collation_tag(gv._default_ddl_collation_tag)

            self.set_log_level(kwargs[gv._log_level_tag])
            self.set_trace_level(kwargs[gv._trace_level_tag])

            self.set_storage_serialization_policy(kwargs[gv._storage_serialization_policy_tag])
            self.set_storage_serialization_policy_tag(gv._storage_serialization_policy_tag)

            self.set_comment(kwargs[gv._comment_tag])
            self.set_comment_tag(gv._comment_tag)

            self.prepare_query()
            self.logger.info(f"creating database {self.attr.name}")
            self.create_database()
            self.grant_default_privileges()
            self.create_deployment_entry()

            

