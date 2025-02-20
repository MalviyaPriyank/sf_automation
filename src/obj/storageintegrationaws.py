import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.gvobject import StorageIntegrationAws as gv_stgintaws,Config as cfg, Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy
from validation.validateobject import ValidateObject as vo
from setup import privilege


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

class Type:
    def __get__(self,instance,owner):
        return instance._type
    
    def __set__(self,instance,value):
        instance._type = gv_stgintaws._allowed_value_type
    
    def __delete__(self,instance):
        del instance._type

class Enabled:
    def __get__(self,instance,owner):
        return instance._enabled
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        instance._enabled = value
    
    def __delete__(self,instance):
        del instance._enabled

class StorageAllowedLocations:
    def __get__(self,instance,owner):
        return instance._storage_allowed_locations
    
    def __set__(self,instance,value):
        instance._storage_allowed_locations = value
    
    def __delete__(self,instance):
        del instance._storage_allowed_locations

class StorageProvider:
    def __get__(self,instance,owner):
        return instance._storage_provider
    
    def __set__(self,instance,value):
        instance._storage_provider = value
    
    def __delete__(self,instance):
        del instance._storage_provider

class StorageAwsRoleArn:
    def __get__(self,instance,owner):
        return instance._storage_aws_role_arn
    
    def __set__(self,instance,value):
        instance._storage_aws_role_arn = value
    
    def __delete__(self,instance):
        del instance._storage_aws_role_arn

class StorageAwsExternalId:
    def __get__(self,instance,owner):
        return instance._storage_aws_external_id
    
    def __set__(self,instance,value):
        instance._storage_aws_external_id = value
    
    def __delete__(self,instance):
        del instance._storage_aws_external_id

class StorageAwsObjectAcl:
    def __get__(self,instance,owner):
        return instance._storage_aws_object_acl
    
    def __set__(self,instance,value):
        instance._storage_aws_object_acl = value
    
    def __delete__(self,instance):
        del instance._storage_aws_object_acl

class UsePrivateLinkEndPoint:
    def __get__(self,instance,owner):
        return instance._use_private_link_end_point
    
    def __set__(self,instance,value):
        if value=='NONE':
            instance._use_private_link_end_point=value
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._use_private_link_end_point = value
    
    def __delete__(self,instance):
        del instance._use_private_link_end_point

class StorageBlockedLocations:
    def __get__(self,instance,owner):
        return instance._storage_blocked_locations
    
    def __set__(self,instance,value):
        instance._storage_blocked_locations = value
    
    def __delete__(self,instance):
        del instance._storage_blocked_locations

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = value

    def __delete__(self,instance):
        del instance._comment


class StorageIntegrationAttrs:
    def __init__(self,parent):
        self.parent = parent
        
    name=Name()
    type=Type()
    enabled=Enabled()
    storage_allowed_locations=StorageAllowedLocations()
    storage_provider=StorageProvider()
    storage_aws_role_arn=StorageAwsRoleArn()
    storage_aws_external_id=StorageAwsExternalId()
    storage_aws_object_acl=StorageAwsObjectAcl()
    use_private_link_endpoint=UsePrivateLinkEndPoint()
    storage_blocked_locations=StorageBlockedLocations()
    comment=Comment()

