
from accountglobalvars import *

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
        else:
            instance._name = value

    def __delete__(self,instance):
        del instance._name

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
        if len(value) < 2:
            raise ValueError
        if (value[0] != "'" and value[-1] != "'" ) and (value[0] != "\"" and value[-1] != "\"" ):
            raise ValueError
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
        if value not in ADMT._allowed_display_name_values: # ['PERSON','SERVICE','LEGACY_SERVICE','NULL']
            raise ValueError
        else:
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
        if value == None:
            raise KeyError
        else:
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
        if value not in ADMT._allowed_must_change_password_values: # ['TRUE','FALSE']
            raise ValueError
        else:
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
        if value not in ADMT._allowed_disabled_values: # ['TRUE','FALSE']
            raise ValueError
        else:
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
        if type(value) != int:
            raise TypeError
        else:
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
        if type(value) != int:
            raise TypeError
        else:
            instance._mins_to_unlock = value
    
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
        if value not in USRT._allowed_default_secondary_roles_values:#['ALL',{}]
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
        if type(value) != ADMT._allowed_mins_to_by_pass_mfa_type:
            raise TypeError
        else:
            instance._mins_to_by_pass_mfa = value
    
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
        if type(value) != ADMT._allowed_type_rsa_public_key:
            raise TypeError
        else:
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
        if type(value) != ADMT._allowed_type_rsa_public_key_fp:
            raise TypeError
        else:
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
        if type(value) != ADMT._allowed_type_rsa_public_key_2:
            raise TypeError
        else:
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
        if type(value) != ADMT._allowed_type_rsa_public_key_2_fp:
            raise TypeError
        else:
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
        if type(value) != ADMT._allowed_type_type: #'PERSON','SERVICE','LEGACY_SERVICE','NULL'
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
        if value not in USRT._allowed_values_enable_unredacted_query_syntax_error:# TRUE FALSE
            raise ValueError
        else:
            instance._enable_unredacted_query_syntax_error = value
    
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

    rsa_public_key_2 = RSAPublicKey2FP()
    rsa_public_key_2_tag = RSAPublicKey2FPTag()

    type = Type()
    type_tag = TypeTag()

    comment = Comment()
    comment_tag = CommentTag()

    enable_unredacted_query_syntax_error = EnableUnredactedQuerySyntaxError()
    enable_unredacted_query_syntax_error_tag = EnableUnredactedQuerySyntaxErrorTag()

