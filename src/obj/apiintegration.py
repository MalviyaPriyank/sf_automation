
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from .baseobj import BaseObject 
from vars.obj.apiintegration.gvapiintegration import ComputePoolTag as tags
from src.usr.user import ChatHistory


class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)

    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(
                value=value,
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            vo.is_new_object(
                session=instance.parent.session,
                object_type="INTEGRATION",
                object_name=name
            )
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
                vv.required_attribute_check(
                    value=value,
                    object_type=instance.parent.object_type,
                    attr_name=self.__class__.__name__
                )
                vo.object_exist(
                    session=instance.parent.session,
                    object_type="INTEGRATION",
                    object_name=old_name
                )
                vo.is_new_object(
                    session=instance.parent.session,
                    object_type="INTEGRATION",
                    object_name=new_name
                )
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to

class APIType:
    def __get__(self,instance,owner):
        return instance._api_type
    
    def __set__(self,instance,value):
        value=value.upper()
        vv.required_attribute_check(
            value=value,
            object_type=instance.parent.__class__.__name__,
            attr_name=self.__class__.__name__
        )
        vv.is_allowed_value(
            value=value,
            allowed_list=tags.allowed_value_list().get(tags.API_TYPE),
            object_type=instance.parent.__class__.__name__,
            attr_name=self.__class__.__name__
        )
        instance._api_type = value
    
    def __delete__(self,instance):
        del instance._api_type


class APIProvider:
    def __get__(self,instance,owner):
        return instance._api_provider
    
    def __set__(self,instance,value):
        if instance._api_type == 'GIT':
            instance._api_provider = 'git_https_api'  
        elif instance._api_type=='AMAZON':
            vv.required_attribute_check(
                value=value,
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            vv.is_allowed_value(
                value=value,
                allowed_list=tags.allowed_value_list().get(tags.API_PROVIDER).get('AMAZON'),
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._api_provider=value
        elif instance._api_type=='GOOGLE':
            instance._api_provider='google_api_gateway'
        elif instance._api_type=='AZURE':
            instance._api_provider='azure_api_management'
        
    def __delete__(self,instance):
        del instance._api_provider

class APIAWSRoleARN:
    def __get__(self,instance,owner):
        return instance._api_aws_role_arn
    
    def __set__(self,instance,value):
        if instance._api_type=='AMAZON':
            vv.required_attribute_check(
                value=value,
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._api_aws_role_arn=value
        elif value == "NONE":
            instance._api_aws_role_arn="NONE"
        else:
            vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} can only be used for AMAZON Api Gateways.")
    
    def __delete__(self,instance):
        del instance._api_aws_role_arn

class APIKey:
    def __get__(self,instance,owner):
        return instance._api_key
    
    def __set__(self,instance,value):
        if (instance._api_type=='AZURE' or 
            instance._api_type=='AMAZON'):
            instance._api_key=value
        else:
            vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} can only be used when API_TYPE is AZURE or AMAZON API.")
    
    def __delete__(self,instance):
        del instance._api_key

class APIAllowedPrefixes:
    def __get__(self,instance,owner):
        return instance._api_allowed_prefixes
    
    def __set__(self,instance,value):
        vv.required_attribute_check(
            value=value,
            object_type=instance.parent.object_type,
            attr_name=self.__class__.__name__
        )
        if isinstance(value,list):
            instance.parent.logger.info("Value received as list")
            val_string=""
            for i in range(0,len(value)):
                instance.parent.logger.info(f"Validating {value[i]} for {self.__class__.__name__}")
                vv.is_valid_url_for_contact(
                    object_type=instance.parent.object_type,
                    attr_name=self.__class__.__name__,
                    url=value
                )
                if i != len(value)-1:
                    val_string=val_string+f"'{value[i]}',"
                elif i == len(value)-1:
                    val_string=val_string+f"'{value[i]}'"
            instance.parent.logger.info(f" final value string : {val_string}")
            instance._api_allowed_prefixes=f"({val_string})"
        elif isinstance(value,str):
            vv.is_valid_url_for_contact(
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__,
                url=value
            )
            instance._api_allowed_prefixes=f"('{value}')"

    def __delete__(self,instance):
        del instance._api_allowed_prefixes

class Enabled:
    def __get__(self,instance,owner):
        return instance._enabled
    
    def __set__(self,instance,value):
        vv.required_attribute_check(
            value=value,
            object_type=instance.parent.object_type,
            attr_name=self.__class__.__name__
        )
        vv.is_bool(
            value=value,
            object_type=instance.parent.object_type,
            attr_name=self.__class__.__name__
        )
        instance._enabled=value
    
    def __delete__(self,instance):
        del instance._enabled

class AzureTenantID:
    def __get__(self,instance,owner):
        return instance._azure_tenant_id
    
    def __set__(self,instance,value):
        if instance._api_type!='AZURE' and value =='NONE':
            instance._azure_tenant_id="NONE"
        elif instance._api_type!='AZURE' and value != 'NONE':
            vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} parameter can only be used for API TYPE AZURE.")
        elif instance._api_type=='AZURE':
            vv.required_attribute_check(
                value=value,
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._azure_tenant_id=value
    
    def __delete__(self,instance):
        del instance._azure_tenant_id

class AzureADApplicationID:
    def __get__(self,instance,owner):
        return instance._azure_ad_application_id
    
    def __set__(self,instance,value):
        if instance._api_type!='AZURE' and value =='NONE':
            instance._azure_ad_application_id="NONE"
        elif instance._api_type!='AZURE' and value != 'NONE':
            vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} parameter can only be used for API TYPE AZURE.")
        elif instance._api_type=='AZURE':
            vv.required_attribute_check(
                value=value,
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._azure_ad_application_id=value
    
    def __delete__(self,instance):
        del instance._azure_ad_application_id

class APIBlockedPrefixes:
    def __get__(self,instance,owner):
        return instance._api_blocked_prefixes
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._api_blocked_prefixes="NONE"
        else:
            if isinstance(value,list):
                instance.parent.logger.info("Value received as list")
                val_string=""
                for i in range(0,len(value)):
                    instance.parent.logger.info(f"Validating {value[i]} for {self.__class__.__name__}")
                    vv.is_valid_url_for_contact(
                        object_type=instance.parent.object_type,
                        attr_name=self.__class__.__name__,
                        url=value
                    )
                    if i != len(value)-1:
                        val_string=val_string+f"'{value[i]}',"
                    elif i == len(value)-1:
                        val_string=val_string+f"'{value[i]}'"
                instance.parent.logger.info(f" final value string : {val_string}")
                instance._api_blocked_prefixes=f"({val_string})"
            elif isinstance(value,str):
                vv.is_valid_url_for_contact(
                    object_type=instance.parent.object_type,
                    attr_name=self.__class__.__name__,
                    url=value
                )
                instance._api_blocked_prefixes=f"('{value}')"
    
    def __delete__(self,instance):
        del instance._api_blocked_prefixes

class GoogleAudience:
    def __get__(self,instance,owner):
        return instance._google_audience
    
    def __set__(self,instance,value):
        if instance._api_type=='GOOGLE':
            vv.required_attribute_check(
                value=value,
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._google_audience = value
    
    def __delete__(self,instance):
        del instance._google_audience


class AllowedAuthenticationSecrets:
    def __get__(self,instance,owner):
        return instance._allowed_authentication_secrets
    
    def __set__(self,instance,value):
        if instance._api_type=='GIT':
            if isinstance(value,list):
                if ('none' in value or 'NONE' in value):
                    instance._allowed_authentication_secrets= 'NONE'
                elif('all' in value or 'ALL' in value):
                    instance._allowed_authentication_secrets= 'ALL'
                else:
                    instance.parent.logger.info("Value received as list")
                    val_string=""
                    for i in range(0,len(value)):
                        instance.parent.logger.info(f"Validating {value[i]} for {self.__class__.__name__}")
                        vv.is_valid_url_for_contact(
                            object_type=instance.parent.object_type,
                            attr_name=self.__class__.__name__,
                            url=value
                        )
                        if i != len(value)-1:
                            val_string=val_string+f"'{value[i]}',"
                        elif i == len(value)-1:
                            val_string=val_string+f"'{value[i]}'"
                    instance.parent.logger.info(f" final value string : {val_string}")
                    instance._allowed_authentication_secrets=f"({val_string})"
            elif isinstance(value,str):
                if ( value == 'none' or value == 'NONE'):
                    instance._allowed_authentication_secrets= 'NONE'
                elif(value == 'all' or value == 'ALL'):
                    instance._allowed_authentication_secrets= 'ALL'
                else:
                    vv.is_valid_url_for_contact(
                        object_type=instance.parent.object_type,
                        attr_name=self.__class__.__name__,
                        url=value
                    )
                    instance._allowed_authentication_secrets=f"('{value}')"
    
    def __delete__(self,instance):
        del instance._allowed_authentication_secrets


class APIIntegrationAttrs:
    def __init__(self,parent):
        self.parent = parent

    name = Name()
    api_type=APIType()
    api_provider=APIProvider()
    api_aws_role_arn=APIAWSRoleARN()
    api_key=APIKey()
    api_allowed_prefixes=APIAllowedPrefixes()
    enabled=Enabled()
    azure_tenant_id=AzureTenantID()
    azure_ad_application_id=AzureADApplicationID()
    api_blocked_prefixes=APIBlockedPrefixes()
    google_audience=GoogleAudience()
    allowed_authentication_secrets=AllowedAuthenticationSecrets()

class APIIntegration(BaseObject):
    def __init__(self, session, user_id, logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger)
        self.attr = APIIntegrationAttrs(self)
        self.object_type=self.__class__.__name__

    def set_name(self,val):self.attr.name = val
    def set_api_type(self,val):self.attr.api_type=val
    def set_api_provider(self,val): self.attr.api_provider=val
    def set_api_aws_role_arn(self,val):self.attr.api_aws_role_arn=val
    def set_api_key(self,val):self.attr.api_key=val
    def set_api_allowed_prefixes(self,val):self.attr.api_allowed_prefixes=val
    def set_enabled(self,val):self.attr.enabled=val
    def set_azure_tenant_id(self,val):self.attr.azure_tenant_id=val
    def set_azure_ad_application_id(self,val):self.attr.azure_ad_application_id=val
    def set_api_blocked_prefixes(self,val):self.attr.api_blocked_prefixes=val
    def set_google_audience(self,val):self.attr.google_audience=val
    def set_allowed_authentication_secrets(self,val):self.attr.allowed_authentication_secrets=val
    def set_comment(self,val):self.base_attrs.comment=val

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            if attribute_tag != tags.COMMENT:
                self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
            elif attribute_tag==tags.COMMENT:
                self.flag_dic[attribute_tag] = 1 if getattr(self.base_attrs, attribute_name) != "NONE" else 0
        
        if self.attr.api_type=='AMAZON':
            set_flag(tags.API_KEY,"_api_key")
            set_flag(tags.API_ALLOWED_PREFIXES,"_api_allowed_prefixes")
            set_flag(tags.ENABLED,"_enabled")
            set_flag(tags.COMMENT,"_comment")
        if self.attr.api_type=='AZURE':
            set_flag(tags.API_KEY,"_api_key")
            set_flag(tags.API_ALLOWED_PREFIXES,"_api_allowed_prefixes")
            set_flag(tags.API_BLOCKED_PREFIXES,"_api_blocked_prefixes")
            set_flag(tags.ENABLED,"_enabled")
            set_flag(tags.COMMENT,"_comment")
        if self.attr.api_type=='GOOGLE':
            set_flag(tags.API_BLOCKED_PREFIXES,"_api_blocked_prefixes")
            set_flag(tags.ENABLED,"_enabled")
            set_flag(tags.COMMENT,"_comment")
        if self.attr.api_type=='GIT':
            set_flag(tags.API_BLOCKED_PREFIXES,"_api_blocked_prefixes")
            set_flag(tags.ALLOWED_AUTHENTICATION_SECRETS,"_allowed_authentication_secrets")
            set_flag(tags.ENABLED,"_enabled")
            set_flag(tags.COMMENT,"_comment")


    def alter_object(self):        
        for prop in self.property_lst:
            if prop == tags.VALUE_LIST:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.VALUE_LIST} = {self.attr.value_list}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER NETWORK RULE {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming {self.__class__.__name__} {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_query(self):
        self.qry = f"""
        CREATE API INTEGRATION 
        {self.attr.name[0]}
        {tags.API_PROVIDER} = {self.attr.api_provider}
        """
        if self.attr.api_type=='AMAZON':
            self.qry+= f"""
            {tags.API_AWS_ROLE_ARN} = '{self.attr.api_aws_role_arn}'
            """
        if self.attr.api_type=='AZURE':
            self.qry+=f"""
            {tags.AZURE_TENANT_ID} = '{self.attr.azure_tenant_id}'
            {tags.AZURE_AD_APPLICATION_ID} = '{self.attr.azure_ad_application_id}'
            """
        if self.attr.api_type=='GOOGLE':
            self.qry+=f"""
            {tags.API_PROVIDER} = {self.attr.api_provider}
            {tags.GOOGLE_AUDIENCE} = '{self.attr.google_audience}'
            {tags.API_ALLOWED_PREFIXES} = {self.attr.api_allowed_prefixes}
            """
        if self.attr.api_type=='GIT':
            self.qry+=f"""
            {tags.API_ALLOWED_PREFIXES} = {self.attr.api_allowed_prefixes}
            """


    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if self.attr.api_type=='AMAZON':
                    if prop == tags.API_KEY:
                        self.qry = f" {self.qry} {tags.API_KEY} = '{self.attr.api_key}' "
                    if prop == tags.API_ALLOWED_PREFIXES:
                        self.qry = f" {self.qry} {tags.API_ALLOWED_PREFIXES} = {self.attr.api_allowed_prefixes} "
                    if prop == tags.ENABLED:
                        self.qry = f" {self.qry} {tags.ENABLED} = {self.attr.enabled} "
                    if prop == tags.COMMENT:
                        self.qry = f" {self.qry} {tags.COMMENT} = {self.base_attrs.comment} "
                if self.attr.api_type=='AZURE':
                    if prop == tags.API_KEY:
                        self.qry = f" {self.qry} {tags.API_KEY} = '{self.attr.api_key}' "
                    if prop == tags.API_ALLOWED_PREFIXES:
                        self.qry = f" {self.qry} {tags.API_ALLOWED_PREFIXES} = {self.attr.api_allowed_prefixes} "
                    if prop == tags.API_BLOCKED_PREFIXES:
                        self.qry = f" {self.qry} {tags.API_BLOCKED_PREFIXES} = {self.attr.api_blocked_prefixes} "
                    if prop == tags.ENABLED:
                        self.qry = f" {self.qry} {tags.ENABLED} = {self.attr.enabled} "
                    if prop == tags.COMMENT:
                        self.qry = f" {self.qry} {tags.COMMENT} = {self.base_attrs.comment} "
                if self.attr.api_type=='GOOGLE':
                    if prop == tags.API_BLOCKED_PREFIXES:
                        self.qry = f" {self.qry} {tags.API_BLOCKED_PREFIXES} = {self.attr.api_blocked_prefixes} "
                    if prop == tags.ENABLED:
                        self.qry = f" {self.qry} {tags.ENABLED} = {self.attr.enabled} "
                    if prop == tags.COMMENT:
                        self.qry = f" {self.qry} {tags.COMMENT} = {self.base_attrs.comment} "
                if self.attr.api_type=='GIT':
                    if prop == tags.API_BLOCKED_PREFIXES:
                        self.qry = f" {self.qry} {tags.API_BLOCKED_PREFIXES} = {self.attr.api_blocked_prefixes} "
                    if prop == tags.ALLOWED_AUTHENTICATION_SECRETS:
                        self.qry = f" {self.qry} {tags.ALLOWED_AUTHENTICATION_SECRETS} = {self.attr.allowed_authentication_secrets} "
                    if prop == tags.ENABLED:
                        self.qry = f" {self.qry} {tags.ENABLED} = {self.attr.enabled} "
                    if prop == tags.COMMENT:
                        self.qry = f" {self.qry} {tags.COMMENT} = {self.base_attrs.comment} "


    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == 'TRUE':
            self.set_create_query()
            self.add_properties_to_query()
        elif self.is_create=='FALSE':
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()
    
class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=APIIntegration(session=session,
                         user_id=user_id,
                         logger=logger)
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        obj_inst.logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        obj_inst.logger.info("set api_type")
        if tags.API_TYPE in kwargs.keys():
            obj_inst.set_api_type(kwargs[tags.API_TYPE])
        else:
            obj_inst.set_api_type('NONE')

        if obj_inst.attr.api_type=='AMAZON':
            if tags.API_PROVIDER in kwargs.keys():
                obj_inst.set_api_provider(kwargs[tags.API_PROVIDER])
            else:
                obj_inst.set_api_provider('NONE')
            obj_inst.logger.info(f"API_PROVIDER : {obj_inst.attr.api_provider}")

            if tags.API_AWS_ROLE_ARN in kwargs.keys():
                obj_inst.set_api_aws_role_arn(kwargs[tags.API_AWS_ROLE_ARN])
            else:
                obj_inst.set_api_aws_role_arn('NONE')
            obj_inst.logger.info(f"API_AWS_ROLE_ARN : {obj_inst.attr.api_aws_role_arn}")

            if tags.API_KEY in kwargs.keys():
                obj_inst.set_api_key(kwargs[tags.API_KEY])
            else:
                obj_inst.set_api_key('NONE')
            obj_inst.logger.info(f"API_KEY : {obj_inst.attr.api_key}")

            if tags.API_ALLOWED_PREFIXES in kwargs.keys():
                obj_inst.set_api_allowed_prefixes(kwargs[tags.API_ALLOWED_PREFIXES])
            else:
                obj_inst.set_api_allowed_prefixes('NONE')
            obj_inst.logger.info(f"API_ALLOWED_PREFIXES : {obj_inst.attr.api_allowed_prefixes}")

            if tags.ENABLED in kwargs.keys():
                obj_inst.set_enabled(kwargs[tags.ENABLED])
            else:
                obj_inst.set_enabled('NONE')
            obj_inst.logger.info(f"ENABLED : {obj_inst.attr.enabled}")

            if tags.COMMENT in kwargs.keys():
                obj_inst.set_comment(kwargs[tags.COMMENT])
            else:
                obj_inst.set_comment('NONE')
            obj_inst.logger.info(f"COMMENT : {obj_inst.base_attrs.comment}")
        
        if obj_inst.attr.api_type=='AZURE':
            if tags.API_PROVIDER in kwargs.keys():
                obj_inst.set_api_provider(kwargs[tags.API_PROVIDER])
            else:
                obj_inst.set_api_provider('NONE')
            obj_inst.logger.info(f"API_PROVIDER : {obj_inst.attr.api_provider}")

            if tags.AZURE_TENANT_ID in kwargs.keys():
                obj_inst.set_azure_tenant_id(kwargs[tags.AZURE_TENANT_ID])
            else:
                obj_inst.set_azure_tenant_id('NONE')
            obj_inst.logger.info(f"AZURE_TENANT_ID : {obj_inst.attr.azure_tenant_id}")

            if tags.AZURE_AD_APPLICATION_ID in kwargs.keys():
                obj_inst.set_azure_ad_application_id(kwargs[tags.AZURE_AD_APPLICATION_ID])
            else:
                obj_inst.set_azure_ad_application_id('NONE')
            obj_inst.logger.info(f"AZURE_AD_APPLICATION_ID : {obj_inst.attr.azure_ad_application_id}")

            if tags.API_KEY in kwargs.keys():
                obj_inst.set_api_key(kwargs[tags.API_KEY])
            else:
                obj_inst.set_api_key('NONE')
            obj_inst.logger.info(f"API_KEY : {obj_inst.attr.api_key}")

            if tags.API_ALLOWED_PREFIXES in kwargs.keys():
                obj_inst.set_api_allowed_prefixes(kwargs[tags.API_ALLOWED_PREFIXES])
            else:
                obj_inst.set_api_allowed_prefixes('NONE')
            obj_inst.logger.info(f"API_ALLOWED_PREFIXES : {obj_inst.attr.api_allowed_prefixes}")

            if tags.API_BLOCKED_PREFIXES in kwargs.keys():
                obj_inst.set_api_blocked_prefixes(kwargs[tags.API_BLOCKED_PREFIXES])
            else:
                obj_inst.set_api_blocked_prefixes('NONE')
            obj_inst.logger.info(f"API_BLOCKED_PREFIXES : {obj_inst.attr.api_blocked_prefixes}")

            if tags.ENABLED in kwargs.keys():
                obj_inst.set_enabled(kwargs[tags.ENABLED])
            else:
                obj_inst.set_enabled('NONE')
            obj_inst.logger.info(f"ENABLED : {obj_inst.attr.enabled}")

            if tags.COMMENT in kwargs.keys():
                obj_inst.set_comment(kwargs[tags.COMMENT])
            else:
                obj_inst.set_comment('NONE')
            obj_inst.logger.info(f"COMMENT : {obj_inst.base_attrs.comment}")

        if obj_inst.attr.api_type=='GOOGLE':
            if tags.API_PROVIDER in kwargs.keys():
                obj_inst.set_api_provider(kwargs[tags.API_PROVIDER])
            else:
                obj_inst.set_api_provider('NONE')
            obj_inst.logger.info(f"API_PROVIDER : {obj_inst.attr.api_provider}")

            if tags.GOOGLE_AUDIENCE in kwargs.keys():
                obj_inst.set_google_audience(kwargs[tags.GOOGLE_AUDIENCE])
            else:
                obj_inst.set_google_audience('NONE')
            obj_inst.logger.info(f"GOOGLE_AUDIENCE : {obj_inst.attr.google_audience}")

            if tags.API_ALLOWED_PREFIXES in kwargs.keys():
                obj_inst.set_api_allowed_prefixes(kwargs[tags.API_ALLOWED_PREFIXES])
            else:
                obj_inst.set_api_allowed_prefixes('NONE')
            obj_inst.logger.info(f"API_ALLOWED_PREFIXES : {obj_inst.attr.api_allowed_prefixes}")

            if tags.API_BLOCKED_PREFIXES in kwargs.keys():
                obj_inst.set_api_blocked_prefixes(kwargs[tags.API_BLOCKED_PREFIXES])
            else:
                obj_inst.set_api_blocked_prefixes('NONE')
            obj_inst.logger.info(f"API_BLOCKED_PREFIXES : {obj_inst.attr.api_blocked_prefixes}")

            if tags.ENABLED in kwargs.keys():
                obj_inst.set_enabled(kwargs[tags.ENABLED])
            else:
                obj_inst.set_enabled('NONE')
            obj_inst.logger.info(f"ENABLED : {obj_inst.attr.enabled}")

            if tags.COMMENT in kwargs.keys():
                obj_inst.set_comment(kwargs[tags.COMMENT])
            else:
                obj_inst.set_comment('NONE')
            obj_inst.logger.info(f"COMMENT : {obj_inst.base_attrs.comment}")

        if obj_inst.attr.api_type=='GIT':
            if tags.DATABASE in kwargs.keys():
                obj_inst.set_database(kwargs[tags.DATABASE])
            else:
                obj_inst.set_database('NONE')
            obj_inst.logger.info(f"DATABASE : {obj_inst.base_attrs.database}")

            if tags.SCHEMA in kwargs.keys():
                obj_inst.set_schema(kwargs[tags.SCHEMA])
            else:
                obj_inst.set_schema('NONE')
            obj_inst.logger.info(f"SCHEMA : {obj_inst.base_attrs.schema}")

            if tags.API_PROVIDER in kwargs.keys():
                obj_inst.set_api_provider(kwargs[tags.API_PROVIDER])
            else:
                obj_inst.set_api_provider('NONE')
            obj_inst.logger.info(f"API_PROVIDER : {obj_inst.attr.api_provider}")

            if tags.API_ALLOWED_PREFIXES in kwargs.keys():
                obj_inst.set_api_allowed_prefixes(kwargs[tags.API_ALLOWED_PREFIXES])
            else:
                obj_inst.set_api_allowed_prefixes('NONE')
            obj_inst.logger.info(f"API_ALLOWED_PREFIXES : {obj_inst.attr.api_allowed_prefixes}")

            if tags.API_BLOCKED_PREFIXES in kwargs.keys():
                obj_inst.set_api_blocked_prefixes(kwargs[tags.API_BLOCKED_PREFIXES])
            else:
                obj_inst.set_api_blocked_prefixes('NONE')
            obj_inst.logger.info(f"API_BLOCKED_PREFIXES : {obj_inst.attr.api_blocked_prefixes}")

            if tags.ALLOWED_AUTHENTICATION_SECRETS in kwargs.keys():
                obj_inst.set_allowed_authentication_secrets(kwargs[tags.ALLOWED_AUTHENTICATION_SECRETS])
            else:
                obj_inst.set_allowed_authentication_secrets('NONE')
            obj_inst.logger.info(f"ALLOWED_AUTHENTICATION_SECRETS : {obj_inst.attr.allowed_authentication_secrets}")

            if tags.ENABLED in kwargs.keys():
                obj_inst.set_enabled(kwargs[tags.ENABLED])
            else:
                obj_inst.set_enabled('NONE')
            obj_inst.logger.info(f"ENABLED : {obj_inst.attr.enabled}")

            if tags.COMMENT in kwargs.keys():
                obj_inst.set_comment(kwargs[tags.COMMENT])
            else:
                obj_inst.set_comment('NONE')
            obj_inst.logger.info(f"COMMENT : {obj_inst.base_attrs.comment}")

 
        logger.info('prepare query')
        obj_inst.prepare_query()
        obj_inst.print_query()
        
        logger.info('execute query')
        if obj_inst.attr.api_type != 'GIT':
            obj_inst.execute_final_query()
        else:
            obj_inst.execute_final_query(**{"DATABASE":obj_inst.base_attrs.database, "SCHEMA":obj_inst.base_attrs.schema})

        '''
        obj_inst.create_deployment_entry(object_name=obj_inst.attr.name[0],
                                         object_type=obj_inst.__class__.__name__,
                                         object_database=obj_inst.attr.database,
                                         object_schema=obj_inst.attr.schema)
        '''
        
        obj_inst.write_file_to_git(object_name=obj_inst.attr.name[0],
                                         object_type=obj_inst.__class__.__name__,
                                         object_database='NA',
                                         object_schema='NA')
        
        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                        object_identifier=obj_inst.attr.name[0],
                                        qry=obj_inst.qry)


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
