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
from src.usr.user import ChatHistory

class Name:   
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._sql = value

    def __delete__(self,instance):
        del instance._sql


class Warehouse:
    def __get__(self,instance,owner):
        return instance._warehouse
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
        if value == 'NONE':
            instance._schedule = value
        else:
            ret,type,num=vv.is_valid_schedule(schedule=value,object_name=instance.parent.__class__.__name__,attribute_name=self.__class__.__name__)
            if ret:
                if type=='CRON':
                    vv.is_valid_cron(value=value,
                                     object_type=instance.parent.__class__.__name__,
                                     attr_name=self.__class__.__name__)
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
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
        if isinstance(value,str):
            if value == 'NONE':
                instance._after = value
            else:
                vo.task_exist(session=instance.parent.session,database=instance.parent.attr.database,schema=instance.parent.attr.schema,task=value)
                instance._after = value
        elif isinstance(value,list):
            val_strng=""
            if len(value)==0:
                instance._after='NONE'
            else:
                for i in range(0,len(value)):
                    vo.task_exist(
                        session=instance.parent.session,
                        database=instance.parent.attr.database,
                        schema=instance.parent.attr.schema,
                        task=value[i]
                    )
                if i != len(value)-1:
                    val_strng=val_strng + value[i] + ","
                elif i == len(value)-1:
                    val_strng=val_strng + value[i]
            instance._after = val_strng
    
    def __delete__(self,instance):
        del instance._after


class When:
    def __get__(self,instance,owner):
        return instance._when
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        instance._when="NONE"
    
    def __delete__(self,instance):
        del instance._when


class Tag:
    def __get__(self,instance,owner):
        return instance._tag
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
        instance._finalize="NONE"
    
    def __delete__(self,instance):
        del instance._finalize

class TaskAutoRetryAttempts:
    def __get__(self,instance,owner):
        return instance._task_auto_retry_attempts
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
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
        instance.parent.print_setter(self.__class__.__name__,value)
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
        super().__init__(session, user_id, logger,database_required=True,schema_required=True)
        self.attr = TaskAttrs(self)
        self.session=session
        self.user_id=user_id
        self.logger=logger.getChild(self.__class__.__name__)

    def set_name(self,name):
        self.attr.name = name

    def set_definition(self,definition):
        self.attr.definition = definition 

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
        self.qualified_name = f"{self.attr.database}.{self.attr.schema}.{self.attr.name[0]}"

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
        set_flag(tags.COMMENT,"comment")
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
        self.qry = f"CREATE TASK {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} "

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
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.qualified_name} SET {tags.WAREHOUSE} = {self.attr.warehouse}"
                self.execute_final_query()
            if prop == tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.qualified_name} SET {tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE} = {self.attr.user_task_managed_initial_warehouse_size}"
                self.execute_final_query()
            if prop == tags.SCHEDULE:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.qualified_name} SET {tags.SCHEDULE} = {self.attr.schedule}"
                self.execute_final_query()
            if prop == tags.CONFIG:
                self.qry = f"ALTER {self.__class__.__name__} {self.qualified_name} SET {tags.CONFIG} = {self.attr.config}"
                self.execute_final_query()
            if prop == tags.ALLOW_OVERLAPPING_EXECUTION:
                self.qry = f"ALTER {self.__class__.__name__} {self.qualified_name} SET {tags.ALLOW_OVERLAPPING_EXECUTION} = {self.attr.allow_overlapping_execution}"
                self.execute_final_query()
            if prop == tags.USER_TASK_TIMEOUT_MS:
                self.qry = f"ALTER {self.__class__.__name__} {self.qualified_name} SET {tags.USER_TASK_TIMEOUT_MS} = {self.attr.user_task_timeout_ms}"
                self.execute_final_query()
            if prop == tags.SUSPEND_TASK_AFTER_NUM_FAILURES:
                self.qry = f"ALTER {self.__class__.__name__} {self.qualified_name} SET {tags.SUSPEND_TASK_AFTER_NUM_FAILURES} = {self.attr.suspend_task_after_num_failures}"
                self.execute_final_query()
            if prop == tags.ERROR_INTEGRATION:
                self.qry = f"ALTER {self.__class__.__name__} {self.qualified_name} SET {tags.ERROR_INTEGRATION} = {self.attr.error_integration}"
                self.execute_final_query()
            if prop == tags.SUCCESS_INTEGRATION:
                self.qry = f"ALTER {self.__class__.__name__} {self.qualified_name} SET {tags.SUCCESS_INTEGRATION} = {self.attr.success_integration}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__} {self.qualified_name} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()
            if prop == tags.AFTER:
                self.qry = f"ALTER {self.__class__.__name__} {self.qualified_name} SET {tags.AFTER} = {self.attr.after}"
                self.execute_final_query()
            if prop == tags.AFTER:
                self.qry = f"ALTER {self.__class__.__name__} {self.qualified_name} SET {tags.AFTER} = {self.attr.after}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER {self.__class__.__name__.upper()} {self.qualified_name} RENAME TO {self.attr.database}.{self.attr.schema}.{self.attr.name[1]}"
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


