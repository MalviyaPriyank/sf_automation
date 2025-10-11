import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.provisionedthroughput.gvprovisionedthroughput import ProvisionedThroughputTag as tags

class PTName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class PTCloudProvider:
    def __get__(self, instance, owner):
        return instance._cloud_provider
    def __set__(self, instance, value):
        instance._cloud_provider = value
    def __delete__(self, instance):
        del instance._cloud_provider

class PTModel:
    def __get__(self, instance, owner):
        return instance._model
    def __set__(self, instance, value):
        instance._model = value
    def __delete__(self, instance):
        del instance._model

class PTPtus:
    def __get__(self, instance, owner):
        return instance._ptus
    def __set__(self, instance, value):
        instance._ptus = value
    def __delete__(self, instance):
        del instance._ptus

class PTTermStart:
    def __get__(self, instance, owner):
        return instance._term_start
    def __set__(self, instance, value):
        instance._term_start = value
    def __delete__(self, instance):
        del instance._term_start

class PTTermEnd:
    def __get__(self, instance, owner):
        return instance._term_end
    def __set__(self, instance, value):
        instance._term_end = value
    def __delete__(self, instance):
        del instance._term_end

class PTComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = value
    def __delete__(self, instance):
        del instance._comment

class PTTagClause:
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

class ProvisionedThroughputAttrs:
    name = PTName()
    cloud_provider = PTCloudProvider()
    model = PTModel()
    ptus = PTPtus()
    term_start = PTTermStart()
    term_end = PTTermEnd()
    comment = PTComment()
    tag_clause = PTTagClause()

class ProvisionedThroughput(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = ProvisionedThroughputAttrs()
        self.session = session
        self.user_id = user_id
        self.logger = logger

    # setter methods
    def set_name(self, v): self.attr.name = v
    def set_cloud_provider(self, v): self.attr.cloud_provider = v
    def set_model(self, v): self.attr.model = v
    def set_ptus(self, v): self.attr.ptus = v
    def set_term_start(self, v): self.attr.term_start = v
    def set_term_end(self, v): self.attr.term_end = v
    def set_comment(self, v): self.attr.comment = v
    def set_tag_clause(self, v): self.attr.tag_clause = v

    def set_object_properties_flag(self):
        self.flag_dic = {}
        def set_flag(tag, attrname):
            self.flag_dic[tag] = 1 if getattr(self.attr, attrname, None) is not None else 0

        set_flag(tags.CLOUD_PROVIDER, "cloud_provider")
        set_flag(tags.MODEL, "model")
        set_flag(tags.PTUS, "ptus")
        set_flag(tags.TERM_START, "term_start")
        set_flag(tags.TERM_END, "term_end")
        set_flag(tags.COMMENT, "comment")
        set_flag(tags.TAG_CLAUSE, "tag_clause")

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_provisionedthroughput_qry(self):
        self.qry = f"CREATE PROVISIONED THROUGHPUT {self.attr.name[0]} "

    def add_properties_to_query(self):
        if tags.CLOUD_PROVIDER in self.property_lst:
            self.qry += f"CLOUD_PROVIDER = '{self.attr.cloud_provider}' "
        if tags.MODEL in self.property_lst:
            self.qry += f"MODEL = '{self.attr.model}' "
        if tags.PTUS in self.property_lst:
            self.qry += f"PTUS = {self.attr.ptus} "
        if tags.TERM_START in self.property_lst:
            self.qry += f"TERM_START = '{self.attr.term_start}' "
        if tags.TERM_END in self.property_lst:
            self.qry += f"TERM_END = '{self.attr.term_end}' "
        if tags.COMMENT in self.property_lst:
            self.qry += f"COMMENT = '{self.attr.comment}' "
        if tags.TAG_CLAUSE in self.property_lst:
            self.qry += f"{self.attr.tag_clause} "

    def alter_object(self):
        for prop in self.property_lst:
            self.qry = f"ALTER PROVISIONED THROUGHPUT {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER PROVISIONED THROUGHPUT {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming provisioned throughput {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_provisionedthroughput_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        self.is_create = kwargs.get(tags.IS_CREATE)
        self.set_name(kwargs.get(tags.NAME))
        self.set_cloud_provider(kwargs.get(tags.CLOUD_PROVIDER))
        self.set_model(kwargs.get(tags.MODEL))
        self.set_ptus(kwargs.get(tags.PTUS))
        self.set_term_start(kwargs.get(tags.TERM_START))
        self.set_term_end(kwargs.get(tags.TERM_END))
        self.set_comment(kwargs.get(tags.COMMENT))
        self.set_tag_clause(kwargs.get(tags.TAG_CLAUSE))

        self.prepare_query()
        self.execute_final_query()


class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        obj_inst=ProvisionedThroughput(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        logger.info("set cloud_provider")
        if tags.CLOUD_PROVIDER in kwargs.keys():
            obj_inst.set_cloud_provider(kwargs[tags.CLOUD_PROVIDER])
        else:
            obj_inst.set_cloud_provider('NONE')

        logger.info("set model")
        if tags.MODEL in kwargs.keys():
            obj_inst.set_model(kwargs[tags.MODEL])
        else:
            obj_inst.set_model('NONE')

        logger.info("set ptus")
        if tags.PTUS in kwargs.keys():
            obj_inst.set_ptus(kwargs[tags.PTUS])
        else:
            obj_inst.set_ptus('NONE')

        logger.info("set term_start")
        if tags.TERM_START in kwargs.keys():
            obj_inst.set_term_start(kwargs[tags.TERM_START])
        else:
            obj_inst.set_term_start('NONE')

        logger.info("set term_end")
        if tags.TERM_END in kwargs.keys():
            obj_inst.set_term_end(kwargs[tags.TERM_END])
        else:
            obj_inst.set_term_end('NONE')

        logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')

        logger.info("set tag_clause")
        if tags.TAG_CLAUSE in kwargs.keys():
            obj_inst.set_tag_clause(kwargs[tags.TAG_CLAUSE])
        else:
            obj_inst.set_tag_clause('NONE')

        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
