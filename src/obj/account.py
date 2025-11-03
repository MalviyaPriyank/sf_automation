import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))


from vars.gvobject import Account as gv
from validation.validatevalue import ValidateValue as vv



class AccountName:
    def __get__(self,instance,owner):
        return instance._account_name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if ( vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__) 
              and not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
              and not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__)
              ):
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
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__):
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
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)   
        if (
            (vv.is_enclosed_in_single_quotes(value,instance.parent.__class__.__name__,self.__class__.__name__) 
            or vv.is_enclosed_in_double_quotes(value,instance.parent.__class__.__name__,self.__class__.__name__))
            and
            (vv.is_valid_password(value,instance.parent.__class__.__name__,self.__class__.__name__))):
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
        if value not in gv._allowed_values_admin_user_type:
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
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
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
        if value not in gv._allowed_values_must_change_password:
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
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if value not in gv._allowed_values_edition: 
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
        if value not in gv._allowed_values_polaris:
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
    def __init__(self,parent):
        self.parent = parent
    account_name = AccountName()
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
    def __init__(self,session,logger):
        self.attr = AdminAttrs(self)
        self.session = session
        self.qry = ""
        self.logger = logger.getChild(self.__class__.__name__)

    def set_account_name(self, value):
        self.attr.account_name = value

    def set_account_name_tag(self, value):
        self.attr.account_name_tag = value

    def set_admin_name(self, value):
        self.attr.admin_name = value

    def set_admin_name_tag(self, value):
        self.attr.admin_name_tag = value

    def set_admin_password(self, value):
        self.attr.admin_password = value

    def set_admin_password_tag(self, value):
        self.attr.admin_password_tag = value

    def set_admin_user_type(self, value):
        self.attr.admin_user_type = value

    def set_admin_user_type_tag(self, value):
        self.attr.admin_user_type_tag = value

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

    def set_edition(self, value):
        self.attr.edition = value

    def set_edition_tag(self, value):
        self.attr.edition_tag = value

    def set_region_group(self, value):
        self.attr.region_group = value

    def set_region_group_tag(self, value):
        self.attr.region_group_tag = value

    def set_region(self, value):
        self.attr.region = value

    def set_region_tag(self, value):
        self.attr.region_tag = value

    def set_comment(self, value):
        self.attr.comment = value

    def set_comment_tag(self, value):
        self.attr.comment_tag = value

    def set_polaris(self, value):
        self.attr.polaris = value

    def set_polaris_tag(self, value):
        self.attr.polaris_tag = value



    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv._account_name_tag,"_account_name")
        set_flag(gv._admin_name_tag,"_admin_name")
        set_flag(gv._admin_password_tag,"_admin_password")
        set_flag(gv._admin_user_type_tag,"_admin_user_type")
        set_flag(gv._first_name_tag,"_first_name")
        set_flag(gv._last_name_tag,"_last_name")
        set_flag(gv._email_tag,"_email")
        set_flag(gv._must_change_password_tag,"_must_change_password")
        set_flag(gv._edition_tag,"_edition")
        set_flag(gv._region_group_tag,"_region_group")
        set_flag(gv._region_tag,"_region")
        set_flag(gv._comment_tag,"_comment")
        set_flag(gv._polaris_tag,"_polaris")

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
                if prop == gv._admin_name_tag:
                    self.qry = f" {self.qry} {self.attr.admin_name_tag} = {self.attr.admin_name} "
                if prop == gv._admin_password_tag:
                    self.qry = f" {self.qry} {self.attr.admin_password_tag} = {self.attr.admin_password} "
                if prop == gv._admin_user_type_tag:
                    self.qry = f" {self.qry} {self.attr.admin_user_type_tag} = {self.attr.admin_user_type} "
                if prop == gv._first_name_tag:
                    self.qry = f" {self.qry} {self.attr.first_name_tag} = {self.attr.first_name} "
                if prop == gv._last_name_tag:
                    self.qry = f" {self.qry} {self.attr.last_name_tag} = {self.attr.last_name} "
                if prop == gv._email_tag:
                    self.qry = f" {self.qry} {self.attr.email_tag} = {self.attr.email} "
                if prop == gv._must_change_password_tag:
                    self.qry = f" {self.qry} {self.attr.must_change_password_tag} = {self.attr.must_change_password} "
                if prop == gv._edition_tag:
                    self.qry = f" {self.qry} {self.attr.edition_tag} = {self.attr.edition} "
                if prop == gv._region_group_tag:
                    self.qry = f" {self.qry} {self.attr.region_group_tag} = {self.attr.region_group} "
                if prop == gv._region_tag:
                    self.qry = f" {self.qry} {self.attr.region_tag} = {self.attr.region} "
                if prop == gv._comment_tag:
                    self.qry = f" {self.qry} {self.attr.comment_tag} = {self.attr.comment} "
                if prop == gv._polaris_tag:
                    self.qry = f" {self.qry} {self.attr.polaris_tag} = {self.attr.polaris} "


    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()
    
    def create_account(self):
        self.session.sql(self.qry)
    
    def create_object(session,**kwargs):
        adm = Admin(session)

        adm.set_account_name(kwargs[gv._account_name_tag])
        adm.set_account_name_tag(gv._account_name_tag)

        adm.set_admin_name(kwargs[gv._admin_name_tag])
        adm.set_admin_name_tag(gv._admin_name_tag)

        adm.set_admin_password(kwargs[gv._admin_password_tag])
        adm.set_admin_password_tag(gv._admin_password_tag)

        adm.set_admin_user_type(kwargs[gv._admin_user_type_tag])
        adm.set_admin_user_type_tag(gv._admin_user_type_tag)

        adm.set_first_name(kwargs[gv._first_name_tag])
        adm.set_first_name_tag(gv._first_name_tag)

        adm.set_last_name(kwargs[gv._last_name_tag])
        adm.set_last_name_tag(gv._last_name_tag)

        adm.set_email(kwargs[gv._email_tag])
        adm.set_email_tag(gv._email_tag)

        adm.set_must_change_password(kwargs[gv._must_change_password_tag])
        adm.set_must_change_password_tag(gv._must_change_password_tag)

        adm.set_edition(kwargs[gv._edition_tag])
        adm.set_edition_tag(gv._edition_tag)

        adm.set_region_group(kwargs[gv._region_group_tag])
        adm.set_region_group_tag(gv._region_group_tag)

        adm.set_region(kwargs[gv._region_tag])
        adm.set_region_tag(gv._region_tag)

        adm.set_comment(kwargs[gv._comment_tag])
        adm.set_comment_tag(gv._comment_tag)


        adm.set_polaris(kwargs[gv._polaris_tag])
        adm.set_polaris_tag(gv._polaris_tag)

        adm.prepare_query()
        adm.create_account()
