
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from .baseobj import BaseObject 
from vars.obj.securityintegration.gvsecurityintegration import SecurityIntegrationTag as tags


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

class Type:
    def __get__(self,instance,owner):
        return instance._type
    
    def __set__(self,instance,value):
        instance._type = "API_AUTHENTICATION"
    
    def __delete__(self,instance):
        del instance._type


class AuthType:
    def __get__(self,instance,owner):
        return instance._auth_type
    
    def __set__(self,instance,value):
        instance._auth_type="OAUTH2"    

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


class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        obj_inst=SecurityIntegration(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        logger.info("set type")
        if tags.TYPE in kwargs.keys():
            obj_inst.set_type(kwargs[tags.TYPE])
        else:
            obj_inst.set_type('NONE')

        logger.info("set auth_type")
        if tags.AUTH_TYPE in kwargs.keys():
            obj_inst.set_auth_type(kwargs[tags.AUTH_TYPE])
        else:
            obj_inst.set_auth_type('NONE')

        logger.info("set enabled")
        if tags.ENABLED in kwargs.keys():
            obj_inst.set_enabled(kwargs[tags.ENABLED])
        else:
            obj_inst.set_enabled('NONE')

        logger.info("set oauth_token_endpoint")
        if tags.OAUTH_TOKEN_ENDPOINT in kwargs.keys():
            obj_inst.set_oauth_token_endpoint(kwargs[tags.OAUTH_TOKEN_ENDPOINT])
        else:
            obj_inst.set_oauth_token_endpoint('NONE')

        logger.info("set oauth_client_auth_method")
        if tags.OAUTH_CLIENT_AUTH_METHOD in kwargs.keys():
            obj_inst.set_oauth_client_auth_method(kwargs[tags.OAUTH_CLIENT_AUTH_METHOD])
        else:
            obj_inst.set_oauth_client_auth_method('NONE')

        logger.info("set oauth_client_id")
        if tags.OAUTH_CLIENT_ID in kwargs.keys():
            obj_inst.set_oauth_client_id(kwargs[tags.OAUTH_CLIENT_ID])
        else:
            obj_inst.set_oauth_client_id('NONE')

        logger.info("set oauth_client_secret")
        if tags.OAUTH_CLIENT_SECRET in kwargs.keys():
            obj_inst.set_oauth_client_secret(kwargs[tags.OAUTH_CLIENT_SECRET])
        else:
            obj_inst.set_oauth_client_secret('NONE')

        logger.info("set oauth_grant")
        if tags.OAUTH_GRANT in kwargs.keys():
            obj_inst.set_oauth_grant(kwargs[tags.OAUTH_GRANT])
        else:
            obj_inst.set_oauth_grant('NONE')

        logger.info("set oauth_access_token_validity")
        if tags.OAUTH_ACCESS_TOKEN_VALIDITY in kwargs.keys():
            obj_inst.set_oauth_access_token_validity(kwargs[tags.OAUTH_ACCESS_TOKEN_VALIDITY])
        else:
            obj_inst.set_oauth_access_token_validity('NONE')

        logger.info("set oauth_allowed_scopes")
        if tags.OAUTH_ALLOWED_SCOPES in kwargs.keys():
            obj_inst.set_oauth_allowed_scopes(kwargs[tags.OAUTH_ALLOWED_SCOPES])
        else:
            obj_inst.set_oauth_allowed_scopes('NONE')

        logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')

        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
