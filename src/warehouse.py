# The Snowpark package is required for Python Worksheets. 
# You can add more packages by selecting them using the Packages control and then importing them.

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col
import warehousevars as WHV

class Name:
    def __get__(self,instance,owner):
        return instance._name

    def __set__(self,instance,value):
        instance._name = value

    def __delete__(self,instance):
        del instance._name

class NameLabel:
    def __get__(self,instance,owner):
        return instance._name_label

    def __set__(self,instance,value):
        instance._name_label = value

    def __delete__(self,instance):
        del instance._name_label

class Type:
    def __get__(self,instance,owner):
        return instance._type

    def __set__(self,instance,value):
        
        if value not in _allowed_values_type:
            raise WarehouseTypeError
        else:
            instance._type = value

    def __delete__(self,instance):
        del instance._type

class TypeLabel:
    def __get__(self,instance,owner):
        return instance._type_label

    def __set__(self,instance,value):
        instance._type_label = value

    def __delete__(self,instance):
        del instance._type_label

class Size:
    def __get__(self,instance,owner):
        return instance._size

    def __set__(self,instance,value):
        if instance._type == 'SNOWPARK-OPTIMIZED':
            allowed_values = _allow_allowed_values_wh_snowpark_optimized
        else:
            allowed_values = _allowed_values_wh_standard
        if value not in allowed_values:
            raise ValueError
        else:
            instance._size = value

    def __delete__(self,instance):
        del instance._size

class SizeLabel:
    def __get__(self,instance,owner):
        return instance._size_label

    def __set__(self,instance,value):
        instance._size_label = value

    def __delete__(self,instance):
        del instance._size_label



class ResourceConstraint:
    def __get__(self,instance,owner):
        return instance._resource_constraint

    def __set__(self,instance,value):
        if instance._type == 'SNOWPARK-OPTIMIZED': 
            instance._resource_constraint = value
        elif value == None:
            instance._resource_constraint = None
        else:
            raise ValueError

    def __delete__(self,instance):
        del instance._resource_constraint

class ResourceConstraintLabel:
    def __get__(self,instance,owner):
        return instance._resource_constraint_label

    def __set__(self,instance,value): 
        instance._resource_constraint_label = value

    def __delete__(self,instance):
        del instance._resource_constraint_label

class MaxClusterCount:
    def __get__(self,instance,owner):
        return instance._max_cluster_count

    def __set__(self,instance,value):
        if value == None:
            instance._max_cluster_count = None
        else:
            instance._max_cluster_count = value

    def __delete__(self,instance):
        del instance._max_cluster_count


class MaxClusterCountLabel:
    def __get__(self,instance,owner):
        return instance._max_cluster_count_label

    def __set__(self,instance,value):
        instance._max_cluster_count_label = value

    def __delete__(self,instance):
        del instance._max_cluster_count_label

class MinClusterCount:
    def __get__(self,instance,owner):
        return instance._min_cluster_count

    def __set__(self,instance,value):
        if value == None:
            instance._min_cluster_count = None
        elif value >= 1:
            instance._min_cluster_count = value   
        else:
            raise ValueError

    def __delete__(self,instance):
        del instance._min_cluster_count


class MinClusterCountLabel:
    def __get__(self,instance,owner):
        return instance._min_cluster_count_label

    def __set__(self,instance,value):
        instance._min_cluster_count_label = value

    def __delete__(self,instance):
        del instance._min_cluster_count_label

class ScalingPolicy:
    def __get__(self,instance,owner):
        return instance._scaling_policy

    def __set__(self,instance,value):
        if value == None:
            instance._scaling_policy = None
        elif instance._scaling_policy > 1:
            instance._scaling_policy = value       
        else:
            raise ValueError

    def __delete__(self,instance):
        del instance._scaling_policy


class ScalingPolicyLabel:
    def __get__(self,instance,owner):
        return instance._scaling_policy_label

    def __set__(self,instance,value):
        instance._scaling_policy_label = value

    def __delete__(self,instance):
        del instance._scaling_policy_label


class AutoSuspend:
    def __get__(self,instance,owner):
        return instance._auto_suspend

    def __set__(self,instance,value):
        if value == None:
            instance._auto_suspend = None
        else:
            instance._auto_suspend = value

    def __delete__(self,instance):
        del instance._auto_suspend

