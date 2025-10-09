import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.computepool.gvcomputepool import ComputePoolTag as tags

class CPName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class CPMinNodes:
    def __get__(self, instance, owner):
        return instance._min_nodes
    def __set__(self, instance, value):
        instance._min_nodes = value
    def __delete__(self, instance):
        del instance._min_nodes

class CPMaxNodes:
    def __get__(self, instance, owner):
        return instance._max_nodes
    def __set__(self, instance, value):
        instance._max_nodes = value
    def __delete__(self, instance):
        del instance._max_nodes

class CPInstanceFamily:
    def __get__(self, instance, owner):
        return instance._instance_family
    def __set__(self, instance, value):
        instance._instance_family = value
    def __delete__(self, instance):
        del instance._instance_family

class CPAutoResume:
    def __get__(self, instance, owner):
        return instance._auto_resume
    def __set__(self, instance, value):
        instance._auto_resume = value
    def __delete__(self, instance):
        del instance._auto_resume

class CPInitiallySuspended:
    def __get__(self, instance, owner):
        return instance._initially_suspended
    def __set__(self, instance, value):
        instance._initially_suspended = value
    def __delete__(self, instance):
        del instance._initially_suspended

class CPAutoSuspendSecs:
    def __get__(self, instance, owner):
        return instance._auto_suspend_secs
    def __set__(self, instance, value):
        instance._auto_suspend_secs = value
    def __delete__(self, instance):
        del instance._auto_suspend_secs

class CPComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = value
    def __delete__(self, instance):
        del instance._comment

class CPTagClause:
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

class ComputePoolAttrs:
    name = CPName()
    min_nodes = CPMinNodes()
    max_nodes = CPMaxNodes()
    instance_family = CPInstanceFamily()
    auto_resume = CPAutoResume()
    initially_suspended = CPInitiallySuspended()
    auto_suspend_secs = CPAutoSuspendSecs()
    comment = CPComment()
    tag_clause = CPTagClause()

class ComputePool(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = ComputePoolAttrs()
        self.session = session
        self.user_id = user_id
        self.logger = logger

    # setter methods
    def set_name(self, v): self.attr.name = v
    def set_min_nodes(self, v): self.attr.min_nodes = v
    def set_max_nodes(self, v): self.attr.max_nodes = v
    def set_instance_family(self, v): self.attr.instance_family = v
    def set_auto_resume(self, v): self.attr.auto_resume = v
    def set_initially_suspended(self, v): self.attr.initially_suspended = v
    def set_auto_suspend_secs(self, v): self.attr.auto_suspend_secs = v
    def set_comment(self, v): self.attr.comment = v
    def set_tag_clause(self, v): self.attr.tag_clause = v

    def set_object_properties_flag(self):
        self.flag_dic = {}
        def set_flag(tag, attrname):
            self.flag_dic[tag] = 1 if getattr(self.attr, attrname, None) is not None else 0

        set_flag(tags.MIN_NODES, "min_nodes")
        set_flag(tags.MAX_NODES, "max_nodes")
        set_flag(tags.INSTANCE_FAMILY, "instance_family")
        set_flag(tags.AUTO_RESUME, "auto_resume")
        set_flag(tags.INITIALLY_SUSPENDED, "initially_suspended")
        set_flag(tags.AUTO_SUSPEND_SECS, "auto_suspend_secs")
        set_flag(tags.COMMENT, "comment")
        set_flag(tags.TAG_CLAUSE, "tag_clause")

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_computepool_qry(self):
        self.qry = f"CREATE COMPUTE POOL {self.attr.name[0]} "

    def add_properties_to_query(self):
        if tags.MIN_NODES in self.property_lst:
            self.qry += f"MIN_NODES = {self.attr.min_nodes} "
        if tags.MAX_NODES in self.property_lst:
            self.qry += f"MAX_NODES = {self.attr.max_nodes} "
        if tags.INSTANCE_FAMILY in self.property_lst:
            self.qry += f"INSTANCE_FAMILY = {self.attr.instance_family} "
        if tags.AUTO_RESUME in self.property_lst:
            self.qry += f"AUTO_RESUME = {self.attr.auto_resume} "
        if tags.INITIALLY_SUSPENDED in self.property_lst:
            self.qry += f"INITIALLY_SUSPENDED = {self.attr.initially_suspended} "
        if tags.AUTO_SUSPEND_SECS in self.property_lst:
            self.qry += f"AUTO_SUSPEND_SECS = {self.attr.auto_suspend_secs} "
        if tags.COMMENT in self.property_lst:
            self.qry += f"COMMENT = '{self.attr.comment}' "
        if tags.TAG_CLAUSE in self.property_lst:
            self.qry += f"{self.attr.tag_clause} "

    def alter_object(self):
        for prop in self.property_lst:
            self.qry = f"ALTER COMPUTE POOL {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER COMPUTE POOL {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming compute pool {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_computepool_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        self.is_create = kwargs.get(tags.IS_CREATE)
        self.set_name(kwargs.get(tags.NAME))
        self.set_min_nodes(kwargs.get(tags.MIN_NODES))
        self.set_max_nodes(kwargs.get(tags.MAX_NODES))
        self.set_instance_family(kwargs.get(tags.INSTANCE_FAMILY))
        self.set_auto_resume(kwargs.get(tags.AUTO_RESUME))
        self.set_initially_suspended(kwargs.get(tags.INITIALLY_SUSPENDED))
        self.set_auto_suspend_secs(kwargs.get(tags.AUTO_SUSPEND_SECS))
        self.set_comment(kwargs.get(tags.COMMENT))
        self.set_tag_clause(kwargs.get(tags.TAG_CLAUSE))

        self.prepare_query()
        self.execute_final_query()
