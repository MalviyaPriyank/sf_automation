import sys
import os

# Add paths for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../validation'))

from vars.gvobject import ApiIntegration as gv
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from .baseobj import BaseObject
from vars.obj.secret.gvsecret import SecretTag as tags

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

class SecretOption:
    def __get__(self, instance, owner):
        return instance._secret_option

    def __set__(self, instance, value):
        vv.required_attribute_check(value, instance.parent.__class__.__name__, self.__class__.__name__)
        vv.is_allowed_value(value=value,
                            allowed_list=tags.allowed_value_list().get(tags.SECRET_OPTION),
                            object_type=instance.object_type,
                            attr_name=self.__class__.__name__)
        instance._secret_option = value

    def __delete__(self, instance):
        del instance._secret_option


class Type:
    def __get__(self, instance, owner):
        return instance._type

    def __set__(self, instance, value):
        if instance._secret_option in ["OAUTH_WITH_CLIENT_CREDENTIALS","OAUTH_WITH_AUTH_CODE_GRANT_FLOW"]:
            instance._type="OAUTH2"
        elif instance._secret_option=="CLOUD_PROVIDER":
            instance._type="CLOUD_PROVIDER_TOKEN"
        elif instance._secret_option=="BASIC_AUTHENTICATION":
            instance._type="PASSWORD"
        elif instance._secret_option=="GENERIC_STRING":
            instance._type="GENERIC_STRING"
        elif instance._secret_option=="SYMMETRIC_KEY":
            instance._type="SYMMETRIC_KEY"

    def __delete__(self, instance):
        del instance._type


class ApiAuthentication:
    def __get__(self, instance, owner):
        return instance._api_authentication

    def __set__(self, instance, value):
        if instance._secret_option in ["OAUTH_WITH_CLIENT_CREDENTIALS","OAUTH_WITH_AUTH_CODE_GRANT_FLOW","CLOUD_PROVIDER"]:
            vv.required_attribute_check(value=value,
                                        object_type=instance.object_type,
                                        attr_name=self.__class__.__name__)
            instance._api_authentication=value
        else:
            instance._api_authentication="NONE"

    def __delete__(self, instance):
        del instance._api_authentication


class OauthScopes:
    def __get__(self, instance, owner):
        return instance._oauth_scopes

    def __set__(self, instance, value):
        if instance._secret_option=="OAUTH_WITH_CLIENT_CREDENTIALS":
            vv.required_attribute_check(value=value,
                                        object_type=instance.object_type,
                                        attr_name=self.__class__.__name__)
            instance._oauth_scopes=value
        else:
            instance._oauth_scopes="NONE"

    def __delete__(self, instance):
        del instance._oauth_scopes


class OauthRefreshToken:
    def __get__(self, instance, owner):
        return instance._oauth_refresh_token

    def __set__(self, instance, value):
        if value=="NONE":
            instance._oauth_refresh_token="NONE"
        else:
            instance._oauth_refresh_token=value

    def __delete__(self, instance):
        del instance._oauth_refresh_token


class OauthRefreshTokenExpiryTime:
    def __get__(self, instance, owner):
        return instance._oauth_refresh_token_expiry_time

    def __set__(self, instance, value):
        if value=="NONE":
            instance._oauth_refresh_token_expiry_time="NONE"
        else:
            instance._oauth_refresh_token_expiry_time = value

    def __delete__(self, instance):
        del instance._oauth_refresh_token_expiry_time


class Enabled:
    def __get__(self, instance, owner):
        return instance._enabled

    def __set__(self, instance, value):
        if instance._secret_option=="CLOUD_PROVIDER":
            vv.is_bool(value=value,
                       object_type=instance.object_type,
                       attr_name=self.__class__.__name__)
            instance._enabled = value
        else:
            instance._enabled="NONE"

    def __delete__(self, instance):
        del instance._enabled


