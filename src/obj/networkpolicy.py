import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.networkpolicy.gvnetworkpolicy import NetworkPolicyTag as tags

class NPName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class NPAllowedNetworkRuleList:
    def __get__(self, instance, owner):
        return instance._allowed_network_rule_list
    def __set__(self, instance, value):
        # expects list of rule names
        if isinstance(value, list):
            instance._allowed_network_rule_list = value
        else:
            instance._allowed_network_rule_list = value
    def __delete__(self, instance):
        del instance._allowed_network_rule_list

class NPBlockedNetworkRuleList:
    def __get__(self, instance, owner):
        return instance._blocked_network_rule_list
    def __set__(self, instance, value):
        if isinstance(value, list):
            instance._blocked_network_rule_list = value
        else:
            instance._blocked_network_rule_list = value
    def __delete__(self, instance):
        del instance._blocked_network_rule_list

class NPAllowedIPList:
    def __get__(self, instance, owner):
        return instance._allowed_ip_list
    def __set__(self, instance, value):
        if isinstance(value, list):
            instance._allowed_ip_list = value
        else:
            instance._allowed_ip_list = f"ALLOWED_IP_LIST = ('{value}')"
    def __delete__(self, instance):
        del instance._allowed_ip_list

class NPBlockedIPList:
    def __get__(self, instance, owner):
        return instance._blocked_ip_list
    def __set__(self, instance, value):
        if isinstance(value, list):
            instance._blocked_ip_list = value
        else:
            instance._blocked_ip_list = f"BLOCKED_IP_LIST = ('{value}')"
    def __delete__(self, instance):
        del instance._blocked_ip_list

class NPComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = f"COMMENT = '{value}'"
    def __delete__(self, instance):
        del instance._comment

class NPTagClause:
    def __get__(self, instance, owner):
        return instance._tag_clause
    def __set__(self, instance, value):
        # expects dict of tag_name: tag_value
        if isinstance(value, dict):
            clause = ", ".join(f"{k} = '{v}'" for k, v in value.items())
        else:
            # single tag: {k:v}
            k, v = next(iter(value.items()))
            clause = f"{k} = '{v}'"
        instance._tag_clause = f"TAG {clause}"
    def __delete__(self, instance):
        del instance._tag_clause

class NetworkPolicyAttrs:
    name = NPName()
    allowed_network_rule_list = NPAllowedNetworkRuleList()
    blocked_network_rule_list = NPBlockedNetworkRuleList()
    allowed_ip_list = NPAllowedIPList()
    blocked_ip_list = NPBlockedIPList()
    comment = NPComment()
    tag_clause = NPTagClause()

class NetworkPolicy(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = NetworkPolicyAttrs()
        self.session = session
        self.user_id = user_id
        self.logger = logger

    # setter methods
    def set_name(self, val=None):
        self.attr.name = val
    def set_allowed_network_rule_list(self, val=None):
        self.attr.allowed_network_rule_list = val
    def set_blocked_network_rule_list(self, val=None):
        self.attr.blocked_network_rule_list = val
    def set_allowed_ip_list(self, val=None):
        self.attr.allowed_ip_list = val
    def set_blocked_ip_list(self, val=None):
        self.attr.blocked_ip_list = val
    def set_comment(self, val=None):
        self.attr.comment = val
    def set_tag_clause(self, val=None):
        self.attr.tag_clause = val

    def set_object_properties_flag(self):
        self.flag_dic = {}
        def set_flag(tag, attrname):
            self.flag_dic[tag] = 1 if getattr(self.attr, attrname, None) is not None else 0

        set_flag(tags.ALLOWED_NETWORK_RULE_LIST, "allowed_network_rule_list")
        set_flag(tags.BLOCKED_NETWORK_RULE_LIST, "blocked_network_rule_list")
        set_flag(tags.ALLOWED_IP_LIST, "allowed_ip_list")
        set_flag(tags.BLOCKED_IP_LIST, "blocked_ip_list")
        set_flag(tags.COMMENT, "comment")
        set_flag(tags.TAG_CLAUSE, "tag_clause")

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_network_policy_qry(self):
        self.qry = f"CREATE NETWORK POLICY {self.attr.name[0]}"

    def add_properties_to_query(self):
        for prop in self.property_lst:
            if prop == tags.ALLOWED_NETWORK_RULE_LIST:
                self.qry += f" {self.attr.allowed_network_rule_list}"
            if prop == tags.BLOCKED_NETWORK_RULE_LIST:
                self.qry += f" {self.attr.blocked_network_rule_list}"
            if prop == tags.ALLOWED_IP_LIST:
                self.qry += f" {self.attr.allowed_ip_list}"
            if prop == tags.BLOCKED_IP_LIST:
                self.qry += f" {self.attr.blocked_ip_list}"
            if prop == tags.COMMENT:
                self.qry += f" {self.attr.comment}"
            if prop == tags.TAG_CLAUSE:
                self.qry += f" {self.attr.tag_clause}"

    def alter_object(self):
        for prop in self.property_lst:
            if prop in (tags.ALLOWED_NETWORK_RULE_LIST, tags.BLOCKED_NETWORK_RULE_LIST,
                        tags.ALLOWED_IP_LIST, tags.BLOCKED_IP_LIST, tags.COMMENT):
                self.qry = f"ALTER NETWORK POLICY {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
                self.execute_final_query()

            if prop == tags.TAG_CLAUSE:
                self.qry = f"ALTER NETWORK POLICY {self.attr.name[0]} SET {self.attr.tag_clause}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER NETWORK POLICY {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming network policy {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_network_policy_qry()
            self.add_properties_to_query()
        else:
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        """
        kwargs expects:
          tags.IS_CREATE : "TRUE" / "FALSE"
          tags.NAME : [name, new_name?]
          tags.ALLOWED_NETWORK_RULE_LIST : list or single
          tags.BLOCKED_NETWORK_RULE_LIST : list or single
          tags.ALLOWED_IP_LIST : list or single
          tags.BLOCKED_IP_LIST : list or single
          tags.COMMENT : comment string
          tags.TAG_CLAUSE : dict of tag: value
        """
        self.logger.info(f"Operate on {self.__class__.__name__}, create flag : {kwargs.get(tags.IS_CREATE)}")
        self.is_create = kwargs.get(tags.IS_CREATE)
        self.set_name(kwargs.get(tags.NAME))
        self.set_allowed_network_rule_list(kwargs.get(tags.ALLOWED_NETWORK_RULE_LIST))
        self.set_blocked_network_rule_list(kwargs.get(tags.BLOCKED_NETWORK_RULE_LIST))
        self.set_allowed_ip_list(kwargs.get(tags.ALLOWED_IP_LIST))
        self.set_blocked_ip_list(kwargs.get(tags.BLOCKED_IP_LIST))
        self.set_comment(kwargs.get(tags.COMMENT))
        self.set_tag_clause(kwargs.get(tags.TAG_CLAUSE))

        self.prepare_query()
        self.execute_final_query()
