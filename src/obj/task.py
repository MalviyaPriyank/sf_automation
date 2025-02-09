import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.gvobject import Snowpipe as gv,Config as cfg
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy
from validation.validateobject import ValidateObject as vo


class Session:
    def __get__(self,instance,owner):
        return instance._session
    
    def __set__(self,instance,value):
        instance._session = value
    
    def __delete__(self,instance):
        del instance._session

class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if vo.database_exist(value):
            instance._database = value

    def __delete__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if vo.schema_exist(instance._database,value):
            instance._schema = value

    def __delete__(self,instance):
        del instance._schema

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if vv.ValidateString.is_enclosed_in_double_quotes(value):
            instance._name = value
        elif not vv.ValidateString.starts_with_alphabet(value):
            raise ValueError
        elif vv.ValidateString.has_space(value):
            raise ValueError
        elif vv.ValidateString.has_special_characters(value):
            raise ValueError
        else:
            instance._name = value

    def __delete__(self,instance):
        del instance._name

class NameTag:
    def __get__(self,instance,owner):
        return instance._name_tag
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
        else:
            instance._name_tag = value

    def __delete__(self,instance):
        del instance._name_tag

class Definition:
    def __get__(self,instance,owner):
        return instance._definition
    
    def __set__(self,instance,value):
        if value == None:
            raise KeyError
        else:
            instance._definition = value

    def __delete__(self,instance):
        del instance._definition

class DefinitionTag:
    def __get__(self,instance,owner):
        return instance._definition_tag
    
    def __set__(self,instance,value):
        if value == None:
            raise KeyError
        else:
            instance._definition_tag = value

    def __delete__(self,instance):
        del instance._definition_tag

class Warehouse:
    def __get__(self,instance,owner):
        return instance._warehouse
    
    def __set__(self,instance,value):
        instance._warehouse = value

    def __delete__(self,instance):
        del instance._warehouse

class WarehouseTag:
    def __get__(self,instance,owner):
        return instance._warehouse_tag
    
    def __set__(self,instance,value):
        instance._warehouse_tag = value

    def __delete__(self,instance):
        del instance._warehouse_tag

class UserTaskManagedInitialWarehouseSize:
    def __get__(self,instance,owner):
        return instance._user_task_managed_initial_warehouse_size
    
    def __set__(self,instance,value):
        if value not in tgv._allowed_values__user_task_managed_initial_warehouse_size:
            raise ValueError
        if instance._warehouse is None:
            instance._user_task_managed_initial_warehouse_size = value


    def __delete__(self,instance):
        del instance._user_task_managed_initial_warehouse_size

class UserTaskManagedInitialWarehouseSizeTag:
    def __get__(self,instance,owner):
        return instance._user_task_managed_initial_warehouse_size_tag
    
    def __set__(self,instance,value):
        instance._user_task_managed_initial_warehouse_size_tag = value

    def __delete__(self,instance):
        del instance._user_task_managed_initial_warehouse_size_tag


class Schedule:
    def __get__(self,instance,owner):
        return instance._schedule
    
    def __set__(self,instance,value):
        if not vv.is_valid_cron(value):
            raise ValueError
        else:
            instance._schedule = value
    
    def __delete__(self,instance):
        del instance._schedule

class ScheduleTag:
    def __get__(self,instance,owner):
        return instance._schedule_tag
    
    def __set__(self,instance,value):
        instance._schedule_tag = value
    
    def __delete__(self,instance):
        del instance._schedule_tag

class Config:
    def __get__(self,instance,owner):
        return instance._config
    
    def __set__(self,instance,value):
        if not vv.is_json(value):
            raise ValueError
        else:
            instance._config = value
    
    def __delete__(self,instance):
        del instance._config

class ConfigTag:
    def __get__(self,instance,owner):
        return instance._config_tag
    
    def __set__(self,instance,value):
        instance._config_tag = value
    
    def __delete__(self,instance):
        del instance._config_tag

