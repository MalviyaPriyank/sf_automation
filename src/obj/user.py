

import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.gvobject import User as gv,Config as cfg
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if ( vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__) 
              and not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
              and not vv.has_special_characters(value,instance.parent.__class__.__name__,self.__class__.__name__)
              ):
            instance._account_name = value

class NameTag:
    def __get__(self,instance,owner):
        return instance._name_tag
    
    def __set__(self,instance,value):
        instance._name_tag = value

    def __delete__(self,instance):
        del instance._name_tag

class Password:
    def __get__(self,instance,owner):
        return instance._password
    
    def __set__(self,instance,value):
        if ( vv.is_enclosed_in_single_quotes(value,instance.parent.__class__.__name__,self.__class__.__name__) and 
            vv.is_string(value,instance.parent.__class__.__name__,self.__class__.__name__)):
            instance._password = value
        else:
            instance._password = value

    def __delete__(self,instance):
        del instance._password

class PasswordTag:
    def __get__(self,instance,owner):
        return instance._password_tag
    
    def __set__(self,instance,value):
        instance._password_tag = value

    def __delete__(self,instance):
        del instance._password_tag

class LoginName:
    def __get__(self,instance,owner):
        return instance._login_name
    
    def __set__(self,instance,value):
        if ( vv.is_enclosed_in_single_quotes(value,instance.parent.__class__.__name__,self.__class__.__name__) and 
            vv.is_string(value,instance.parent.__class__.__name__,self.__class__.__name__)):
            instance._login_name = value

    def __delete__(self,instance):
        del instance._login_name

class LoginNameTag:
    def __get__(self,instance,owner):
        return instance._login_name_tag
    
    def __set__(self,instance,value):
        instance._login_name_tag = value

    def __delete__(self,instance):
        del instance._login_name_tag

class DisplayName:
    def __get__(self,instance,owner):
        return instance._display_name
    
    def __set__(self,instance,value):
        if ( vv.is_enclosed_in_single_quotes(value,instance.parent.__class__.__name__,self.__class__.__name__) and 
            vv.is_string(value,instance.parent.__class__.__name__,self.__class__.__name__)):
            instance._display_name = value

    def __delete__(self,instance):
        del instance._display_name

class DisplayNameTag:
    def __get__(self,instance,owner):
        return instance._display_name_tag
    
    def __set__(self,instance,value):
        instance._display_name_tag = value

    def __delete__(self,instance):
        del instance._display_name_tag

class FirstName:
    def __get__(self,instance,owner):
        return instance._first_name
    
    def __set__(self,instance,value):
        if ( vv.is_enclosed_in_single_quotes(value,instance.parent.__class__.__name__,self.__class__.__name__) and 
            vv.is_string(value,instance.parent.__class__.__name__,self.__class__.__name__)):
            instance._first_name = value

    def __delete__(self,instance):
        del instance._first_name

class FirstNameTag:
    def __get__(self,instance,owner):
        return instance._first_name_tag
    
    def __set__(self,instance,value):
        instance._first_name_tag = value

    def __delete__(self,instance):
        del instance._first_name_tag

class MiddleName:
    def __get__(self,instance,owner):
        return instance._middle_name
    
    def __set__(self,instance,value):
        if ( vv.is_enclosed_in_single_quotes(value,instance.parent.__class__.__name__,self.__class__.__name__) and 
            vv.is_string(value,instance.parent.__class__.__name__,self.__class__.__name__)):
            instance._middle_name = value

    def __delete__(self,instance):
        del instance._middle_name


class MiddleNameTag:
    def __get__(self,instance,owner):
        return instance._middle_name_tag
    
    def __set__(self,instance,value):
        instance._middle_name_tag = value

    def __delete__(self,instance):
        del instance._middle_name_tag

class LastName:
    def __get__(self,instance,owner):
        return instance._last_name
    
    def __set__(self,instance,value):
        if ( vv.is_enclosed_in_single_quotes(value,instance.parent.__class__.__name__,self.__class__.__name__) and 
            vv.is_string(value,instance.parent.__class__.__name__,self.__class__.__name__)):
            instance._last_name = value

    def __delete__(self,instance):
        del instance._last_name

