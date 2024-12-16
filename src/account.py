
from accountglobalvars import *

class AccountNamne:
    def __get__(self,instance,owner):
        return instance._account_name
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
        else:
            instance._account_name = value

    def __delete__(self,instance):
        del instance._account_name

class AccountNameTag:
    def __get__(self,instance,owner):
        return instance._account_name_tag
    
    def __set__(self,instance,value):
        instance._account_name_tag = value

    def __delete__(self,instance):
        del instance._account_name_tag

class AdminName:
    def __get__(self,instance,owner):
        return instance._admin_name
    
    def __set__(self,instance,value):
        if value == None:
            raise KeyError
        else:
            instance._admin_name = value

    def __delete__(self,instance):
        del instance._admin_name

class AdminNameTag:
    def __get__(self,instance,owner):
        return instance._admin_name_tag
    
    def __set__(self,instance,value):
        instance._admin_name_tag = value

    def __delete__(self,instance):
        del instance._admin_name_tag

class AdminPassword:
    def __get__(self,instance,owner):
        return instance._admin_password
    
    def __set__(self,instance,value):
        if value == None:
            raise KeyError
        else:
            instance._admin_password = value

    def __delete__(self,instance):
        del instance._admin_password

class AdminPasswordTag:
    def __get__(self,instance,owner):
        return instance._admin_password_tag
    
    def __set__(self,instance,value):
        instance._admin_password_tag = value

    def __delete__(self,instance):
        del instance._admin_password_tag

class AdminUserType:
    def __get__(self,instance,owner):
        return instance._admin_user_type
    
    def __set__(self,instance,value):
        if value not in ADMT._allowed_admin_user_type_values: # ['PERSON','SERVICE','LEGACY_SERVICE','NULL']
            raise ValueError
        else:
            instance._admin_user_type = value

    def __delete__(self,instance):
        del instance._admin_user_type

class AdminUserTypeTag:
    def __get__(self,instance,owner):
        return instance._admin_user_type_tag
    
    def __set__(self,instance,value):
        instance._admin_user_type_tag = value

    def __delete__(self,instance):
        del instance._admin_user_type_tag

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

class Edition:
    def __get__(self,instance,owner):
        return instance._edition
    
    def __set__(self,instance,value):
        if value == None:
            raise KeyError
        else:
            if value not in ADMT._allowed_edition_values: # ['STANDARD','ENTERPRISE','BUSINESS_CRITICAL']
                raise ValueError
            else:
                instance._edition = value
    
    def __delete__(self,instance):
        del instance._edition

class EditionTag:
    def __get__(self,instance,owner):
        return instance._edition_tag
    
    def __set__(self,instance,value):
        instance._edition_tag = value
    
    def __delete__(self,instance):
        del instance._edition_tag

class RegionGroup:
    def __get__(self,instance,owner):
        return instance._region_group
    
    def __set__(self,instance,value):
        instance._region_group = value
    
    def __delete__(self,instance):
        del instance._region_group

class RegionGroupTag:
    def __get__(self,instance,owner):
        return instance._region_group_tag
    
    def __set__(self,instance,value):
        instance._region_group_tag = value
    
    def __delete__(self,instance):
        del instance._region_group_tag

class Region:
    def __get__(self,instance,owner):
        return instance._region
    
    def __set__(self,instance,value):
        instance._region = value
    
    def __delete__(self,instance):
        del instance._region

class RegionTag:
    def __get__(self,instance,owner):
        return instance._region_tag
    
    def __set__(self,instance,value):
        instance._region_tag = value
    
    def __delete__(self,instance):
        del instance._region_tag


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

class Polaris:
    def __get__(self,instance,owner):
        return instance._polaris
    
    def __set__(self,instance,value):
        if value not in ADMT._allowed_polaris_values: #['TRUE','FALSE']
            raise ValueError
        else:
            instance._polaris = value
    
    def __delete__(self,instance):
        del instance._polaris

class PolarisTag:
    def __get__(self,instance,owner):
        return instance._polaris_tag
    
    def __set__(self,instance,value):
        instance._polaris_tag = value
    
    def __delete__(self,instance):
        del instance._polaris_tag


