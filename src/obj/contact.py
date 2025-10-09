import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.contact.gvcontact import ContactTag as tags

class ContactName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class ContactUsers:
    def __get__(self, instance, owner):
        return instance._users
    def __set__(self, instance, value):
        instance._users = value
    def __delete__(self, instance):
        del instance._users

class ContactEmailDistributionList:
    def __get__(self, instance, owner):
        return instance._email_distribution_list
    def __set__(self, instance, value):
        instance._email_distribution_list = value
    def __delete__(self, instance):
        del instance._email_distribution_list

class ContactUrl:
    def __get__(self, instance, owner):
        return instance._url
    def __set__(self, instance, value):
        instance._url = value
    def __delete__(self, instance):
        del instance._url

class ContactComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = value
    def __delete__(self, instance):
        del instance._comment

class ContactAttrs:
    name = ContactName()
    users = ContactUsers()
    email_distribution_list = ContactEmailDistributionList()
    url = ContactUrl()
    comment = ContactComment()

class Contact(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = ContactAttrs()
        self.session = session
        self.user_id = user_id
        self.logger = logger

    # Setter methods
    def set_name(self, v): self.attr.name = v
    def set_users(self, v): self.attr.users = v
    def set_email_distribution_list(self, v): self.attr.email_distribution_list = v
    def set_url(self, v): self.attr.url = v
    def set_comment(self, v): self.attr.comment = v

    # Object property flags
    def set_object_properties_flag(self):
        self.flag_dic = {}
        for attr, tag in [
            ("users", tags.USERS),
            ("email_distribution_list", tags.EMAIL_DISTRIBUTION_LIST),
            ("url", tags.URL),
            ("comment", tags.COMMENT),
        ]:
            self.flag_dic[tag] = 1 if getattr(self.attr, attr) is not None else 0

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_contact_qry(self):
        self.qry = f"CREATE CONTACT {self.attr.name[0]} "

    def add_properties_to_query(self):
        if tags.USERS in self.property_lst:
            self.qry += f"USERS = ({', '.join(self.attr.users)}) "
        if tags.EMAIL_DISTRIBUTION_LIST in self.property_lst:
            self.qry += f"EMAIL_DISTRIBUTION_LIST = '{self.attr.email_distribution_list}' "
        if tags.URL in self.property_lst:
            self.qry += f"URL = '{self.attr.url}' "
        if tags.COMMENT in self.property_lst:
            self.qry += f"COMMENT = '{self.attr.comment}' "

    def alter_object(self):
        for prop in self.property_lst:
            self.qry = f"ALTER CONTACT {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()
        if tags.NAME in self.property_lst:
            self.qry = f"ALTER CONTACT {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming contact {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_contact_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        self.is_create = kwargs.get(tags.IS_CREATE)
        self.set_name(kwargs.get(tags.NAME))
        self.set_users(kwargs.get(tags.USERS))
        self.set_email_distribution_list(kwargs.get(tags.EMAIL_DISTRIBUTION_LIST))
        self.set_url(kwargs.get(tags.URL))
        self.set_comment(kwargs.get(tags.COMMENT))
        self.prepare_query()
        self.execute_final_query()
