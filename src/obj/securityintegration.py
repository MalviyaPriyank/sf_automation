
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from .baseobj import BaseObject 
from vars.obj.externalaccessintegration.gvexternalaccessintegration import ExternalAccessIntegration as tags


class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if not vv.starts_with_alphabet(value):
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

class Type:
    def __get__(self,instance,owner):
        return instance._type
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vo.object_exist(session=instance.parent.session,
                        object_type=instance.parent.__class__.__name__,
                        object_name=value)
        instance._type = value
    
    def __delete__(self,instance):
        del instance._type


class AuthType:
    def __get__(self,instance,owner):
        return instance._auth_type
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vv.is_bool(value=value,
                   object_type=instance.parent.__class__.__name__,
                   attr_name=self.__class__.__name__)
        instance._auth_type=value    

    def __delete__(self,instance):
        del instance._auth_type

class Enabled:
    def __get__(self,instance,owner):
        return instance._enabled
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._enabled="NONE"
        else:
            vo.object_exist(session=instance.parent.session,
                            object_type="SECURITY INTEGRATION",
                            object_name=value
                            )
            instance._enabled=value
            
    def __delete__(self,instance):
        del instance._enabled

class OauthTokenEndpoint:
    def __get__(self,instance,owner):
        return instance._oauth_token_endpoint
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._oauth_token_endpoint="NONE"
        elif value.upper()=="ALL":
            instance._oauth_token_endpoint=value
        else:
            vo.object_exist(session=instance.parent.session,
                            object_type="SECRET",
                            object_name=value)
            instance._oauth_token_endpoint = value
    
    def __delete__(self,instance):
        del instance._oauth_token_endpoint

class OauthClientAuthMethod:
    def __get__(self,instance,owner):
        return instance._oauth_client_auth_method
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._oauth_client_auth_method="NONE"
        elif value.upper()=="ALL":
            instance._oauth_client_auth_method=value
        else:
            vo.object_exist(session=instance.parent.session,
                            object_type="SECRET",
                            object_name=value)
            instance._oauth_client_auth_method = value
    
    def __delete__(self,instance):
        del instance._oauth_client_auth_method

class OauthClientID:
    def __get__(self,instance,owner):
        return instance._oauth_client_id
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._oauth_client_id="NONE"
        elif value.upper()=="ALL":
            instance._oauth_client_id=value
        else:
            vo.object_exist(session=instance.parent.session,
                            object_type="SECRET",
                            object_name=value)
            instance._oauth_client_id = value
    
    def __delete__(self,instance):
        del instance._oauth_client_id

class OauthClientSecret:
    def __get__(self,instance,owner):
        return instance._oauth_client_secret
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._oauth_client_secret="NONE"
        elif value.upper()=="ALL":
            instance._oauth_client_secret=value
        else:
            vo.object_exist(session=instance.parent.session,
                            object_type="SECRET",
                            object_name=value)
            instance._oauth_client_secret = value
    
    def __delete__(self,instance):
        del instance._oauth_client_secret

class OauthGrant:
    def __get__(self,instance,owner):
        return instance._oauth_grant
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._oauth_grant="NONE"
        elif value.upper()=="ALL":
            instance._oauth_grant=value
        else:
            vo.object_exist(session=instance.parent.session,
                            object_type="SECRET",
                            object_name=value)
            instance._oauth_grant = value
    
    def __delete__(self,instance):
        del instance._oauth_grant

class OauthAccessTokenValidity:
    def __get__(self,instance,owner):
        return instance._oauth_access_token_validity
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._oauth_access_token_validity="NONE"
        elif value.upper()=="ALL":
            instance._oauth_access_token_validity=value
        else:
            vo.object_exist(session=instance.parent.session,
                            object_type="SECRET",
                            object_name=value)
            instance._oauth_access_token_validity=value
    
    def __delete__(self,instance):
        del instance._oauth_access_token_validity

class OauthAllowedScopes:
    def __get__(self,instance,owner):
        return instance._oauth_allowed_scopes
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._oauth_allowed_scopes="NONE"
        elif value.upper()=="ALL":
            instance._oauth_allowed_scopes=value
        else:
            vo.object_exist(session=instance.parent.session,
                            object_type="SECRET",
                            object_name=value)
            instance._oauth_allowed_scopes=value
    
    def __delete__(self,instance):
        del instance._oauth_allowed_scopes

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = value
    
    def __delete__(self,instance):
        del instance._comment

class SecurityIntegrationAttrs:
    def __init__(self,parent):
        self.parent=parent
    name=Name()
    type=Type()
    auth_type=AuthType()
    enabled=Enabled()
    oauth_token_endpoint = OauthTokenEndpoint()
    oauth_client_auth_method=OauthClientAuthMethod()
    oauth_client_id=OauthClientID()
    oauth_client_secret=OauthClientSecret()
    oauth_grant=OauthGrant()
    oauth_access_token_validity=OauthAccessTokenValidity()
    oauth_allowed_scopes=OauthAllowedScopes()
    comment=Comment()

class SecurityIntegration(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session, user_id, logger)
        self.attr=SecurityIntegrationAttrs(self)

    def set_name(self,val):
        self.attr.name = val

    def set_type(self,val):
        self.attr.type = val

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

    def set_oauth_grant(self,val):
        self.attr.oauth_grant=val

    def set_oauth_access_token_validity(self,val):
        self.attr.oauth_access_token_validity=val

    def set_oauth_allowed_scopes(self,val):
        self.attr.oauth_allowed_scopes=val

    def set_comment(self,val):
        self.attr.comment = val

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
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
        self.qry = f"CREATE SECURITY INTEGRATION {self.attr.name} {tags.ALLOWED_NETWORK_RULES} = {self.attr.allowed_network_rules} {tags.ENABLED} = {self.attr.enabled} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop==tags.ALLOWED_API_AUTHENTICATION_INTEGRATIONS:
                    self.qry = f" {self.qry} {tags.ALLOWED_API_AUTHENTICATION_INTEGRATIONS} = {self.attr.allowed_api_authentication_integrations} "
                if prop==tags.ALLOWED_AUTHENTICATION_SECRETS:
                    self.qry = f" {self.qry} {tags.ALLOWED_AUTHENTICATION_SECRETS} = {self.attr.allowed_authentication_secrets} "
                if prop==tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "

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
    
    def create_database_role(self):
        self.execute_final_query()

    def create_object(self,**kwargs):
        self.logger.info(f"Operating on {self.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        self.logger.info(f'dictionary passed {kwargs}')
        self.is_create=kwargs[tags.IS_CREATE]


        self.set_name(kwargs[tags.NAME])
        self.set_type(kwargs[tags.TYPE])
        self.set_value_list(kwargs[tags.VALUE_LIST])
        self.set_mode(kwargs[tags.MODE])
        self.set_comment(kwargs[tags.COMMENT])

        self.prepare_query()
        self.create_database_role()

        self.logger.info('create deployment entry')
        self.create_deployment_entry(object_name=self.attr.name[0],object_type=self.__class__.__name__,object_database='NA',object_schema='NA')

        self.logger.info('writing file to git')
        self.write_file_to_git(object_name=self.attr.name[0],object_type=self.__class__.__name__,object_database='NA',object_schema='NA')
