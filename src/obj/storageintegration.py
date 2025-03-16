import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.gvobject import StorageIntegration as gv_stgint,Config as cfg, Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy
from validation.validateobject import ValidateObject as vo
from setup import privilege
from .baseobj import BaseObject 

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.is_new_integration(session=instance.parent.session,object_type=instance.parent.__class__.__name__,object_name=value)
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
        instance._type = gv_stgint._allowed_value_type
    
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

class StorageProvider:
    def __get__(self,instance,owner):
        return instance._storage_provider
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        vv.is_allowed_value(value=value,allowed_list=gv_stgint._allowed_value_storage_provider,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        instance._storage_provider = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._storage_provider

class StorageAwsRoleArn:
    def __get__(self,instance,owner):
        return instance._storage_aws_role_arn
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._storage_aws_role_arn=value
        elif 'S3' not in instance._storage_provider.upper():
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition="for non S3 storage providers") 
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._storage_aws_role_arn = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._storage_aws_role_arn

class StorageAwsExternalId:
    def __get__(self,instance,owner):
        return instance._storage_aws_external_id
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._storage_aws_external_id=value
        elif 'S3' not in instance._storage_provider.upper():
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition="for non S3 storage providers") 
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._storage_aws_external_id = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._storage_aws_external_id

class StorageAwsObjectAcl:
    def __get__(self,instance,owner):
        return instance._storage_aws_object_acl
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._storage_aws_external_id=value
        elif 'S3' not in instance._storage_provider.upper():
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition="for non S3 storage providers") 
        else:
            instance._storage_aws_object_acl = 'bucket-owner-full-control'
    
    def __delete__(self,instance):
        del instance._storage_aws_object_acl

class UsePrivateLinkEndPoint:
    def __get__(self,instance,owner):
        return instance._use_private_link_end_point
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._storage_aws_external_id=value
        elif 'GCS' in instance._storage_provider.upper():
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition="for GCS storage providers")
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._use_private_link_end_point = value
    
    def __delete__(self,instance):
        del instance._use_private_link_end_point

class AzureTenantId:
    def __get__(self,instance,owner):
        return instance._azure_tenant_id
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._storage_aws_external_id=value
        elif 'AZURE' not in instance._storage_provider.upper():
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition="for non AZURE storage providers")
        else:
            instance._azure_tenant_id = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._azure_tenant_id

