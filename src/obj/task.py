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
            vv.is_allowed_value(value=value,allowed_list=gvtask._allowed_values_user_task_managed_initial_warehouse_size,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
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
                        vv.is_between(value=int(num),num1=gvtask._allowed_min_value_seconds,num2=gvtask._allowed_max_value_seconds,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                        instance._schedule=f"'{value}'"
                    elif type=='MINUTE':
                        vv.is_between(value=int(num),num1=gvtask._allowed_min_value_minute,num2=gvtask._allowed_max_value_minute,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                        instance._schedule=f"'{value}'"
                    elif type=='HOUR':
                        vv.is_between(value=int(num),num1=gvtask._allowed_min_value_hour,num2=gvtask._allowed_max_value_hour,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
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
            vv.is_between(value=value,num1=gvtask._allowed_min_user_task_timeout_ms,num2=gvtask._allowed_max_user_task_timeout_ms,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
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
            vv.is_allowed_value(gvtask._allowed_values_log_level,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
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
            vv.is_between(value=value,num1=gvtask._allowed_min_value_task_auto_retry_attempts,num2=gvtask._allowed_max_value_task_auto_retry_attempts,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
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
            vv.is_between(value=value,num1=gvtask._allowed_min_value_user_task_minimum_trigger_interval_in_seconds,num2=gvtask._allowed_max_value_user_task_minimum_trigger_interval_in_seconds,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
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
                        vv.is_between(value=int(num),num1=gvtask._allowed_min_value_seconds_task_comletion_interval,num2=gvtask._allowed_max_value_seconds_task_comletion_interval,object_type=object_type,attr_name=attr_name)
                    elif type=='MINUTE':
                        vv.is_between(value=int(num),num1=gvtask._allowed_min_value_minutes_task_comletion_interval,num2=gvtask._allowed_max_value_minutes_task_comletion_interval,object_type=object_type,attr_name=attr_name)
                    elif type=='HOUR':
                        vv.is_between(value=int(num),num1=gvtask._allowed_min_value_hours_task_comletion_interval, num2=gvtask._allowed_max_value_hours_task_comletion_interval,object_type=object_type,attr_name=attr_name)
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
                vv.is_allowed_value(value=value,allowed_list=gvtask._allowed_values_user_task_managed_initial_warehouse_size,object_type=object_type,attr_name=attr_name)
                index_user_task_managed_initial_warehouse_size = gvtask._allowed_values_user_task_managed_initial_warehouse_size.index(instance._user_task_managed_initial_warehouse_size)
                index_serverless_task_min_statement_size = gvtask._allowed_values_user_task_managed_initial_warehouse_size.index(value)
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
                vv.is_allowed_value(value=value,allowed_list=gvtask._allowed_values_user_task_managed_initial_warehouse_size,object_type=object_type,attr_name=attr_name)
                index_user_task_managed_initial_warehouse_size = gvtask._allowed_values_user_task_managed_initial_warehouse_size.index(instance._user_task_managed_initial_warehouse_size)
                index_serverless_task_min_statement_size = gvtask._allowed_values_user_task_managed_initial_warehouse_size.index(instance._serverless_task_min_statement_size)
                index_serverless_task_max_statement_size = gvtask._allowed_values_user_task_managed_initial_warehouse_size.index(value)
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

class Task:
    def __init__(self,session,user_id):
        self.session = session
        self.user_id = user_id
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

        set_flag(gvtask._warehouse_tag,"_warehouse")
        set_flag(gvtask._user_task_managed_initial_warehouse_size_tag,"_user_task_managed_initial_warehouse_size")
        set_flag(gvtask._schedule_tag,"_schedule")
        set_flag(gvtask._config_tag,"_config")
        set_flag(gvtask._allow_overlapping_execution_tag,"_allow_overlapping_execution")
        set_flag(gvtask._user_task_timeout_ms_tag,"_user_task_timeout_ms")
        set_flag(gvtask._suspend_task_after_num_failures_tag,"_suspend_task_after_num_failures")
        set_flag(gvtask._error_integration_tag,"_error_integration")
        set_flag(gvtask._success_integration_tag,"_success_integration")
        set_flag(gvtask._comment_tag,"_comment")
        set_flag(gvtask._after_tag,"_after")
        set_flag(gvtask._when_tag,"_when")
        set_flag(gvtask._tag_tag,"_tag")
        set_flag(gvtask._finalize_tag,"_finalize")
        set_flag(gvtask._user_task_minimum_trigger_interval_in_seconds_tag,"_user_task_minimum_trigger_interval_in_seconds")
        set_flag(gvtask._serverless_task_min_statement_size_tag,"_serverless_task_min_statement_size")
        set_flag(gvtask._serverless_task_max_statement_size_tag,"_serverless_task_max_statement_size")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"CREATE TASK {self.attr.database}.{self.attr.schema}.{self.attr.name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gvtask._warehouse_tag:
                    self.qry = f" {self.qry} {gvtask._warehouse_tag} = {self.attr.warehouse} "
                if prop == gvtask._user_task_managed_initial_warehouse_size_tag:
                    self.qry = f" {self.qry} {gvtask._user_task_managed_initial_warehouse_size_tag } = {self.attr.user_task_managed_initial_warehouse_size} "
                if prop == gvtask._schedule_tag:
                    self.qry = f" {self.qry} {gvtask._schedule_tag} = {self.attr.schedule} "
                if prop == gvtask._config_tag:
                    self.qry = f" {self.qry} {gvtask._config_tag} = {self.attr.config} "
                if prop == gvtask._allow_overlapping_execution_tag:
                    self.qry = f" {self.qry} {gvtask._allow_overlapping_execution_tag} = {self.attr.allow_overlapping_execution} "
                if prop == gvtask._user_task_timeout_ms_tag:
                    self.qry = f" {self.qry} {gvtask._user_task_timeout_ms_tag} = {self.attr.user_task_timeout_ms} "
                if prop == gvtask._suspend_task_after_num_failures_tag:
                    self.qry = f" {self.qry} {gvtask._suspend_task_after_num_failures_tag} = {self.attr.suspend_task_after_num_failures} "
                if prop == gvtask._error_integration_tag:
                    self.qry = f" {self.qry} {gvtask._error_integration_tag} = {self.attr.error_integration} "
                if prop == gvtask._success_integration_tag:
                    self.qry = f" {self.qry} {gvtask._success_integration_tag} = {self.attr.success_integration} "
                if prop == gvtask._comment_tag:
                    self.qry = f" {self.qry} {gvtask._comment_tag} = {self.attr.comment} "
                if prop == gvtask._after_tag:
                    self.qry = f" {self.qry} {gvtask._after_tag} = {self.attr.after} "
                if prop == gvtask._when_tag:
                    self.qry = f" {self.qry} {gvtask._when_tag} = {self.attr.when} "
                if prop == gvtask._tag_tag:
                    self.qry = f" {self.qry} {gvtask._tag_tag} = {self.attr.tag} "
                if prop == gvtask._finalize_tag:
                    self.qry = f" {self.qry} {gvtask._finalize_tag} = {self.attr.finalize} "
                if prop == gvtask._task_auto_retry_attempts_tag:
                    self.qry = f" {self.qry} {gvtask._task_auto_retry_attempts_tag} = {self.attr.task_auto_retry_attempts} "
                if prop == gvtask._user_task_minimum_trigger_interval_in_seconds_tag:
                    self.qry = f" {self.qry} {gvtask._user_task_minimum_trigger_interval_in_seconds_tag} = {self.attr.user_task_minimum_trigger_interval_in_seconds} "
                if prop == gvtask._target_completion_interval_tag:
                    self.qry = f" {self.qry} {gvtask._target_completion_interval_tag} = {self.attr.target_completion_interval} "
                if prop == gvtask._serverless_task_min_statement_size_tag:
                    self.qry = f" {self.qry} {gvtask._serverless_task_min_statement_size_tag} = {self.attr.serverless_task_min_statement_size} "
                if prop == gvtask._serverless_task_min_statement_size_tag:
                    self.qry = f" {self.qry} {gvtask._serverless_task_min_statement_size_tag} = {self.attr.serverless_task_min_statement_size} "

        self.qry = self.qry + f" AS  {self.attr.definition} "    
        

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()

    def create_task(self):
        self.session.sql(self.qry).collect()

    def create_object(self,**kwargs):
        self.set_database(kwargs[gvtask._database_tag])
        self.set_schema(kwargs[gvtask._schema_tag])
        self.set_name(kwargs[gvtask._name_tag])
        self.set_definition(kwargs[gvtask._sql_tag])
        self.set_warehouse(kwargs[gvtask._warehouse_tag])
        self.set_user_task_managed_initial_warehouse_size(kwargs[gvtask._user_task_managed_initial_warehouse_size_tag])
        self.set_schedule(kwargs[gvtask._schedule_tag])
        self.set_config(kwargs[gvtask._config_tag])
        self.set_allow_overlapping_execution(kwargs[gvtask._allow_overlapping_execution_tag])
        self.set_user_task_timeout_ms(kwargs[gvtask._user_task_timeout_ms_tag])
        self.set_suspend_task_after_num_failures(kwargs[gvtask._suspend_task_after_num_failures_tag])
        self.set_error_integration(kwargs[gvtask._error_integration_tag])
        self.set_success_integration(kwargs[gvtask._success_integration_tag])
        self.set_comment(kwargs[gvtask._comment_tag])
        self.set_after(kwargs[gvtask._after_tag])
        self.set_when(kwargs[gvtask._when_tag])
        self.set_tag(kwargs[gvtask._tag_tag])
        self.set_finalize(kwargs[gvtask._finalize_tag])
        self.set_task_auto_retry_attempts(kwargs[gvtask._task_auto_retry_attempts_tag])
        self.set_user_task_minimum_trigger_interval_in_seconds(kwargs[gvtask._user_task_minimum_trigger_interval_in_seconds_tag])
        self.set_target_completion_interval(kwargs[gvtask._target_completion_interval_tag])
        self.set_serverless_task_min_statement_size(kwargs[gvtask._serverless_task_min_statement_size_tag])
        self.set_serverless_task_max_statement_size(kwargs[gvtask._serverless_task_max_statement_size_tag])
        self.set_qualified_name()

        self.prepare_query()
        self.create_task()
        self.create_deployment_entry()

    def grant_default_privileges(self):
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges[self.__class__.__name__.upper()]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = self.__class__.__name__.upper(),object_identifier=self.qualified_name,role = role)

    def create_deployment_entry(self):
        deploy_inst = Deploy(self.session)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database(self.attr.database)
        deploy_inst.set_object_schema(self.attr.schema)
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()