class AdminAttrs:
    account_name = AccountNamne()
    account_name_tag = AccountNameTag()
    admin_name = AdminName()
    admin_name_tag = AdminNameTag()
    admin_password = AdminPassword()
    admin_password_tag = AdminPasswordTag()
    admin_user_type = AdminUserType()
    admin_user_type_tag = AdminUserTypeTag()
    first_name = FirstName()
    first_name_tag = FirstNameTag()
    last_name = LastName()
    last_name_tag = LastNameTag()
    email = Email()
    email_tag = EmailTag()
    must_change_password = MustChangePassword()
    must_change_password_tag = MustChangePasswordTag()
    edition = Edition()
    edition_tag = EditionTag()
    region_group = RegionGroup()
    region_group_tag = RegionGroupTag()
    region = Region()
    region_tag = RegionTag()
    comment = Comment()
    comment_tag = CommentTag()
    polaris = Polaris()
    polaris_tag = PolarisTag()



class Admin:
    def __init__(self,session):
        self.attr = AdminAttrs()
        self.session = session
        self.qry = ""

    def set_account_name(self,account_name):
        self.attr.account_name = account_name

    def set_account_name_tag(self,account_name_tag):
        self.attr.account_name_tag = account_name_tag

    def set_admin_name(self,admin_name):
        self.attr.admin_name = admin_name 

    def set_admin_name_tag(self,admin_name_tag):
        self.attr.admin_name_tag = admin_name_tag 

    def set_admin_password(self,admin_password):
        self.attr.admin_password = admin_password

    def set_admin_password_tag(self,admin_password_tag):
        self.attr.admin_password_tag = admin_password_tag


    def set_admin_user_type(self,admin_user_type):
        self.attr.admin_user_type = admin_user_type

    def set_admin_user_type_tag(self,admin_user_type_tag):
        self.attr.admin_user_type_tag = admin_user_type_tag

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

    def set_edition(self,edition):
        self.attr.edition = edition

    def set_edition_tag(self,edition_tag):
        self.attr.edition_tag = edition_tag

    def set_region_group(self,region_group):
        self.attr.region_group = region_group

    def set_region_group_tag(self,region_group_tag):
        self.attr.region_group_tag = region_group_tag

    def set_region(self,region):
        self.attr.region = region

    def set_region_tag(self,region_tag):
        self.attr.region_tag = region_tag

    def set_comment(self,comment):
        self.attr.comment = comment

    def set_comment_tag(self,comment_tag):
        self.attr.comment_tag = comment_tag

    def set_polaris(self,polaris):
        self.attr.polaris = polaris

    def set_polaris_tag(self,polaris_tag):
        self.attr.polaris_tag = polaris_tag


    def set_object_properties_flag(self):
        self.flag_dic = {}

        if self.attr.account_name is not None:
            self.flag_dic['account_name'] = 1
        else:
            self.flag_dic['account_name'] = 0

        if self.attr.admin_name is not None:
            self.flag_dic['admin_name'] = 1
        else:
            self.flag_dic['admin_name'] = 0

        if self.attr.admin_password is not None:
            self.flag_dic['admin_password'] = 1
        else:
            self.flag_dic['admin_password'] = 0

        if self.attr.admin_user_type is not None:
            self.flag_dic['admin_user_type'] = 1
        else:
            self.flag_dic['admin_user_type'] = 0

        if self.attr.first_name is not None:
            self.flag_dic['first_name'] = 1
        else:
            self.flag_dic['first_name'] = 0

        if self.attr.last_name is not None:
            self.flag_dic['last_name'] = 1
        else:
            self.flag_dic['last_name'] = 0

        if self.attr.email is not None:
            self.flag_dic['email'] = 1
        else:
            self.flag_dic['email'] = 0
        
        if self.attr.must_change_password is not None:
            self.flag_dic['must_change_password'] = 1
        else:
            self.flag_dic['must_change_password'] = 0

        if self.attr.edition is not None:
            self.flag_dic['edition'] = 1
        else:
            self.flag_dic['edition'] = 0

        if self.attr.region_group is not None:
            self.flag_dic['region_group'] = 1
        else:
            self.flag_dic['region_group'] = 0

        if self.attr.region is not None:
            self.flag_dic['region'] = 1
        else:
            self.flag_dic['region'] = 0

        if self.attr.comment is not None:
            self.flag_dic['comment'] = 1
        else:
            self.flag_dic['comment'] = 0

        if self.attr.polaris is not None:
            self.flag_dic['polaris'] = 1
        else:
            self.flag_dic['polaris'] = 0



    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"CREATE ACCOUNT {self.attr.account_name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == 'account_name':
                    self.qry = f" {self.qry} {self.attr.account_name_tag}  = {self.attr.account_name} "
                if prop == 'admin_name':
                    self.qry = f" {self.qry} {self.attr.admin_name_tag} = {self.attr.admin_name} "
                if prop == 'admin_user_type':
                    self.qry = f" {self.qry} {self.attr.admin_user_type_tag} = {self.attr.admin_user_type} "
                if prop == 'first_name':
                    self.qry = f" {self.qry} {self.attr.first_name_tag} = {self.attr.first_name} "
                if prop == 'last_name':
                    self.qry = f" {self.qry} {self.attr.last_name_tag} = {self.attr.last_name} "
                if prop == 'email':
                    self.qry = f" {self.qry} {self.attr.email_tag} = {self.attr.email} "
                if prop == 'must_change_password':
                    self.qry = f" {self.qry} {self.attr.must_change_password_tag} = {self.attr.must_change_password} "
                if prop == 'edition':
                    self.qry = f" {self.qry} {self.attr.edition_tag} = {self.attr.edition} "
                if prop == 'region_group':
                    self.qry = f" {self.qry} {self.attr.region_group_tag} = {self.attr.region_group} "
                if prop == 'region':
                    self.qry = f" {self.qry} {self.attr.region_tag} = {self.attr.region} "
                if prop == 'comment':
                    self.qry = f" {self.qry} {self.attr.comment_tag} = {self.attr.comment} "
                if prop == 'polaris':
                    self.qry = f" {self.qry} {self.attr.polaris_tag} = {self.attr.polaris} "


    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()


