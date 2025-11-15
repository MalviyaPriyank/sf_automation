
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from .baseobj import BaseObject 
from vars.obj.securityintegrationexternalapiauthentication.gvsecurityintegrationexternalapiauthentication  import SecurityIntegrationExternalApiAuthentication as tags
from src.usr.user import ChatHistory

class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)

    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_database(session=instance.parent.session, database_name=name)
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
                vo.database_exist(session=instance.parent.session,database_name=old_name)
                vo.is_new_database(session=instance.parent.session,database_name=new_name)
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
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vv.is_allowed_value(value=value,
                            allowed_list=tags.allowed_value_list().get(tags.API_TYPE),
                            object_type=instance.parent.__class__.__name__,
                            attr_name=self.__class__.__name__)
        instance._api_type = value
    
    def __delete__(self,instance):
        del instance._api_type

class Type:
    def __get__(self,instance,owner):
        return instance._type
    
    def __set__(self,instance,value):
        instance._type = value
    
    def __delete__(self,instance):
        del instance._type

class IntegrationType:
    def __get__(self,instance,owner):
        return instance._integration_type
    
    def __set__(self,instance,value):
        instance._integration_type = "API_AUTHENTICATION"
    
    def __delete__(self,instance):
        del instance._integration_type


class AuthType:
    def __get__(self,instance,owner):
        return instance._auth_type
    
    def __set__(self,instance,value):
        instance._auth_type=value   

    def __delete__(self,instance):
        del instance._auth_type

class Enabled:
    def __get__(self,instance,owner):
        return instance._enabled
    
    def __set__(self,instance,value):
            vv.required_attribute_check(value=value,
                                        object_type=instance.parent.__class__.__name__,
                                        attr_name=self.__class__.__name__
                                        )
            vv.is_bool(value=value,
                       object_type=instance.parent.__class__.__name__,
                       attr_name=self.__class__.__name__
                       )
            instance._enabled=value
            
    def __delete__(self,instance):
        del instance._enabled



class OauthTokenEndpoint:
    def __get__(self,instance,owner):
        return instance._oauth_token_endpoint
    
    def __set__(self,instance,value):
        instance._oauth_token_endpoint=f"'{value}'"
            
    def __delete__(self,instance):
        del instance._oauth_token_endpoint

class OauthClientAuthMethod:
    def __get__(self,instance,owner):
        return instance._oauth_client_auth_method
    
    def __set__(self,instance,value):
        vv.is_allowed_value(value=value,
                            allowed_list=tags.allowed_value_list().get(tags.OAUTH_CLIENT_AUTH_METHOD),
                            object_type=instance.parent.__class__.__name__,
                            attr_name=self.__class__.__name__)
        instance._oauth_client_auth_method=f"'{value}'"
            
    def __delete__(self,instance):
        del instance._oauth_client_auth_method

class OauthClientID:
    def __get__(self,instance,owner):
        return instance._oauth_client_id
    
    def __set__(self,instance,value):
        instance._oauth_client_id=f"'{value}'"
            
    def __delete__(self,instance):
        del instance._oauth_client_id

class OauthClientSecret:
    def __get__(self,instance,owner):
        return instance._oauth_client_secret
    
    def __set__(self,instance,value):
        instance._oauth_client_secret=f"'{value}'"
            
    def __delete__(self,instance):
        del instance._oauth_client_secret

class OauthGrant:
    def __get__(self,instance,owner):
        return instance._oauth_grant
    
    def __set__(self,instance,value):
        instance._oauth_grant=f"'{value}'"
            
    def __delete__(self,instance):
        del instance._oauth_grant

class OauthAccessTokenValidity:
    def __get__(self,instance,owner):
        return instance._oauth_access_token_validity
    
    def __set__(self,instance,value):
        vv.is_positive_number(value=value,
                              object_type=instance.parent.__class__.__name__,
                              attr_name=self.__class__.__name__)
        instance._oauth_access_token_validity=value
            
    def __delete__(self,instance):
        del instance._oauth_access_token_validity

