import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.gvobject import Snowpipe as gv,Config as cfg
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy
from validation.validateobject import ValidateObject as vo


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
        vo.schema_exist(instance._database,value):
        instance._schema = value

    def __delete__(self,instance):
        del instance._schema

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if ( vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__) 
              and not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
              and not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__)
            ):
            instance._name = value

    def __delete__(self,instance):
        del instance._name


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
        vo.warehouse_exist(session=instance.parent.session, warehouse_name=value)
        instance._warehouse = value

    def __delete__(self,instance):
        del instance._warehouse

class UserTaskManagedInitialWarehouseSize:
    def __get__(self,instance,owner):
        return instance._user_task_managed_initial_warehouse_size
    
    def __set__(self,instance,value):
        if instance._warehouse is None:
            instance._user_task_managed_initial_warehouse_size = 'MEDIUM'

    def __delete__(self,instance):
        del instance._user_task_managed_initial_warehouse_size


class Schedule:
    def __get__(self,instance,owner):
        return instance._schedule    
    
    def __set__(self,instance,value):
        vv.is_valid_cron(value=value,object_type=instance.parent.__class__,attr_name=self.__class__.__name__)
        instance._schedule = value

    def __delete__(self,instance):
        del instance._schedule


class Config:
    def __get__(self,instance,owner):
        return instance._config
    
    def __set__(self,instance,value):
        vv.is_json(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        instance._config = value
    
    def __delete__(self,instance):
        del instance._config


class AllowOverlappingExecution:
    def __get__(self,instance,owner):
        return instance._allow_overlapping_execution
    
    def __set__(self,instance,value):
        vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        instance._allow_overlapping_execution = value
    
    def __delete__(self,instance):
        del instance._allow_overlapping_execution


class UserTaskTimeoutMs:
    def __get__(self,instance,owner):
        return instance._user_task_timeout_ms
    
    def __set__(self,instance,value):
        vv.is_positive_number(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        vv.is_between(value=value,num1=0,num2=86400000,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        instance._user_task_timeout_ms = value
    
    def __delete__(self,instance):
        del instance._user_task_timeout_ms

class SuspendTaskAfterNumFailures:
    def __get__(self,instance,owner):
        return instance._suspend_task_after_num_failures
    
    def __set__(self,instance,value):
        vv.is_positive_number(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        instance._suspend_task_after_num_failures = value
    
    def __delete__(self,instance):
        del instance._suspend_task_after_num_failures

class ErrorIntegration:
    def __get__(self,instance,owner):
        return instance._error_integration
    
    def __set__(self,instance,value):
        instance._error_integration = value
    
    def __delete__(self,instance):
        del instance._error_integration


class SuccessIntegration:
    def __get__(self,instance,owner):
        return instance._success_integration
    
    def __set__(self,instance,value):
        instance._success_integration = value
    
    def __delete__(self,instance):
        del instance._success_integration

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = value
    
    def __delete__(self,instance):
        del instance._comment


class After:
    def __get__(self,instance,owner):
        return instance._after
    
    def __set__(self,instance,value):
        instance._after = value
    
    def __delete__(self,instance):
        del instance._after


class When:
    def __get__(self,instance,owner):
        return instance._when
    
    def __set__(self,instance,value):
        instance._when = value
    
    def __delete__(self,instance):
        del instance._when


class Tag:
    def __get__(self,instance,owner):
        return instance._tag
    
    def __set__(self,instance,value):
        instance._tag = value
    
    def __delete__(self,instance):
        del instance._tag


class Finalize:
    def __get__(self,instance,owner):
        return instance._finalize
    
    def __set__(self,instance,value):
        instance._finalize = value
    
    def __delete__(self,instance):
        del instance._finalize

class TaskAutoRetryAttempts:
    def __get__(self,instance,owner):
        return instance._task_auto_retry_attempts
    
    def __set__(self,instance,value):
        instance._task_auto_retry_attempts = value
    
    def __delete__(self,instance):
        del instance._task_auto_retry_attempts

class UserTaskMinimumTriggerIntervalInSeconds:
    def __get__(self,instance,owner):
        return instance._user_task_minimum_trigger_interval_in_seconds
    
    def __set__(self,instance,value):
        instance._user_task_minimum_trigger_interval_in_seconds = value
    
    def __delete__(self,instance):
        del instance._user_task_minimum_trigger_interval_in_seconds

class TargetCompletionInterval:
    def __get__(self,instance,owner):
        return instance._target_completion_interval
    
    def __set__(self,instance,value):
        instance._target_completion_interval = value
    
    def __delete__(self,instance):
        del instance._target_completion_interval

class ServerlessTaskMinStatementSize:
    def __get__(self,instance,owner):
        return instance._serverless_task_min_statement_size
    
    def __set__(self,instance,value):
        instance._serverless_task_min_statement_size = value
    
    def __delete__(self,instance):
        del instance._serverless_task_min_statement_size


class ServerlessTaskMaxStatementSize:
    def __get__(self,instance,owner):
        return instance._serverless_task_max_statement_size
    
    def __set__(self,instance,value):
        instance._serverless_task_max_statement_size = value
    
    def __delete__(self,instance):
        del instance._serverless_task_max_statement_size


class TaskAttrs:
    def __init__(self,parent):
        self.parent = parent

    database = Database()
    schema = Schema()
    name = Name()


    definition = Definition()
    definition_tag = DefinitionTag()

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

class Task:
    def __init__(self,session):
        self.attr = TaskAttrs(self)
        self.attr.session = session

    def set_database(self,value):
        self.attr.database = value

    def set_schema(self,value):
        self.attr.schema = value

    def set_name(self,name):
        self.attr.name = name

    def set_definition(self,definition):
        self.attr.definition = definition 

    def set_definition_tag(self,definition_tag):
        self.attr.definition_tag = definition_tag 

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

    def set_allow_overlapping_execution_tag(self,allow_overlapping_execution_tag):
        self.attr.allow_overlapping_execution_tag = allow_overlapping_execution_tag

    def set_user_task_timeout_ms(self,user_task_timeout_ms):
        self.attr.user_task_timeout_ms = user_task_timeout_ms

    def set_user_task_timeout_ms_tag(self,user_task_timeout_ms_tag):
        self.attr.user_task_timeout_ms_tag = user_task_timeout_ms_tag

    def set_suspend_task_after_num_failures(self,suspend_task_after_num_failures):
        self.attr.suspend_task_after_num_failures = suspend_task_after_num_failures

    def set_suspend_task_after_num_failures_tag(self,suspend_task_after_num_failures_tag):
        self.attr.suspend_task_after_num_failures_tag = suspend_task_after_num_failures_tag


    def set_error_integration(self,error_integration):
        self.attr.error_integration = error_integration

    def set_error_integration_tag(self,error_integration_tag):
        self.attr.error_integration_tag = error_integration_tag

    def set_success_integration(self,success_integration):
        self.attr.success_integration = success_integration

    def set_success_integration_tag(self,success_integration_tag):
        self.attr.success_integration_tag = success_integration_tag

    def set_comment(self,comment):
        self.attr.comment = comment

    def set_comment_tag(self,comment_tag):
        self.attr.comment_tag = comment_tag

    def set_after(self,after):
        self.attr.after = after

    def set_after_tag(self,after_tag):
        self.attr.after_tag = after_tag

    def set_when(self,when):
        self.attr.when = when

    def set_when_tag(self,when_tag):
        self.attr.when_tag = when_tag

    def set_tag(self,tag):
        self.attr.tag = tag

    def set_tag_tag(self,tag_tag):
        self.attr.tag_tag = tag_tag

    def set_finalize(self,finalize):
        self.attr.finalize = finalize

    def set_finalize_tag(self,finalize_tag):
        self.attr.finalize_tag = finalize_tag

    def set_task_auto_retry_attempts(self,task_auto_retry_attempts):
        self.attr.task_auto_retry_attempts = task_auto_retry_attempts

    def set_task_auto_retry_attempts_tag(self,task_auto_retry_attempts_tag):
        self.attr.task_auto_retry_attempts_tag = task_auto_retry_attempts_tag

    def set_user_task_minimum_trigger_interval_in_seconds(self,user_task_minimum_trigger_interval_in_seconds):
        self.attr.user_task_minimum_trigger_interval_in_seconds = user_task_minimum_trigger_interval_in_seconds

    def set_user_task_minimum_trigger_interval_in_seconds_tag(self,user_task_minimum_trigger_interval_in_seconds_tag):
        self.attr.user_task_minimum_trigger_interval_in_seconds_tag = user_task_minimum_trigger_interval_in_seconds_tag

    def set_target_completion_interval(self,target_completion_interval):
        self.attr.target_completion_interval = target_completion_interval

    def set_target_completion_interval_tag(self,target_completion_interval_tag):
        self.attr.target_completion_interval_tag = target_completion_interval_tag

    def set_serverless_task_min_statement_size(self,serverless_task_min_statement_size):
        self.attr.serverless_task_min_statement_size = serverless_task_min_statement_size

    def set_serverless_task_min_statement_size_tag(self,serverless_task_min_statement_size_tag):
        self.attr.serverless_task_min_statement_size_tag = serverless_task_min_statement_size_tag

    def set_serverless_task_max_statement_size(self,serverless_task_max_statement_size):
        self.attr.serverless_task_max_statement_size = serverless_task_max_statement_size

    def set_serverless_task_max_statement_size_tag(self,serverless_task_max_statement_size_tag):
        self.attr.serverless_task_max_statement_size_tag = serverless_task_max_statement_size_tag

    def create_task(self):
        self.attr.session.sql(self.qry).collect()

    def create_object(session,**kwargs):
        task = Task(session)

        task.set_name(kwargs[_name_tag])
        task.set_name_tag(_name_tag)

        task.set_definition(kwargs[_definition_tag])
        task.set_definition_tag(_definition_tag)

        task.set_warehouse(kwargs[_warehouse_tag])
        task.set_warehouse_tag(_warehouse_tag)

        task.set_user_task_managed_initial_warehouse_size(kwargs[_user_task_managed_initial_warehouse_tag])
        task.set_user_task_managed_initial_warehouse_size_tag(_user_task_managed_initial_warehouse_tag)

        task.set_schedule(kwargs[_schedule_tag])
        task.set_schedule_tag(_schedule_tag)

        task.set_config(kwargs[_config])
        task.set_config_tag(_config)

        task.set_allow_overlapping_execution(kwargs[_allow_overlapping_execution_tag])
        task.set_allow_overlapping_execution_tag(_allow_overlapping_execution_tag)

        task.set_user_task_timeout_ms(kwargs[_user_task_timeout_ms_tag])
        task.set_user_task_timeout_ms_tag(_user_task_timeout_ms_tag)

        task.set_suspend_task_after_num_failures(kwargs[_suspend_task_after_num_failures_tag])
        task.set_suspend_task_after_num_failures_tag(_suspend_task_after_num_failures_tag)

        task.set_error_integration(kwargs[_error_integration_tag])
        task.set_error_integration(_error_integration_tag)

        task.set_success_integration(kwargs[_success_integration_tag])
        task.set_success_integration_tag(_success_integration_tag)

        task.set_comment(kwargs[_comment_tag])
        task.set_comment_tag(_comment_tag)

        task.set_after(kwargs[_after_tag])
        task.set_after_tag(_after_tag)

        task.set_when(kwargs[_when_tag])
        task.set_when_tag(_when_tag)

        task.set_tag(kwargs[_tag_tag])
        task.set_tag_tag(_tag_tag)

        task.set_finalize(kwargs[_finalize_tag])
        task.set_finalize_tag(_finalize_tag)

        task.set_task_auto_retry_attempts(kwargs[_task_auto_retry_attempts_tag])
        task.set_task_auto_retry_attempts_tag(_task_auto_retry_attempts_tag)

        task.set_user_task_minimum_trigger_interval_in_seconds(kwargs[_user_task_minimum_trigger_interval_in_seconds_tag])
        task.set_user_task_minimum_trigger_interval_in_seconds_tag(_user_task_minimum_trigger_interval_in_seconds_tag)

        task.set_target_completion_interval(kwargs[_target_completion_interval_tag])
        task.set_target_completion_interval_tag(_target_completion_interval_tag)

        task.set_serverless_task_min_statement_size(kwargs[_serverless_task_min_statement_size_tag])
        task.set_serverless_task_min_statement_size_tag(_serverless_task_min_statement_size_tag)

        task.create_task()

    def create_deployment_entry(self):
        deploy_inst = Deploy(self.attr.session)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database(self.attr.database)
        deploy_inst.set_object_schema(self.attr.schema)
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()