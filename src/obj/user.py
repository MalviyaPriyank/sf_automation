

import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.obj.user.gvuser import UserTag as tags
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from dep.deploy import Deploy
from .baseobj import BaseObject 
from src.usr.user import ChatHistory

class Name:   
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_user(session=instance.parent.session,
                           user_name=name,
                           object_type=instance.parent.__class__.__name__)
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
                vo.user_exist(session=instance.parent.session,
                              user_name=old_name)
                vo.is_new_user(session=instance.parent.session,
                           user_name=new_name,
                           object_type=instance.parent.__class__.__name__)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"


    def __del__(self,instance):
        del instance._name
        del instance._rename_to

class Password:
    def __get__(self,instance,owner):
        return instance._password
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._password=value
        else:
            vv.is_string(value,instance.parent.__class__.__name__,self.__class__.__name__)
            vv.is_valid_password(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._password = f"'{value}'"

    def __delete__(self,instance):
        del instance._password

class LoginName:
    def __get__(self,instance,owner):
        return instance._login_name
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._login_name=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._login_name = value

    def __delete__(self,instance):
        del instance._login_name

class DisplayName:
    def __get__(self,instance,owner):
        return instance._display_name
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._display_name=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._display_name = f"'{value}'"

    def __delete__(self,instance):
        del instance._display_name

class FirstName:
    def __get__(self,instance,owner):
        return instance._first_name
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._first_name=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._first_name = f"'{value}'"

    def __delete__(self,instance):
        del instance._first_name

class MiddleName:
    def __get__(self,instance,owner):
        return instance._middle_name
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._middle_name=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._middle_name = f"'{value}'"

    def __delete__(self,instance):
        del instance._middle_name

class LastName:
    def __get__(self,instance,owner):
        return instance._last_name
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._last_name=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._last_name = f"'{value}'"

    def __delete__(self,instance):
        del instance._last_name

class Email:
    def __get__(self,instance,owner):
        return instance._email
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._email=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._email =f"'{value}'"
    
    def __delete__(self,instance):
        del instance._email

class MustChangePassword:
    def __get__(self,instance,owner):
        return instance._must_change_password
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        #if value == "NONE":
        #    instance._must_change_password = value
        #else: 
        vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._must_change_password = "TRUE"    

    def __delete__(self,instance):
        del instance._must_change_password

class Disabled:
    def __get__(self,instance,owner):
        return instance._disabled
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value == "NONE":
            instance._disabled = value
        else: 
            vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._disabled = value 
    
    def __delete__(self,instance):
        del instance._disabled

class DaysToExpiry:
    def __get__(self,instance,owner):
        return instance._days_to_expiry
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._days_to_expiry=value
        else:
            vv.is_positive_number(value,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._days_to_expiry = value
            
    
    def __delete__(self,instance):
        del instance._days_to_expiry

class MinsToUnlock:
    def __get__(self,instance,owner):
        return instance._mins_to_unlock
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._mins_to_unlock=value
        else:
            vv.is_positive_number(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._mins_to_unlock = value
    
    def __delete__(self,instance):
        del instance._mins_to_unlock

class DefaultWarehouse:
    def __get__(self,instance,owner):
        return instance._default_warehouse
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._default_warehouse=value
        else:
            vo.warehouse_exist(session=instance.parent.session,warehouse_name=value)
            instance._default_warehouse=value
    
    def __delete__(self,instance):
        del instance._default_warehouse

class DefaultRole:
    def __get__(self,instance,owner):
        return instance._default_role
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._default_role=value
        else:
            vo.role_exist(session=instance.parent.session,role_name=value)
            instance._default_role=value
    
    def __delete__(self,instance):
        del instance._default_role

class DefaultSecondaryRoles:
    def __get__(self,instance,owner):
        return instance._default_secondary_roles
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._default_secondary_roles=value
        else:
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.DEFAULT_SECONDARY_ROLES),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._default_secondary_roles = value
    
    def __delete__(self,instance):
        del instance._default_secondary_roles

class MinsToByPassMFA:
    def __get__(self,instance,owner):
        return instance._mins_to_by_pass_mfa
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._mins_to_by_pass_mfa=value
        else:
            vv.is_positive_number(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._mins_to_by_pass_mfa = value     
    
    def __delete__(self,instance):
        del instance._mins_to_by_pass_mfa

class RSAPublicKey:
    def __get__(self,instance,owner):
        return instance._rsa_public_key
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._rsa_public_key=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._rsa_public_key = value
    
    def __delete__(self,instance):
        del instance._rsa_public_key

class RSAPublicKeyFP:
    def __get__(self,instance,owner):
        return instance._rsa_public_key_fp
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._rsa_public_key_fp=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._rsa_public_key_fp = value
     
    def __delete__(self,instance):
        del instance._rsa_public_key_fp

class RSAPublicKey2:
    def __get__(self,instance,owner):
        return instance._rsa_public_key_2
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._rsa_public_key_2=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._rsa_public_key_2 = value
    
    def __delete__(self,instance):
        del instance._rsa_public_key_2

class RSAPublicKey2FP:
    def __get__(self,instance,owner):
        return instance._rsa_public_key_2_fp
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._rsa_public_key_2_fp=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._rsa_public_key_2_fp = value
    
    def __delete__(self,instance):
        del instance._rsa_public_key_2_fp

class Type:
    def __get__(self,instance,owner):
        return instance._type
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._type=value
        else:
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.TYPE),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._type=value

    def __delete__(self,instance):
        del instance._type

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._comment=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._comment = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._comment

class EnableUnredactedQuerySyntaxError:
    def __get__(self,instance,owner):
        return instance._enable_unredacted_query_syntax_error
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._enable_unredacted_query_syntax_error=value
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._enable_unredacted_query_syntax_error = value
    
    def __delete__(self,instance):
        del instance._enable_unredacted_query_syntax_error

class UserAttrs:
    def __init__(self,parent):
        self.parent = parent

    name = Name()
    password = Password()
    login_name = LoginName()
    display_name = DisplayName()
    first_name = FirstName()
    middle_name = MiddleName()
    last_name = LastName()
    email = Email()
    must_change_password = MustChangePassword()
    disabled = Disabled()
    days_to_expiry = DaysToExpiry()
    mins_to_unlock = MinsToUnlock()
    default_warehouse = DefaultWarehouse()
    default_role = DefaultRole()
    default_secondary_roles = DefaultSecondaryRoles()
    mins_to_by_pass_mfa = MinsToByPassMFA()
    rsa_public_key = RSAPublicKey()
    rsa_public_key_fp = RSAPublicKeyFP()
    rsa_public_key_2 = RSAPublicKey2()
    rsa_public_key_2_fp = RSAPublicKey2FP()
    type = Type()
    comment = Comment()
    enable_unredacted_query_syntax_error = EnableUnredactedQuerySyntaxError()

class User(BaseObject):
    def __init__(self, session, user_id, logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger)
        self.attr = UserAttrs(self)

    def set_name(self, value):
        self.attr.name = value

    def set_password(self, value):
        self.attr.password = value

    def set_login_name(self, value):
        self.attr.login_name = value

    def set_display_name(self, value):
        self.attr.display_name = value

    def set_first_name(self, value):
        self.attr.first_name = value

    def set_last_name(self, value):
        self.attr.last_name = value

    def set_email(self, value):
        self.attr.email = value

    def set_must_change_password(self, value):
        self.attr.must_change_password = value

    def set_disabled(self, value):
        self.attr.disabled = value

    def set_days_to_expiry(self, value):
        self.attr.days_to_expiry = value

    def set_mins_to_unlock(self, value):
        self.attr.mins_to_unlock = value

    def set_default_warehouse(self, value):
        self.attr.default_warehouse = value

    def set_default_role(self, value):
        self.attr.default_role = value

    def set_default_secondary_roles(self, value):
        self.attr.default_secondary_roles = value

    def set_mins_to_by_pass_mfa(self, value):
        self.attr.mins_to_by_pass_mfa = value

    def set_rsa_public_key(self, value):
        self.attr.rsa_public_key = value

    def set_rsa_public_key_fp(self, value):
        self.attr.rsa_public_key_fp = value

    def set_rsa_public_key_2(self, value):
        self.attr.rsa_public_key_2 = value

    def set_rsa_public_key_2_fp(self, value):
        self.attr.rsa_public_key_2_fp = value

    def set_type(self, value):
        self.attr.type = value

    def set_comment(self, value):
        self.attr.comment = value

    def set_enable_unredacted_query_syntax_error(self, value):
        self.attr.enable_unredacted_query_syntax_error = value

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.logger.info(f"setting flag for {attribute_tag} : {attribute_name}")
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.PASSWORD,"password")
        set_flag(tags.LOGIN_NAME,"login_name")
        set_flag(tags.DISPLAY_NAME,"display_name")
        set_flag(tags.FIRST_NAME,"first_name")
        set_flag(tags.LAST_NAME,"last_name")
        set_flag(tags.EMAIL,"email")
        set_flag(tags.MUST_CHANGE_PASSWORD,"must_change_password")
        set_flag(tags.DISABLED,"disabled")
        set_flag(tags.DAYS_TO_EXPIRY,"days_to_expiry")
        set_flag(tags.MINS_TO_UNLOCK,"mins_to_unlock")
        set_flag(tags.DEFAULT_WAREHOUSE,"default_warehouse")
        set_flag(tags.DEFAULT_ROLE,"default_role")
        set_flag(tags.DEFAULT_SECONDARY_ROLES,"default_secondary_roles")
        set_flag(tags.MINS_TO_BY_PASS_MFA,"mins_to_by_pass_mfa")
        set_flag(tags.RSA_PUBLIC_KEY,"rsa_public_key")
        set_flag(tags.RSA_PUBLIC_KEY_FP,"rsa_public_key_fp")
        set_flag(tags.RSA_PUBLIC_KEY_2,"rsa_public_key_2")
        set_flag(tags.RSA_PUBLIC_KEY_2_FP,"rsa_public_key_2_fp")
        set_flag(tags.TYPE,"type")
        set_flag(tags.COMMENT,"comment")
        set_flag(tags.ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR,"enable_unredacted_query_syntax_error")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"CREATE USER {self.attr.name[0]} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.PASSWORD:
                    self.qry = f" {self.qry} {tags.PASSWORD} = {self.attr.password} \n"
                if prop == tags.DISPLAY_NAME:
                    self.qry = f" {self.qry} {tags.DISPLAY_NAME} = {self.attr.display_name} \n"
                if prop == tags.FIRST_NAME:
                    self.qry = f" {self.qry} {tags.FIRST_NAME} = {self.attr.first_name} \n"
                if prop == tags.LAST_NAME:
                    self.qry = f" {self.qry} {tags.LAST_NAME} = {self.attr.last_name} \n"
                if prop == tags.EMAIL:
                    self.qry = f" {self.qry} {tags.EMAIL} = {self.attr.email} \n"
                if prop == tags.MUST_CHANGE_PASSWORD:
                    self.qry = f" {self.qry} {tags.MUST_CHANGE_PASSWORD} = {self.attr.must_change_password} \n"
                if prop == tags.DISABLED:
                    self.qry = f" {self.qry} {tags.DISABLED} = {self.attr.disabled} \n"
                if prop == tags.DAYS_TO_EXPIRY:
                    self.qry = f" {self.qry} {tags.DAYS_TO_EXPIRY} = {self.attr.days_to_expiry} \n"
                if prop == tags.MINS_TO_UNLOCK:
                    self.qry = f" {self.qry} {tags.MINS_TO_UNLOCK} = {self.attr.mins_to_unlock} \n"
                if prop == tags.DEFAULT_WAREHOUSE:
                    self.qry = f" {self.qry} {tags.DEFAULT_WAREHOUSE} = {self.attr.default_warehouse} \n"
                if prop == tags.DEFAULT_ROLE:
                    self.qry = f" {self.qry} {tags.DEFAULT_ROLE} = {self.attr.default_role} \n"
                if prop == tags.DEFAULT_SECONDARY_ROLES:
                    self.qry = f" {self.qry} {tags.DEFAULT_SECONDARY_ROLES} = {self.attr.default_secondary_roles} \n"
                if prop == tags.MINS_TO_BY_PASS_MFA:
                    self.qry = f" {self.qry} {tags.MINS_TO_BY_PASS_MFA} = {self.attr.mins_to_by_pass_mfa} \n"
                if prop == tags.RSA_PUBLIC_KEY:
                    self.qry = f" {self.qry} {tags.RSA_PUBLIC_KEY} = {self.attr.rsa_public_key} \n"
                if prop == tags.RSA_PUBLIC_KEY_FP:
                    self.qry = f" {self.qry} {tags.RSA_PUBLIC_KEY_FP} = {self.attr.rsa_public_key_fp} \n"
                if prop == tags.RSA_PUBLIC_KEY_2:
                    self.qry = f" {self.qry} {tags.RSA_PUBLIC_KEY_2} = {self.attr.rsa_public_key_2} \n"
                if prop == tags.RSA_PUBLIC_KEY_2_FP:
                    self.qry = f" {self.qry} {tags.RSA_PUBLIC_KEY_2_FP} = {self.attr.rsa_public_key_2_fp} \n"
                if prop == tags.TYPE:
                    self.qry = f" {self.qry} {tags.TYPE} = {self.attr.type} \n"
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = '{self.attr.comment}' \n"
                if prop == tags.ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR:
                    self.qry = f" {self.qry} {tags.ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR} = {self.attr.enable_unredacted_query_syntax_error} "


    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()

    def create_user(self):
        self.execute_final_query()


    def create_object(self,**kwargs):
        self.logger.info(f"Operating on {self.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        self.logger.info(f'dictionary passed {kwargs}')
        self.is_create=kwargs[tags.IS_CREATE]

        self.logger.info(f'set name {kwargs[tags.NAME]}')
        self.set_name(kwargs[tags.NAME])

        self.set_password(kwargs[tags.PASSWORD])
        self.logger.info(f'set password {kwargs[tags.PASSWORD]}')

        self.set_login_name(kwargs[tags.LOGIN_NAME])
        self.logger.info(f'set login name {kwargs[tags.LOGIN_NAME]}')

        self.set_display_name(kwargs[tags.DISPLAY_NAME])
        self.logger.info(f'set display name {kwargs[tags.DISPLAY_NAME]}')

        self.set_first_name(kwargs[tags.FIRST_NAME])
        self.logger.info(f'set first name {kwargs[tags.FIRST_NAME]}')

        self.set_last_name(kwargs[tags.LAST_NAME])
        self.logger.info(f'set last name {kwargs[tags.LAST_NAME]}')

        self.set_email(kwargs[tags.EMAIL])
        self.logger.info(f'set email  {kwargs[tags.EMAIL]}')

        self.set_must_change_password(kwargs[tags.MUST_CHANGE_PASSWORD])
        self.set_disabled(kwargs[tags.DISABLED])
        self.set_days_to_expiry(kwargs[tags.DAYS_TO_EXPIRY])
        self.set_mins_to_unlock(kwargs[tags.MINS_TO_UNLOCK])
        self.set_default_warehouse(kwargs[tags.DEFAULT_WAREHOUSE])
        self.set_default_role(kwargs[tags.DEFAULT_ROLE])
        self.set_default_secondary_roles(kwargs[tags.DEFAULT_SECONDARY_ROLES])
        self.set_mins_to_by_pass_mfa(kwargs[tags.MINS_TO_BY_PASS_MFA])
        self.set_rsa_public_key(kwargs[tags.RSA_PUBLIC_KEY])
        self.set_rsa_public_key_fp(kwargs[tags.RSA_PUBLIC_KEY_FP])
        self.set_rsa_public_key_2(kwargs[tags.RSA_PUBLIC_KEY_2])
        self.set_rsa_public_key_2_fp(kwargs[tags.RSA_PUBLIC_KEY_2_FP])
        self.set_type(kwargs[tags.TYPE])
        self.set_comment(kwargs[tags.COMMENT])
        self.set_enable_unredacted_query_syntax_error(kwargs[tags.ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR])
        self.prepare_query()
        self.create_user()
        self.create_deployment_entry(object_name=self.attr.name[0],object_type=self.__class__.__name__,object_database='NA',object_schema='NA')
        self.write_file_to_git(object_name=self.attr.name[0],object_type=self.__class__.__name__,object_database='NA',object_schema='NA')


class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=User(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info("set name")
        if tags.NAME in kwargs.keys():
            logger.info("name found in dictionary")
            logger.info(f"{kwargs[tags.NAME]}")
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        logger.info("set password")
        if tags.PASSWORD in kwargs.keys():
            obj_inst.set_password(kwargs[tags.PASSWORD])
        else:
            obj_inst.set_password('NONE')

        logger.info("set login_name")
        if tags.LOGIN_NAME in kwargs.keys():
            obj_inst.set_login_name(kwargs[tags.LOGIN_NAME])
        else:
            obj_inst.set_login_name('NONE')

        logger.info("set display_name")
        if tags.DISPLAY_NAME in kwargs.keys():
            obj_inst.set_display_name(kwargs[tags.DISPLAY_NAME])
        else:
            obj_inst.set_display_name('NONE')

        logger.info("set first_name")
        if tags.FIRST_NAME in kwargs.keys():
            obj_inst.set_first_name(kwargs[tags.FIRST_NAME])
        else:
            obj_inst.set_first_name('NONE')

        logger.info("set last_name")
        if tags.LAST_NAME in kwargs.keys():
            obj_inst.set_last_name(kwargs[tags.LAST_NAME])
        else:
            obj_inst.set_last_name('NONE')

        logger.info("set email")
        if tags.EMAIL in kwargs.keys():
            obj_inst.set_email(kwargs[tags.EMAIL])
        else:
            obj_inst.set_email('NONE')

        logger.info("set must_change_password")
        if tags.MUST_CHANGE_PASSWORD in kwargs.keys():
            obj_inst.set_must_change_password(kwargs[tags.MUST_CHANGE_PASSWORD])
        else:
            obj_inst.set_must_change_password('NONE')

        logger.info("set disabled")
        if tags.DISABLED in kwargs.keys():
            obj_inst.set_disabled(kwargs[tags.DISABLED])
        else:
            obj_inst.set_disabled('NONE')

        logger.info("set days_to_expiry")
        if tags.DAYS_TO_EXPIRY in kwargs.keys():
            obj_inst.set_days_to_expiry(kwargs[tags.DAYS_TO_EXPIRY])
        else:
            obj_inst.set_days_to_expiry('NONE')

        logger.info("set mins_to_unlock")
        if tags.MINS_TO_UNLOCK in kwargs.keys():
            obj_inst.set_mins_to_unlock(kwargs[tags.MINS_TO_UNLOCK])
        else:
            obj_inst.set_mins_to_unlock('NONE')

        logger.info("set default_warehouse")
        if tags.DEFAULT_WAREHOUSE in kwargs.keys():
            obj_inst.set_default_warehouse(kwargs[tags.DEFAULT_WAREHOUSE])
        else:
            obj_inst.set_default_warehouse('NONE')

        logger.info("set default_role")
        if tags.DEFAULT_ROLE in kwargs.keys():
            obj_inst.set_default_role(kwargs[tags.DEFAULT_ROLE])
        else:
            obj_inst.set_default_role('NONE')

        logger.info("set default_secondary_roles")
        if tags.DEFAULT_SECONDARY_ROLES in kwargs.keys():
            obj_inst.set_default_secondary_roles(kwargs[tags.DEFAULT_SECONDARY_ROLES])
        else:
            obj_inst.set_default_secondary_roles('NONE')

        logger.info("set mins_to_by_pass_mfa")
        if tags.MINS_TO_BY_PASS_MFA in kwargs.keys():
            obj_inst.set_mins_to_by_pass_mfa(kwargs[tags.MINS_TO_BY_PASS_MFA])
        else:
            obj_inst.set_mins_to_by_pass_mfa('NONE')

        logger.info("set rsa_public_key")
        if tags.RSA_PUBLIC_KEY in kwargs.keys():
            obj_inst.set_rsa_public_key(kwargs[tags.RSA_PUBLIC_KEY])
        else:
            obj_inst.set_rsa_public_key('NONE')

        logger.info("set rsa_public_key_fp")
        if tags.RSA_PUBLIC_KEY_FP in kwargs.keys():
            obj_inst.set_rsa_public_key_fp(kwargs[tags.RSA_PUBLIC_KEY_FP])
        else:
            obj_inst.set_rsa_public_key_fp('NONE')

        logger.info("set rsa_public_key_2")
        if tags.RSA_PUBLIC_KEY_2 in kwargs.keys():
            obj_inst.set_rsa_public_key_2(kwargs[tags.RSA_PUBLIC_KEY_2])
        else:
            obj_inst.set_rsa_public_key_2('NONE')

        logger.info("set rsa_public_key_2_fp")
        if tags.RSA_PUBLIC_KEY_2_FP in kwargs.keys():
            obj_inst.set_rsa_public_key_2_fp(kwargs[tags.RSA_PUBLIC_KEY_2_FP])
        else:
            obj_inst.set_rsa_public_key_2_fp('NONE')

        logger.info("set type")
        if tags.TYPE in kwargs.keys():
            obj_inst.set_type(kwargs[tags.TYPE])
        else:
            obj_inst.set_type('NONE')

        logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')

        logger.info("set enable_unredacted_query_syntax_error")
        if tags.ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR in kwargs.keys():
            obj_inst.set_enable_unredacted_query_syntax_error(kwargs[tags.ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR])
        else:
            obj_inst.set_enable_unredacted_query_syntax_error('NONE')



        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('git sync')
        obj_inst.write_file_to_git()
        
        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                        object_identifier=obj_inst.attr.name[0],
                                        qry=obj_inst.qry)

    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