class StorageIntegration:
    def __init__(self,session,user_id,logger):
        self.session = session
        self.user_id = user_id
        self.qry = ""
        self.logger = logger
        self.attr = StorageIntegrationAttrs(self)


    def set_name(self, value):
        self.attr.name = value

    def set_type(self, value):
        self.attr.type = value

    def set_enabled(self, value):
        self.attr.enabled = value

    def set_storage_allowed_locations(self, value):
        self.attr.storage_allowed_locations = value

    def set_storage_provider(self, value):
        self.attr.storage_provider = value

    def set_storage_aws_role_arn(self, value):
        self.attr.storage_aws_role_arn = value

    def set_storage_aws_external_id(self, value):
        self.attr.storage_aws_external_id = value

    def set_storage_aws_object_acl(self, value):
        self.attr.storage_aws_object_acl = value

    def set_use_private_link_endpoint(self, value):
        self.attr.use_private_link_endpoint = value

    def set_storage_blocked_locations(self, value):
        self.attr.storage_blocked_locations = value

    def set_comment(self, value):
        self.attr.comment = value

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv_stgintaws._name_tag,"_name")
        set_flag(gv_stgintaws._with_managed_access_tag,"_with_managed_access")
        set_flag(gv_stgintaws._data_retention_time_in_days_tag,"_data_retention_time_in_days")
        set_flag(gv_stgintaws._max_data_extension_time_in_days_tag,"_max_data_extension_time_in_days")
        set_flag(gv_stgintaws._external_volume_tag,"_external_volume")
        set_flag(gv_stgintaws._catalog_tag,"_catalog")
        set_flag(gv_stgintaws._replace_invalid_characters_tag,"_replace_invalid_characters")
        set_flag(gv_stgintaws._default_ddl_collation_tag,"_default_ddl_collation")
        set_flag(gv_stgintaws._log_level_tag,"_log_level")
        set_flag(gv_stgintaws._trace_level_tag,"_trace_level")
        set_flag(gv_stgintaws._storage_serialization_policy_tag,"_storage_serialization_policy")
        set_flag(gv_stgintaws._classification_profile_tag,"_classification_profile")
        set_flag(gv_stgintaws._comment_tag,"_comment")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"CREATE STORAGE INTEGRATION {self.attr.name} {gv_stgintaws._type_tag} = {self.attr.type} {gv_stgintaws._enabled_tag}={self.attr.enabled} {gv_stgintaws._storage_allowed_locations_tag}={self.attr.storage_allowed_locations} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gv_stgintaws._storage_blocked_locations_tag:
                    self.qry = f" {self.qry} {gv_stgintaws._storage_blocked_locations_tag} = {self.attr.storage_blocked_locations} "
                if prop == gv_stgintaws._comment_tag:
                    self.qry = f" {self.qry} {gv_stgintaws._comment_tag} = {self.attr.comment} "
                if prop == gv_stgintaws._storage_provider_tag:
                    self.qry = f" {self.qry} {gv_stgintaws._storage_provider_tag} = {self.attr.storage_provider} "
                if prop == gv_stgintaws._storage_aws_role_arn_tag:
                    self.qry = f" {self.qry} {gv_stgintaws._storage_aws_role_arn_tag} = {self.attr.storage_aws_role_arn} "
                if prop == gv_stgintaws._storage_aws_external_id_tag:
                    self.qry = f" {self.qry} {gv_stgintaws._storage_aws_external_id_tag} = {self.attr.storage_aws_external_id} "
                if prop == gv_stgintaws._storage_aws_object_acl_tag:
                    self.qry = f" {self.qry} {gv_stgintaws._storage_aws_object_acl_tag} = {self.attr.storage_aws_object_acl} "
                if prop == gv_stgintaws._use_private_link_endpoint_tag:
                    self.qry = f" {self.qry} {gv_stgintaws._use_private_link_endpoint_tag} = {self.attr.use_private_link_endpoint} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()

    def create_storage_integration(self):
        self.session.sql(self.qry).collect()

    def create_deployment_entry(self):
        deploy_inst = Deploy(self.session)
        self.logger.info(f"Tracking for deployment schema object : {self.attr.name}")
        deploy_inst.insert_into_deployment_script_table(qry=self.qry, user_id=self.user_id)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database(self.attr.database)
        deploy_inst.set_object_schema('NA')
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()

    def grant_default_privileges(self):
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges[self.__class__.__name__.upper()]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = self.__class__.__name__.upper(),object_identifier=self.qualified_name,role = role)


    def create_object(self,*largs,**kwargs):
        self.set_name(kwargs[gv_stgintaws._name_tag])
        self.set_type(kwargs[gv_stgintaws._type_tag])
        self.set_enabled(kwargs[gv_stgintaws._enabled_tag])
        self.set_storage_allowed_locations(kwargs[gv_stgintaws._storage_allowed_locations_tag])
        self.set_storage_blocked_locations(kwargs[gv_stgintaws._storage_blocked_locations_tag])
        self.set_comment(kwargs[gv_stgintaws._comment_tag])
        self.set_storage_aws_role_arn(kwargs[gv_stgintaws._storage_aws_role_arn_tag])
        self.set_storage_aws_external_id(kwargs[gv_stgintaws._storage_aws_external_id_tag])
        self.set_storage_aws_object_acl(kwargs[gv_stgintaws._storage_aws_object_acl_tag])
        self.set_use_private_link_endpoint(kwargs[gv_stgintaws._use_private_link_endpoint_tag])

        self.prepare_query()
        self.create_storage_integration()
        self.logger.info(f"creating schema {self.attr.name}")
        self.grant_default_privileges()
        if len(largs) == 0:
            self.create_deployment_entry()
