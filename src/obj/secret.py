
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from .baseobj import BaseObject 
from vars.obj.networkrule.gvnetworkrule import NetworkRuleTag as tags

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
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vv.is_allowed_value(value=value,
                            allowed_list=tags.allowed_value_list().get(f"{tags.TYPE}"),
                            object_type=instance.parent.__class__.__name__,
                            attr_name=self.__class__.__name__)
        instance._type = value
    
    def __delete__(self,instance):
        del instance._type


class OauthRefreshToken:
    def __get__(self,instance,owner):
        return instance._oauth_refresh_token
    
    def __set__(self,instance,value):
            instance._oauth_refresh_token=value
    
    def __delete__(self,instance):
        del instance._oauth_refresh_token

class OauthRefreshTokenExpiryTime:
    def __get__(self,instance,owner):
        return instance._oauth_refresh_token_expiry_time
    
    def __set__(self,instance,value):
            instance._oauth_refresh_token_expiry_time=value
    
    def __delete__(self,instance):
        del instance._oauth_refresh_token_expiry_time

class APIAuthentication:
    def __get__(self,instance,owner):
        return instance._api_authentication
    
    def __set__(self,instance,value):
        instance._api_authentication = value
    
    def __delete__(self,instance):
        del instance._api_authentication

class OauthScopes:
    def __get__(self,instance,owner):
        return instance._oauth_scopes
    
    def __set__(self,instance,value):
        instance._oauth_scopes = value
    
    def __delete__(self,instance):
        del instance._oauth_scopes

class UserName:
    def __get__(self,instance,owner):
        return instance._user_name
    
    def __set__(self,instance,value):
        instance._user_name = value
    
    def __delete__(self,instance):
        del instance._user_name

class Password:
    def __get__(self,instance,owner):
        return instance._password
    
    def __set__(self,instance,value):
        instance._password = value
    
    def __delete__(self,instance):
        del instance._password

class SecretString:
    def __get__(self,instance,owner):
        return instance._secret_string
    
    def __set__(self,instance,value):
        instance._secret_string = value
    
    def __delete__(self,instance):
        del instance._secret_string

class Algorithm:
    def __get__(self,instance,owner):
        return instance._algorithm
    
    def __set__(self,instance,value):
        instance._comment = value
    
    def __delete__(self,instance):
        del instance._comment

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = value
    
    def __delete__(self,instance):
        del instance._comment

class NetworkRuleAttrs:
    def __init__(self,parent):
        self.parent = parent

    name = Name()
    type=Type()
    user_name=UserName()
    password=Password()
    secret_string=SecretString()
    algorithm=Algorithm()
    oauth_refresh_token=OauthRefreshToken()
    oauth_refresh_token_expiry_time=OauthRefreshTokenExpiryTime()
    api_authentication=APIAuthentication()
    oauth_scopes=OauthScopes()
    comment = Comment()


class NetworkRule(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session, user_id, logger)
        self.attr = NetworkRuleAttrs(self)


    def set_name(self,val):
        self.attr.name = val

    def set_type(self,val):
        self.attr.type = val

    def set_value_list(self,val):
        self.attr.value_list = val

    def set_mode(self,val):
        self.attr.mode = val

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

    def set_create_network_rule_qry(self):
        self.qry = f"CREATE NETWORK RULE  {self.attr.name} {tags.TYPE} = {self.attr.type} {tags.VALUE_LIST} = {self.attr.value_list} {tags.MODE} = {self.attr.mode}"

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == 'TRUE':
            self.set_create_network_rule_qry()
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