class AutoSuspendLabel:
    def __get__(self,instance,owner):
        return instance._auto_suspend_label

    def __set__(self,instance,value):
        instance._auto_suspend_label = value

    def __delete__(self,instance):
        del instance._auto_suspend_label

class AutoResume:
    def __get__(self,instance,owner):
        return instance._auto_resume

    def __set__(self,instance,value):
        if value == None:
            instance._auto_resume = None
        else:
            instance._auto_resume = value

    def __delete__(self,instance):
        del instance._auto_resume

class AutoResumeLabel:
    def __get__(self,instance,owner):
        return instance._auto_resume_label

    def __set__(self,instance,value):
        instance._auto_resume_label = value


    def __delete__(self,instance):
        del instance._auto_resume_label

class InitiallySuspended:
    def __get__(self,instance,owner):
        return instance._initially_suspended

    def __set__(self,instance,value):
        if value == None:
            instance._initially_suspended = None
        else:
            instance._initially_suspended = value

    def __delete__(self,instance):
        del instance._initially_suspended


class InitiallySuspendedLabel:
    def __get__(self,instance,owner):
        return instance._initially_suspended_label

    def __set__(self,instance,value):
        instance._initially_suspended_label = value

    def __delete__(self,instance):
        del instance._initially_suspended_label

class ResourceMonitor:
    def __get__(self,instance,owner):
        return instance._resource_monitor

    def __set__(self,instance,value):
        if value == None:
            instance._resource_monitor = None
        else:
            instance._resource_monitor = value

    def __delete__(self,instance):
        del instance._resource_monitor

class ResourceMonitorLabel:
    def __get__(self,instance,owner):
        return instance._resource_monitor_label

    def __set__(self,instance,value):
        instance._resource_monitor_label = value

    def __delete__(self,instance):
        del instance._resource_monitor_label

class Comment:
    def __get__(self,instance,owner):
        return instance._comment

    def __set__(self,instance,value):
        if value == None:
            instance._comment = None
        else:
            instance._comment = value
    def __delete__(self,instance):
        del instance._comment

class CommentLabel:
    def __get__(self,instance,owner):
        return instance._comment_label

    def __set__(self,instance,value):
        instance._comment_label = value

    def __delete__(self,instance):
        del instance._comment_label


class Tag:
    def __get__(self,instance,owner):
        return instance._tag

    def __set__(self,instance,value):
        if value == None:
            instance._tag = None
        else:
            instance._tag = value

    def __delete__(self,instance):
        del instance._tag

class TagLabel:
    def __get__(self,instance,owner):
        return instance._tag_label

    def __set__(self,instance,value):
        instance._tag_label = value

    def __delete__(self,instance):
        del instance._tag_label


class EnableQueryAcceleration:
    def __get__(self,instance,owner):
        return instance._enable_query_acceleration

    def __set__(self,instance,value):
        if value == None:
            instance._enable_query_acceleration = None
        elif value in _allowed_values_query_acceleration:
            instance._enable_query_acceleration = value
        else:
            raise ValueError

    def __delete__(self,instance):
        del instance._enable_query_acceleration


class EnableQueryAccelerationLabel:
    def __get__(self,instance,owner):
        return instance._enable_query_acceleration_label

    def __set__(self,instance,value):
        instance._enable_query_acceleration_label = value

    def __delete__(self,instance):
        del instance._enable_query_acceleration_label

class QueryAccelerationMaxScaleFactor:
    def __get__(self,instance,owner):
        return instance._query_acceleration_max_scale_factor

    def __set__(self,instance,value):
        if value == None:
            instance._query_acceleration_max_scale_factor = None
        else:
            instance._query_acceleration_max_scale_factor = value

    def __delete__(self,instance):
        del instance._query_acceleration_max_scale_factor

class QueryAccelerationMaxScaleFactorLabel:
    def __get__(self,instance,owner):
        return instance._query_acceleration_max_scale_factor_label

    def __set__(self,instance,value):
        instance._query_acceleration_max_scale_factor_label = value

    def __delete__(self,instance):
        del instance._query_acceleration_max_scale_factor_label

class MaxConcurrencyLevel:
    def __get__(self,instance,owner):
        return instance._max_concurrency_level

    def __set__(self,instance,value):
        if value == None:
            instance._max_concurrency_level = None
        else:
            instance._max_concurrency_level = value

    def __delete__(self,instance):
        del instance._max_concurrency_level

