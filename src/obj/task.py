import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../setup'))


from vars.gvobject import Task as gvtask,Config as cfg,Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy
from validation.validateobject import ValidateObject as vo
from setup import privilege
from .baseobj import BaseObject 
from vars.obj.task.gvtask import TaskTag as tags

class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.database_exist(session=instance.parent.session, database_name=value)
        instance._database = value

    def __delete__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.schema_exist(session=instance.parent.session,database_name=instance._database,schema_name=value)
        instance._schema = value

    def __delete__(self,instance):
        del instance._schema

class Name:   
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)
    
    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_object(session=instance.parent.session,
                             object_type=instance.parent.__class__.__name__,
                             object_name=name)
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
                vo.object_exist(session=instance.parent.session,
                                object_type=instance.parent.__class__.__name__,
                                object_name=old_name)
                vo.is_new_object(session=instance.parent.session,
                                object_type=instance.parent.__class__.__name__,
                                object_name=new_name)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"


    def __del__(self,instance):
        del instance._name
        del instance._rename_to


class Sql:
    def __get__(self,instance,owner):
        return instance._sql
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._sql = value

    def __delete__(self,instance):
        del instance._sql


class Warehouse:
    def __get__(self,instance,owner):
        return instance._warehouse
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._warehouse=value
        else:
            vo.warehouse_exist(session=instance.parent.session, warehouse_name=value)
            instance._warehouse = value

    def __delete__(self,instance):
        del instance._warehouse

class UserTaskManagedInitialWarehouseSize:
    def __get__(self,instance,owner):
        return instance._user_task_managed_initial_warehouse_size
    
    def __set__(self,instance,value):
        if instance._warehouse == 'NONE':
            instance._user_task_managed_initial_warehouse_size = 'MEDIUM'
        else:
            if value == 'NONE':
                instance._user_task_managed_initial_warehouse_size = 'NONE'
            else:
                vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                instance._user_task_managed_initial_warehouse_size = value

    def __delete__(self,instance):
        del instance._user_task_managed_initial_warehouse_size


