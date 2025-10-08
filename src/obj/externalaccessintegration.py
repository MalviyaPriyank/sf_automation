
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

class AllowedNetworkRules:
    def __get__(self,instance,owner):
        return instance._allowed_network_rules
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vo.object_exist(session=instance.parent.session,
                        object_type=instance.parent.__class__.__name__,
                        object_name=value)
        instance._allowed_network_rules = value
    
    def __delete__(self,instance):
        del instance._allowed_network_rules


class Enabled:
    def __get__(self,instance,owner):
        return instance._enabled
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vv.is_bool(value=value,
                   object_type=instance.parent.__class__.__name__,
                   attr_name=self.__class__.__name__)
        instance._enabled=value    

    def __delete__(self,instance):
        del instance._enabled

class AllowedAPIAuthenticationIntegrations:
    def __get__(self,instance,owner):
        return instance._allowed_api_authentication_integration
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._allowed_api_authentication_integration="NONE"
        else:
            vo.object_exist(session=instance.parent.session,
                            object_type="SECURITY INTEGRATION",
                            object_name=value
                            )
            instance._allowed_api_authentication_integration=value
            
    def __delete__(self,instance):
        del instance._allowed_api_authentication_integration

class AllowedAuthenticationSecrets:
    def __get__(self,instance,owner):
        return instance._allowed_authentication_secrets
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._allowed_authentication_secrets="NONE"
        elif value.upper()=="ALL":
            instance._allowed_authentication_secrets=value
        else:
            vo.object_exist(session=instance.parent.session,
                            object_type="SECRET",
                            object_name=value)
            instance._allowed_authentication_secrets = value
    
    def __delete__(self,instance):
        del instance._allowed_authentication_secrets

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
    allowed_network_rules=AllowedNetworkRules()
    enabled=Enabled()
    allowed_api_authentication_integrations=AllowedAPIAuthenticationIntegrations()
    allowed_authentication_secrets = AllowedAuthenticationSecrets()
    comment=Comment()


class NetworkRule(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session, user_id, logger)
        self.attr = NetworkRuleAttrs(self)


    def set_name(self,val):
        self.attr.name = val

    def set_allowed_network_rules(self,val):
        self.attr.allowed_network_rules = val

    def set_enabled(self,val):
        self.attr.enabled = val

    def set_allowed_api_authentication_integrations(self,val):
        self.attr.allowed_api_authentication_integrations = val

    def set_allowed_authentication_secrets(self,val):
        self.attr.allowed_authentication_secrets=val

    def set_comment(self,val):
        self.attr.comment = val

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
        
        set_flag(tags.ALLOWED_API_AUTHENTICATION_INTEGRATIONS,"_allowed_api_authentication_integrations")
        set_flag(tags.ALLOWED_AUTHENTICATION_SECRETS,"_allowed_authentication_secrets")
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

    def set_create_external_access_integration(self):
        self.qry = f"CREATE EXTERNAL ACCESS INTEGRATION {self.attr.name} {tags.ALLOWED_NETWORK_RULES} = {self.attr.allowed_network_rules} {tags.ENABLED} = {self.attr.enabled} "

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
            self.set_create_external_access_integration()
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
        self.set_allowed_network_rules(kwargs[tags.ALLOWED_NETWORK_RULES])
        self.set_enabled(kwargs[tags.ENABLED])
        self.set_allowed_api_authentication_integrations(kwargs[tags.ALLOWED_API_AUTHENTICATION_INTEGRATIONS])
        self.set_allowed_authentication_secrets(kwargs[tags.ALLOWED_AUTHENTICATION_SECRETS])
        self.set_comment(kwargs[tags.COMMENT])
        self.prepare_query()
        self.create_database_role()

        self.logger.info('create deployment entry')
        self.create_deployment_entry(object_name=self.attr.name[0],object_type=self.__class__.__name__,object_database='NA',object_schema='NA')

        self.logger.info('writing file to git')
        self.write_file_to_git(object_name=self.attr.name[0],object_type=self.__class__.__name__,object_database='NA',object_schema='NA')