class MaxConcurrencyLevelLabel:
    def __get__(self,instance,owner):
        return instance._max_concurrency_level_label

    def __set__(self,instance,value):
        instance._max_concurrency_level_label = value

    def __delete__(self,instance):
        del instance._max_concurrency_level_label

class StatementQueuedTimeoutInSeconds:
    def __get__(self,instance,owner):
        return instance._statement_queued_timeout_in_seconds

    def __set__(self,instance,value):
        if value == None:
            instance._statement_queued_timeout_in_seconds = None
        else:
            instance._statement_queued_timeout_in_seconds = value

    def __delete__(self,instance):
        del instance._statement_queued_timeout_in_seconds

class StatementQueuedTimeoutInSecondsLabel:
    def __get__(self,instance,owner):
        return instance._statement_queued_timeout_in_seconds_label

    def __set__(self,instance,value):
        instance._statement_queued_timeout_in_seconds_label = value

    def __delete__(self,instance):
        del instance._statement_queued_timeout_in_seconds_label

class StatementTimeoutInSeconds:
    def __get__(self,instance,owner):
        return instance._statement_timeout_in_seconds

    def __set__(self,instance,value):
        if value == None:
            instance._statement_timeout_in_seconds = None
        else:
            instance._statement_timeout_in_seconds = value

    def __delete__(self,instance):
        del instance._statement_timeout_in_seconds

class StatementTimeoutInSecondsLabel:
    def __get__(self,instance,owner):
        return instance._statement_timeout_in_seconds_label

    def __set__(self,instance,value):
        instance._statement_timeout_in_seconds_label = value

    def __delete__(self,instance):
        del instance._statement_timeout_in_seconds_label


class WarehouseAttrs:
    name = Name()
    name_label = NameLabel()
    size = Size()
    size_label = SizeLabel()
    type = Type()
    type_label = TypeLabel()
    resource_constraint = ResourceConstraint()
    resource_constraint_label = ResourceConstraintLabel()
    max_cluster_count = MaxClusterCount()
    max_cluster_count_label = MaxClusterCountLabel()
    min_cluster_count = MinClusterCount()
    min_cluster_count_label = MinClusterCountLabel()
    scaling_policy = ScalingPolicy()
    scaling_policy_label = ScalingPolicyLabel()
    auto_suspend = AutoSuspend()
    auto_suspend_label = AutoSuspendLabel()
    auto_resume = AutoResume()
    auto_resume_label = AutoResumeLabel()
    initially_suspended = InitiallySuspended()
    initially_suspended_label = InitiallySuspendedLabel()
    resource_monitor = ResourceMonitor()
    resource_monitor_label = ResourceMonitorLabel()
    comment = Comment()
    comment_label = CommentLabel()
    tag = Tag()
    tag_label = TagLabel()
    enable_query_acceleration = EnableQueryAcceleration()
    enable_query_acceleration_label = EnableQueryAccelerationLabel()
    query_acceleration_max_scale_factor = QueryAccelerationMaxScaleFactor()
    query_acceleration_max_scale_factor_label = QueryAccelerationMaxScaleFactorLabel()
    max_concurrency_level = MaxConcurrencyLevel()
    max_concurrency_level_label = MaxConcurrencyLevelLabel()
    statemet_queued_timeout_in_seconds = StatementQueuedTimeoutInSeconds()
    statemet_queued_timeout_in_seconds_label = StatementQueuedTimeoutInSecondsLabel()
    statement_timeout_in_seconds = StatementTimeoutInSeconds()
    statement_timeout_in_seconds_label = StatementTimeoutInSecondsLabel()