class Username:
    def __get__(self, instance, owner):
        return instance._username

    def __set__(self, instance, value):
        if instance._secret_option=="BASIC_AUTHENTICATION":
            instance._username=value
        else:
            instance._username="NONE"

    def __delete__(self, instance):
        del instance._username


class Password:
    def __get__(self, instance, owner):
        return instance._password

    def __set__(self, instance, value):
        if instance._secret_option=="BASIC_AUTHENTICATION":
            instance._password=value
        else:
            instance._password="NONE"

    def __delete__(self, instance):
        del instance._password


class SecretString:
    def __get__(self, instance, owner):
        return instance._secret_string

    def __set__(self, instance, value):
        if instance._secret_option=="GENERIC_STRING":
            instance._secret_string=value
        else:
            instance._secret_string="NONE"

    def __delete__(self, instance):
        del instance._secret_string


class Algorithm:
    def __get__(self, instance, owner):
        return instance._algorithm

    def __set__(self, instance, value):
        if instance._secret_option=="SYMMETRIC_KEY":
            instance._algorithm = "GENERIC"
        else:
            instance._algorithm="NONE"

    def __delete__(self, instance):
        del instance._algorithm


class SecretAttrs:
    def __init__(self, parent):
        self.parent = parent
        self.object_type=parent.__class__.__name__
    name=Name()
    secret_option=SecretOption()
    type = Type()
    api_authentication = ApiAuthentication()
    oauth_scopes = OauthScopes()
    oauth_refresh_token = OauthRefreshToken()
    oauth_refresh_token_expiry_time = OauthRefreshTokenExpiryTime()
    enabled = Enabled()
    username = Username()
    password = Password()
    secret_string = SecretString()
    algorithm = Algorithm()




