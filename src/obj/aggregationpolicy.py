import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))
from .baseobj import BaseObject
from vars.obj.aggregationpolicy.gvaggregationpolicy import AggregationPolicyTag as tags

class AggregationPolicyName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class AggregationPolicyBody:
    def __get__(self, instance, owner):
        return instance._body
    def __set__(self, instance, value):
        instance._body = value
    def __delete__(self, instance):
        del instance._body

class AggregationPolicyComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = value
    def __delete__(self, instance):
        del instance._comment

class AggregationPolicyAttrs:
    name = AggregationPolicyName()
    body = AggregationPolicyBody()
    comment = AggregationPolicyComment()

class AggregationPolicy(BaseObject):
    def __init__(self, session, user_id):
        super().__init__(session=session,user_id=user_id)
        self.attr = AggregationPolicyAttrs()

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

    def set_create_aggregation_policy_qry(self):
        self.qry = f"CREATE AGGREGATION POLICY {self.attr.name[0]} "

    def add_properties_to_query(self):
        if tags.BODY in self.property_lst:
            self.qry += f"AS () RETURNS AGGREGATION_CONSTRAINT -> {self.attr.body} "
        if tags.COMMENT in self.property_lst:
            self.qry += f"COMMENT = '{self.attr.comment}' "

    def alter_object(self):
        for prop in self.property_lst:
            self.qry = f"ALTER AGGREGATION POLICY {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()
        if tags.NAME in self.property_lst:
            self.qry = f"ALTER AGGREGATION POLICY {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming aggregation policy {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_aggregation_policy_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

    def create_aggregation_policy(self):
        self.execute_final_query()

class Operation:
    @staticmethod
    def create_object(session,user_id,kwargs,*largs):
        agg_policy_inst=AggregationPolicy(session=session,
                         user_id=user_id,
                         )
        
        agg_policy_inst.logger.info(f"Operating on {agg_policy_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        agg_policy_inst.logger.logger.info(f'dictionary passed {kwargs}')
        agg_policy_inst.is_create=kwargs[tags.IS_CREATE]
        agg_policy_inst.logger.info('set name')
        agg_policy_inst.set_name(kwargs[tags.NAME])

        agg_policy_inst.logger.info('set BODY')
        if tags.BODY in  kwargs.keys(): 
            agg_policy_inst.set_body(kwargs[tags.BODY])
        else:
            agg_policy_inst.set_body("NONE")

        agg_policy_inst.logger.info('set comment')
        if tags.COMMENT in kwargs.keys():
            agg_policy_inst.set_comment(kwargs[tags.COMMENT])
        else:
            agg_policy_inst.set_comment("NONE")

        agg_policy_inst.logger.info('preapare query')
        agg_policy_inst.prepare_query()

        if kwargs[tags.IS_CREATE] == "TRUE":
            agg_policy_inst.logger.info('execute query')
            agg_policy_inst.create_aggregation_policy()
 
            agg_policy_inst.logger.info('create deployment entry')
            agg_policy_inst.create_deployment_entry(object_name=agg_policy_inst.attr.name[0],object_type=agg_policy_inst.__class__.__name__,object_database='NA',object_schema='NA')

            agg_policy_inst.logger.info('writing file to git')
            agg_policy_inst.write_file_to_git(object_name=agg_policy_inst.attr.name[0],object_type=agg_policy_inst.__class__.__name__,object_database='NA',object_schema='NA')

    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