class Warehouse:
    def __init__(self,session):
        self.attr = WarehouseAttrs()
        self.session =  session
        self.qry = ""

    def set_name(self,name):
        self.attr.name = name

    def set_name_label(self,name_label):
        self.attr.name_label = name_label

    def set_size(self,size):
        self.attr.size =  size

    def set_size_label(self,size_label):
        self.attr.size_label = size_label

    def set_type(self,type):
        self.attr.type = type

    def set_type_label(self,type_label):
        self.attr.type_label = type_label
    
    def set_resource_constraint(self,resource_constraint):
        self.attr.resource_constraint = resource_constraint

    def set_resource_constraint_label(self,resource_constraint_label):
        self.attr.resource_constraint_label = resource_constraint_label

    def set_max_cluster_count(self,max_cluster_count):
        self.attr.max_cluster_count = max_cluster_count

    def set_max_cluster_count_label(self,max_cluster_count_label):
        self.attr.max_cluster_count_label = max_cluster_count_label

    def set_min_cluster_count(self,min_cluster_count):
        self.attr.min_cluster_count = min_cluster_count

    def set_min_cluster_count_label(self,min_cluster_count_label):
        self.attr.min_cluster_count_label = min_cluster_count_label
    
    def set_scaling_policy(self,scaling_policy):
        self.attr.scaling_policy = scaling_policy

    def set_scaling_policy_label(self,scaling_policy_label):
        self.attr.scaling_policy_label = scaling_policy_label
    
    def set_auto_suspend(self,auto_suspend):
        self.attr.auto_suspend = auto_suspend

    def set_auto_suspend_label(self,auto_suspend_label):
        self.attr.auto_suspend_label = auto_suspend_label

    def set_auto_resume(self,auto_resume):
        self.attr.auto_resume = auto_resume

    def set_auto_resume_label(self,auto_resume_label):
        self.attr.auto_resume_label = auto_resume_label

    def set_initially_suspended(self,initially_suspended):
        self.attr.initially_suspended = initially_suspended

    def set_initially_suspended_label(self,initially_suspended_label):
        self.attr.initially_suspended_label = initially_suspended_label
    
    def set_resource_monitor(self,resource_monitor):
        self.attr.resource_monitor = resource_monitor

    def set_resource_monitor_label(self,resource_monitor_label):
        self.attr.resource_monitor_label = resource_monitor_label

    def set_comment(self,comment):
        self.attr.comment = comment

    def set_comment_label(self,comment_label):
        self.attr.comment_label = comment_label
    
    def set_tag(self,tag):
        self.attr.tag = tag

    def set_tag_label(self,tag_label):
        self.attr.tag_label = tag_label
    
    def set_enable_query_acceleration(self,enable_query_acceleration):
        self.attr.enable_query_acceleration = enable_query_acceleration

    def set_enable_query_acceleration_label(self,enable_query_acceleration_label):
        self.attr.enable_query_acceleration_label = enable_query_acceleration_label
    
    def set_query_acceleration_max_scale_factor(self,query_acceleration_max_scale_factor):
        self.attr.query_acceleration_max_scale_factor = query_acceleration_max_scale_factor

    def set_query_acceleration_max_scale_factor_label(self,query_acceleration_max_scale_factor_label):
        self.attr.query_acceleration_max_scale_factor_label = query_acceleration_max_scale_factor_label

    def set_max_concurrency_level(self,max_concurrency_level):
        self.attr.max_concurrency_level = max_concurrency_level

    def set_max_concurrency_level_label(self,max_concurrency_level_label):
        self.attr.max_concurrency_level_label = max_concurrency_level_label

    def set_statemet_queued_timeout_in_seconds(self,statemet_queued_timeout_in_seconds):
        self.attr.statemet_queued_timeout_in_seconds = statemet_queued_timeout_in_seconds

    def set_statemet_queued_timeout_in_seconds_label(self,statemet_queued_timeout_in_seconds_label):
        self.attr.statemet_queued_timeout_in_seconds_label = statemet_queued_timeout_in_seconds_label

    def set_statement_timeout_in_seconds(self,statement_timeout_in_seconds):
        self.attr.statement_timeout_in_seconds = statement_timeout_in_seconds

    def set_statement_timeout_in_seconds_label(self,statement_timeout_in_seconds_label):
        self.attr.statement_timeout_in_seconds_label = statement_timeout_in_seconds_label
        
    def execute_query(self,qry):
        self.session.sql(qry).collect()


    def set_object_properties_flag(self):
        self.flag_dic = {}
        if self.attr.type is not None:
            self.flag_dic['type'] = 1
        else:
            self.flag_dic['type'] = 0

        if self.attr.size is not None:
            self.flag_dic['size'] = 1
        else:
            self.flag_dic['size'] = 0

        if self.attr.resource_constraint is not None:
            self.flag_dic['resource_constraint'] = 1
        else:
            self.flag_dic['resource_constraint'] = 0

        if self.attr.max_cluster_count is not None:
            self.flag_dic['max_cluster_count'] = 1
        else:
            self.flag_dic['max_cluster_count'] = 0

        if self.attr.min_cluster_count is not None:
            self.flag_dic['min_cluster_count'] = 1
        else:
            self.flag_dic['min_cluster_count'] = 0

        if self.attr.scaling_policy is not None:
            self.flag_dic['scaling_policy'] = 1
        else:
            self.flag_dic['scaling_policy'] = 0

        if self.attr.auto_suspend is not None:
            self.flag_dic['auto_suspend'] = 1
        else:
            self.flag_dic['auto_suspend'] = 0

        if self.attr.auto_resume is not None:
            self.flag_dic['auto_resume'] = 1
        else:
            self.flag_dic['auto_resume'] = 0

        if self.attr.initially_suspended is not None:
            self.flag_dic['initially_suspended'] = 1
        else:
            self.flag_dic['initially_suspended'] = 0

        if self.attr.resource_monitor is not None:
            self.flag_dic['resource_monitor'] = 1
        else:
            self.flag_dic['resource_monitor'] = 0

        if self.attr.comment is not None:
            self.flag_dic['comment'] = 1
        else:
            self.flag_dic['comment'] = 0

        if self.attr.tag is not None:
            self.flag_dic['tag'] = 1
        else:
            self.flag_dic['tag'] = 0

        if self.attr.enable_query_acceleration is not None:
            self.flag_dic['enable_query_acceleration'] = 1
        else:
            self.flag_dic['enable_query_acceleration'] = 0

        if self.attr.query_acceleration_max_scale_factor is not None:
            self.flag_dic['query_acceleration_max_scale_factor'] = 1
        else:
            self.flag_dic['query_acceleration_max_scale_factor'] = 0

        if self.attr.max_concurrency_level is not None:
            self.flag_dic['max_concurrency_level'] = 1
        else:
            self.flag_dic['max_concurrency_level'] = 0

        if self.attr.statemet_queued_timeout_in_seconds is not None:
            self.flag_dic['statemet_queued_timeout_in_seconds'] = 1
        else:
            self.flag_dic['statemet_queued_timeout_in_seconds'] = 0

        if self.attr.statement_timeout_in_seconds is not None:
            self.flag_dic['statement_timeout_in_seconds'] = 1
        else:
            self.flag_dic['statement_timeout_in_seconds'] = 0


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_warehouse_qry(self):
        self.qry = f"CREATE OR REPLACE WAREHOUSE IF NOT EXISTS {self.attr.name} "


    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            self.qry = f"{self.qry} WITH "
            for prop in self.property_lst:
                if prop == 'type':
                    self.qry = f" {self.qry} {self.attr.type_label}  = {self.attr.type} "
                if prop == 'size':
                    self.qry = f" {self.qry} {self.attr.size_label} = {self.attr.size} "
                if prop == 'resource_constraint':
                    self.qry = f" {self.qry} {self.attr.resource_constraint_label} = {self.attr.resource_constraint} "
                if prop == 'max_cluster_count':
                    self.qry = f" {self.qry} {self.attr.max_cluster_count_label} = {self.attr.max_cluster_count} "
                if prop == 'min_cluster_count':
                    self.qry = f" {self.qry} {self.attr.min_cluster_count_label} = {self.attr.min_cluster_count} "
                if prop == 'scaling_policy':
                    self.qry = f" {self.qry} {self.attr.scaling_policy_label} = {self.attr.scaling_policy} "
                if prop == 'auto_suspend':
                    self.qry = f" {self.qry} {self.attr.auto_suspend_label} = {self.attr.auto_suspend} "
                if prop == 'auto_resume':
                    self.qry = f" {self.qry} {self.attr.auto_resume_label} = {self.attr.auto_resume} "
                if prop == 'initially_suspended':
                    self.qry = f" {self.qry} {self.attr.initially_suspended_label} = {self.attr.initially_suspended} "
                if prop == 'resource_monitor':
                    self.qry = f" {self.qry} {self.attr.resource_monitor_label} = {self.attr.resource_monitor} "
                if prop == 'comment':
                    self.qry = f" {self.qry} {self.attr.comment_label} = {self.attr.comment} "
                if prop == 'tag':
                    self.qry = f" {self.qry} {self.attr.tag_label} = {self.attr.tag} "
                if prop == 'enable_query_acceleration':
                    self.qry = f" {self.qry} {self.attr.enable_query_acceleration_label} = {self.attr.enable_query_acceleration} "
                if prop == 'query_acceleration_max_scale_factor':
                    self.qry = f" {self.qry} {self.attr.query_acceleration_max_scale_factor_label} = {self.attr.query_acceleration_max_scale_factor} "
                if prop == 'max_concurrency_level':
                    self.qry = f" {self.qry} {self.attr.max_concurrency_level_label} = {self.attr.max_concurrency_level} "
                if prop == 'statemet_queued_timeout_in_seconds':
                    self.qry = f" {self.qry} {self.attr.statemet_queued_timeout_in_seconds_label} = {self.attr.statemet_queued_timeout_in_seconds} "
                if prop == 'statement_timeout_in_seconds':
                    self.qry = f" {self.qry} {self.attr.statement_timeout_in_seconds_label} = {self.attr.statement_timeout_in_seconds} "


    def prepare_create_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_warehouse_qry()
        self.add_properties_to_query()
        
    
    def drop_warehouse(self):
       self.qry = f" DROP WAREHOUSE IF EXISTS {self.attr.name) "
        

        
                 