class Secret(BaseObject):
    def __init__(self, session, user_id):
        super().__init__(session, user_id)
        self.attr = SecretAttrs(self)
    
    def set_name(self,val):
        self.attr.name=val
    def set_type(self, val):
        self.attr.type = val

    def set_secret_option(self,val):
        self.attr.secret_option=val

    def set_api_authentication(self, val):
        self.attr.api_authentication = val

    def set_oauth_scopes(self, val):
        self.attr.oauth_scopes = val

    def set_oauth_refresh_token(self, val):
        self.attr.oauth_refresh_token = val

    def set_oauth_refresh_token_expiry_time(self, val):
        self.attr.oauth_refresh_token_expiry_time = val

    def set_enabled(self, val):
        self.attr.enabled = val

    def set_username(self, val):
        self.attr.username = val

    def set_password(self, val):
        self.attr.password = val

    def set_secret_string(self, val):
        self.attr.secret_string = val

    def set_algorithm(self, val):
        self.attr.algorithm = val

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag, attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
        set_flag(tags.COMMENT, "_algorithm")

    def check_properties_to_set(self):
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def alter_object(self):
        for prop in self.property_lst:
            if prop == tags.TYPE:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.type} SET {tags.TYPE} = {self.attr.type}"
                self.execute_final_query()
            
            if prop == tags.API_AUTHENTICATION:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.type} SET {tags.API_AUTHENTICATION} = {self.attr.api_authentication}"
                self.execute_final_query()

            if prop == tags.OAUTH_SCOPES:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.type} SET {tags.OAUTH_SCOPES} = {self.attr.oauth_scopes}"
                self.execute_final_query()

            if prop == tags.OAUTH_REFRESH_TOKEN:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.type} SET {tags.OAUTH_REFRESH_TOKEN} = {self.attr.oauth_refresh_token}"
                self.execute_final_query()

            if prop == tags.OAUTH_REFRESH_TOKEN_EXPIRY_TIME:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.type} SET {tags.OAUTH_REFRESH_TOKEN_EXPIRY_TIME} = {self.attr.oauth_refresh_token_expiry_time}"
                self.execute_final_query()

            if prop == tags.ENABLED:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.type} SET {tags.ENABLED} = {self.attr.enabled}"
                self.execute_final_query()

            if prop == tags.USERNAME:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.type} SET {tags.USERNAME} = {self.attr.username}"
                self.execute_final_query()

            if prop == tags.PASSWORD:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.type} SET {tags.PASSWORD} = {self.attr.password}"
                self.execute_final_query()

            if prop == tags.SECRET_STRING:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.type} SET {tags.SECRET_STRING} = {self.attr.secret_string}"
                self.execute_final_query()

            if prop == tags.ALGORITHM:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.type} SET {tags.ALGORITHM} = {self.attr.algorithm}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming database {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()


    def set_create_account_qry(self):
        if self.attr.secret_option=="OAUTH_WITH_CLIENT_CREDENTIALS":
            self.qry = f"""CREATE SECRET {self.attr.name} 
                        {tags.TYPE} = {self.attr.type} 
                        {tags.API_AUTHENTICATION} = {self.attr.api_authentication} 
                        {tags.OAUTH_SCOPES} = {self.attr.oauth_scopes}"""
        elif self.attr.secret_option=="OAUTH_WITH_AUTH_CODE_GRANT_FLOW":
            self.qry = f"""CREATE SECRET {self.attr.name} 
                        {tags.TYPE} = {self.attr.type} 
                        {tags.OAUTH_REFRESH_TOKEN} = {self.attr.oauth_refresh_token} 
                        {tags.OAUTH_REFRESH_TOKEN_EXPIRY_TIME} = {self.attr.oauth_refresh_token_expiry_time} 
                        {tags.API_AUTHENTICATION} = {self.attr.api_authentication}"""
        elif self.attr.secret_option=="CLOUD_PROVIDER":
            self.qry = f"""CREATE SECRET {self.attr.name} 
                        {tags.TYPE} = {self.attr.type} 
                        {tags.OAUTH_REFRESH_TOKEN} = {self.attr.oauth_refresh_token} 
                        {tags.OAUTH_REFRESH_TOKEN_EXPIRY_TIME} = {self.attr.oauth_refresh_token_expiry_time} 
                        {tags.API_AUTHENTICATION} = {self.attr.api_authentication}
                        {tags.ENABLED} = {self.attr.enabled}"""
        elif self.attr.secret_option=="BASIC_AUTHENTICATION":
            self.qry = f"""CREATE SECRET {self.attr.name} 
                        {tags.TYPE} = {self.attr.type} 
                        {tags.USERNAME} = {self.attr.username} 
                        {tags.PASSWORD} = {self.attr.password}"""
        elif self.attr.secret_option=="GENERIC_STRING":
            self.qry = f"""CREATE SECRET {self.attr.name} 
                        {tags.TYPE} = {self.attr.type} 
                        {tags.SECRET_STRING} = {self.attr.secret_string}"""
        elif self.attr.secret_option=="SYMMETRIC_KEY":
            self.qry = f"""CREATE SECRET {self.attr.name} 
                        {tags.TYPE} = {self.attr.type} 
                        {tags.ALGORITHM} = {self.attr.algorithm}"""

    def add_properties_to_query(self):
        if len(self.property_lst) != 0:
            for prop in self.property_lst:
                self.qry = f"{self.qry} {prop} = {getattr(self.attr, prop.lower())}"

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == 'TRUE':
            self.set_create_account_qry()
            self.add_properties_to_query()
        elif self.is_create=='FALSE':
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()


    def create_api_integration(self):
        self.session.sql(self.qry)

    def create_object(self, **kwargs):
        self.logger.info(f"Operating on {self.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        self.logger.info(f'dictionary passed {kwargs}')
        self.is_create=kwargs[tags.IS_CREATE]

        self.set_name(kwargs[tags.NAME])
        self.set_type(kwargs[tags.TYPE])
        self.set_api_authentication(kwargs[tags.API_AUTHENTICATION])
        self.set_oauth_scopes(kwargs[tags.OAUTH_SCOPES])
        self.set_oauth_refresh_token(kwargs[tags.OAUTH_REFRESH_TOKEN])
        self.set_oauth_refresh_token_expiry_time(kwargs[tags.OAUTH_REFRESH_TOKEN_EXPIRY_TIME])
        self.set_enabled(kwargs[tags.ENABLED])
        self.set_username(kwargs[tags.USERNAME])
        self.set_password(kwargs[tags.PASSWORD])
        self.set_secret_string(kwargs[tags.SECRET_STRING])
        self.set_algorithm(kwargs[tags.ALGORITHM])

        self.prepare_query()
        self.create_api_integration()


class Operation:
    @staticmethod
    def create_object(session,user_id,kwargs,*largs):
        obj_inst=Secret(session=session,
                         user_id=user_id
                        )
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        obj_inst.logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        obj_inst.logger.info("set secret_option")
        if tags.SECRET_OPTION in kwargs.keys():
            obj_inst.set_secret_option(kwargs[tags.SECRET_OPTION])
        else:
            obj_inst.set_secret_option('NONE')

        obj_inst.logger.info("set type")
        if tags.TYPE in kwargs.keys():
            obj_inst.set_type(kwargs[tags.TYPE])
        else:
            obj_inst.set_type('NONE')

        obj_inst.logger.info("set api_authentication")
        if tags.API_AUTHENTICATION in kwargs.keys():
            obj_inst.set_api_authentication(kwargs[tags.API_AUTHENTICATION])
        else:
            obj_inst.set_api_authentication('NONE')

        obj_inst.logger.info("set oauth_scopes")
        if tags.OAUTH_SCOPES in kwargs.keys():
            obj_inst.set_oauth_scopes(kwargs[tags.OAUTH_SCOPES])
        else:
            obj_inst.set_oauth_scopes('NONE')

        obj_inst.logger.info("set oauth_refresh_token")
        if tags.OAUTH_REFRESH_TOKEN in kwargs.keys():
            obj_inst.set_oauth_refresh_token(kwargs[tags.OAUTH_REFRESH_TOKEN])
        else:
            obj_inst.set_oauth_refresh_token('NONE')

        obj_inst.logger.info("set oauth_refresh_token_expiry_time")
        if tags.OAUTH_REFRESH_TOKEN_EXPIRY_TIME in kwargs.keys():
            obj_inst.set_oauth_refresh_token_expiry_time(kwargs[tags.OAUTH_REFRESH_TOKEN_EXPIRY_TIME])
        else:
            obj_inst.set_oauth_refresh_token_expiry_time('NONE')

        obj_inst.logger.info("set enabled")
        if tags.ENABLED in kwargs.keys():
            obj_inst.set_enabled(kwargs[tags.ENABLED])
        else:
            obj_inst.set_enabled('NONE')

        obj_inst.logger.info("set username")
        if tags.USERNAME in kwargs.keys():
            obj_inst.set_username(kwargs[tags.USERNAME])
        else:
            obj_inst.set_username('NONE')

        obj_inst.logger.info("set password")
        if tags.PASSWORD in kwargs.keys():
            obj_inst.set_password(kwargs[tags.PASSWORD])
        else:
            obj_inst.set_password('NONE')

        obj_inst.logger.info("set secret_string")
        if tags.SECRET_STRING in kwargs.keys():
            obj_inst.set_secret_string(kwargs[tags.SECRET_STRING])
        else:
            obj_inst.set_secret_string('NONE')

        obj_inst.logger.info("set algorithm")
        if tags.ALGORITHM in kwargs.keys():
            obj_inst.set_algorithm(kwargs[tags.ALGORITHM])
        else:
            obj_inst.set_algorithm('NONE')

        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        
        obj_inst.logger.info('execute query')
        obj_inst.execute_final_query()

        obj_inst.logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