class AllowOverlappingExecution:
    def __get__(self,instance,owner):
        return instance._allow_overlapping_execution
    
    def __set__(self,instance,value):
        if value is None:
            instance._allow_overlapping_execution = 'FALSE'
        else:
            if not vv.is_bool(value):
                raise ValueError
            else:
                instance._allow_overlapping_execution = value
    
    def __delete__(self,instance):
        del instance._allow_overlapping_execution

class AllowOverlappingExecutionTag:
    def __get__(self,instance,owner):
        return instance._allow_overlapping_execution_tag
    
    def __set__(self,instance,value):
        instance._allow_overlapping_execution_tag = value
    
    def __delete__(self,instance):
        del instance._allow_overlapping_execution_tag


class UserTaskTimeoutMs:
    def __get__(self,instance,owner):
        return instance._user_task_timeout_ms
    
    def __set__(self,instance,value):
        instance._user_task_timeout_ms = value
    
    def __delete__(self,instance):
        del instance._user_task_timeout_ms

class UserTaskTimeoutMsTag:
    def __get__(self,instance,owner):
        return instance._user_task_timeout_ms_tag
    
    def __set__(self,instance,value):
        if not vv.is_positive_number(value):
            raise ValueError
        else:
            if not 0<= float(value) <= 86400000:
                raise ValueError
            else:
                instance._user_task_timeout_ms_tag = value
    
    def __delete__(self,instance):
        del instance._user_task_timeout_ms_tag

class SuspendTaskAfterNumFailures:
    def __get__(self,instance,owner):
        return instance._suspend_task_after_num_failures
    
    def __set__(self,instance,value):
        if not vv.is_positive_number(value):
            raise ValueError
        else:
            instance._suspend_task_after_num_failures = value
    
    def __delete__(self,instance):
        del instance._suspend_task_after_num_failures

class SuspendTaskAfterNumFailuresTag:
    def __get__(self,instance,owner):
        return instance._suspen_task_after_num_failures_tag
    
    def __set__(self,instance,value):
        instance._suspen_task_after_num_failures_tag = value
    
    def __delete__(self,instance):
        del instance._suspen_task_after_num_failures_tag

class ErrorIntegration:
    def __get__(self,instance,owner):
        return instance._error_integration
    
    def __set__(self,instance,value):
        instance._error_integration = value
    
    def __delete__(self,instance):
        del instance._error_integration

class ErrorIntegrationTag:
    def __get__(self,instance,owner):
        return instance._error_integration_tag
    
    def __set__(self,instance,value):
        instance._error_integration_tag = value
    
    def __delete__(self,instance):
        del instance._error_integration_tag

class SuccessIntegration:
    def __get__(self,instance,owner):
        return instance._success_integration
    
    def __set__(self,instance,value):
        instance._success_integration = value
    
    def __delete__(self,instance):
        del instance._success_integration

class SuccessIntegrationTag:
    def __get__(self,instance,owner):
        return instance._success_integration_tag
    
    def __set__(self,instance,value):
        instance._success_integration_tag = value
    
    def __delete__(self,instance):
        del instance._success_integration_tag

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = value
    
    def __delete__(self,instance):
        del instance._comment

class CommentTag:
    def __get__(self,instance,owner):
        return instance._comment_tag
    
    def __set__(self,instance,value):
        instance._comment_tag = value
    
    def __delete__(self,instance):
        del instance._comment_tag

class After:
    def __get__(self,instance,owner):
        return instance._after
    
    def __set__(self,instance,value):
        instance._after = value
    
    def __delete__(self,instance):
        del instance._after

class AfterTag:
    def __get__(self,instance,owner):
        return instance._after_tag
    
    def __set__(self,instance,value):
        instance._after_tag = value
    
    def __delete__(self,instance):
        del instance._after_tag

class When:
    def __get__(self,instance,owner):
        return instance._when
    
    def __set__(self,instance,value):
        instance._when = value
    
    def __delete__(self,instance):
        del instance._when