def main(session,**kwargs):
    if mode == "CREATE":
        wh = Warehouse(session)
        wh.set_name(kwargs[WHV._name_label])
        wh.set_name_label(WHV._name_label)
        wh.set_type(kwargs[WHV._type_label])
        wh.set_type(WHV._type_label)
        wh.set_size(kwargs[WHV._size_label])
        wh.set_size_label(WHV._size_label)
        wh.set_auto_resume(kwargs[WHV._auto_resume_label])
        wh.set_auto_resume_label(WHV._auto_resume_label)
        wh.set_auto_suspend(kwargs[WHV._auto_suspend_label])
        wh.set_auto_suspend_label(WHV._auto_suspend_label)
        wh.set_comment(kwargs[WHV._comment_label])
        wh.set_comment_label(WHV._comment_label)
        wh.set_enable_query_acceleration(kwargs[WHV._enable_query_acceleration_label])
        wh.set_enable_query_acceleration_label(WHV._enable_query_acceleration_label)
        wh.set_initially_suspended(kwargs[WHV._initially_suspended_label])
        wh.set_initially_suspended_label(WHV._initially_suspended_label)
        wh.set_max_cluster_count(kwargs[WHV._max_cluster_count_label])
        wh.set_max_cluster_count_label(WHV._max_cluster_count_label)
        wh.set_resource_constraint(kwargs[WHV._resource_constraint_label])
        wh.set_resource_constraint_label(WHV._resource_constraint_label)
        wh.set_max_concurrency_level(kwargs[WHV._max_concurrency_level_label])
        wh.set_max_concurrency_level_label(WHV._max_concurrency_level_label)
        wh.set_min_cluster_count(kwargs[WHV._min_cluster_count_label])
        wh.set_min_cluster_count_label(WHV._min_cluster_count_label)
        wh.set_query_acceleration_max_scale_factor(WHV._query_acceleration_max_scale_factor_label)
        wh.set_query_acceleration_max_scale_factor_label(WHV._query_acceleration_max_scale_factor_label)
        wh.set_resource_monitor(kwargs[WHV._resource_monitor_label])
        wh.set_resource_monitor_label(WHV._resource_monitor_label)
        wh.set_scaling_policy(kwargs[WHV._scaling_policy_label])
        wh.set_scaling_policy_label(WHV._scaling_policy_label)
        wh.set_statement_timeout_in_seconds(kwargs[WHV._statement_timeout_in_seconds_label])
        wh.set_statement_timeout_in_seconds_label(WHV._statement_timeout_in_seconds_label)
        wh.set_statemet_queued_timeout_in_seconds(WHV._statement_queued_timeout_in_seconds_label)
        wh.set_statemet_queued_timeout_in_seconds_label(WHV._statement_queued_timeout_in_seconds_label)
        wh.set_tag(WHV._tag_label)
        wh.set_tag_label(WHV._tag_label)
        wh.prepare_create_query()
        wh.execute_query(wh.qry)
        
    elif mode == "DROP":
        wh = Warehouse(session)
        wh.set_name(kwargs[WHV._name_label])
        wh.set_name_label(WHV._name_label)
        wh.drop_warehouse()
        wh.execute_query(wh.qry)
        

    return wh.qry
