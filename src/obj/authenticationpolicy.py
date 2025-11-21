import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))
import logging
logger = logging.getLogger('authentication policy logs')
from .baseobj import BaseObject
from vars.obj.authenticationpolicy.gvauthenticationpolicy import AuthenticationPolicyTag as tags
from src.validation.validateobject import ValidateObject as vo,ValidateDependentAttributes as vda
from src.validation.validatevalue import ValidateValue as vv
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
            vo.is_new_object(session=instance.parent.session,
                             object_type=instance.parent.__class__.__name__,
                             object_name=name)
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
                vo.object_exist(session=instance.parent.session,
                                object_type=instance.parent.__class__.__name__,
                                object_name=old_name)
                vo.is_new_object(session=instance.parent.session,
                             object_type=instance.parent.__class__.__name__,
                             object_name=new_name)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to


class AuthenticationMethods:
    def __get__(self, instance, owner):
        return instance._authentication_methods
    
    def __set__(self, instance, value):
        if isinstance(value,list):
                instance.parent.logger.info("Value received as list")
                val_string=""
                for i in range(0,len(value)):
                    instance.parent.logger.info(f"Validating {value[i]} for {self.__class__.__name__}")
                    vv.is_allowed_value(
                        value=value,
                        allowed_list=tags.allowed_value_list().get(tags.AUTHENTICATION_METHODS),
                        object_type=instance.parent.object_type,
                        attr_name=self.__class__.__name__
                    )
                    if i != len(value)-1:
                        val_string=val_string+f"'{value[i]}',"
                    elif i == len(value)-1:
                        val_string=val_string+f"'{value[i]}'"
                instance.parent.logger.info(f" final value string : {val_string}")
                instance._authentication_methods=f"({val_string})"
        elif isinstance(value,str):
            vv.is_allowed_value(
                value=value,
                allowed_list=tags.allowed_value_list().get(tags.AUTHENTICATION_METHODS),
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._authentication_methods=f"('{value}')"

    def __delete__(self, instance):
        del instance._authentication_methods

class ClientTypes:
    def __get__(self, instance, owner):
        return instance._client_types
    
    def __set__(self, instance, value):
        if value=="NONE":
            instance._client_types="NONE"
        else:
            vv.is_list(
                value=value,
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._orig_value_client_types=value
            if instance._mfa_enrollment.upper()=='REQUIRED' and 'SNOWFLAKE_UI' not in value:
                vo.operation_on_object_not_suppported(message="If you set MFA_ENROLLMENT to REQUIRED, then you must include SNOWFLAKE_UI in the CLIENT_TYPES list to allow users to enroll in MFA.")
            instance.parent.logger.info("Value received as list")
            val_string=""
            for i in range(0,len(value)):
                instance.parent.logger.info(f"Validating {value[i]} for {self.__class__.__name__}")
                vv.is_allowed_value(
                    value=value,
                    allowed_list=tags.allowed_value_list().get(tags.AUTHENTICATION_METHODS),
                    object_type=instance.parent.object_type,
                    attr_name=self.__class__.__name__
                )
                if i != len(value)-1:
                    val_string=val_string+f"'{value[i]}',"
                elif i == len(value)-1:
                    val_string=val_string+f"'{value[i]}'"
            instance.parent.logger.info(f" final value string : {val_string}")
            instance._client_types=f"({val_string})"

    def __delete__(self, instance):
        del instance._client_types

class ClientPolicy:
    def __get__(self, instance, owner):
        return instance._client_policy
    
    def __set__(self, instance, value):
        if value=="NONE":
            instance._client_policy="NONE"
        else:
            val_string=" ( "
            if ('ALL' in instance._orig_value_client_types or 
                'all' in instance._orig_value_client_types or
                'DRIVER' in instance._orig_value_client_types ) or (
                    len(instance._orig_value_client_types)==0
                ):
                vv.is_dict(
                    value=value,
                    object_type=instance.parent.object_type,
                    attr_name=self.__class__.__name__
                )
                keys=list(value.keys())
                for i in range(0,len(keys)):
                    driver=keys[i]
                    vv.is_allowed_value(
                        value=driver,
                        allowed_list=tags.ALLOWED_DRIVERS
                    )
                    if i != len(keys) -1:
                        val_string=val_string + f" {driver} = ( MINIMUM_VERSION = '{value[keys[i]]}'),"
                    elif i == len(keys)-1:
                        val_string=val_string + f" {keys} = ( MINIMUM_VERSION = '{value[keys[i]]}')"
                val_string=val_string + " ) "
            else:
                vo.operation_on_object_not_suppported(message=f" To setup client policy Client type should have either ALL or DRIVER in it.")

    def __delete__(self, instance):
        del instance._client_types


class MFAEnrollment:
    def __get__(self, instance, owner):
        return instance._mfa_enrollment
    def __set__(self, instance, value):
        vv.is_allowed_value(
            value=value,
            allowed_list=tags.allowed_value_list().get(tags.MFA_ENROLLMENT),
            object_type=instance.parent.__class__.__name__,
            attr_name=self.__class__.__name__
        )
        instance._mfa_enrollment = value

    def __delete__(self, instance):
        del instance._mfa_enrollment

class MFAPolicy:
    def __get__(self, instance, owner):
        return instance._mfa_policy
    def __set__(self, instance, value):
        if isinstance(value,list):
                instance.parent.logger.info("Value received as list")
                val_string=""
                for i in range(0,len(value)):
                    instance.parent.logger.info(f"Validating {value[i]} for {self.__class__.__name__}")
                    vv.is_allowed_value(
                        value=value,
                        allowed_list=tags.allowed_value_list().get(tags.MFA_POLICY),
                        object_type=instance.parent.object_type,
                        attr_name=self.__class__.__name__
                    )
                    if i != len(value)-1:
                        val_string=val_string+f"'{value[i]}',"
                    elif i == len(value)-1:
                        val_string=val_string+f"'{value[i]}'"
                instance.parent.logger.info(f" final value string : {val_string}")
                instance._mfa_policy=f"({val_string})"
        elif isinstance(value,str):
            vv.is_allowed_value(
                value=value,
                allowed_list=tags.allowed_value_list().get(tags.MFA_POLICY),
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._mfa_policy=f"('{value}')"

    def __delete__(self, instance):
        del instance._mfa_policy

class ClientTypes:
    def __get__(self, instance, owner):
        return instance._client_types
    def __set__(self, instance, value):
        instance._client_types = value
    def __delete__(self, instance):
        del instance._client_types

class ClientPolicy:
    def __get__(self, instance, owner):
        return instance._client_policy
    def __set__(self, instance, value):
        instance._client_policy = value
    def __delete__(self, instance):
        del instance._client_policy

class SecurityIntegrations:
    def __get__(self, instance, owner):
        return instance._security_integrations
    def __set__(self, instance, value):
        instance._security_integrations = value
    def __delete__(self, instance):
        del instance._security_integrations

class PATPolicy:
    def __get__(self, instance, owner):
        return instance._pat_policy
    def __set__(self, instance, value):
        instance._pat_policy = value
    def __delete__(self, instance):
        del instance._pat_policy

class WorkloadIdentityPolicy:
    def __get__(self, instance, owner):
        return instance._workload_identity_policy
    def __set__(self, instance, value):
        instance._workload_identity_policy = value
    def __delete__(self, instance):
        del instance._workload_identity_policy


class Comment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = value
    def __delete__(self, instance):
        del instance._comment

class AuthenticationPolicyAttrs:
    def __init__(self,parent):
        self.parent=parent
    name = Name()
    authentication_methods = AuthenticationMethods()
    #mfa_authentication_methods = MFAAuthenticationMethods()
    mfa_enrollment = MFAEnrollment()
    mfa_policy = MFAPolicy()
    client_types = ClientTypes()
    client_policy = ClientPolicy()
    security_integrations = SecurityIntegrations()
    pat_policy = PATPolicy()
    workload_identity_policy = WorkloadIdentityPolicy()
    comment = Comment()

class AuthenticationPolicy(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = AuthenticationPolicyAttrs(self)
        self.session = session
        self.user_id = user_id
        self.logger = logger.getChild(self.__class__.__name__)

    # setters
    def set_name(self, v): self.attr.name = v
    def set_authentication_methods(self, val): self.attr.authentication_methods = val
    #def set_mfa_authentication_methods(self, val): self.attr.mfa_authentication_methods = val
    def set_mfa_enrollment(self, val): self.attr.mfa_enrollment = val
    def set_mfa_policy(self, val): self.attr.mfa_policy = val
    def set_client_types(self,val):self.attr.client_types=val
    def set_client_policy(self,val): self.attr.client_policy=val
    def set_security_integrations(self,val): self.attr.security_integrations=val
    def set_pat_policy(self,val) : self.attr.pat_policy=val
    def set_workload_identity_policy(self,val) : self.attr.workload_identity_policy=val
    def set_comment(self,val): self.attr.comment=val

    def set_object_properties_flag(self):
        self.flag_dic = {}
        def set_flag(tag, attrname):
            if tag != tags.COMMENT:
                self.flag_dic[tag] = 1 if getattr(self.attr, attrname) !="NONE" else 0
            elif tag == tags.COMMENT:
                self.flag_dic[tag] = 1 if getattr(self.attr, attrname) != "NONE" else 0

        set_flag(tags.AUTHENTICATION_METHODS, "authentication_methods")
        #set_flag(tags.MFA_AUTHENTICATION_METHODS, "mfa_authentication_methods")
        set_flag(tags.MFA_ENROLLMENT, "mfa_enrollment")
        set_flag(tags.MFA_POLICY, "mfa_policy")
        set_flag(tags.CLIENT_TYPES, "client_types")
        set_flag(tags.CLIENT_POLICY, "client_policy")
        set_flag(tags.SECURITY_INTEGRATIONS, "security_integrations")
        set_flag(tags.PAT_POLICY, "pat_policy")
        set_flag(tags.WORKLOAD_IDENTITY_POLICY, "workload_identity_policy")
        set_flag(tags.COMMENT, "comment")

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_auth_policy_qry(self):
        self.qry = f"CREATE AUTHENTICATION POLICY {self.attr.name[0]}"

    def add_properties_to_query(self):
        for prop in self.property_lst:
            self.qry += f" {getattr(self.attr, prop.lower())}"

    def alter_object(self):
        for prop in self.property_lst:
            self.qry = f"ALTER AUTHENTICATION POLICY {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_auth_policy_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=AuthenticationPolicy(session=session,
                         user_id=user_id,
                         logger=logger)
        
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        obj_inst.logger.info(f"set name {kwargs[tags.NAME]}")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        obj_inst.logger.info(f"set authentication methods {kwargs[tags.AUTHENTICATION_METHODS]}")
        if tags.AUTHENTICATION_METHODS in kwargs.keys():
            obj_inst.set_authentication_methods(kwargs[tags.AUTHENTICATION_METHODS])
        else:
            obj_inst.set_authentication_methods('NONE')
        '''
        obj_inst.logger.info(f"set mfa_authentication_methods {kwargs[tags.MFA_AUTHENTICATION_METHODS]}")
        if tags.MFA_AUTHENTICATION_METHODS in kwargs.keys():
            obj_inst.set_mfa_authentication_methods(kwargs[tags.MFA_AUTHENTICATION_METHODS])
        else:
            obj_inst.set_mfa_authentication_methods('NONE')
        '''
        obj_inst.logger.info(f"set mfa_enrollment {kwargs[tags.MFA_ENROLLMENT]}")
        if tags.MFA_ENROLLMENT in kwargs.keys():
            obj_inst.set_mfa_enrollment(kwargs[tags.MFA_ENROLLMENT])
        else:
            obj_inst.set_mfa_enrollment('NONE')

        obj_inst.logger.info(f"set mfa_policy {kwargs[tags.MFA_POLICY]}")
        if tags.MFA_POLICY in kwargs.keys():
            obj_inst.set_mfa_policy(kwargs[tags.MFA_POLICY])
        else:
            obj_inst.set_mfa_policy('NONE')

        obj_inst.logger.info(f"set client_types {kwargs[tags.CLIENT_TYPES]}")
        if tags.CLIENT_TYPES in kwargs.keys():
            obj_inst.set_client_types(kwargs[tags.CLIENT_TYPES])
        else:
            obj_inst.set_client_types('NONE')

        obj_inst.logger.info(f"set client_policy {kwargs[tags.CLIENT_POLICY]}")
        if tags.CLIENT_POLICY in kwargs.keys():
            obj_inst.set_client_policy(kwargs[tags.CLIENT_POLICY])
        else:
            obj_inst.set_client_policy('NONE')

        obj_inst.logger.info(f"set security_integrations {kwargs[tags.SECURITY_INTEGRATIONS]}")
        if tags.MFA_ENROLLMENT in kwargs.keys():
            obj_inst.set_security_integrations(kwargs[tags.SECURITY_INTEGRATIONS])
        else:
            obj_inst.set_security_integrations('NONE')

        obj_inst.logger.info(f"set pat_policy {kwargs[tags.PAT_POLICY]}")
        if tags.PAT_POLICY in kwargs.keys():
            obj_inst.set_pat_policy(kwargs[tags.PAT_POLICY])
        else:
            obj_inst.set_pat_policy('NONE')

        obj_inst.logger.info(f"set comment {kwargs[tags.COMMENT]}")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')

        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
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