class WhenTag:
    def __get__(self,instance,owner):
        return instance._when_tag
    
    def __set__(self,instance,value):
        instance._when_tag = value
    
    def __delete__(self,instance):
        del instance._when_tag

class Tag:
    def __get__(self,instance,owner):
        return instance._tag
    
    def __set__(self,instance,value):
        instance._tag = value
    
    def __delete__(self,instance):
        del instance._tag

class TagTag:
    def __get__(self,instance,owner):
        return instance._tag_tag
    
    def __set__(self,instance,value):
        instance._tag_tag = value
    
    def __delete__(self,instance):
        del instance._tag_tag

class Finalize:
    def __get__(self,instance,owner):
        return instance._finalize
    
    def __set__(self,instance,value):
        instance._finalize = value
    
    def __delete__(self,instance):
        del instance._finalize

class FinalizeTag:
    def __get__(self,instance,owner):
        return instance._finalize_tag
    
    def __set__(self,instance,value):
        instance._finalize_tag = value
    
    def __delete__(self,instance):
        del instance._finalize_tag

class TaskAutoRetryAttempts:
    def __get__(self,instance,owner):
        return instance._task_auto_retry_attempts
    
    def __set__(self,instance,value):
        instance._task_auto_retry_attempts = value
    
    def __delete__(self,instance):
        del instance._task_auto_retry_attempts

class TaskAutoRetryAttemptsTag:
    def __get__(self,instance,owner):
        return instance._task_auto_retry_attempts_tag
    
    def __set__(self,instance,value):
        instance._task_auto_retry_attempts_tag = value
    
    def __delete__(self,instance):
        del instance._task_auto_retry_attempts_tag

class UserTaskMinimumTriggerIntervalInSeconds:
    def __get__(self,instance,owner):
        return instance._user_task_minimum_trigger_interval_in_seconds
    
    def __set__(self,instance,value):
        instance._user_task_minimum_trigger_interval_in_seconds = value
    
    def __delete__(self,instance):
        del instance._user_task_minimum_trigger_interval_in_seconds

class UserTaskMinimumTriggerIntervalInSecondsTag:
    def __get__(self,instance,owner):
        return instance._user_task_minimum_trigger_interval_in_seconds_tag
    
    def __set__(self,instance,value):
        instance._user_task_minimum_trigger_interval_in_seconds_tag = value
    
    def __delete__(self,instance):
        del instance._user_task_minimum_trigger_interval_in_seconds_tag

class TargetCompletionInterval:
    def __get__(self,instance,owner):
        return instance._target_completion_interval
    
    def __set__(self,instance,value):
        instance._target_completion_interval = value
    
    def __delete__(self,instance):
        del instance._target_completion_interval

class TargetCompletionIntervalTag:
    def __get__(self,instance,owner):
        return instance._target_completion_interval_tag
    
    def __set__(self,instance,value):
        instance._target_completion_interval_tag = value
    
    def __delete__(self,instance):
        del instance._target_completion_interval_tag

class ServerlessTaskMinStatementSize:
    def __get__(self,instance,owner):
        return instance._serverless_task_min_statement_size
    
    def __set__(self,instance,value):
        instance._serverless_task_min_statement_size = value
    
    def __delete__(self,instance):
        del instance._serverless_task_min_statement_size

class ServerlessTaskMinStatementSizeTag:
    def __get__(self,instance,owner):
        return instance._serverless_task_min_statement_size_tag
    
    def __set__(self,instance,value):
        instance._serverless_task_min_statement_size_tag = value
    
    def __delete__(self,instance):
        del instance._serverless_task_min_statement_size_tag

class ServerlessTaskMaxStatementSize:
    def __get__(self,instance,owner):
        return instance._serverless_task_max_statement_size
    
    def __set__(self,instance,value):
        instance._serverless_task_max_statement_size = value
    
    def __delete__(self,instance):
        del instance._serverless_task_max_statement_size