class StorageAllowedLocations:
    def __get__(self,instance,owner):
        return instance._storage_allowed_locations
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        vv.is_tuple(value=value,object_type=instance.parent.__class__.__name__,object_name=self.__class__.__name__)
        for val in value:
            if val!='*':
                vv.is_valid_url(value=val,allowed_protocols=gv_stgint._allowed_value_storage_provider,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        instance._storage_allowed_locations = value
    
    def __delete__(self,instance):
        del instance._storage_allowed_locations

class StorageBlockedLocations:
    def __get__(self,instance,owner):
        return instance._storage_blocked_locations
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._storage_blocked_locations=value
        else:
            vv.is_tuple(value=value,object_type=instance.parent.__class__.__name__,object_name=self.__class__.__name__)
            for val in value:
                if val!='*':
                    vv.is_valid_url(value=val,allowed_protocols=gv_stgint._allowed_value_storage_provider,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._storage_blocked_locations = value

    
    def __delete__(self,instance):
        del instance._storage_blocked_locations

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._comment=value
        else:
            instance._comment = f"'{value}'"

    def __delete__(self,instance):
        del instance._comment


class StorageIntegrationAttrs:
    def __init__(self,parent):
        self.parent = parent
        
    name=Name()
    type=Type()
    enabled=Enabled()
    storage_provider=StorageProvider()
    storage_aws_role_arn=StorageAwsRoleArn()
    storage_aws_external_id=StorageAwsExternalId()
    storage_aws_object_acl=StorageAwsObjectAcl()
    use_private_link_endpoint=UsePrivateLinkEndPoint()
    azure_tenant_id=AzureTenantId()
    storage_allowed_locations=StorageAllowedLocations()
    storage_blocked_locations=StorageBlockedLocations()
    comment=Comment()

class StorageIntegration(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session, user_id, logger)
        self.attr = StorageIntegrationAttrs(self)


    def set_name(self, value):
        self.attr.name = value

    def set_type(self, value):
        self.attr.type = value

    def set_enabled(self, value):
        self.attr.enabled = value

    def set_storage_provider(self, value):
        self.attr.storage_provider = value

    def set_storage_aws_role_arn(self, value):
        self.attr.storage_aws_role_arn = value

    def set_storage_aws_external_id(self, value):
        self.attr.storage_aws_external_id = value

    def set_storage_aws_object_acl(self, value):
        self.attr.storage_aws_object_acl = value

    def set_use_private_link_end_point(self,value):
        self.attr.use_private_link_endpoint=value

    def set_azure_tenant_id(self,value):
        self.attr.azure_tenant_id=value

    def set_storage_allowed_locations(self, value):
        self.attr.storage_allowed_locations = value

    def set_storage_blocked_locations(self, value):
        self.attr.storage_blocked_locations = value

    def set_comment(self, value):
        self.attr.comment = value

    def set_qualified_name(self):
        self.qualified_name=self.attr.name

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv_stgint._name_tag,"_name")
        set_flag(gv_stgint._type_tag,"_type")
        set_flag(gv_stgint._enabled_tag,"_enabled")
        set_flag(gv_stgint._storage_provider_tag,"_storage_provider")
        set_flag(gv_stgint._storage_aws_role_arn_tag,"_storage_aws_role_arn")
        set_flag(gv_stgint._storage_aws_external_id_tag,"_storage_aws_external_id")
        set_flag(gv_stgint._storage_aws_object_acl_tag,"_storage_aws_object_acl")
        set_flag(gv_stgint._use_private_link_endpoint_tag,"_use_private_link_endpoint")
        set_flag(gv_stgint._azure_tenant_id_tag,"_azure_tenant_id")
        set_flag(gv_stgint._storage_allowed_locations_tag,"_storage_allowed_locations")
        set_flag(gv_stgint._storage_blocked_locations_tag,"_storage_blocked_locations")
        set_flag(gv_stgint._comment_tag,"_comment")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"CREATE STORAGE INTEGRATION {self.attr.name} {gv_stgint._type_tag} = {self.attr.type} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gv_stgint._storage_provider_tag:
                    self.qry = f" {self.qry} {gv_stgint._storage_provider_tag} = {self.attr.storage_provider} "
                if prop == gv_stgint._storage_aws_role_arn_tag:
                    self.qry = f" {self.qry} {gv_stgint._storage_aws_role_arn_tag} = {self.attr.storage_aws_role_arn} "
                if prop == gv_stgint._storage_aws_external_id_tag:
                    self.qry = f" {self.qry} {gv_stgint._storage_aws_external_id_tag} = {self.attr.storage_aws_external_id} "
                if prop == gv_stgint._storage_aws_object_acl_tag:
                    self.qry = f" {self.qry} {gv_stgint._storage_aws_object_acl_tag} = {self.attr.storage_aws_object_acl} "
                if prop == gv_stgint._azure_tenant_id_tag:
                    self.qry = f" {self.qry} {gv_stgint._azure_tenant_id_tag} = {self.attr.azure_tenant_id} "
                if prop == gv_stgint._use_private_link_endpoint_tag:
                    self.qry = f" {self.qry} {gv_stgint._use_private_link_endpoint_tag} = {self.attr.use_private_link_endpoint} "
                if prop == gv_stgint._enabled_tag:
                    self.qry = f" {self.qry} {gv_stgint._enabled_tag} = {self.attr.enabled} "
                if prop == gv_stgint._storage_allowed_locations_tag:
                    self.qry = f" {self.qry} {gv_stgint._storage_allowed_locations_tag} = {self.attr.storage_allowed_locations} "
                if prop == gv_stgint._storage_blocked_locations_tag:
                    self.qry = f" {self.qry} {gv_stgint._storage_blocked_locations_tag} = {self.attr.storage_blocked_locations} "
                if prop == gv_stgint._comment_tag:
                    self.qry = f" {self.qry} {gv_stgint._comment_tag} = {self.attr.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()

    def create_storage_integration(self):
        self.execute_final_query()

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
        self.set_name(kwargs[gv_stgint._name_tag])
        self.set_type(kwargs[gv_stgint._type_tag])
        self.set_storage_provider(kwargs[gv_stgint._storage_provider_tag])
        self.set_storage_aws_role_arn(kwargs[gv_stgint._storage_aws_role_arn_tag])
        self.set_storage_aws_external_id(kwargs[gv_stgint._storage_aws_external_id_tag])
        self.set_storage_aws_object_acl(kwargs[gv_stgint._storage_aws_object_acl_tag])
        self.set_azure_tenant_id(kwargs[gv_stgint._azure_tenant_id_tag])
        self.set_use_private_link_end_point(kwargs[gv_stgint._use_private_link_endpoint_tag])
        self.set_enabled(kwargs[gv_stgint._enabled_tag])
        self.set_storage_allowed_locations(kwargs[gv_stgint._storage_allowed_locations_tag])
        self.set_storage_blocked_locations(kwargs[gv_stgint._storage_blocked_locations_tag])
        self.set_comment(kwargs[gv_stgint._comment_tag])
        self.set_qualified_name()
        self.prepare_query()
        self.create_storage_integration()
        self.logger.info(f"creating schema {self.attr.name}")
        self.grant_default_privileges()
        if len(largs) == 0:
            self.create_deployment_entry()
