import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.networkpolicy.gvnetworkpolicy import NetworkPolicyTag as tags
from src.validation.validateobject import ValidateObject as vo
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
            vo.is_new_object(
                session=instance.parent.session,
                object_type=instance.parent.__class__.__name__,
                object_name=name
            )
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
                vo.object_exist(
                    session=instance.parent.session,
                    object_type=instance.parent.__class__.__name__,
                    object_name=old_name
                )
                vo.is_new_object(
                    session=instance.parent.session,
                    object_type=instance.parent.__class__.__name__,
                    object_name=new_name
                )
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to


class AllowedNetworkRuleList:
    def __get__(self, instance, owner):
        return instance._allowed_network_rule_list
    def __set__(self, instance, value):
        vv.required_attribute_check(value=instance._allowed_network_rule_database,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name="AllowedNetworkRuleDatabase")
        vv.required_attribute_check(value=instance._allowed_network_rule_schema,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name="AllowedNetworkRuleSchema")
        
        vv.is_list(value=value,
                   object_type=instance.parent.__class__.__name__,
                   attr_name=self.__class__.__name__)

        vo.object_exist(session=instance.parent.session,
                        object_type='NETWORK RULE',
                        object_name=rules,
                        kwargs={
                            "DATABASE":instance._allowed_network_rule_database,
                            "SCHEMA":instance._allowed_network_rule_schema
                        })
        instance._allowed_network_rule_list = value

    def __delete__(self, instance):
        del instance._allowed_network_rule_list

class BlockedNetworkRuleList:
    def __get__(self, instance, owner):
        return instance._blocked_network_rule_list
    def __set__(self, instance, value):
        if value=="NONE":
            instance._blocked_network_rule_list="NONE"
        else:
            vv.is_list(value=value,
                    object_type=instance.parent.__class__.__name__,
                    attr_name=self.__class__.__name__)
            
            for rules in value:
                vo.object_exist(session=instance.parent.session,
                                object_type='NETWORK RULE',
                                object_name=rules,
                                kwargs={"DATABASE":instance._allowed_network_rule_database})
            instance._blocked_network_rule_list = value

    def __delete__(self, instance):
        del instance._blocked_network_rule_list

class AllowedIPList:
    def __get__(self, instance, owner):
        return instance._allowed_ip_list
    def __set__(self, instance, value):
        if value=="NONE":
            instance._allowed_ip_list="NONE"
        else:
            vo.operation_on_object_not_suppported("Recommendation is to configure Network Rule with ALLOWED_NETWORK_RULE_LIST instead of setting this in network policy.")

    def __delete__(self, instance):
        del instance._allowed_ip_list

class BlockedIPList:
    def __get__(self, instance, owner):
        return instance._blocked_ip_list
    def __set__(self, instance, value):
        if value=="NONE":
            instance._blocked_ip_list="NONE"
        else:
            vo.operation_on_object_not_suppported("Recommendation is to configure Network Rule with BLOCKED_NETWORK_RULE_LIST instead of setting this in network policy.")

    def __delete__(self, instance):
        del instance._blocked_ip_list

class AllowedNetworkRuleDatabase:
    def __get__(self, instance, owner):
        return instance._allowed_network_rule_database
    def __set__(self, instance, value):
        vo.database_exist(session=instance.parent.session,
                            database_name=value)
        instance._allowed_network_rule_database = value
    def __delete__(self, instance):
        del instance._allowed_network_rule_database

class AllowedNetworkRuleSchema:
    def __get__(self, instance, owner):
        return instance._allowed_network_rule_schema
    
    def __set__(self, instance, value):
        vo.schema_exist(session=instance.parent.session,
                        database_name=instance._allowed_network_rule_database,
                        schema_name=value)
        instance._allowed_network_rule_schema = value

    def __delete__(self, instance):
        del instance._allowed_network_rule_schema

