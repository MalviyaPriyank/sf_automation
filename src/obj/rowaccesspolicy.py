import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.rowaccesspolicy.gvrowaccesspolicy import RowAccessPolicyTag as tags

class RAPName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class RAPSignature:
    def __get__(self, instance, owner):
        return instance._signature
    def __set__(self, instance, value):
        # value could be e.g. "(col1 VARCHAR, col2 INT)"
        instance._signature = f"({value})"
    def __delete__(self, instance):
        del instance._signature

class RAPReturns:
    def __get__(self, instance, owner):
        return instance._returns
    def __set__(self, instance, value):
        # value should be "BOOLEAN"
        instance._returns = f"RETURNS {value}"
    def __delete__(self, instance):
        del instance._returns

class RAPExpression:
    def __get__(self, instance, owner):
        return instance._expression
    def __set__(self, instance, value):
        # value should be the policy condition expression (as SQL string)
        instance._expression = value
    def __delete__(self, instance):
        del instance._expression

class RAPComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = f"COMMENT = '{value}'"
    def __delete__(self, instance):
        del instance._comment

class RAPTagClause:
    def __get__(self, instance, owner):
        return instance._tag_clause
    def __set__(self, instance, value):
        if isinstance(value, dict):
            clause = ", ".join(f"{k} = '{v}'" for k, v in value.items())
        else:
            k, v = next(iter(value.items()))
            clause = f"{k} = '{v}'"
        instance._tag_clause = f"TAG {clause}"
    def __delete__(self, instance):
        del instance._tag_clause

class RowAccessPolicyAttrs:
    name = RAPName()
    signature = RAPSignature()
    returns = RAPReturns()
    expression = RAPExpression()
    comment = RAPComment()
    tag_clause = RAPTagClause()

class RowAccessPolicy(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = RowAccessPolicyAttrs()
        self.session = session
        self.user_id = user_id
        self.logger = logger

    # setter methods
    def set_name(self, v): self.attr.name = v
    def set_signature(self, v): self.attr.signature = v
    def set_returns(self, v): self.attr.returns = v
    def set_expression(self, v): self.attr.expression = v
    def set_comment(self, v): self.attr.comment = v
    def set_tag_clause(self, v): self.attr.tag_clause = v

    def set_object_properties_flag(self):
        self.flag_dic = {}
        def set_flag(tag, attrname):
            self.flag_dic[tag] = 1 if getattr(self.attr, attrname, None) is not None else 0

        set_flag(tags.SIGNATURE, "signature")
        set_flag(tags.RETURNS, "returns")
        set_flag(tags.EXPRESSION, "expression")
        set_flag(tags.COMMENT, "comment")
        set_flag(tags.TAG_CLAUSE, "tag_clause")

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_row_access_policy_qry(self):
        self.qry = f"CREATE ROW ACCESS POLICY {self.attr.name[0]} "

    def add_properties_to_query(self):
        # must include signature, returns, expression
        if tags.SIGNATURE in self.property_lst:
            self.qry += f" AS {self.attr.signature} "
        if tags.RETURNS in self.property_lst:
            self.qry += f"{self.attr.returns} -> "
        if tags.EXPRESSION in self.property_lst:
            self.qry += f"{self.attr.expression} "
        if tags.COMMENT in self.property_lst:
            self.qry += f"{self.attr.comment} "
        if tags.TAG_CLAUSE in self.property_lst:
            self.qry += f"{self.attr.tag_clause} "

    def alter_object(self):
        # In Snowflake, often one does CREATE OR REPLACE instead of ALTER for row access policy
        # But we support altering expression, comment, tags
        for prop in self.property_lst:
            if prop == tags.EXPRESSION:
                self.qry = f"ALTER ROW ACCESS POLICY {self.attr.name[0]} SET {self.attr.expression}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER ROW ACCESS POLICY {self.attr.name[0]} SET {self.attr.comment}"
                self.execute_final_query()
            if prop == tags.TAG_CLAUSE:
                self.qry = f"ALTER ROW ACCESS POLICY {self.attr.name[0]} SET {self.attr.tag_clause}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER ROW ACCESS POLICY {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming row access policy {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_row_access_policy_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        """
        Expected kwargs:
          tags.IS_CREATE : "TRUE" / "FALSE"
          tags.NAME : [policy_name, new_name?]
          tags.SIGNATURE : e.g. "col1 VARCHAR, col2 INT"
          tags.RETURNS : "BOOLEAN"
          tags.EXPRESSION : SQL condition string
          tags.COMMENT : comment text
          tags.TAG_CLAUSE : dict of tags
        """
        self.is_create = kwargs.get(tags.IS_CREATE)
        self.set_name(kwargs.get(tags.NAME))
        self.set_signature(kwargs.get(tags.SIGNATURE))
        self.set_returns(kwargs.get(tags.RETURNS))
        self.set_expression(kwargs.get(tags.EXPRESSION))
        self.set_comment(kwargs.get(tags.COMMENT))
        self.set_tag_clause(kwargs.get(tags.TAG_CLAUSE))

        self.prepare_query()
        self.execute_final_query()


class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        obj_inst=DatabaseRole(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info("set database")
        if tags.DATABASE in kwargs.keys():
            obj_inst.set_database(kwargs[tags.DATABASE])
        else:
            obj_inst.set_database(kwargs[tags.DATABASE])

        logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name(kwargs[tags.NAME])

        logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment(kwargs[tags.COMMENT])


        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