class OauthAllowedScopes:
    def __get__(self,instance,owner):
        return instance._oauth_allowed_scopes
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._oauth_allowed_scopes="NONE"
        else:
            if instance._api_type=="CLIENT_CREDENTIALS":
                if isinstance(value,list):
                    instance.parent.logger.info(f" value is a list: {value}")
                    val_string=""
                    for i in range(0,len(value)):
                        instance.parent.logger.info(f"adding {value[i]}")
                        if i != len(value)-1:
                            val_string=val_string+f"'{value[i]}',"
                        elif i == len(value)-1:
                            val_string=val_string+f"'{value[i]}'"
                    instance.parent.logger.info(f" final value string : {val_string}")
                    instance._oauth_allowed_scopes=f"({val_string})"
                if isinstance(value,str):
                    instance._oauth_allowed_scopes=f"('{value}')"
            else:
                vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} can only be used for CLIENT_CREDENTIALS api type.")
            
    def __delete__(self,instance):
        del instance._oauth_allowed_scopes   

class OauthAuthorizationEndpoint: 
    def __get__(self,instance,owner):
        return instance._oauth_authorization_endpoint
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._oauth_authorization_endpoint="NONE"
        else:
            if instance._api_type=="CLIENT_CREDENTIALS":
                vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} is not supported parameter for CLIENT_CREDENTIALS api type.")
            else:
                instance._oauth_authorization_endpoint=f"'{value}'"
            
    def __delete__(self,instance):
        del instance._oauth_authorization_endpoint

class OauthRefreshTokenValidity:
    def __get__(self,instance,owner):
        return instance._oauth_refresh_token_validity
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._oauth_refresh_token_validity="NONE"
        else:
            if instance._api_type=="CLIENT_CREDENTIALS":
                vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} is not supported parameter for CLIENT_CREDENTIALS api type.")
            else:
                vv.is_positive_number(value=value,
                                      object_type=instance.parent.__class__.__name__,
                                      attr_name=self.__class__.__name__)
                instance._oauth_refresh_token_validity=value
            
    def __delete__(self,instance):
        del instance._oauth_refresh_token_validity

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._comment="NONE"
        else:
            instance._comment=f"'{value}'"
            
    def __delete__(self,instance):
        del instance._comment

class SecurityIntegrationAWSAttrs:
    def __init__(self,parent):
        self.parent=parent
    name=Name()
    type=Type()
    api_type=APIType()
    auth_type=AuthType()
    enabled=Enabled()
    oauth_token_endpoint=OauthTokenEndpoint()
    oauth_client_auth_method=OauthClientAuthMethod()
    oauth_client_id=OauthClientID()
    oauth_client_secret=OauthClientSecret()
    oauth_grant=OauthGrant()
    oauth_access_token_validity=OauthAccessTokenValidity()
    oauth_allowed_scopes=OauthAllowedScopes()
    oauth_authorization_endpoint=OauthAuthorizationEndpoint()
    oauth_refresh_token_validity=OauthRefreshTokenValidity()
    comment=Comment()

