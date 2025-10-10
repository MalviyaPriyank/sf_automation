import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.projectionpolicy.gvprojectionpolicy import ProjectionPolicyTag as tags

class ProjectionPolicyName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class ProjectionPolicyBody:
    def __get__(self, instance, owner):
        return instance._body
    def __set__(self, instance, value):
        instance._body = value
    def __delete__(self, instance):
        del instance._body

class ProjectionPolicyComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = value
    def __delete__(self, instance):
        del instance._comment

class ProjectionPolicyAttrs:
    name = ProjectionPolicyName()
    body = ProjectionPolicyBody()
    comment = ProjectionPolicyComment()

class ProjectionPolicy(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session=session,user_id=user_id)
        self.attr = ProjectionPolicyAttrs()


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

    def set_create_projection_policy_qry(self):
        self.qry = f"CREATE PROJECTION POLICY {self.attr.name[0]} "

    def add_properties_to_query(self):
        if tags.BODY in self.property_lst:
            self.qry += f"AS () RETURNS PROJECTION_CONSTRAINT -> {self.attr.body} "
        if tags.COMMENT in self.property_lst:
            self.qry += f"COMMENT = '{self.attr.comment}' "

    def alter_object(self):
        for prop in self.property_lst:
            self.qry = f"ALTER PROJECTION POLICY {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()
        if tags.NAME in self.property_lst:
            self.qry = f"ALTER PROJECTION POLICY {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming projection policy {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_projection_policy_qry()
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


class Operation:
    @staticmethod
    def create_object(session,user_id,kwargs,*largs):
        obj_inst=ProjectionPolicy(session=session,
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

        obj_inst.logger.info("set body")
        if tags.BODY in kwargs.keys():
            obj_inst.set_body(kwargs[tags.BODY])
        else:
            obj_inst.set_body('NONE')

        obj_inst.logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')

        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        
        obj_inst.logger.info('execute query')
        obj_inst.execute_final_query()

        obj_inst.logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