def main(session,**kwargs):
    adm = Admin()
    adm_tags = ADMT()

    adm.set_account_name(kwargs[adm_tags._account_name_tag])
    adm.set_account_name_tag(adm_tags._account_name_tag)

    adm.set_admin_name(kwargs[adm_tags._admin_name_tag])
    adm.set_admin_name_tag(adm_tags._admin_name_tag)

    adm.set_admin_password(kwargs[adm_tags._admin_password_tag])
    adm.set_admin_password_tag(adm_tags._admin_password_tag)

    adm.set_admin_user_type(kwargs[adm_tags._admin_user_type_tag])
    adm.set_admin_user_type_tag(adm_tags._admin_user_type_tag)

    adm.set_first_name(kwargs[adm_tags._first_name_tag])
    adm.set_first_name_tag(adm_tags._first_name_tag)

    adm.set_last_name(kwargs[adm_tags._last_name_tag])
    adm.set_last_name_tag(adm_tags._last_name_tag)

    adm.set_email(kwargs[adm_tags._email_tag])
    adm.set_email_tag(adm_tags._email_tag)

    adm.set_must_change_password(kwargs[adm_tags._must_change_password_tag])
    adm.set_must_change_password_tag(adm_tags._must_change_password_tag)

    adm.set_edition(kwargs[adm_tags._edition_tag])
    adm.set_edition_tag(adm_tags._edition_tag)

    adm.set_region_group(kwargs[adm_tags._region_group_tag])
    adm.set_region_group_tag(adm_tags._region_group_tag)

    adm.set_region(kwargs[adm_tags._region_tag])
    adm.set_region_tag(adm_tags._region_tag)

    adm.set_comment(kwargs[adm_tags._comment_tag])
    adm.set_comment_tag(adm_tags._comment_tag)


    adm.set_polaris(kwargs[adm_tags._polaris_tag])
    adm.set_polaris_tag(adm_tags._polaris_tag)

    adm.prepare_query()

    return adm.qry