class BlockedNetworkRuleSchema:
    def __get__(self, instance, owner):
        return instance._blocked_network_rule_schema
    
    def __set__(self, instance, value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vo.schema_exist(session=instance.parent.session,
                        database_name=instance._blocked_network_rule_database,
                        schema_name=value)
        instance._blocked_network_rule_schema = value

    def __delete__(self, instance):
        del instance._allowed_network_rule_schema

class BlockedNetworkRuleDatabase:
    def __get__(self, instance, owner):
        return instance._blocked_network_rule_database
    def __set__(self, instance, value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vo.database_exist(session=instance.parent.session,
                            database_name=value)
        instance._blocked_network_rule_database = value
    def __delete__(self, instance):
        del instance._blocked_network_rule_database


class NetworkPolicyAttrs:
    def __init__(self,parent):
        self.parent=parent
    name = Name()
    allowed_network_rule_database=AllowedNetworkRuleDatabase()
    allowed_network_rule_schema=AllowedNetworkRuleSchema()
    blocked_network_rule_database=BlockedNetworkRuleDatabase()
    blocked_network_rule_schema=BlockedNetworkRuleSchema()
    allowed_network_rule_list = AllowedNetworkRuleList()
    blocked_network_rule_list = BlockedNetworkRuleList()
    allowed_ip_list = AllowedIPList()
    blocked_ip_list = BlockedIPList()


class NetworkPolicy(BaseObject):
    def __init__(self, session, user_id, logger):
        self.logger = logger.getChild(self.__class__.__name__)
        super().__init__(session=session,user_id=user_id,logger=logger,database_required=False,schema_required=False)
        self.attr = NetworkPolicyAttrs(self)


    # setter methods
    def set_name(self, val=None):
        self.attr.name = val

    def set_allowed_network_rule_list(self, val=None):
        self.attr.allowed_network_rule_list = val
    def set_blocked_network_rule_list(self, val=None):
        self.attr.blocked_network_rule_list = val

    def set_allowed_network_rule_database(self,val):
        self.attr.allowed_network_rule_database=val

    def set_allowed_network_rule_schema(self,val):
        self.attr.allowed_network_rule_schema=val

    def set_blocked_network_rule_database(self,val):
        self.attr.blocked_network_rule_database=val

    def set_blocked_network_rule_schema(self,val):
        self.attr.blocked_network_rule_schema=val

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

        set_flag(tags.ALLOWED_NETWORK_RULE_DATABASE , "allowed_network_rule_database")
        set_flag(tags.ALLOWED_NETWORK_RULE_SCHEMA,"allowed_network_rule_schema")
        set_flag(tags.BLOCKED_NETWORK_RULE_DATABASE,"blocked_network_rule_database")
        set_flag(tags.BLOCKED_NETWORK_RULE_SCHEMA,"blocked_network_rule_schema")
        set_flag(tags.ALLOWED_NETWORK_RULE_LIST, "allowed_network_rule_list")
        set_flag(tags.BLOCKED_NETWORK_RULE_LIST, "blocked_network_rule_list")
        set_flag(tags.ALLOWED_IP_LIST, "allowed_ip_list")
        set_flag(tags.BLOCKED_IP_LIST, "blocked_ip_list")
        set_flag(tags.COMMENT, "comment")

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

    def alter_object(self):
        for prop in self.property_lst:
            if prop == tags.ALLOWED_NETWORK_RULE_LIST:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} SET {tags.ALLOWED_NETWORK_RULE_LIST} = {self.attr.allowed_network_rule_list}"
                self.execute_final_query()
            if prop == tags.BLOCKED_NETWORK_RULE_LIST:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} SET {tags.BLOCKED_NETWORK_RULE_LIST} = {self.attr.blocked_network_rule_list}"
                self.execute_final_query()
            if prop == tags.ALLOWED_IP_LIST:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} SET {tags.ALLOWED_IP_LIST} = {self.attr.allowed_ip_list}"
                self.execute_final_query()
            if prop == tags.BLOCKED_IP_LIST:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} SET {tags.BLOCKED_IP_LIST} = {self.attr.blocked_ip_list}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER NETWORK POLICY {self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
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

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=NetworkPolicy(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.set_base_attributes(kwargs=kwargs)

        obj_inst.logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        obj_inst.logger.info("set allowed_network_rule_list")
        if tags.ALLOWED_NETWORK_RULE_LIST in kwargs.keys():
            obj_inst.set_allowed_network_rule_list(kwargs[tags.ALLOWED_NETWORK_RULE_LIST])
        else:
            obj_inst.set_allowed_network_rule_list('NONE')

        obj_inst.logger.info("set blocked_network_rule_list")
        if tags.BLOCKED_NETWORK_RULE_LIST in kwargs.keys():
            obj_inst.set_blocked_network_rule_list(kwargs[tags.BLOCKED_NETWORK_RULE_LIST])
        else:
            obj_inst.set_blocked_network_rule_list('NONE')

        obj_inst.logger.info("set allowed_ip_list")
        if tags.ALLOWED_IP_LIST in kwargs.keys():
            obj_inst.set_allowed_ip_list(kwargs[tags.ALLOWED_IP_LIST])
        else:
            obj_inst.set_allowed_ip_list('NONE')

        obj_inst.logger.info("set blocked_ip_list")
        if tags.BLOCKED_IP_LIST in kwargs.keys():
            obj_inst.set_blocked_ip_list(kwargs[tags.BLOCKED_IP_LIST])
        else:
            obj_inst.set_blocked_ip_list('NONE')


        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.write_file_to_git(object_name=obj_inst.attr.name[0],
                                   object_type=obj_inst.__class__.__name__,
                                   object_database=obj_inst.attr.database,
                                   object_schema=obj_inst.attr.schema)
        
        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                           object_identifier=obj_inst.attr.name[0],
                                           qry=obj_inst.qry)


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()

