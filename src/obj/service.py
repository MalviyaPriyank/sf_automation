import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.service.gvservice import ServiceTag as tags

class ServiceName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class ServiceComputePool:
    def __get__(self, instance, owner):
        return instance._compute_pool
    def __set__(self, instance, value):
        instance._compute_pool = value
    def __delete__(self, instance):
        del instance._compute_pool

class ServiceSpecificationFile:
    def __get__(self, instance, owner):
        return instance._specification_file
    def __set__(self, instance, value):
        instance._specification_file = value
    def __delete__(self, instance):
        del instance._specification_file

class ServiceSpecificationTemplateFile:
    def __get__(self, instance, owner):
        return instance._specification_template_file
    def __set__(self, instance, value):
        instance._specification_template_file = value
    def __delete__(self, instance):
        del instance._specification_template_file

class ServiceAutoSuspendSecs:
    def __get__(self, instance, owner):
        return instance._auto_suspend_secs
    def __set__(self, instance, value):
        instance._auto_suspend_secs = value
    def __delete__(self, instance):
        del instance._auto_suspend_secs

class ServiceExternalAccessIntegrations:
    def __get__(self, instance, owner):
        return instance._external_access_integrations
    def __set__(self, instance, value):
        instance._external_access_integrations = value
    def __delete__(self, instance):
        del instance._external_access_integrations

class ServiceAutoResume:
    def __get__(self, instance, owner):
        return instance._auto_resume
    def __set__(self, instance, value):
        instance._auto_resume = value
    def __delete__(self, instance):
        del instance._auto_resume

class ServiceMinInstances:
    def __get__(self, instance, owner):
        return instance._min_instances
    def __set__(self, instance, value):
        instance._min_instances = value
    def __delete__(self, instance):
        del instance._min_instances

class ServiceMinReadyInstances:
    def __get__(self, instance, owner):
        return instance._min_ready_instances
    def __set__(self, instance, value):
        instance._min_ready_instances = value
    def __delete__(self, instance):
        del instance._min_ready_instances

class ServiceMaxInstances:
    def __get__(self, instance, owner):
        return instance._max_instances
    def __set__(self, instance, value):
        instance._max_instances = value
    def __delete__(self, instance):
        del instance._max_instances

class ServiceLogLevel:
    def __get__(self, instance, owner):
        return instance._log_level
    def __set__(self, instance, value):
        instance._log_level = value
    def __delete__(self, instance):
        del instance._log_level

class ServiceQueryWarehouse:
    def __get__(self, instance, owner):
        return instance._query_warehouse
    def __set__(self, instance, value):
        instance._query_warehouse = value
    def __delete__(self, instance):
        del instance._query_warehouse

class ServiceTagClause:
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

class ServiceComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = value
    def __delete__(self, instance):
        del instance._comment

class ServiceAttrs:
    name = ServiceName()
    compute_pool = ServiceComputePool()
    specification_file = ServiceSpecificationFile()
    specification_template_file = ServiceSpecificationTemplateFile()
    auto_suspend_secs = ServiceAutoSuspendSecs()
    external_access_integrations = ServiceExternalAccessIntegrations()
    auto_resume = ServiceAutoResume()
    min_instances = ServiceMinInstances()
    min_ready_instances = ServiceMinReadyInstances()
    max_instances = ServiceMaxInstances()
    log_level = ServiceLogLevel()
    query_warehouse = ServiceQueryWarehouse()
    tag_clause = ServiceTagClause()
    comment = ServiceComment()

