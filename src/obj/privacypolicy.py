import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.privacypolicy.gvprivacypolicy import PrivacyPolicyTag as tags

class PrivacyPolicyName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class PrivacyPolicyBody:
    def __get__(self, instance, owner):
        return instance._body
    def __set__(self, instance, value):
        instance._body = value
    def __delete__(self, instance):
        del instance._body

class PrivacyPolicyComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = value
    def __delete__(self, instance):
        del instance._comment

class PrivacyPolicyAttrs:
    name = PrivacyPolicyName()
    body = PrivacyPolicyBody()
    comment = PrivacyPolicyComment()

class PrivacyPolicy(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = PrivacyPolicyAttrs()
        self.session = session
        self.user_id = user_id
        self.logger = logger

    # Setter methods
    def set_name(self, v): self.attr.name = v
    def set_body(self, v): self.attr.body = v
    def set_comment(self, v): self.attr.comment = v

    # Object property flags
    def set_object_properties_flag(self):
        self.flag_dic = {}
        for attr, tag in [
            ("body", tags.BODY),
            ("comment", tags.COMMENT),
        ]:
            self.flag_dic[tag] = 1 if getattr(self.attr, attr) is not None else 0

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_privacy_policy_qry(self):
        self.qry = f"CREATE PRIVACY POLICY {self.attr.name[0]} "

    def add_properties_to_query(self):
        if tags.BODY in self.property_lst:
            self.qry += f"AS () RETURNS PRIVACY_BUDGET -> {self.attr.body} "
        if tags.COMMENT in self.property_lst:
            self.qry += f"COMMENT = '{self.attr.comment}' "

    def alter_object(self):
        for prop in self.property_lst:
            self.qry = f"ALTER PRIVACY POLICY {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()
        if tags.NAME in self.property_lst:
            self.qry = f"ALTER PRIVACY POLICY {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming privacy policy {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_privacy_policy_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        self.is_create = kwargs.get(tags.IS_CREATE)
        self.set_name(kwargs.get(tags.NAME))
        self.set_body(kwargs.get(tags.BODY))
        self.set_comment(kwargs.get(tags.COMMENT))
        self.prepare_query()
        self.execute_final_query()
