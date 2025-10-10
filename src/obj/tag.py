import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.tag.gvtag import TagTag as tags

class TagName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class TagAllowedValues:
    def __get__(self, instance, owner):
        return instance._allowed_values
    def __set__(self, instance, value):
        # expects list or single string
        if isinstance(value, list):
            val_list = ", ".join(f"'{v}'" for v in value)
        else:
            val_list = f"'{value}'"
        instance._allowed_values = f"ALLOWED_VALUES {val_list}"
    def __delete__(self, instance):
        del instance._allowed_values

class TagPropagate:
    def __get__(self, instance, owner):
        return instance._propagate
    def __set__(self, instance, value):
        # value expected as one of the allowed keywords:
        instance._propagate = f"PROPAGATE = {value}"
    def __delete__(self, instance):
        del instance._propagate

class TagOnConflict:
    def __get__(self, instance, owner):
        return instance._on_conflict
    def __set__(self, instance, value):
        # value might be a string literal or ALLOWED_VALUES_SEQUENCE
        instance._on_conflict = f"ON_CONFLICT = {value}"
    def __delete__(self, instance):
        del instance._on_conflict

class TagComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = f"COMMENT = '{value}'"
    def __delete__(self, instance):
        del instance._comment

class TagTagClause:
    def __get__(self, instance, owner):
        return instance._tag_clause
    def __set__(self, instance, value):
        # fallback / generic tag clause (rarely used here)
        if isinstance(value, dict):
            clause = ", ".join(f"{k} = '{v}'" for k, v in value.items())
        else:
            k, v = next(iter(value.items()))
            clause = f"{k} = '{v}'"
        instance._tag_clause = f"TAG {clause}"
    def __delete__(self, instance):
        del instance._tag_clause

class TagAttrs:
    name = TagName()
    allowed_values = TagAllowedValues()
    propagate = TagPropagate()
    on_conflict = TagOnConflict()
    comment = TagComment()
    tag_clause = TagTagClause()

class Tag(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session=session,user_id=user_id)
        self.attr = TagAttrs()

    # setter convenience methods
    def set_name(self, v): self.attr.name = v
    def set_allowed_values(self, v): self.attr.allowed_values = v
    def set_propagate(self, v): self.attr.propagate = v
    def set_on_conflict(self, v): self.attr.on_conflict = v
    def set_comment(self, v): self.attr.comment = v
    def set_tag_clause(self, v): self.attr.tag_clause = v

    def set_object_properties_flag(self):
        self.flag_dic = {}
        def set_flag(tag, attrname):
            self.flag_dic[tag] = 1 if getattr(self.attr, attrname, None) is not None else 0

        set_flag(tags.ALLOWED_VALUES, "allowed_values")
        set_flag(tags.PROPAGATE, "propagate")
        set_flag(tags.ON_CONFLICT, "on_conflict")
        set_flag(tags.COMMENT, "comment")
        set_flag(tags.TAG_CLAUSE, "tag_clause")

    def check_properties_to_set(self):
        self.property_lst = [p for p, flag in self.flag_dic.items() if flag == 1]

    def set_create_tag_qry(self):
        self.qry = "CREATE TAG"
        # optionally OR REPLACE or IF NOT EXISTS could be managed via flags (you can extend)
        self.qry += f" {self.attr.name[0]}"

    def add_properties_to_query(self):
        for prop in self.property_lst:
            if prop == tags.ALLOWED_VALUES:
                self.qry += f" {self.attr.allowed_values}"
            if prop == tags.PROPAGATE:
                self.qry += f" {self.attr.propagate}"
            if prop == tags.ON_CONFLICT:
                self.qry += f" {self.attr.on_conflict}"
            if prop == tags.COMMENT:
                self.qry += f" {self.attr.comment}"
            if prop == tags.TAG_CLAUSE:
                self.qry += f" {self.attr.tag_clause}"

    def alter_object(self):
        for prop in self.property_lst:
            # SET some property
            self.qry = f"ALTER TAG {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER TAG {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming tag {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_tag_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        self.is_create = kwargs.get(tags.IS_CREATE)
        self.set_name(kwargs.get(tags.NAME))
        self.set_allowed_values(kwargs.get(tags.ALLOWED_VALUES))
        self.set_propagate(kwargs.get(tags.PROPAGATE))
        self.set_on_conflict(kwargs.get(tags.ON_CONFLICT))
        self.set_comment(kwargs.get(tags.COMMENT))
        self.set_tag_clause(kwargs.get(tags.TAG_CLAUSE))

        self.prepare_query()
        self.execute_final_query()


class Operation:
    @staticmethod
    def create_object(session,user_id,kwargs,*largs):
        obj_inst=Tag(session=session,
                         user_id=user_id,
                        )
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        obj_inst.logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        obj_inst.logger.info("set allowed_values")
        if tags.ALLOWED_VALUES in kwargs.keys():
            obj_inst.set_allowed_values(kwargs[tags.ALLOWED_VALUES])
        else:
            obj_inst.set_allowed_values('NONE')

        obj_inst.logger.info("set propagate")
        if tags.PROPAGATE in kwargs.keys():
            obj_inst.set_propagate(kwargs[tags.PROPAGATE])
        else:
            obj_inst.set_propagate('NONE')

        obj_inst.logger.info("set on_conflict")
        if tags.ON_CONFLICT in kwargs.keys():
            obj_inst.set_on_conflict(kwargs[tags.ON_CONFLICT])
        else:
            obj_inst.set_on_conflict('NONE')

        obj_inst.logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')

        obj_inst.logger.info("set tag_clause")
        if tags.TAG_CLAUSE in kwargs.keys():
            obj_inst.set_tag_clause(kwargs[tags.TAG_CLAUSE])
        else:
            obj_inst.set_tag_clause('NONE')

        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        
        obj_inst.logger.info('execute query')
        obj_inst.execute_final_query()

        obj_inst.logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