class Schedule:
    def __get__(self,instance,owner):
        return instance._schedule    
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._schedule = value
        else:
            ret,type,num=vv.is_valid_schedule(schedule=value,object_name=instance.parent.__class__.__name__,attribute_name=self.__class__.__name__)
            if ret:
                if type=='CRON':
                    vv.is_valid_cron(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                    instance._schedule = f"'{value}'"
                else:
                    vv.is_positive_number(value=int(num),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                    if type=='SECOND':
                        vv.is_between(value=int(num),num1=tags.min_allowed_value().get(tags.SCHEDULE[tags.SECONDS]),num2=tags.max_allowed_value().get(tags.SCHEDULE[tags.SECONDS]),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                        instance._schedule=f"'{value}'"
                    elif type=='MINUTE':
                        vv.is_between(value=int(num),num1=tags.min_allowed_value().get(tags.SCHEDULE[tags.MINUTE]), num2 = tags.max_allowed_value().get(tags.SCHEDULE[tags.MINUTE]), object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                        instance._schedule=f"'{value}'"
                    elif type=='HOUR':
                        vv.is_between(value=int(num),num1=tags.min_allowed_value().get(tags.SCHEDULE[tags.HOUR]), num2 = tags.max_allowed_value().get(tags.SCHEDULE[tags.HOUR]), object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                        instance._schedule=f"'{value}'"

    def __delete__(self,instance):
        del instance._schedule


class Config:
    def __get__(self,instance,owner):
        return instance._config
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._config = value
        else:
            vv.is_json(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._config = value
    
    def __delete__(self,instance):
        del instance._config


class AllowOverlappingExecution:
    def __get__(self,instance,owner):
        return instance._allow_overlapping_execution
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._allow_overlapping_execution = value
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._allow_overlapping_execution = value
    
    def __delete__(self,instance):
        del instance._allow_overlapping_execution


class UserTaskTimeoutMs:
    def __get__(self,instance,owner):
        return instance._user_task_timeout_ms
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._user_task_timeout_ms = value
        else:
            vv.is_positive_number(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_between(value=value,num1=tags.min_allowed_value().get(tags.USER_TASK_TIMEOUT_MS), num2 = tags.max_allowed_value().get(tags.USER_TASK_TIMEOUT_MS) , object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._user_task_timeout_ms = value
    
    def __delete__(self,instance):
        del instance._user_task_timeout_ms

class SuspendTaskAfterNumFailures:
    def __get__(self,instance,owner):
        return instance._suspend_task_after_num_failures
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._suspend_task_after_num_failures = value
        else:
            vv.is_positive_number(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._suspend_task_after_num_failures = value
    
    def __delete__(self,instance):
        del instance._suspend_task_after_num_failures

class ErrorIntegration:
    def __get__(self,instance,owner):
        return instance._error_integration
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._error_integration = value
        else:
            vo.integration_exist(session=instance.parent.session,integration_name=value)
            instance._error_integration = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._error_integration


class SuccessIntegration:
    def __get__(self,instance,owner):
        return instance._success_integration
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._success_integration = value
        else:
            vo.integration_exist(session=instance.parent.session,integration_name=value)
            instance._success_integration = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._success_integration

class LogLevel:
    def __get__(self,instance,owner):
        return instance._log_level
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._log_level = value
        else:
            vv.is_allowed_value(tags.allowed_value_list().get(tags.LOG_LEVEL) , object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._log_level = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._log_level

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._comment = value
        else:
            instance._comment = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._comment


class After:
    def __get__(self,instance,owner):
        return instance._after
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._after = value
        else:
            vo.task_exist(session=instance.parent.session,database=instance._database,schema=instance._schema,task=value)
            instance._after = value
    
    def __delete__(self,instance):
        del instance._after


class When:
    def __get__(self,instance,owner):
        return instance._when
    
    def __set__(self,instance,value):
        instance._when="NONE"
    
    def __delete__(self,instance):
        del instance._when


class Tag:
    def __get__(self,instance,owner):
        return instance._tag
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._tag = value
        else:
            instance._tag = value
    
    def __delete__(self,instance):
        del instance._tag


class Finalize:
    def __get__(self,instance,owner):
        return instance._finalize
    
    def __set__(self,instance,value):
        instance._finalize="NONE"
    
    def __delete__(self,instance):
        del instance._finalize

class TaskAutoRetryAttempts:
    def __get__(self,instance,owner):
        return instance._task_auto_retry_attempts
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._task_auto_retry_attempts = value
        else:
            vv.is_between(value=value, num1 = tags.min_allowed_value().get(tags.TASK_AUTO_RETRY_ATTEMPTS) ,num2 = tags.max_allowed_value().get(tags.TASK_AUTO_RETRY_ATTEMPTS) , object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._task_auto_retry_attempts = value
    
    def __delete__(self,instance):
        del instance._task_auto_retry_attempts

class UserTaskMinimumTriggerIntervalInSeconds:
    def __get__(self,instance,owner):
        return instance._user_task_minimum_trigger_interval_in_seconds
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._user_task_minimum_trigger_interval_in_seconds = value
        else:
            vv.is_between(value=value, num1 = tags.min_allowed_value().get(tags.USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS) , num2 = tags.max_allowed_value().get(tags.USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS) , object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._user_task_minimum_trigger_interval_in_seconds = value
    
    def __delete__(self,instance):
        del instance._user_task_minimum_trigger_interval_in_seconds

class TargetCompletionInterval:
    def __get__(self,instance,owner):
        return instance._target_completion_interval
    
    def __set__(self,instance,value):
        object_type=instance.parent.__class__.__name__
        attr_name=self.__class__.__name__
        if value == 'NONE':
            instance._target_completion_interval = value
        else:
            if instance._user_task_managed_initial_warehouse_size!="NONE":
                ret,type,num=vv.is_valid_schedule(schedule=value,object_name=instance.parent.__class__.__name__,attribute_name=self.__class__.__name__)
                if ret:
                    vv.is_positive_number(value=int(num),object_type=object_type,attr_name=attr_name)
                    if type=='SECOND':
                        vv.is_between(value=int(num), num1 = tags.min_allowed_value().get(tags.TARGET_COMPLETION_INTERVAL[tags.SECONDS]) , num2 = tags.allowed_value_list().get(tags.TARGET_COMPLETION_INTERVAL[tags.SECONDS]) , object_type=object_type,attr_name=attr_name)
                    elif type=='MINUTE':
                        vv.is_between(value=int(num), num1 = tags.min_allowed_value().get(tags.TARGET_COMPLETION_INTERVAL[tags.MINUTE]) , num2 = tags.max_allowed_value().get(tags.TARGET_COMPLETION_INTERVAL[tags.MINUTE]) , object_type=object_type,attr_name=attr_name)
                    elif type=='HOUR':
                        vv.is_between(value=int(num), num1 = tags.min_allowed_value().get(tags.TARGET_COMPLETION_INTERVAL[tags.HOUR]) , num2 = tags.max_allowed_value().get(tags.TARGET_COMPLETION_INTERVAL[tags.HOUR]) , object_type=object_type,attr_name=attr_name)
                    instance._target_completion_interval = f"'{value}'"
            else:
                vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f"for tasks with dedicated warehouse.Only needed for serverless tasks")

    def __delete__(self,instance):
        del instance._target_completion_interval

class ServerlessTaskMinStatementSize:

    def __get__(self,instance,owner):
        return instance._serverless_task_min_statement_size
    
    def __set__(self,instance,value):
        object_type=instance.parent.__class__.__name__
        attr_name=self.__class__.__name__
        if value == 'NONE':
            instance._serverless_task_min_statement_size = value
        else:
            if instance._user_task_managed_initial_warehouse_size!="NONE":
                vv.is_allowed_value(value=value, allowed_list=tags.allowed_value_list().get(tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE) ,object_type=object_type,attr_name=attr_name)
                index_user_task_managed_initial_warehouse_size = tags.allowed_value_list().get(tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE).index(instance._user_task_managed_initial_warehouse_size)
                index_serverless_task_min_statement_size = tags.allowed_value_list().get(tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE).index(value)
                vv.is_between(value=index_serverless_task_min_statement_size,num1=0,num2=index_user_task_managed_initial_warehouse_size,object_type=object_type,attr_name=attr_name,kwargs={"Serverless_Task_Min_Statement_Size":"must be smaller than User_Task_Managed_Initial_Warehouse_Size"})
                instance._serverless_task_min_statement_size=value
            elif instance._user_task_managed_initial_warehouse_size=="NONE":
                vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f"for tasks with dedicated warehouse.Only needed for serverless tasks")


    def __delete__(self,instance):
        del instance._serverless_task_min_statement_size


class ServerlessTaskMaxStatementSize:
    def __get__(self,instance,owner):
        return instance._serverless_task_max_statement_size
    
    def __set__(self,instance,value):
        object_type=instance.parent.__class__.__name__
        attr_name=self.__class__.__name__
        if value == 'NONE':
            instance._serverless_task_max_statement_size = value
        else:
            if instance._user_task_managed_initial_warehouse_size!="NONE":
                vv.is_allowed_value(value=value, allowed_list=tags.allowed_value_list().get(tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE),object_type=object_type,attr_name=attr_name)
                index_user_task_managed_initial_warehouse_size = tags.allowed_value_list().get(tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE).index(instance._user_task_managed_initial_warehouse_size)
                index_serverless_task_min_statement_size = tags.allowed_value_list().get(tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE).index(instance._serverless_task_min_statement_size)
                index_serverless_task_max_statement_size = tags.allowed_value_list().get(tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE).index(value)
                vv.is_between(value=index_serverless_task_min_statement_size,num1=0,num2=index_serverless_task_max_statement_size,object_type=object_type,attr_name=attr_name,kwargs={"Serverless_Task_Max_Statement_Size":"must be greater than or equal to Serverless_Task_Min_Statement_Size"})
                vv.is_between(value=index_user_task_managed_initial_warehouse_size,num1=0,num2=index_serverless_task_max_statement_size,object_type=object_type,attr_name=attr_name,kwargs={"Serverless_Task_Max_Statement_Size":"must be greater than or equal to USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE"})
                instance._serverless_task_max_statement_size=value
            elif instance._user_task_managed_initial_warehouse_size=="NONE":
                vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f"for tasks with dedicated warehouse.Only needed for serverless tasks")

    
    def __delete__(self,instance):
        del instance._serverless_task_max_statement_size


class TaskAttrs:
    def __init__(self,parent):
        self.parent = parent

    database = Database()
    schema = Schema()
    name = Name()
    definition=Sql()
    warehouse = Warehouse()
    user_task_managed_initial_warehouse_size = UserTaskManagedInitialWarehouseSize()
    schedule = Schedule()
    config = Config()
    allow_overlapping_execution = AllowOverlappingExecution()
    user_task_timeout_ms = UserTaskTimeoutMs()
    suspend_task_after_num_failures = SuspendTaskAfterNumFailures()
    error_integration = ErrorIntegration()
    success_integration = SuccessIntegration()
    comment = Comment()
    after = After()
    when = When()
    tag = Tag()
    finalize = Finalize()
    task_auto_retry_attempts = TaskAutoRetryAttempts()
    user_task_minimum_trigger_interval_in_seconds = UserTaskMinimumTriggerIntervalInSeconds()
    target_completion_interval = TargetCompletionInterval()
    serverless_task_min_statement_size = ServerlessTaskMinStatementSize()
    serverless_task_max_statement_size = ServerlessTaskMaxStatementSize()

class Task(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session, user_id, logger)
        self.attr = TaskAttrs(self)


    def set_database(self,value):
        self.attr.database = value

    def set_schema(self,value):
        self.attr.schema = value

    def set_name(self,name):
        self.attr.name = name

    def set_definition(self,definition):
        self.attr.definition = definition 

    def set_database(self,database):
        self.attr.database = database

    def set_warehouse(self,warehouse):
        self.attr.warehouse = warehouse

    def set_user_task_managed_initial_warehouse_size(self,user_task_managed_initial_warehouse_size):
        self.attr.user_task_managed_initial_warehouse_size = user_task_managed_initial_warehouse_size

    def set_schedule(self,schedule):
        self.attr.schedule = schedule

    def set_config(self,config):
        self.attr.config = config

    def set_allow_overlapping_execution(self,allow_overlapping_execution):
        self.attr.allow_overlapping_execution = allow_overlapping_execution

    def set_user_task_timeout_ms(self,user_task_timeout_ms):
        self.attr.user_task_timeout_ms = user_task_timeout_ms

    def set_suspend_task_after_num_failures(self,suspend_task_after_num_failures):
        self.attr.suspend_task_after_num_failures = suspend_task_after_num_failures

    def set_error_integration(self,error_integration):
        self.attr.error_integration = error_integration

    def set_success_integration(self,success_integration):
        self.attr.success_integration = success_integration

    def set_comment(self,comment):
        self.attr.comment = comment

    def set_after(self,after):
        self.attr.after = after

    def set_when(self,when):
        self.attr.when = when

    def set_tag(self,tag):
        self.attr.tag = tag

    def set_finalize(self,finalize):
        self.attr.finalize = finalize

    def set_task_auto_retry_attempts(self,task_auto_retry_attempts):
        self.attr.task_auto_retry_attempts = task_auto_retry_attempts

    def set_user_task_minimum_trigger_interval_in_seconds(self,user_task_minimum_trigger_interval_in_seconds):
        self.attr.user_task_minimum_trigger_interval_in_seconds = user_task_minimum_trigger_interval_in_seconds

    def set_target_completion_interval(self,target_completion_interval):
        self.attr.target_completion_interval = target_completion_interval

    def set_serverless_task_min_statement_size(self,serverless_task_min_statement_size):
        self.attr.serverless_task_min_statement_size = serverless_task_min_statement_size

    def set_serverless_task_max_statement_size(self,serverless_task_max_statement_size):
        self.attr.serverless_task_max_statement_size = serverless_task_max_statement_size

    def set_qualified_name(self):
        self.qualified_name = f"{self.attr.database}.{self.attr.schema}.{self.attr.name}"

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.WAREHOUSE,"_warehouse")
        set_flag(tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE,"_user_task_managed_initial_warehouse_size")
        set_flag(tags.SCHEDULE,"_schedule")
        set_flag(tags.CONFIG,"_config")
        set_flag(tags.ALLOW_OVERLAPPING_EXECUTION,"_allow_overlapping_execution")
        set_flag(tags.USER_TASK_TIMEOUT_MS,"_user_task_timeout_ms")
        set_flag(tags.SUSPEND_TASK_AFTER_NUM_FAILURES,"_suspend_task_after_num_failures")
        set_flag(tags.ERROR_INTEGRATION,"_error_integration")
        set_flag(tags.SUCCESS_INTEGRATION,"_success_integration")
        set_flag(tags.COMMENT,"_comment")
        set_flag(tags.AFTER,"_after")
        set_flag(tags.WHEN,"_when")
        set_flag(tags.FINALIZE,"_finalize")
        set_flag(tags.TASK_AUTO_RETRY_ATTEMPTS,"_task_auto_retry_attempts")
        set_flag(tags.USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS,"_user_task_minimum_trigger_interval_in_seconds")
        set_flag(tags.TARGET_COMPLETION_INTERVAL,"_target_completion_interval")
        set_flag(tags.SERVERLESS_TASK_MIN_STATEMENT_SIZE,"_serverless_task_min_statement_size")
        set_flag(tags.SERVERLESS_TASK_MAX_STATEMENT_SIZE,"_serverless_task_max_statement_size")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_qry(self):
        self.qry = f"CREATE TASK {self.attr.database}.{self.attr.schema}.{self.attr.name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.WAREHOUSE:
                    self.qry = f" {self.qry} {tags.WAREHOUSE} = {self.attr.warehouse} "
                if prop == tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE:
                    self.qry = f" {self.qry} {tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE } = {self.attr.user_task_managed_initial_warehouse_size} "
                if prop == tags.SCHEDULE:
                    self.qry = f" {self.qry} {tags.SCHEDULE} = {self.attr.schedule} "
                if prop == tags.CONFIG:
                    self.qry = f" {self.qry} {tags.CONFIG} = {self.attr.config} "
                if prop == tags.ALLOW_OVERLAPPING_EXECUTION:
                    self.qry = f" {self.qry} {tags.ALLOW_OVERLAPPING_EXECUTION} = {self.attr.allow_overlapping_execution} "
                if prop == tags.USER_TASK_TIMEOUT_MS:
                    self.qry = f" {self.qry} {tags.USER_TASK_TIMEOUT_MS} = {self.attr.user_task_timeout_ms} "
                if prop == tags.SUSPEND_TASK_AFTER_NUM_FAILURES:
                    self.qry = f" {self.qry} {tags.SUSPEND_TASK_AFTER_NUM_FAILURES} = {self.attr.suspend_task_after_num_failures} "
                if prop == tags.ERROR_INTEGRATION:
                    self.qry = f" {self.qry} {tags.ERROR_INTEGRATION} = {self.attr.error_integration} "
                if prop == tags.SUCCESS_INTEGRATION:
                    self.qry = f" {self.qry} {tags.SUCCESS_INTEGRATION} = {self.attr.success_integration} "
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "
                if prop == tags.AFTER:
                    self.qry = f" {self.qry} {tags.AFTER} = {self.attr.after} "
                if prop == tags.WHEN:
                    self.qry = f" {self.qry} {tags.WHEN} = {self.attr.when} "
                if prop == tags.FINALIZE:
                    self.qry = f" {self.qry} {tags.FINALIZE} = {self.attr.finalize} "
                if prop == tags.TASK_AUTO_RETRY_ATTEMPTS:
                    self.qry = f" {self.qry} {tags.TASK_AUTO_RETRY_ATTEMPTS} = {self.attr.task_auto_retry_attempts} "
                if prop == tags.USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS:
                    self.qry = f" {self.qry} {tags.USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS} = {self.attr.user_task_minimum_trigger_interval_in_seconds} "
                if prop == tags.TARGET_COMPLETION_INTERVAL:
                    self.qry = f" {self.qry} {tags.TARGET_COMPLETION_INTERVAL} = {self.attr.target_completion_interval} "
                if prop == tags.SERVERLESS_TASK_MIN_STATEMENT_SIZE:
                    self.qry = f" {self.qry} {tags.SERVERLESS_TASK_MIN_STATEMENT_SIZE} = {self.attr.serverless_task_min_statement_size} "
                if prop == tags.SERVERLESS_TASK_MIN_STATEMENT_SIZE:
                    self.qry = f" {self.qry} {tags.SERVERLESS_TASK_MIN_STATEMENT_SIZE} = {self.attr.serverless_task_min_statement_size} "

        self.qry = self.qry + f" AS  {self.attr.definition} "    

    def alter_object(self):
        for prop in self.property_lst:
            if prop == tags.WAREHOUSE:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.WAREHOUSE} = {self.attr.warehouse}"
                self.execute_final_query()
            if prop == tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE} = {self.attr.user_task_managed_initial_warehouse_size}"
                self.execute_final_query()
            if prop == tags.SCHEDULE:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.SCHEDULE} = {self.attr.schedule}"
                self.execute_final_query()
            if prop == tags.CONFIG:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.CONFIG} = {self.attr.config}"
                self.execute_final_query()
            if prop == tags.ALLOW_OVERLAPPING_EXECUTION:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.ALLOW_OVERLAPPING_EXECUTION} = {self.attr.allow_overlapping_execution}"
                self.execute_final_query()
            if prop == tags.USER_TASK_TIMEOUT_MS:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.USER_TASK_TIMEOUT_MS} = {self.attr.user_task_timeout_ms}"
                self.execute_final_query()
            if prop == tags.SUSPEND_TASK_AFTER_NUM_FAILURES:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.SUSPEND_TASK_AFTER_NUM_FAILURES} = {self.attr.suspend_task_after_num_failures}"
                self.execute_final_query()
            if prop == tags.ERROR_INTEGRATION:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.ERROR_INTEGRATION} = {self.attr.error_integration}"
                self.execute_final_query()
            if prop == tags.SUCCESS_INTEGRATION:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.SUCCESS_INTEGRATION} = {self.attr.success_integration}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()
            if prop == tags.AFTER:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.AFTER} = {self.attr.after}"
                self.execute_final_query()
            if prop == tags.AFTER:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.AFTER} = {self.attr.after}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER {self.__class__.__name__}.upper() {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming {self.__class__.__name__.upper()} {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()
        

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create=="TRUE":
            self.set_create_qry()
            self.add_properties_to_query()
        elif self.is_create=="FALSE":
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()

    def create_task(self):
        self.execute_final_query()

    def create_object(self,**kwargs):
        self.logger.info(f"Operating on {self.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        self.logger.info(f'dictionary passed {kwargs}')
        self.is_create=kwargs[tags.IS_CREATE]
        self.set_database(kwargs[tags.DATABASE])
        self.set_schema(kwargs[tags.SCHEMA])
        self.set_name(kwargs[tags.NAME])
        self.set_definition(kwargs[tags.SQL])
        self.set_warehouse(kwargs[tags.WAREHOUSE])
        self.set_user_task_managed_initial_warehouse_size(kwargs[tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE])
        self.set_schedule(kwargs[tags.SCHEDULE])
        self.set_config(kwargs[tags.CONFIG])
        self.set_allow_overlapping_execution(kwargs[tags.ALLOW_OVERLAPPING_EXECUTION])
        self.set_user_task_timeout_ms(kwargs[tags.USER_TASK_TIMEOUT_MS])
        self.set_suspend_task_after_num_failures(kwargs[tags.SUSPEND_TASK_AFTER_NUM_FAILURES])
        self.set_error_integration(kwargs[tags.ERROR_INTEGRATION])
        self.set_success_integration(kwargs[tags.SUCCESS_INTEGRATION])
        self.set_comment(kwargs[tags.COMMENT])
        self.set_after(kwargs[tags.AFTER])
        self.set_when(kwargs[tags.WHEN])
        self.set_finalize(kwargs[tags.FINALIZE])
        self.set_task_auto_retry_attempts(kwargs[tags.TASK_AUTO_RETRY_ATTEMPTS])
        self.set_user_task_minimum_trigger_interval_in_seconds(kwargs[tags.USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS])
        self.set_target_completion_interval(kwargs[tags.TARGET_COMPLETION_INTERVAL])
        self.set_serverless_task_min_statement_size(kwargs[tags.SERVERLESS_TASK_MIN_STATEMENT_SIZE])
        self.set_serverless_task_max_statement_size(kwargs[tags.SERVERLESS_TASK_MAX_STATEMENT_SIZE])
        self.set_qualified_name()

        self.prepare_query()
        self.create_task()
        self.logger.info('create deployment entry')
        self.create_deployment_entry(object_name=self.attr.name[0],
                                        object_type=self.__class__.__name__,
                                        object_database=self.attr.database,
                                        object_schema=self.attr.schema)

        self.logger.info('writing file to git')
        self.write_file_to_git(object_name=self.attr.name[0],
                                object_type=self.__class__.__name__,
                                object_database=self.attr.database,
                                object_schema=self.attr.schema)