class LastNameTag:
    def __get__(self,instance,owner):
        return instance._last_name_tag
    
    def __set__(self,instance,value):
        instance._last_name_tag = value

    def __delete__(self,instance):
        del instance._last_name_tag

class Email:
    def __get__(self,instance,owner):
        return instance._email
    
    def __set__(self,instance,value):
        if ( vv.is_enclosed_in_single_quotes(value,instance.parent.__class__.__name__,self.__class__.__name__) and 
            vv.is_string(value,instance.parent.__class__.__name__,self.__class__.__name__)):
            instance._email = value
    
    def __delete__(self,instance):
        del instance._email

class EmailTag:
    def __get__(self,instance,owner):
        return instance._email_tag
    
    def __set__(self,instance,value):
        instance._email_tag = value
    
    def __delete__(self,instance):
        del instance._email_tag

class MustChangePassword:
    def __get__(self,instance,owner):
        return instance._must_change_password
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._must_change_password = value
        elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._must_change_password = value    
    
    def __delete__(self,instance):
        del instance._must_change_password

class MustChangePasswordTag:
    def __get__(self,instance,owner):
        return instance._must_change_password_tag
    
    def __set__(self,instance,value):
        instance._must_change_password_tag = value
    
    def __delete__(self,instance):
        del instance._must_change_password_tag

class Disabled:
    def __get__(self,instance,owner):
        return instance._disabled
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._disabled = value
        elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._disabled = value 
    
    def __delete__(self,instance):
        del instance._disabled

class DisabledTag:
    def __get__(self,instance,owner):
        return instance._disabled_tag
    
    def __set__(self,instance,value):
        instance._disabled_tag = value
    
    def __delete__(self,instance):
        del instance._disabled_tag

