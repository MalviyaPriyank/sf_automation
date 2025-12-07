import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.contact.gvcontact import ContactTag as tags
from src.validation.validatevalue import ValidateValue as vv
from src.validation.validateobject import ValidateObject as vo
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

class Users:
    def __get__(self, instance, owner):
        return instance._users
    def __set__(self, instance, value):
        if value=="NONE":
            instance._users="NONE"
        elif isinstance(value,list) and len(value):
            instance.parent.logger.info("Value received as list")
            val_string=""
            for i in range(0,len(value)):
                instance.parent.logger.info(f"Validating {value[i]} user")
                vo.object_exist(session=instance.parent.session,
                                object_type="USER",
                                object_name=value[i])
                if i != len(value)-1:
                    val_string=val_string+f"'{value[i]}',"
                elif i == len(value)-1:
                    val_string=val_string+f"'{value[i]}'"
            instance.parent.logger.info(f" final value string : {val_string}")
            instance._users=f"({val_string})"
        elif isinstance(value,str):
            vo.object_exist(session=instance.parent.session,
                                object_type="USER",
                                object_name=value)
            instance._users=f"('{value}')"

    def __delete__(self, instance):
        del instance._users

class EmailDistributionList:
    def __get__(self, instance, owner):
        return instance._email_distribution_list
    def __set__(self, instance, value):
        if value=="NONE":
            instance._email_distribution_list="NONE"
        else:
            if instance._users != "NONE":
                vo.operation_on_object_not_suppported(message="Only one of Email,Users or distribution list can be used.")
            elif instance._users=="NONE":
                vv.is_valid_email(object_type=instance.parent.__class__.__name__,
                                attribute_name=self.__class__.__name__,
                                email=value)
                instance._email_distribution_list = f"'{value}'"
    def __delete__(self, instance):
        del instance._email_distribution_list

class Url:
    def __get__(self, instance, owner):
        return instance._url
    def __set__(self, instance, value):
        if value=="NONE":
            instance._url=value
        else:
            vv.is_valid_url_for_contact(object_type=instance.parent.__class__.__name__,
                                        attr_name=self.__class__.__name__,
                                        url=value)
        instance._url = value
    def __delete__(self, instance):
        del instance._url

class ContactAttrs:
    def __init__(self,parent):
        self.parent=parent
    name = Name()
    users = Users()
    email_distribution_list = EmailDistributionList()
    url = Url()

class Contact(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session=session,user_id=user_id,logger=logger,database_required=True,schema_required=True)
        self.attr = ContactAttrs(self)
        self.logger = logger.getChild(self.__class__.__name__)

    # Setter methods
    def set_name(self, v): self.attr.name = v
    def set_users(self, v): self.attr.users = v
    def set_email_distribution_list(self, v): self.attr.email_distribution_list = v
    def set_url(self, v): self.attr.url = v

    # Object property flags
    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
        set_flag(tags.USERS,"users")
        set_flag(tags.EMAIL_DISTRIBUTION_LIST,"email_distribution_list")
        set_flag(tags.URL,"url")


    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_contact_qry(self):
        self.qry = f"CREATE CONTACT {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.USERS:
                    self.qry = f" {self.qry} {tags.USERS} = {self.attr.users} \n"
                if prop == tags.EMAIL_DISTRIBUTION_LIST:
                    self.qry = f" {self.qry} {tags.EMAIL_DISTRIBUTION_LIST} = {self.attr.email_distribution_list} \n"
                if prop == tags.URL:
                    self.qry = f" {self.qry} {tags.URL} = '{self.attr.url}' \n"
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = '{self.attr.comment}' "

    def alter_object(self):        
        for prop in self.property_lst:
            if prop == tags.USERS:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.USERS} = {self.attr.users}"
                self.execute_final_query()
            if prop == tags.EMAIL_DISTRIBUTION_LIST:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.EMAIL_DISTRIBUTION_LIST} = {self.attr.email_distribution_list}"
                self.execute_final_query()
            if prop == tags.URL:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.URL} = {self.attr.url}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.COMMENT} = '{self.attr.comment}'"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER  {self.__class__.__name__.upper()}  {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming {self.__class__.__name__} {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_contact_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=Contact(session=session,
                         user_id=user_id,
                         logger=logger)
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.set_base_attributes(kwargs=kwargs)

        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')
        obj_inst.logger.info(f"set name {obj_inst.attr.name}")

        
        if tags.USERS in kwargs.keys():
            obj_inst.set_users(kwargs[tags.USERS])
        else:
            obj_inst.set_users('NONE')
        obj_inst.logger.info(f"set users {obj_inst.attr.users}")

        
        if tags.EMAIL_DISTRIBUTION_LIST in kwargs.keys():
            obj_inst.set_email_distribution_list(kwargs[tags.EMAIL_DISTRIBUTION_LIST])
        else:
            obj_inst.set_email_distribution_list('NONE')
        obj_inst.logger.info(f"set email_distribution_list {obj_inst.attr.email_distribution_list}")

        
        if tags.URL in kwargs.keys():
            obj_inst.set_url(kwargs[tags.URL])
        else:
            obj_inst.set_url('NONE')
        obj_inst.logger.info(f"set url {obj_inst.attr.url}")

        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        obj_inst.print_query()
        
        obj_inst.logger.info('execute query')
        obj_inst.execute_final_query()

        obj_inst.logger.info('create deployment entry')
        obj_inst.create_deployment_entry()
        
        obj_inst.write_file_to_git()

        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                           object_identifier=obj_inst.attr.name[0],
                                           qry=obj_inst.qry)


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()