class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=Task(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.set_base_attributes(kwargs=kwargs)

        # set name
        if tags.NAME in kwargs.keys():
            obj_inst.logger.info(f"set name: {kwargs[tags.NAME]}")
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.logger.info(f"set name: NONE")
            obj_inst.set_name('NONE')

        # set definition
        if tags.SQL in kwargs.keys():
            obj_inst.logger.info(f"set definition: {kwargs[tags.SQL]}")
            obj_inst.set_definition(kwargs[tags.SQL])
        else:
            obj_inst.logger.info(f"set definition: NONE")
            obj_inst.set_definition('NONE')

        # set warehouse
        if tags.WAREHOUSE in kwargs.keys():
            obj_inst.logger.info(f"set warehouse: {kwargs[tags.WAREHOUSE]}")
            obj_inst.set_warehouse(kwargs[tags.WAREHOUSE])
        else:
            obj_inst.logger.info(f"set warehouse: NONE")
            obj_inst.set_warehouse('NONE')

        # set user_task_managed_initial_warehouse_size
        if tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE in kwargs.keys():
            obj_inst.logger.info(f"set user_task_managed_initial_warehouse_size: {kwargs[tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE]}")
            obj_inst.set_user_task_managed_initial_warehouse_size(kwargs[tags.USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE])
        else:
            obj_inst.logger.info(f"set user_task_managed_initial_warehouse_size: NONE")
            obj_inst.set_user_task_managed_initial_warehouse_size('NONE')

        # set schedule
        if tags.SCHEDULE in kwargs.keys():
            obj_inst.logger.info(f"set schedule: {kwargs[tags.SCHEDULE]}")
            obj_inst.set_schedule(kwargs[tags.SCHEDULE])
        else:
            obj_inst.logger.info(f"set schedule: NONE")
            obj_inst.set_schedule('NONE')

        # set config
        if tags.CONFIG in kwargs.keys():
            obj_inst.logger.info(f"set config: {kwargs[tags.CONFIG]}")
            obj_inst.set_config(kwargs[tags.CONFIG])
        else:
            obj_inst.logger.info(f"set config: NONE")
            obj_inst.set_config('NONE')

        # set allow_overlapping_execution
        if tags.ALLOW_OVERLAPPING_EXECUTION in kwargs.keys():
            obj_inst.logger.info(f"set allow_overlapping_execution: {kwargs[tags.ALLOW_OVERLAPPING_EXECUTION]}")
            obj_inst.set_allow_overlapping_execution(kwargs[tags.ALLOW_OVERLAPPING_EXECUTION])
        else:
            obj_inst.logger.info(f"set allow_overlapping_execution: NONE")
            obj_inst.set_allow_overlapping_execution('NONE')

        # set user_task_timeout_ms
        if tags.USER_TASK_TIMEOUT_MS in kwargs.keys():
            obj_inst.logger.info(f"set user_task_timeout_ms: {kwargs[tags.USER_TASK_TIMEOUT_MS]}")
            obj_inst.set_user_task_timeout_ms(kwargs[tags.USER_TASK_TIMEOUT_MS])
        else:
            obj_inst.logger.info(f"set user_task_timeout_ms: NONE")
            obj_inst.set_user_task_timeout_ms('NONE')

        # set suspend_task_after_num_failures
        if tags.SUSPEND_TASK_AFTER_NUM_FAILURES in kwargs.keys():
            obj_inst.logger.info(f"set suspend_task_after_num_failures: {kwargs[tags.SUSPEND_TASK_AFTER_NUM_FAILURES]}")
            obj_inst.set_suspend_task_after_num_failures(kwargs[tags.SUSPEND_TASK_AFTER_NUM_FAILURES])
        else:
            obj_inst.logger.info(f"set suspend_task_after_num_failures: NONE")
            obj_inst.set_suspend_task_after_num_failures('NONE')

        # set error_integration
        if tags.ERROR_INTEGRATION in kwargs.keys():
            obj_inst.logger.info(f"set error_integration: {kwargs[tags.ERROR_INTEGRATION]}")
            obj_inst.set_error_integration(kwargs[tags.ERROR_INTEGRATION])
        else:
            obj_inst.logger.info(f"set error_integration: NONE")
            obj_inst.set_error_integration('NONE')

        # set success_integration
        if tags.SUCCESS_INTEGRATION in kwargs.keys():
            obj_inst.logger.info(f"set success_integration: {kwargs[tags.SUCCESS_INTEGRATION]}")
            obj_inst.set_success_integration(kwargs[tags.SUCCESS_INTEGRATION])
        else:
            obj_inst.logger.info(f"set success_integration: NONE")
            obj_inst.set_success_integration('NONE')

        # set after
        if tags.AFTER in kwargs.keys():
            obj_inst.logger.info(f"set after: {kwargs[tags.AFTER]}")
            obj_inst.set_after(kwargs[tags.AFTER])
        else:
            obj_inst.logger.info(f"set after: NONE")
            obj_inst.set_after('NONE')

        # set when
        if tags.WHEN in kwargs.keys():
            obj_inst.logger.info(f"set when: {kwargs[tags.WHEN]}")
            obj_inst.set_when(kwargs[tags.WHEN])
        else:
            obj_inst.logger.info(f"set when: NONE")
            obj_inst.set_when('NONE')

        # set finalize
        if tags.FINALIZE in kwargs.keys():
            obj_inst.logger.info(f"set finalize: {kwargs[tags.FINALIZE]}")
            obj_inst.set_finalize(kwargs[tags.FINALIZE])
        else:
            obj_inst.logger.info(f"set finalize: NONE")
            obj_inst.set_finalize('NONE')

        # set task_auto_retry_attempts
        if tags.TASK_AUTO_RETRY_ATTEMPTS in kwargs.keys():
            obj_inst.logger.info(f"set task_auto_retry_attempts: {kwargs[tags.TASK_AUTO_RETRY_ATTEMPTS]}")
            obj_inst.set_task_auto_retry_attempts(kwargs[tags.TASK_AUTO_RETRY_ATTEMPTS])
        else:
            obj_inst.logger.info(f"set task_auto_retry_attempts: NONE")
            obj_inst.set_task_auto_retry_attempts('NONE')

        # set user_task_minimum_trigger_interval_in_seconds
        if tags.USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS in kwargs.keys():
            obj_inst.logger.info(f"set user_task_minimum_trigger_interval_in_seconds: {kwargs[tags.USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS]}")
            obj_inst.set_user_task_minimum_trigger_interval_in_seconds(kwargs[tags.USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS])
        else:
            obj_inst.logger.info(f"set user_task_minimum_trigger_interval_in_seconds: NONE")
            obj_inst.set_user_task_minimum_trigger_interval_in_seconds('NONE')

        # set target_completion_interval
        if tags.TARGET_COMPLETION_INTERVAL in kwargs.keys():
            obj_inst.logger.info(f"set target_completion_interval: {kwargs[tags.TARGET_COMPLETION_INTERVAL]}")
            obj_inst.set_target_completion_interval(kwargs[tags.TARGET_COMPLETION_INTERVAL])
        else:
            obj_inst.logger.info(f"set target_completion_interval: NONE")
            obj_inst.set_target_completion_interval('NONE')

        # set serverless_task_min_statement_size
        if tags.SERVERLESS_TASK_MIN_STATEMENT_SIZE in kwargs.keys():
            obj_inst.logger.info(f"set serverless_task_min_statement_size: {kwargs[tags.SERVERLESS_TASK_MIN_STATEMENT_SIZE]}")
            obj_inst.set_serverless_task_min_statement_size(kwargs[tags.SERVERLESS_TASK_MIN_STATEMENT_SIZE])
        else:
            obj_inst.logger.info(f"set serverless_task_min_statement_size: NONE")
            obj_inst.set_serverless_task_min_statement_size('NONE')

        # set serverless_task_max_statement_size
        if tags.SERVERLESS_TASK_MAX_STATEMENT_SIZE in kwargs.keys():
            obj_inst.logger.info(f"set serverless_task_max_statement_size: {kwargs[tags.SERVERLESS_TASK_MAX_STATEMENT_SIZE]}")
            obj_inst.set_serverless_task_max_statement_size(kwargs[tags.SERVERLESS_TASK_MAX_STATEMENT_SIZE])
        else:
            obj_inst.logger.info(f"set serverless_task_max_statement_size: NONE")
            obj_inst.set_serverless_task_max_statement_size('NONE')

        obj_inst.set_qualified_name()
        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        obj_inst.logger.info("creating deployment entry")
        obj_inst.create_deployment_entry()
        obj_inst.logger.info("writing to git")
        obj_inst.write_file_to_git()
        
        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                        object_identifier=obj_inst.attr.name[0],
                                        qry=obj_inst.qry)


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