class User:
    def __init__(self,session):
        self.attr = UserAttrs()
        self.session = session
        self.qry = ""

    def set_name(self,name):
        self.attr.name = name

    def set_name_tag(self,name_tag):
        self.attr.name_tag = name_tag

    def set_password(self,password):
        self.attr.password = password 

    def set_password_tag(self,password_tag):
        self.attr.password_tag = password_tag 

    def set_login_name(self,login_name):
        self.attr.login_name = login_name

    def set_login_name_tag(self,login_name_tag):
        self.attr.login_name_tag = login_name_tag


    def set_display_name(self,display_name):
        self.attr.display_name = display_name

    def set_display_name_tag(self,display_name_tag):
        self.attr.display_name_tag = display_name_tag

    def set_first_name(self,first_name):
        self.attr.first_name = first_name

    def set_first_name_tag(self,first_name_tag):
        self.attr.first_name_tag = first_name_tag

    def set_last_name(self,last_name):
        self.attr.last_name = last_name

    def set_last_name_tag(self,last_name_tag):
        self.attr.last_name_tag = last_name_tag

    def set_email(self,email):
        self.attr.email = email

    def set_email_tag(self,email_tag):
        self.attr.email_tag = email_tag

    def set_must_change_password(self,must_change_password):
        self.attr.must_change_password = must_change_password

    def set_must_change_password_tag(self,must_change_password_tag):
        self.attr.must_change_password_tag = must_change_password_tag

    def set_disabled(self,disabled):
        self.attr.disabled = disabled

    def set_disabled_tag(self,disabled_tag):
        self.attr.disabled_tag = disabled_tag

    def set_days_to_expiry(self,days_to_expiry):
        self.attr.days_to_expiry = days_to_expiry

    def set_days_to_expiry_tag(self,days_to_expiry_tag):
        self.attr.days_to_expiry_tag = days_to_expiry_tag

    def set_mins_to_unlock(self,mins_to_unlock):
        self.attr.mins_to_unlock = mins_to_unlock

    def set_mins_to_unlock_tag(self,mins_to_unlock_tag):
        self.attr.mins_to_unlock_tag = mins_to_unlock_tag

    def set_default_warehouse(self,default_warehouse):
        self.attr.default_warehouse = default_warehouse

    def set_default_warehouse_tag(self,default_warehouse_tag):
        self.attr.default_warehouse_tag = default_warehouse_tag

    def set_default_role(self,default_role):
        self.attr.default_role = default_role

    def set_default_role_tag(self,default_role_tag):
        self.attr.default_role_tag = default_role_tag

    def set_default_secondary_roles(self,default_secondary_roles):
        self.attr.default_secondary_roles = default_secondary_roles

    def set_default_secondary_roles_tag(self,default_secondary_roles_tag):
        self.attr.default_secondary_roles_tag = default_secondary_roles_tag

    def set_mins_to_by_pass_mfa(self,mins_to_by_pass_mfa):
        self.attr.mins_to_by_pass_mfa = mins_to_by_pass_mfa

    def set_mins_to_by_pass_mfa_tag(self,mins_to_by_pass_mfa_tag):
        self.attr.mins_to_by_pass_mfa_tag = mins_to_by_pass_mfa_tag

    def set_rsa_public_key(self,rsa_public_key):
        self.attr.rsa_public_key = rsa_public_key

    def set_rsa_public_key_tag(self,rsa_public_key_tag):
        self.attr.rsa_public_key_tag = rsa_public_key_tag

    def set_rsa_public_key_fp(self,rsa_public_key_fp):
        self.attr.rsa_public_key_fp = rsa_public_key_fp

    def set_rsa_public_key_fp_tag(self,rsa_public_key_fp_tag):
        self.attr.rsa_public_key_fp_tag = rsa_public_key_fp_tag

    def set_rsa_public_key_2(self,rsa_public_key_2):
        self.attr.rsa_public_key_2 = rsa_public_key_2

    def set_rsa_public_key_2_tag(self,rsa_public_key_2_tag):
        self.attr.rsa_public_key_2_tag = rsa_public_key_2_tag

    def set_rsa_public_key_2_fp(self,rsa_public_key_2_fp):
        self.attr.rsa_public_key_2_fp = rsa_public_key_2_fp

    def set_rsa_public_key_2_fp_tag(self,rsa_public_key_2_fp_tag):
        self.attr.rsa_public_key_2_fp_tag = rsa_public_key_2_fp_tag

    def set_type(self,type):
        self.attr.type = type

    def set_type_tag(self,type_tag):
        self.attr.type_tag = type_tag

    def set_comment(self,comment):
        self.attr.comment = comment

    def set_comment_tag(self,comment_tag):
        self.attr.comment_tag = comment_tag

    def set_enable_unredacted_query_syntax_error(self,enable_unredacted_query_syntax_error):
        self.attr.enable_unredacted_query_syntax_error = enable_unredacted_query_syntax_error

    def set_enable_unredacted_query_syntax_error_tag(self,enable_unredacted_query_syntax_error_tag):
        self.attr.enable_unredacted_query_syntax_error_tag = enable_unredacted_query_syntax_error_tag

    def set_object_properties_flag(self):
        self.flag_dic = {}

        if self.attr.name is not None:
            self.flag_dic[USRT._name_tag] = 1
        else:
            self.flag_dic[USRT._name_tag] = 0

        if self.attr.password is not None:
            self.flag_dic[USRT._password_tag] = 1
        else:
            self.flag_dic[USRT._password_tag] = 0

        if self.attr.login_name is not None:
            self.flag_dic[USRT._login_name_tag] = 1
        else:
            self.flag_dic[USRT._login_name_tag] = 0

        if self.attr.display_name is not None:
            self.flag_dic[USRT._display_name_tag] = 1
        else:
            self.flag_dic[USRT.__display_name_tag] = 0

        if self.attr.first_name is not None:
            self.flag_dic[USRT._first_name_tag] = 1
        else:
            self.flag_dic[USRT._first_name_tag] = 0

        if self.attr.last_name is not None:
            self.flag_dic[USRT._last_name_tag] = 1
        else:
            self.flag_dic[USRT._last_name_tag] = 0

        if self.attr.email is not None:
            self.flag_dic[USRT._email_tag] = 1
        else:
            self.flag_dic[USRT._email_tag] = 0
        
        if self.attr.must_change_password is not None:
            self.flag_dic[USRT._must_change_password_tag] = 1
        else:
            self.flag_dic[USRT._must_change_password_tag] = 0

        if self.attr.disabled is not None:
            self.flag_dic[USRT._disabled_tag] = 1
        else:
            self.flag_dic[USRT._disabled_tag] = 0

        if self.attr.days_to_expiry is not None:
            self.flag_dic[USRT._days_to_expiry_tag] = 1
        else:
            self.flag_dic[USRT._days_to_expiry_tag] = 0

        if self.attr.mins_to_unlock is not None:
            self.flag_dic[USRT._mins_to_unlock_tag] = 1
        else:
            self.flag_dic[USRT._mins_to_unlock_tag] = 0

        if self.attr.default_warehouse is not None:
            self.flag_dic[USRT._default_warehouse_tag] = 1
        else:
            self.flag_dic[USRT._default_warehouse_tag] = 0

        if self.attr.default_role is not None:
            self.flag_dic[USRT._default_role_tag] = 1
        else:
            self.flag_dic[USRT._default_role_tag] = 0

        if self.attr.default_secondary_roles is not None:
            self.flag_dic[USRT._default_secondary_roles_tag] = 1
        else:
            self.flag_dic[USRT._default_secondary_roles_tag] = 0

        if self.attr.mins_to_by_pass_mfa is not None:
            self.flag_dic[USRT._mins_to_by_pass_mfa_tag] = 1
        else:
            self.flag_dic[USRT._mins_to_by_pass_mfa_tag] = 0

        if self.attr.rsa_public_key is not None:
            self.flag_dic[USRT._rsa_public_key_tag] = 1
        else:
            self.flag_dic[USRT._rsa_public_key_tag] = 0

        if self.attr.rsa_public_key_fp is not None:
            self.flag_dic[USRT._rsa_public_key_fp_tag] = 1
        else:
            self.flag_dic[USRT._rsa_public_key_fp_tag] = 0

        if self.attr.rsa_public_key_2 is not None:
            self.flag_dic[USRT._rsa_public_key_2_tag] = 1
        else:
            self.flag_dic[USRT._rsa_public_key_2_tag] = 0

        if self.attr.rsa_public_key_2_fp is not None:
            self.flag_dic[USRT._rsa_public_key_2_fp_tag] = 1
        else:
            self.flag_dic[USRT._rsa_public_key_2_fp_tag] = 0

        if self.attr.type is not None:
            self.flag_dic[USRT._type_tag] = 1
        else:
            self.flag_dic[USRT._type_tag] = 0

        if self.attr.comment is not None:
            self.flag_dic[USRT._comment_tag] = 1
        else:
            self.flag_dic[USRT._comment_tag] = 0
            
        if self.attr.enable_unredacted_query_syntax_error is not None:
            self.flag_dic[USRT._enable_unredacted_query_syntax_error_tag] = 1
        else:
            self.flag_dic[USRT._enable_unredacted_query_syntax_error_tag] = 0

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
                if prop == USRT._name_tag:
                    self.qry = f" {self.qry} {self.attr.name_tag}  = {self.attr.name} "
                if prop == USRT._password_tag:
                    self.qry = f" {self.qry} {self.attr.password_tag} = {self.attr.password} "
                if prop == USRT._display_name_tag:
                    self.qry = f" {self.qry} {self.attr.display_name_tag} = {self.attr.display_name} "
                if prop == USRT._first_name_tag:
                    self.qry = f" {self.qry} {self.attr.first_name_tag} = {self.attr.first_name} "
                if prop == USRT._last_name_tag:
                    self.qry = f" {self.qry} {self.attr.last_name_tag} = {self.attr.last_name} "
                if prop == USRT._email_tag:
                    self.qry = f" {self.qry} {self.attr.email_tag} = {self.attr.email} "
                if prop == USRT._must_change_password_tag:
                    self.qry = f" {self.qry} {self.attr.must_change_password_tag} = {self.attr.must_change_password} "
                if prop == USRT._disabled_tag:
                    self.qry = f" {self.qry} {self.attr.disabled_tag} = {self.attr.disabled} "
                if prop == USRT._days_to_expiry_tag:
                    self.qry = f" {self.qry} {self.attr.days_to_expiry_tag} = {self.attr.days_to_expiry} "
                if prop == USRT.mins_to_unlock_tag:
                    self.qry = f" {self.qry} {self.attr.mins_to_unlock_tag} = {self.attr.mins_to_unlock} "
                if prop == USRT._default_warehouse_tag:
                    self.qry = f" {self.qry} {self.attr.default_warehouse_tag} = {self.attr.default_warehouse} "
                if prop == USRT._default_role_tag:
                    self.qry = f" {self.qry} {self.attr.default_role_tag} = {self.attr.default_role} "
                if prop == USRT._default_secondary_roles_tag:
                    self.qry = f" {self.qry} {self.attr.default_secondary_roles_tag} = {self.attr.default_secondary_roles} "
                if prop == USRT._mins_to_by_pass_mfa_tag:
                    self.qry = f" {self.qry} {self.attr.mins_to_by_pass_mfa_tag} = {self.attr.mins_to_by_pass_mfa} "
                if prop == USRT._rsa_public_key_tag:
                    self.qry = f" {self.qry} {self.attr.rsa_public_key_tag} = {self.attr.rsa_public_key} "
                if prop == USRT._rsa_public_key_fp_tag:
                    self.qry = f" {self.qry} {self.attr.rsa_public_key_fp_tag} = {self.attr.rsa_public_key_fp} "
                if prop == USRT._rsa_public_key_2_tag:
                    self.qry = f" {self.qry} {self.attr.rsa_public_key_2_tag} = {self.attr.rsa_public_key_2} "
                if prop == USRT._rsa_public_key_2_fp_tag:
                    self.qry = f" {self.qry} {self.attr.rsa_public_key_2_fp_tag} = {self.attr.rsa_public_key_2_fp} "
                if prop == USRT._type_tag:
                    self.qry = f" {self.qry} {self.attr.type_tag} = {self.attr.type} "
                if prop == USRT._comment_tag:
                    self.qry = f" {self.qry} {self.attr.comment_tag} = {self.attr.comment} "
                if prop == USRT._enable_unredacted_query_syntax_error_tag:
                    self.qry = f" {self.qry} {self.attr.enable_unredacted_query_syntax_error_tag} = {self.attr.enable_unredacted_query_syntax_error} "


    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()