class ServerlessTaskMaxStatementSizeTag:
    def __get__(self,instance,owner):
        return instance._serverless_task_max_statement_size_tag
    
    def __set__(self,instance,value):
        instance._serverless_task_max_statement_size_tag = value
    
    def __delete__(self,instance):
        del instance._serverless_task_max_statement_size_tag

class TaskAttrs:
    def __init__(self,parent):
        self.parent = parent

    session = Session()
    database = Database()

    schema = Schema()

    name = Name()
    name_tag = NameTag()

    definition = Definition()
    definition_tag = DefinitionTag()

    warehouse = Warehouse()
    warehouse_tag = WarehouseTag()

    user_task_managed_initial_warehouse_size = UserTaskManagedInitialWarehouse()
    user_task_managed_initial_warehouse_size_tag = UserTaskManagedInitialWarehouseTag()

    schedule = Schedule()
    schedule_tag = ScheduleTag()

    config = Config()
    config_tag = ConfigTag()

    allow_overlapping_execution = AllowOverlappingExecution()
    allow_overlapping_execution_tag = AllowOverlappingExecutionTag()
    
    user_task_timeout_ms = UserTaskTimeoutMs()
    user_task_timeout_ms_tag = UserTaskTimeoutMsTag()

    suspend_task_after_num_failures = SuspendTaskAfterNumFailures()
    suspend_task_after_num_failures_tag = SuspendTaskAfterNumFailuresTag()

    error_integration = ErrorIntegration()
    error_integration_tag = ErrorIntegrationTag()

    success_integration = SuccessIntegration()
    success_integration_tag = SuccessIntegrationTag()

    comment = Comment()
    comment_tag = CommentTag()

    after = After()
    after_tag = AfterTag()

    when = When()
    when_tag = WhenTag()

    tag = Tag()
    tag_tag = TagTag()

    finalize = Finalize()
    finalize_tag = FinalizeTag()

    task_auto_retry_attempts = TaskAutoRetryAttempts()
    task_auto_retry_attempts_tag = TaskAutoRetryAttemptsTag()

    user_task_minimum_trigger_interval_in_seconds = UserTaskMinimumTriggerIntervalInSeconds()
    user_task_minimum_trigger_interval_in_seconds_tag = UserTaskMinimumTriggerIntervalInSecondsTag()

    target_completion_interval = TargetCompletionInterval()
    target_completion_interval_tag = TargetCompletionIntervalTag()

    serverless_task_min_statement_size = ServerlessTaskMinStatementSize()
    serverless_task_min_statement_size_tag = ServerlessTaskMinStatementSizeTag()

    serverless_task_max_statement_size = ServerlessTaskMaxStatementSize()
    serverless_task_max_statement_size_tag = ServerlessTaskMaxStatementSizeTag()



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

    def set_name_tag(self,name_tag):
        self.attr.name_tag = name_tag

    def set_definition(self,definition):
        self.attr.definition = definition 

    def set_definition_tag(self,definition_tag):
        self.attr.definition_tag = definition_tag 

    def set_database(self,database):
        self.attr.database = database

    def set_database_tag(self,database_tag):
        self.attr.database_tag = database_tag

    def set_warehouse(self,warehouse):
        self.attr.warehouse = warehouse

    def set_warehouse_tag(self,warehouse_tag):
        self.attr.warehouse_tag = warehouse_tag

    def set_user_task_managed_initial_warehouse_size(self,user_task_managed_initial_warehouse_size):
        self.attr.user_task_managed_initial_warehouse_size = user_task_managed_initial_warehouse_size

    def set_user_task_managed_initial_warehouse_size_tag(self,user_task_managed_initial_warehouse_size_tag):
        self.attr.user_task_managed_initial_warehouse_size_tag = user_task_managed_initial_warehouse_size_tag

    def set_schedule(self,schedule):
        self.attr.schedule = schedule

    def set_schedule_tag(self,schedule_tag):
        self.attr.schedule_tag = schedule_tag

    def set_config(self,config):
        self.attr.config = config

    def set_config_tag(self,config_tag):
        self.attr.config_tag = config_tag

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