class SecurityIntegrationAWS(BaseObject):
    def __init__(self, session, user_id, logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger)
        self.attr=SecurityIntegrationAWSAttrs(self)

    def set_name(self,val):
        self.attr.name = val

    def set_api_type(self,val):
        self.attr.api_type=val

    def set_type(self,val):
        self.attr.type = val
    
    def set_oauth_grant(self,val):
        self.attr.oauth_grant=val

    def set_auth_type(self,val):
        self.attr.auth_type = val

    def set_enabled(self,val):
        self.attr.enabled = val

    def set_oauth_token_endpoint(self,val):
        self.attr.oauth_token_endpoint=val
    
    def set_oauth_client_auth_method(self,val):
        self.attr.oauth_client_auth_method=val

    def set_oauth_client_id(self,val):
        self.attr.oauth_client_id=val

    def set_oauth_client_secret(self,val):
        self.attr.oauth_client_secret=val

    def set_oauth_access_token_validity(self,val):
        self.attr.oauth_access_token_validity=val
    
    def set_oauth_allowed_scopes(self,val):
        self.attr.oauth_allowed_scopes=val

    def set_oauth_authorization_endpoint(self,val):
        self.attr.oauth_authorization_endpoint=val

    def set_oauth_refresh_token_validity(self,val):
        self.attr.oauth_refresh_token_validity=val

    def set_comment(self, val):
        super().set_comment(val)

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            if attribute_tag == tags.OAUTH_TOKEN_ENDPOINT:
                self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
            if attribute_tag == tags.OAUTH_CLIENT_AUTH_METHOD:
                self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
            if attribute_tag == tags.OAUTH_CLIENT_ID:
                self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
            if attribute_tag == tags.OAUTH_CLIENT_SECRET:
                self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
            if attribute_tag == tags.OAUTH_ACCESS_TOKEN_VALIDITY:
                self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
            if attribute_tag == tags.OAUTH_ALLOWED_SCOPES:
                self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
            if attribute_tag == tags.OAUTH_AUTHORIZATION_ENDPOINT:
                self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
            if attribute_tag == tags.OAUTH_REFRESH_TOKEN_VALIDITY:
                self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
            if attribute_tag == tags.COMMENT:
                self.flag_dic[attribute_tag] = 1 if getattr(self.base_attrs, attribute_name) != "NONE" else 0
        set_flag(tags.OAUTH_TOKEN_ENDPOINT,"_oauth_token_endpoint")
        set_flag(tags.OAUTH_CLIENT_AUTH_METHOD,"_oauth_client_auth_method")
        set_flag(tags.OAUTH_CLIENT_ID,"_oauth_client_id")
        set_flag(tags.OAUTH_CLIENT_SECRET,"_oauth_client_secret")
        set_flag(tags.OAUTH_ACCESS_TOKEN_VALIDITY,"_oauth_access_token_validity")
        set_flag(tags.OAUTH_ALLOWED_SCOPES,"_oauth_allowed_scopes")
        set_flag(tags.OAUTH_AUTHORIZATION_ENDPOINT,"_oauth_authorization_endpoint")
        set_flag(tags.OAUTH_REFRESH_TOKEN_VALIDITY,"_oauth_refresh_token_validity")     
        set_flag(tags.COMMENT,"_comment")


    def alter_object(self):        
        for prop in self.property_lst:
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming {self.__class__.__name__} {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_security_integration_qry(self):
        self.qry = f"""
        CREATE SECURITY INTEGRATION {self.attr.name[0]} 
        {tags.TYPE} = {self.attr.type} 
        {tags.AUTH_TYPE} = {self.attr.auth_type} 
        {tags.ENABLED} = {self.attr.enabled}
        """

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop==tags.OAUTH_TOKEN_ENDPOINT:
                    self.qry= f" {self.qry} {tags.OAUTH_TOKEN_ENDPOINT} = {self.attr.oauth_token_endpoint}"
                if prop==tags.OAUTH_CLIENT_AUTH_METHOD:
                    self.qry= f" {self.qry} {tags.OAUTH_CLIENT_AUTH_METHOD} = {self.attr.oauth_client_auth_method}"
                if prop==tags.OAUTH_CLIENT_ID:
                    self.qry= f" {self.qry} {tags.OAUTH_CLIENT_ID} = {self.attr.oauth_client_id}"
                if prop==tags.OAUTH_CLIENT_SECRET:
                    self.qry= f" {self.qry} {tags.OAUTH_CLIENT_SECRET} = {self.attr.oauth_client_secret}"
                if prop==tags.OAUTH_ACCESS_TOKEN_VALIDITY:
                    self.qry= f" {self.qry} {tags.OAUTH_ACCESS_TOKEN_VALIDITY} = {self.attr.oauth_access_token_validity}"
                if prop==tags.OAUTH_ALLOWED_SCOPES:
                    self.qry= f" {self.qry} {tags.OAUTH_ALLOWED_SCOPES} = {self.attr.oauth_allowed_scopes}"
                if prop==tags.OAUTH_AUTHORIZATION_ENDPOINT:
                    self.qry= f" {self.qry} {tags.OAUTH_AUTHORIZATION_ENDPOINT} = {self.attr.oauth_authorization_endpoint}"
                if prop==tags.OAUTH_REFRESH_TOKEN_VALIDITY:
                    self.qry= f" {self.qry} {tags.OAUTH_REFRESH_TOKEN_VALIDITY} = {self.attr.oauth_refresh_token_validity}"
                if prop==tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.base_attrs.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == 'TRUE':
            self.set_create_security_integration_qry()
            self.add_properties_to_query()
        elif self.is_create=='FALSE':
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=SecurityIntegrationAWS(session=session,
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

        obj_inst.logger.info("set type")
        obj_inst.set_type("API_AUTHENTICATION")



        obj_inst.logger.info("set auth_type")
        obj_inst.set_auth_type("OAUTH2")

        obj_inst.logger.info("set api_type and oauth grant")
        if tags.API_TYPE in kwargs.keys():                
            obj_inst.set_api_type(kwargs[tags.API_TYPE])
            obj_inst.set_oauth_grant(kwargs[tags.API_TYPE])
        else:
            obj_inst.set_api_type('NONE')

        obj_inst.logger.info("set enabled")
        if tags.ENABLED in kwargs.keys():
            obj_inst.set_enabled(kwargs[tags.ENABLED])
        else:
            obj_inst.set_enabled('NONE')


        obj_inst.logger.info("set OAUTH_TOKEN_ENDPOINT")
        if tags.OAUTH_TOKEN_ENDPOINT in kwargs.keys():
            obj_inst.set_oauth_token_endpoint(kwargs[tags.OAUTH_TOKEN_ENDPOINT])
        else:
            obj_inst.set_oauth_token_endpoint('NONE')

        obj_inst.logger.info("set OAUTH_CLIENT_AUTH_METHOD")
        if tags.OAUTH_CLIENT_AUTH_METHOD in kwargs.keys():
            obj_inst.set_oauth_client_auth_method(kwargs[tags.OAUTH_CLIENT_AUTH_METHOD])
        else:
            obj_inst.set_oauth_client_auth_method('NONE')

        obj_inst.logger.info("set OAUTH_CLIENT_ID")
        if tags.OAUTH_CLIENT_ID in kwargs.keys():
            obj_inst.set_oauth_client_id(kwargs[tags.OAUTH_CLIENT_ID])
        else:
            obj_inst.set_oauth_client_id('NONE')

        obj_inst.logger.info("set OAUTH_CLIENT_SECRET")
        if tags.OAUTH_CLIENT_SECRET in kwargs.keys():
            obj_inst.set_oauth_client_secret(kwargs[tags.OAUTH_CLIENT_SECRET])
        else:
            obj_inst.set_oauth_client_secret('NONE')

        obj_inst.logger.info("set OAUTH_ACCESS_TOKEN_VALIDITY")
        if tags.OAUTH_ACCESS_TOKEN_VALIDITY in kwargs.keys():
            obj_inst.set_oauth_access_token_validity(kwargs[tags.OAUTH_ACCESS_TOKEN_VALIDITY])
        else:
            obj_inst.set_oauth_access_token_validity('NONE')

        obj_inst.logger.info("set OAUTH_ALLOWED_SCOPES")
        if tags.OAUTH_ALLOWED_SCOPES in kwargs.keys():
            obj_inst.set_oauth_allowed_scopes(kwargs[tags.OAUTH_ALLOWED_SCOPES])
        else:
            obj_inst.set_oauth_allowed_scopes('NONE')

        obj_inst.logger.info("set OAUTH_AUTHORIZATION_ENDPOINT")
        if tags.OAUTH_AUTHORIZATION_ENDPOINT in kwargs.keys():
            obj_inst.set_oauth_authorization_endpoint(kwargs[tags.OAUTH_AUTHORIZATION_ENDPOINT])
        else:
            obj_inst.set_oauth_authorization_endpoint('NONE')

        obj_inst.logger.info("set OAUTH_REFRESH_TOKEN_VALIDITY")
        if tags.OAUTH_REFRESH_TOKEN_VALIDITY in kwargs.keys():
            obj_inst.set_oauth_refresh_token_validity(kwargs[tags.OAUTH_REFRESH_TOKEN_VALIDITY])
        else:
            obj_inst.set_oauth_refresh_token_validity('NONE')

        obj_inst.logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')

        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        
        obj_inst.logger.info('execute query')
        obj_inst.execute_final_query()

        obj_inst.logger.info('write file to git')
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
