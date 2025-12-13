
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from src.obj.baseobj import BaseObject 
from vars.obj.securityintegrationaws.gvsecurityintegrationaws  import SecurityIntegrationAWSTag as tags
from src.usr.user import ChatHistory

class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)

    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
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
        instance._enabled=value
            
    def __delete__(self,instance):
        del instance._enabled

class AWSRoleARN:
    def __get__(self,instance,owner):
        return instance._aws_role_arn
    
    def __set__(self,instance,value):
        instance._aws_role_arn=f"'{value}'"
            
    def __delete__(self,instance):
        del instance._aws_role_arn

class SecurityIntegrationAWSAttrs:
    def __init__(self,parent):
        self.parent=parent
    name=Name()
    type=Type()
    auth_type=AuthType()
    enabled=Enabled()
    aws_role_arn=AWSRoleARN()

class SecurityIntegrationAWS(BaseObject):
    def __init__(self, session, user_id, logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger,database_required=False,schema_required=False)
        self.attr=SecurityIntegrationAWSAttrs(self)

    def set_name(self,val):
        self.attr.name = val

    def set_type(self,val):
        self.attr.type = val

    def set_auth_type(self,val):
        self.attr.auth_type = val

    def set_enabled(self,val):
        self.attr.enabled = val

    def set_aws_role_arn(self,val):
        self.attr.aws_role_arn=val


    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.COMMENT,"comment")


    def alter_object(self):        
        for prop in self.property_lst:
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.COMMENT} = '{self.attr.comment}'"
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
        {tags.AWS_ROLE_ARN} = {self.attr.aws_role_arn} 
        {tags.ENABLED} = {self.attr.enabled}
        """

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop==tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = '{self.attr.comment}' "

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
        obj_inst.set_base_attributes(kwargs=kwargs)

        obj_inst.logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        obj_inst.logger.info("set type")
        obj_inst.set_type("API_AUTHENTICATION")

        obj_inst.logger.info("set auth_type")
        obj_inst.set_auth_type("AWS_IAM")

        obj_inst.logger.info("set aws_role_arn")
        if tags.AUTH_TYPE in kwargs.keys():
            obj_inst.set_aws_role_arn(kwargs[tags.AWS_ROLE_ARN])
        else:
            obj_inst.set_aws_role_arn('NONE')

        obj_inst.logger.info("set enabled")
        if tags.ENABLED in kwargs.keys():
            obj_inst.set_enabled(kwargs[tags.ENABLED])
        else:
            obj_inst.set_enabled('NONE')

        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        obj_inst.print_query()
        
        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                           object_identifier=obj_inst.attr.name[0],
                                           qry=obj_inst.qry)


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