class Service(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = ServiceAttrs()
        self.session = session
        self.user_id = user_id
        self.logger = logger.getChild(self.__class__.__name__)

    # Setter methods
    def set_name(self, v): self.attr.name = v
    def set_compute_pool(self, v): self.attr.compute_pool = v
    def set_specification_file(self, v): self.attr.specification_file = v
    def set_specification_template_file(self, v): self.attr.specification_template_file = v
    def set_auto_suspend_secs(self, v): self.attr.auto_suspend_secs = v
    def set_external_access_integrations(self, v): self.attr.external_access_integrations = v
    def set_auto_resume(self, v): self.attr.auto_resume = v
    def set_min_instances(self, v): self.attr.min_instances = v
    def set_min_ready_instances(self, v): self.attr.min_ready_instances = v
    def set_max_instances(self, v): self.attr.max_instances = v
    def set_log_level(self, v): self.attr.log_level = v
    def set_query_warehouse(self, v): self.attr.query_warehouse = v
    def set_tag_clause(self, v): self.attr.tag_clause = v
    def set_comment(self, v): self.attr.comment = v

    # Object property flags
    def set_object_properties_flag(self):
        self.flag_dic = {}
        for attr, tag in [
            ("compute_pool", tags.COMPUTE_POOL),
            ("specification_file", tags.SPECIFICATION_FILE),
            ("specification_template_file", tags.SPECIFICATION_TEMPLATE_FILE),
            ("auto_suspend_secs", tags.AUTO_SUSPEND_SECS),
            ("external_access_integrations", tags.EXTERNAL_ACCESS_INTEGRATIONS),
            ("auto_resume", tags.AUTO_RESUME),
            ("min_instances", tags.MIN_INSTANCES),
            ("min_ready_instances", tags.MIN_READY_INSTANCES),
            ("max_instances", tags.MAX_INSTANCES),
            ("log_level", tags.LOG_LEVEL),
            ("query_warehouse", tags.QUERY_WAREHOUSE),
            ("tag_clause", tags.TAG_CLAUSE),
            ("comment", tags.COMMENT),
        ]:
            self.flag_dic[tag] = 1 if getattr(self.attr, attr) is not None else 0

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_service_qry(self):
        self.qry = f"CREATE SERVICE {self.attr.name[0]} "

    def add_properties_to_query(self):
        if tags.COMPUTE_POOL in self.property_lst:
            self.qry += f"IN COMPUTE POOL {self.attr.compute_pool} "
        if tags.SPECIFICATION_FILE in self.property_lst:
            self.qry += f"FROM SPECIFICATION_FILE = '{self.attr.specification_file}' "
        if tags.SPECIFICATION_TEMPLATE_FILE in self.property_lst:
            self.qry += f"FROM SPECIFICATION_TEMPLATE_FILE = '{self.attr.specification_template_file}' "
        if tags.AUTO_SUSPEND_SECS in self.property_lst:
            self.qry += f"AUTO_SUSPEND_SECS = {self.attr.auto_suspend_secs} "
        if tags.EXTERNAL_ACCESS_INTEGRATIONS in self.property_lst:
            self.qry += f"EXTERNAL_ACCESS_INTEGRATIONS = ({', '.join(self.attr.external_access_integrations)}) "
        if tags.AUTO_RESUME in self.property_lst:
            self.qry += f"AUTO_RESUME = {self.attr.auto_resume} "
        if tags.MIN_INSTANCES in self.property_lst:
            self.qry += f"MIN_INSTANCES = {self.attr.min_instances} "
        if tags.MIN_READY_INSTANCES in self.property_lst:
            self.qry += f"MIN_READY_INSTANCES = {self.attr.min_ready_instances} "
        if tags.MAX_INSTANCES in self.property_lst:
            self.qry += f"MAX_INSTANCES = {self.attr.max_instances} "
        if tags.LOG_LEVEL in self.property_lst:
            self.qry += f"LOG_LEVEL = '{self.attr.log_level}' "
        if tags.QUERY_WAREHOUSE in self.property_lst:
            self.qry += f"QUERY_WAREHOUSE = {self.attr.query_warehouse} "
        if tags.TAG_CLAUSE in self.property_lst:
            self.qry += f"{self.attr.tag_clause} "
        if tags.COMMENT in self.property_lst:
            self.qry += f"COMMENT = '{self.attr.comment}' "

    def alter_object(self):
        for prop in self.property_lst:
            self.qry = f"ALTER SERVICE {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()
        if tags.NAME in self.property_lst:
            self.qry = f"ALTER SERVICE {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming service {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_service_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        self.is_create = kwargs.get(tags.IS_CREATE)
        self.set_name(kwargs.get(tags.NAME))
        self.set_compute_pool(kwargs.get(tags.COMPUTE_POOL))
        self.set_specification_file(kwargs.get(tags.SPECIFICATION_FILE))
        self.set_specification_template_file(kwargs.get(tags.SPECIFICATION_TEMPLATE_FILE))
        self.set_auto_suspend_secs(kwargs.get(tags.AUTO_SUSPEND_SECS))
        self.set_external_access_integrations(kwargs.get(tags.EXTERNAL_ACCESS_INTEGRATIONS))
        self.set_auto_resume(kwargs.get(tags.AUTO_RESUME))
        self.set_min_instances(kwargs.get(tags.MIN_INSTANCES))
        self.set_min_ready_instances(kwargs.get(tags.MIN_READY_INSTANCES))
        self.set_max_instances(kwargs.get(tags.MAX_INSTANCES))
        self.set_log_level(kwargs.get(tags.LOG_LEVEL))
        self.set_query_warehouse(kwargs.get(tags.QUERY_WAREHOUSE))
        self.set_tag_clause(kwargs.get(tags.TAG_CLAUSE))
        self.set_comment(kwargs.get(tags.COMMENT))
        self.prepare_query()
        self.execute_final_query()


class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        obj_inst=Service(session=session,
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

        logger.info("set compute_pool")
        if tags.COMPUTE_POOL in kwargs.keys():
            obj_inst.set_compute_pool(kwargs[tags.COMPUTE_POOL])
        else:
            obj_inst.set_compute_pool('NONE')

        logger.info("set specification_file")
        if tags.SPECIFICATION_FILE in kwargs.keys():
            obj_inst.set_specification_file(kwargs[tags.SPECIFICATION_FILE])
        else:
            obj_inst.set_specification_file('NONE')

        logger.info("set specification_template_file")
        if tags.SPECIFICATION_TEMPLATE_FILE in kwargs.keys():
            obj_inst.set_specification_template_file(kwargs[tags.SPECIFICATION_TEMPLATE_FILE])
        else:
            obj_inst.set_specification_template_file('NONE')

        logger.info("set auto_suspend_secs")
        if tags.AUTO_SUSPEND_SECS in kwargs.keys():
            obj_inst.set_auto_suspend_secs(kwargs[tags.AUTO_SUSPEND_SECS])
        else:
            obj_inst.set_auto_suspend_secs('NONE')

        logger.info("set external_access_integrations")
        if tags.EXTERNAL_ACCESS_INTEGRATIONS in kwargs.keys():
            obj_inst.set_external_access_integrations(kwargs[tags.EXTERNAL_ACCESS_INTEGRATIONS])
        else:
            obj_inst.set_external_access_integrations('NONE')

        logger.info("set auto_resume")
        if tags.AUTO_RESUME in kwargs.keys():
            obj_inst.set_auto_resume(kwargs[tags.AUTO_RESUME])
        else:
            obj_inst.set_auto_resume('NONE')

        logger.info("set min_instances")
        if tags.MIN_INSTANCES in kwargs.keys():
            obj_inst.set_min_instances(kwargs[tags.MIN_INSTANCES])
        else:
            obj_inst.set_min_instances('NONE')

        logger.info("set min_ready_instances")
        if tags.MIN_READY_INSTANCES in kwargs.keys():
            obj_inst.set_min_ready_instances(kwargs[tags.MIN_READY_INSTANCES])
        else:
            obj_inst.set_min_ready_instances('NONE')

        logger.info("set max_instances")
        if tags.MAX_INSTANCES in kwargs.keys():
            obj_inst.set_max_instances(kwargs[tags.MAX_INSTANCES])
        else:
            obj_inst.set_max_instances('NONE')

        logger.info("set log_level")
        if tags.LOG_LEVEL in kwargs.keys():
            obj_inst.set_log_level(kwargs[tags.LOG_LEVEL])
        else:
            obj_inst.set_log_level('NONE')

        logger.info("set query_warehouse")
        if tags.QUERY_WAREHOUSE in kwargs.keys():
            obj_inst.set_query_warehouse(kwargs[tags.QUERY_WAREHOUSE])
        else:
            obj_inst.set_query_warehouse('NONE')

        logger.info("set tag_clause")
        if tags.TAG_CLAUSE in kwargs.keys():
            obj_inst.set_tag_clause(kwargs[tags.TAG_CLAUSE])
        else:
            obj_inst.set_tag_clause('NONE')

        logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')

        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