def main(session,**kwargs):
    user = User()
    user_tags = USRT()

    user.set_name(kwargs[user_tags._name_tag])
    user.set_name_tag(user_tags._name_tag)

    user.set_password(kwargs[user_tags._password_tag])
    user.set_password_tag(user_tags._password_tag)

    user.set_login_name(kwargs[user_tags._login_name_tag])
    user.set_login_name_tag(user_tags._login_name_tag)

    user.set_display_name(kwargs[user_tags._display_name_tag])
    user.set_display_name_tag(user_tags._display_name_tag)

    user.set_first_name(kwargs[user_tags._first_name_tag])
    user.set_first_name_tag(user_tags._first_name_tag)

    user.set_last_name(kwargs[user_tags._last_name_tag])
    user.set_last_name_tag(user_tags._last_name_tag)

    user.set_email(kwargs[user_tags._email_tag])
    user.set_email_tag(user_tags._email_tag)

    user.set_must_change_password(kwargs[user_tags._must_change_password_tag])
    user.set_must_change_password_tag(user_tags._must_change_password_tag)

    user.set_disabled(kwargs[user_tags._disabled_tag])
    user.set_disabled_tag(user_tags._disabled_tag)

    user.set_days_to_expiry(kwargs[user_tags._days_to_expiry_tag])
    user.set_days_to_expiry_tag(user_tags._days_to_expiry_tag)

    user.set_mins_to_unlock(kwargs[user_tags._mins_to_unlock_tag])
    user.set_mins_to_unlock_tag(user_tags._mins_to_unlock_tag)

    user.set_default_warehouse(kwargs[user_tags._default_warehouse_tag])
    user.set_default_warehouse_tag(user_tags._default_warehouse_tag)


    user.set_default_role(kwargs[user_tags._default_role_tag])
    user.set_default_role_tag(user_tags._default_role_tag)

    user.set_default_secondary_roles(kwargs[user_tags._default_secondary_roles_tag])
    user.set_default_secondary_roles_tag(user_tags._default_secondary_roles_tag)

    user.set_mins_to_by_pass_mfa(kwargs[user_tags._mins_to_by_pass_mfa_tag])
    user.set_mins_to_by_pass_mfa_tag(user_tags._mins_to_by_pass_mfa_tag)

    user.set_rsa_public_key(kwargs[user_tags._rsa_public_key_tag])
    user.set_rsa_public_key_tag(user_tags._rsa_public_key_tag)

    user.set_rsa_public_key_fp(kwargs[user_tags._rsa_public_key_fp_tag])
    user.set_rsa_public_key_fp_tag(user_tags._rsa_public_key_fp_tag)

    user.set_rsa_public_key_2(kwargs[user_tags._rsa_public_key_2_tag])
    user.set_rsa_public_key_2_tag(user_tags._rsa_public_key_2_tag)

    user.set_rsa_public_key_2_fp(kwargs[user_tags._rsa_public_key_2_fp_tag])
    user.set_rsa_public_key_2_fp_tag(user_tags._rsa_public_key_2_fp_tag)

    user.set_type(kwargs[user_tags._type_tag])
    user.set_type_tag(user_tags._type_tag)

    user.set_comment(kwargs[user_tags._comment_tag])
    user.set_comment_tag(user_tags._comment_tag)

    user.set_enable_unredacted_query_syntax_error(kwargs[user_tags._enable_unredacted_query_syntax_error_tag])
    user.set_enable_unredacted_query_syntax_error_tag(user_tags._enable_unredacted_query_syntax_error_tag)

    user.prepare_query()

    return user.qry