class DaysToExpiry:
    def __get__(self,instance,owner):
        return instance._days_to_expiry
    
    def __set__(self,instance,value):
        if vv.is_positive_number(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._days_to_expiry = value
            
    
    def __delete__(self,instance):
        del instance._days_to_expiry

class DaysToExpiryTag:
    def __get__(self,instance,owner):
        return instance._days_to_expiry_tag
    
    def __set__(self,instance,value):
        instance._days_to_expiry_tag = value
    
    def __delete__(self,instance):
        del instance._days_to_expiry_tag

class MinsToUnlock:
    def __get__(self,instance,owner):
        return instance._mins_to_unlock
    
    def __set__(self,instance,value):
        if vv.is_positive_number(value):
            instance._mins_to_unlock = value
        else:
            raise ValueError
    
    def __delete__(self,instance):
        del instance._mins_to_unlock

class MinsToUnlockTag:
    def __get__(self,instance,owner):
        return instance._mins_to_unlock_tag
    
    def __set__(self,instance,value):
        instance._mins_to_unlock_tag = value
    
    def __delete__(self,instance):
        del instance._mins_to_unlock_tag


class DefaultWarehouse:
    def __get__(self,instance,owner):
        return instance._default_warehouse
    
    def __set__(self,instance,value):
        if type(value) != str:
            raise TypeError
        else:
            instance._default_warehouse = value
    
    def __delete__(self,instance):
        del instance._default_warehouse

class DefaultWarehouseTag:
    def __get__(self,instance,owner):
        return instance._default_warehouse_tag
    
    def __set__(self,instance,value):
        instance._default_warehouse_tag = value
    
    def __delete__(self,instance):
        del instance._default_warehouse_tag

class DefaultRole:
    def __get__(self,instance,owner):
        return instance._default_role
    
    def __set__(self,instance,value):
        if type(value) != str:
            raise TypeError
        else:
            instance._default_role = value
    
    def __delete__(self,instance):
        del instance._default_role

class DefaultRoleTag:
    def __get__(self,instance,owner):
        return instance._default_role_tag
    
    def __set__(self,instance,value):
        instance._default_role_tag = value
    
    def __delete__(self,instance):
        del instance._default_role_tag


class DefaultSecondaryRoles:
    def __get__(self,instance,owner):
        return instance._default_secondary_roles
    
    def __set__(self,instance,value):
        if value not in gv._allowed_values_default_secondary_roles:#['ALL',{}]
            raise ValueError
        else:
            instance._default_secondary_roles = value
    
    def __delete__(self,instance):
        del instance._default_secondary_roles

class DefaultSecondaryRolesTag:
    def __get__(self,instance,owner):
        return instance._default_secondary_roles_tag
    
    def __set__(self,instance,value):
        instance._default_secondary_roles_tag = value
    
    def __delete__(self,instance):
        del instance._default_secondary_roles_tag

class MinsToByPassMFA:
    def __get__(self,instance,owner):
        return instance._mins_to_by_pass_mfa
    
    def __set__(self,instance,value):
        if vv.is_positive_number(value):
            instance._mins_to_by_pass_mfa = value
        else:
            raise ValueError
            
    
    def __delete__(self,instance):
        del instance._mins_to_by_pass_mfa

class MinsToByPassMFATag:
    def __get__(self,instance,owner):
        return instance._mins_to_by_pass_mfa_tag
    
    def __set__(self,instance,value):
        instance._mins_to_by_pass_mfa_tag = value
    
    def __delete__(self,instance):
        del instance._mins_to_by_pass_mfa_tag

class RSAPublicKey:
    def __get__(self,instance,owner):
        return instance._rsa_public_key
    
    def __set__(self,instance,value):
        instance._rsa_public_key = value
    
    def __delete__(self,instance):
        del instance._rsa_public_key

class RSAPublicKeyTag:
    def __get__(self,instance,owner):
        return instance._rsa_public_key_tag
    
    def __set__(self,instance,value):
        instance._rsa_public_key_tag = value
    
    def __delete__(self,instance):
        del instance._rsa_public_key_tag

class RSAPublicKeyFP:
    def __get__(self,instance,owner):
        return instance._rsa_public_key_fp
    
    def __set__(self,instance,value):
        instance._rsa_public_key_fp = value
    
    def __delete__(self,instance):
        del instance._rsa_public_key_fp

class RSAPublicKeyFPTag:
    def __get__(self,instance,owner):
        return instance._rsa_public_key_fp_tag
    
    def __set__(self,instance,value):
        instance._rsa_public_key_fp_tag = value
    
    def __delete__(self,instance):
        del instance._rsa_public_key_fp_tag

class RSAPublicKey2:
    def __get__(self,instance,owner):
        return instance._rsa_public_key_2
    
    def __set__(self,instance,value):
        instance._rsa_public_key_2 = value
    
    def __delete__(self,instance):
        del instance._rsa_public_key_2

class RSAPublicKey2Tag:
    def __get__(self,instance,owner):
        return instance._rsa_public_key_2_tag
    
    def __set__(self,instance,value):
        instance._rsa_public_key_2_tag = value
    
    def __delete__(self,instance):
        del instance._rsa_public_key_2_tag

class RSAPublicKey2FP:
    def __get__(self,instance,owner):
        return instance._rsa_public_key_2_fp
    
    def __set__(self,instance,value):
        instance._rsa_public_key_2_fp = value
    
    def __delete__(self,instance):
        del instance._rsa_public_key_2_fp

class RSAPublicKey2FPTag:
    def __get__(self,instance,owner):
        return instance._rsa_public_key_2_fp_tag
    
    def __set__(self,instance,value):
        instance._rsa_public_key_2_fp_tag = value
    
    def __delete__(self,instance):
        del instance._rsa_public_key_2_fp_tag

class Type:
    def __get__(self,instance,owner):
        return instance._type
    
    def __set__(self,instance,value):
        if value not in gv._allowed_values_type: #'PERSON','SERVICE','LEGACY_SERVICE','NULL'
            raise TypeError
        else:
            instance._type = value
    
    def __delete__(self,instance):
        del instance._type

class TypeTag:
    def __get__(self,instance,owner):
        return instance._type_tag
    
    def __set__(self,instance,value):
        instance._type_tag = value
    
    def __delete__(self,instance):
        del instance._type_tag

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = value
    
    def __delete__(self,instance):
        del instance._comment

class CommentTag:
    def __get__(self,instance,owner):
        return instance._comment_tag
    
    def __set__(self,instance,value):
        instance._comment_tag = value
    
    def __delete__(self,instance):
        del instance._comment_tag

class EnableUnredactedQuerySyntaxError:
    def __get__(self,instance,owner):
        return instance._enable_unredacted_query_syntax_error
    
    def __set__(self,instance,value):
        if vv.is_bool(value):
            instance._enable_unredacted_query_syntax_error = value
        else:
            raise ValueError
            
    
    def __delete__(self,instance):
        del instance._enable_unredacted_query_syntax_error

class EnableUnredactedQuerySyntaxErrorTag:
    def __get__(self,instance,owner):
        return instance._enable_unredacted_query_syntax_error_tag
    
    def __set__(self,instance,value):
        instance._enable_unredacted_query_syntax_error_tag = value
    
    def __delete__(self,instance):
        del instance._enable_unredacted_query_syntax_error_tag

class UserAttrs:
    def __init__(self,parent):
        self.parent = parent

    name = Name()
    name_tag = NameTag()

    password = Password()
    password_tag = PasswordTag()

    login_name = LoginName()
    login_name_tag = LoginNameTag()

    display_name = DisplayName()
    display_name_tag = DisplayNameTag()

    first_name = FirstName()
    first_name_tag = FirstNameTag()

    middle_name = MiddleName()
    middle_name_tag = MiddleNameTag()
    
    last_name = LastName()
    last_name_tag = LastNameTag()

    email = Email()
    email_tag = EmailTag()

    must_change_password = MustChangePassword()
    must_change_password_tag = MustChangePasswordTag()

    disabled = Disabled()
    disabled_tag = DisabledTag()

    days_to_expiry = DaysToExpiry()
    days_to_expiry_tag = DaysToExpiryTag()

    mins_to_unlock = MinsToUnlock()
    mins_to_unlock_tag = MinsToUnlockTag()

    default_warehouse = DefaultWarehouse()
    default_warehouse_tag = DefaultWarehouseTag()

    default_role = DefaultRole()
    default_role_tag = DefaultRoleTag()

    default_secondary_roles = DefaultSecondaryRoles()
    default_secondary_roles_tag = DefaultSecondaryRolesTag()

    mins_to_by_pass_mfa = MinsToByPassMFA()
    mins_to_by_pass_mfa_tag = MinsToByPassMFATag()

    rsa_public_key = RSAPublicKey()
    rsa_public_key_tag = RSAPublicKeyTag()

    rsa_public_key_fp = RSAPublicKeyFP()
    rsa_public_key_fp_tag = RSAPublicKeyFPTag()

    rsa_public_key_2 = RSAPublicKey2()
    rsa_public_key_2_tag = RSAPublicKey2Tag()

    rsa_public_key_2_fp = RSAPublicKey2FP()
    rsa_public_key_2_fp_tag = RSAPublicKey2FPTag()

    type = Type()
    type_tag = TypeTag()

    comment = Comment()
    comment_tag = CommentTag()

    enable_unredacted_query_syntax_error = EnableUnredactedQuerySyntaxError()
    enable_unredacted_query_syntax_error_tag = EnableUnredactedQuerySyntaxErrorTag()

class User:
    def __init__(self,session,user_id):
        self.attr = UserAttrs(self)
        self.session = session
        self.qry = ""
        self.user_id = user_id

    def set_name(self, value):
        self.attr.name = value

    def set_name_tag(self, value):
        self.attr.name_tag = value

    def set_password(self, value):
        self.attr.password = value

    def set_password_tag(self, value):
        self.attr.password_tag = value

    def set_login_name(self, value):
        self.attr.login_name = value

    def set_login_name_tag(self, value):
        self.attr.login_name_tag = value

    def set_display_name(self, value):
        self.attr.display_name = value

    def set_display_name_tag(self, value):
        self.attr.display_name_tag = value

    def set_first_name(self, value):
        self.attr.first_name = value

    def set_first_name_tag(self, value):
        self.attr.first_name_tag = value

    def set_last_name(self, value):
        self.attr.last_name = value

    def set_last_name_tag(self, value):
        self.attr.last_name_tag = value

    def set_email(self, value):
        self.attr.email = value

    def set_email_tag(self, value):
        self.attr.email_tag = value

    def set_must_change_password(self, value):
        self.attr.must_change_password = value

    def set_must_change_password_tag(self, value):
        self.attr.must_change_password_tag = value

    def set_disabled(self, value):
        self.attr.disabled = value

    def set_disabled_tag(self, value):
        self.attr.disabled_tag = value

    def set_days_to_expiry(self, value):
        self.attr.days_to_expiry = value

    def set_days_to_expiry_tag(self, value):
        self.attr.days_to_expiry_tag = value

    def set_mins_to_unlock(self, value):
        self.attr.mins_to_unlock = value

    def set_mins_to_unlock_tag(self, value):
        self.attr.mins_to_unlock_tag = value

    def set_default_warehouse(self, value):
        self.attr.default_warehouse = value

    def set_default_warehouse_tag(self, value):
        self.attr.default_warehouse_tag = value

    def set_default_role(self, value):
        self.attr.default_role = value

    def set_default_role_tag(self, value):
        self.attr.default_role_tag = value

    def set_default_secondary_roles(self, value):
        self.attr.default_secondary_roles = value

    def set_default_secondary_roles_tag(self, value):
        self.attr.default_secondary_roles_tag = value

    def set_mins_to_by_pass_mfa(self, value):
        self.attr.mins_to_by_pass_mfa = value

    def set_mins_to_by_pass_mfa_tag(self, value):
        self.attr.mins_to_by_pass_mfa_tag = value

    def set_rsa_public_key(self, value):
        self.attr.rsa_public_key = value

    def set_rsa_public_key_tag(self, value):
        self.attr.rsa_public_key_tag = value

    def set_rsa_public_key_fp(self, value):
        self.attr.rsa_public_key_fp = value

    def set_rsa_public_key_fp_tag(self, value):
        self.attr.rsa_public_key_fp_tag = value

    def set_rsa_public_key_2(self, value):
        self.attr.rsa_public_key_2 = value

    def set_rsa_public_key_2_tag(self, value):
        self.attr.rsa_public_key_2_tag = value

    def set_rsa_public_key_2_fp(self, value):
        self.attr.rsa_public_key_2_fp = value

    def set_rsa_public_key_2_fp_tag(self, value):
        self.attr.rsa_public_key_2_fp_tag = value

    def set_type(self, value):
        self.attr.type = value

    def set_type_tag(self, value):
        self.attr.type_tag = value

    def set_comment(self, value):
        self.attr.comment = value

    def set_comment_tag(self, value):
        self.attr.comment_tag = value

    def set_enable_unredacted_query_syntax_error(self, value):
        self.attr.enable_unredacted_query_syntax_error = value

    def set_enable_unredacted_query_syntax_error_tag(self, value):
        self.attr.enable_unredacted_query_syntax_error_tag = value



    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv._name_tag,"_name")
        set_flag(gv._password_tag,"_password")
        set_flag(gv._login_name_tag,"_login_name")
        set_flag(gv._display_name_tag,"_display_name")
        set_flag(gv._first_name_tag,"_first_name")
        set_flag(gv._last_name_tag,"_last_name")
        set_flag(gv._email_tag,"_email")
        set_flag(gv._must_change_password_tag,"_must_change_password")
        set_flag(gv._disabled_tag,"_disabled")
        set_flag(gv._days_to_expiry_tag,"_days_to_expiry_tag")
        set_flag(gv._mins_to_unlock_tag,"_mins_to_unlock")
        set_flag(gv._default_warehouse_tag,"_default_warehouse")
        set_flag(gv._default_role_tag,"_default_role")
        set_flag(gv._default_secondary_roles_tag,"_default_secondary_roles")
        set_flag(gv._mins_to_by_pass_mfa_tag,"_mins_to_by_pass_mfa")
        set_flag(gv._rsa_public_key_tag,"_rsa_public_key")
        set_flag(gv._rsa_public_key_fp_tag,"_rsa_public_key_fp")
        set_flag(gv._rsa_public_key_2_tag,"_rsa_public_key_2")
        set_flag(gv._rsa_public_key_2_fp_tag,"_rsa_public_key_2_fp")
        set_flag(gv._type_tag,"_type")
        set_flag(gv._comment_tag,"_comment")
        set_flag(gv._enable_unredacted_query_syntax_error_tag,"_enable_unredacted_query_syntax_error")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"CREATE USER {self.attr.name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gv._name_tag:
                    self.qry = f" {self.qry} {self.attr.name_tag}  = {self.attr.name} "
                if prop == gv._password_tag:
                    self.qry = f" {self.qry} {self.attr.password_tag} = {self.attr.password} "
                if prop == gv._display_name_tag:
                    self.qry = f" {self.qry} {self.attr.display_name_tag} = {self.attr.display_name} "
                if prop == gv._first_name_tag:
                    self.qry = f" {self.qry} {self.attr.first_name_tag} = {self.attr.first_name} "
                if prop == gv._last_name_tag:
                    self.qry = f" {self.qry} {self.attr.last_name_tag} = {self.attr.last_name} "
                if prop == gv._email_tag:
                    self.qry = f" {self.qry} {self.attr.email_tag} = {self.attr.email} "
                if prop == gv._must_change_password_tag:
                    self.qry = f" {self.qry} {self.attr.must_change_password_tag} = {self.attr.must_change_password} "
                if prop == gv._disabled_tag:
                    self.qry = f" {self.qry} {self.attr.disabled_tag} = {self.attr.disabled} "
                if prop == gv._days_to_expiry_tag:
                    self.qry = f" {self.qry} {self.attr.days_to_expiry_tag} = {self.attr.days_to_expiry} "
                if prop == gv._mins_to_unlock_tag:
                    self.qry = f" {self.qry} {self.attr.mins_to_unlock_tag} = {self.attr.mins_to_unlock} "
                if prop == gv._default_warehouse_tag:
                    self.qry = f" {self.qry} {self.attr.default_warehouse_tag} = {self.attr.default_warehouse} "
                if prop == gv._default_role_tag:
                    self.qry = f" {self.qry} {self.attr.default_role_tag} = {self.attr.default_role} "
                if prop == gv._default_secondary_roles_tag:
                    self.qry = f" {self.qry} {self.attr.default_secondary_roles_tag} = {self.attr.default_secondary_roles} "
                if prop == gv._mins_to_by_pass_mfa_tag:
                    self.qry = f" {self.qry} {self.attr.mins_to_by_pass_mfa_tag} = {self.attr.mins_to_by_pass_mfa} "
                if prop == gv._rsa_public_key_tag:
                    self.qry = f" {self.qry} {self.attr.rsa_public_key_tag} = {self.attr.rsa_public_key} "
                if prop == gv._rsa_public_key_fp_tag:
                    self.qry = f" {self.qry} {self.attr.rsa_public_key_fp_tag} = {self.attr.rsa_public_key_fp} "
                if prop == gv._rsa_public_key_2_tag:
                    self.qry = f" {self.qry} {self.attr.rsa_public_key_2_tag} = {self.attr.rsa_public_key_2} "
                if prop == gv._rsa_public_key_2_fp_tag:
                    self.qry = f" {self.qry} {self.attr.rsa_public_key_2_fp_tag} = {self.attr.rsa_public_key_2_fp} "
                if prop == gv._type_tag:
                    self.qry = f" {self.qry} {self.attr.type_tag} = {self.attr.type} "
                if prop == gv._comment_tag:
                    self.qry = f" {self.qry} {self.attr.comment_tag} = {self.attr.comment} "
                if prop == gv._enable_unredacted_query_syntax_error_tag:
                    self.qry = f" {self.qry} {self.attr.enable_unredacted_query_syntax_error_tag} = {self.attr.enable_unredacted_query_syntax_error} "


    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()

    def create_user(self):
        self.session.sql(self.qry)


    def create_object(self,**kwargs):

        self.set_name(kwargs[gv._name_tag])
        self.set_name_tag(gv._name_tag)

        self.set_password(kwargs[gv._password_tag])
        self.set_password_tag(gv._password_tag)

        self.set_login_name(kwargs[gv._login_name_tag])
        self.set_login_name_tag(gv._login_name_tag)

        self.set_display_name(kwargs[gv._display_name_tag])
        self.set_display_name_tag(gv._display_name_tag)

        self.set_first_name(kwargs[gv._first_name_tag])
        self.set_first_name_tag(gv._first_name_tag)

        self.set_last_name(kwargs[gv._last_name_tag])
        self.set_last_name_tag(gv._last_name_tag)

        self.set_email(kwargs[gv._email_tag])
        self.set_email_tag(gv._email_tag)

        self.set_must_change_password(kwargs[gv._must_change_password_tag])
        self.set_must_change_password_tag(gv._must_change_password_tag)

        self.set_disabled(kwargs[gv._disabled_tag])
        self.set_disabled_tag(gv._disabled_tag)

        self.set_days_to_expiry(kwargs[gv._days_to_expiry_tag])
        self.set_days_to_expiry_tag(gv._days_to_expiry_tag)

        self.set_mins_to_unlock(kwargs[gv._mins_to_unlock_tag])
        self.set_mins_to_unlock_tag(gv._mins_to_unlock_tag)

        self.set_default_warehouse(kwargs[gv._default_warehouse_tag])
        self.set_default_warehouse_tag(gv._default_warehouse_tag)


        self.set_default_role(kwargs[gv._default_role_tag])
        self.set_default_role_tag(gv._default_role_tag)

        self.set_default_secondary_roles(kwargs[gv._default_secondary_roles_tag])
        self.set_default_secondary_roles_tag(gv._default_secondary_roles_tag)

        self.set_mins_to_by_pass_mfa(kwargs[gv._mins_to_by_pass_mfa_tag])
        self.set_mins_to_by_pass_mfa_tag(gv._mins_to_by_pass_mfa_tag)

        self.set_rsa_public_key(kwargs[gv._rsa_public_key_tag])
        self.set_rsa_public_key_tag(gv._rsa_public_key_tag)

        self.set_rsa_public_key_fp(kwargs[gv._rsa_public_key_fp_tag])
        self.set_rsa_public_key_fp_tag(gv._rsa_public_key_fp_tag)

        self.set_rsa_public_key_2(kwargs[gv._rsa_public_key_2_tag])
        self.set_rsa_public_key_2_tag(gv._rsa_public_key_2_tag)

        self.set_rsa_public_key_2_fp(kwargs[gv._rsa_public_key_2_fp_tag])
        self.set_rsa_public_key_2_fp_tag(gv._rsa_public_key_2_fp_tag)

        self.set_type(kwargs[gv._type_tag])
        self.set_type_tag(gv._type_tag)

        self.set_comment(kwargs[gv._comment_tag])
        self.set_comment_tag(gv._comment_tag)

        self.set_enable_unredacted_query_syntax_error(kwargs[gv._enable_unredacted_query_syntax_error_tag])
        self.set_enable_unredacted_query_syntax_error_tag(gv._enable_unredacted_query_syntax_error_tag)

        self.prepare_query()
        self.create_user()
        self.create_deployment_entry()

    def create_deployment_entry(self):
        deploy_inst = Deploy(self.session)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database('NA')
        deploy_inst.set_object_schema('NA')
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()
