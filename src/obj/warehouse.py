# The Snowpark package is required for Python Worksheets. 
# You can add more packages by selecting them using the Packages control and then importing them.

import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))


from global_vars import Warehouse as gv
from validatevalue import ValidateValue as vv

class Name:
    def __get__(self,instance,owner):
        return instance._name

    def __set__(self,instance,value):
        instance._name = value

    def __delete__(self,instance):
        del instance._name

class NameLabel:
    def __get__(self,instance,owner):
        return instance._name_tag

    def __set__(self,instance,value):
        instance._name_tag = value

    def __delete__(self,instance):
        del instance._name_tag

class WarehouseType:
    def __get__(self,instance,owner):
        return instance._warehouse_type

    def __set__(self,instance,value):
        
        if value not in gv._allowed_values_warehouse_type:
            raise ValueError
        else:
            instance._warehouse_type = value

    def __delete__(self,instance):
        del instance._warehouse_type

class WarehouseTypeLabel:
    def __get__(self,instance,owner):
        return instance._warehouse_type_tag

    def __set__(self,instance,value):
        instance._warehouse_type_tag = value

    def __delete__(self,instance):
        del instance._warehouse_type_tag

class WarehouseSize:
    def __get__(self,instance,owner):
        return instance._warehouse_size

    def __set__(self,instance,value):
        if value not in gv._allowed_values_warehouse_size:
            raise ValueError
        else:
            instance._warehouse_size = value

    def __delete__(self,instance):
        del instance._warehouse_size

class WarehouseSizeLabel:
    def __get__(self,instance,owner):
        return instance._warehouse_size_tag

    def __set__(self,instance,value):
        instance._warehouse_size_tag = value

    def __delete__(self,instance):
        del instance._warehouse_size_tag



class ResourceConstraint:
    def __get__(self,instance,owner):
        return instance._resource_constraint

    def __set__(self,instance,value):
        if instance._warehouse_type == 'SNOWPARK-OPTIMIZED': 
            instance._resource_constraint = value
        elif value == "NONE":
            instance._resource_constraint = None
        else:
            raise ValueError

    def __delete__(self,instance):
        del instance._resource_constraint

class ResourceConstraintLabel:
    def __get__(self,instance,owner):
        return instance._resource_constraint_tag

    def __set__(self,instance,value): 
        instance._resource_constraint_tag = value

    def __delete__(self,instance):
        del instance._resource_constraint_tag

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
        return instance._max_cluster_count_tag

    def __set__(self,instance,value):
        instance._max_cluster_count_tag = value

    def __delete__(self,instance):
        del instance._max_cluster_count_tag

class MinClusterCount:
    def __get__(self,instance,owner):
        return instance._min_cluster_count

    def __set__(self,instance,value):
        if value == "NONE":
            instance._min_cluster_count = "NONE"
        elif int(value) >= 1:
            instance._min_cluster_count = value   
        else:
            raise ValueError

    def __delete__(self,instance):
        del instance._min_cluster_count


class MinClusterCountLabel:
    def __get__(self,instance,owner):
        return instance._min_cluster_count_tag

    def __set__(self,instance,value):
        instance._min_cluster_count_tag = value

    def __delete__(self,instance):
        del instance._min_cluster_count_tag

class ScalingPolicy:
    def __get__(self,instance,owner):
        return instance._scaling_policy

    def __set__(self,instance,value):
        if value == "NONE":
            instance._scaling_policy = "NONE"
        elif instance._scaling_policy > 1:
            instance._scaling_policy = value       
        else:
            raise ValueError

    def __delete__(self,instance):
        del instance._scaling_policy


class ScalingPolicyLabel:
    def __get__(self,instance,owner):
        return instance._scaling_policy_tag

    def __set__(self,instance,value):
        instance._scaling_policy_tag = value

    def __delete__(self,instance):
        del instance._scaling_policy_tag


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
        return instance._auto_suspend_tag

    def __set__(self,instance,value):
        instance._auto_suspend_tag = value

    def __delete__(self,instance):
        del instance._auto_suspend_tag

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
        return instance._auto_resume_tag

    def __set__(self,instance,value):
        instance._auto_resume_tag = value


    def __delete__(self,instance):
        del instance._auto_resume_tag

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
        return instance._initially_suspended_tag

    def __set__(self,instance,value):
        instance._initially_suspended_tag = value

    def __delete__(self,instance):
        del instance._initially_suspended_tag

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
        return instance._resource_monitor_tag

    def __set__(self,instance,value):
        instance._resource_monitor_tag = value

    def __delete__(self,instance):
        del instance._resource_monitor_tag

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
        return instance._comment_tag

    def __set__(self,instance,value):
        instance._comment_tag = value

    def __delete__(self,instance):
        del instance._comment_tag


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
        return instance._tag_tag

    def __set__(self,instance,value):
        instance._tag_tag = value

    def __delete__(self,instance):
        del instance._tag_tag


class EnableQueryAcceleration:
    def __get__(self,instance,owner):
        return instance._enable_query_acceleration

    def __set__(self,instance,value):
        if vv.is_bool(value):
            instance._enable_query_acceleration = value
        else:
            raise ValueError

    def __delete__(self,instance):
        del instance._enable_query_acceleration


class EnableQueryAccelerationLabel:
    def __get__(self,instance,owner):
        return instance._enable_query_acceleration_tag

    def __set__(self,instance,value):
        instance._enable_query_acceleration_tag = value

    def __delete__(self,instance):
        del instance._enable_query_acceleration_tag

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
        return instance._query_acceleration_max_scale_factor_tag

    def __set__(self,instance,value):
        instance._query_acceleration_max_scale_factor_tag = value

    def __delete__(self,instance):
        del instance._query_acceleration_max_scale_factor_tag

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
        return instance._max_concurrency_level_tag

    def __set__(self,instance,value):
        instance._max_concurrency_level_tag = value

    def __delete__(self,instance):
        del instance._max_concurrency_level_tag

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
        return instance._statement_queued_timeout_in_seconds_tag

    def __set__(self,instance,value):
        instance._statement_queued_timeout_in_seconds_tag = value

    def __delete__(self,instance):
        del instance._statement_queued_timeout_in_seconds_tag

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
        return instance._statement_timeout_in_seconds_tag

    def __set__(self,instance,value):
        instance._statement_timeout_in_seconds_tag = value

    def __delete__(self,instance):
        del instance._statement_timeout_in_seconds_tag


class WarehouseAttrs:
    def __init__(self,parent):
        self.parent = parent
    name = Name()
    name_tag = NameLabel()
    warehouse_size = WarehouseSize()
    warehouse_size_tag = WarehouseSizeLabel()
    warehouse_type = WarehouseType()
    warehouse_type_tag = WarehouseTypeLabel()
    resource_constraint = ResourceConstraint()
    resource_constraint_tag = ResourceConstraintLabel()
    max_cluster_count = MaxClusterCount()
    max_cluster_count_tag = MaxClusterCountLabel()
    min_cluster_count = MinClusterCount()
    min_cluster_count_tag = MinClusterCountLabel()
    scaling_policy = ScalingPolicy()
    scaling_policy_tag = ScalingPolicyLabel()
    auto_suspend = AutoSuspend()
    auto_suspend_tag = AutoSuspendLabel()
    auto_resume = AutoResume()
    auto_resume_tag = AutoResumeLabel()
    initially_suspended = InitiallySuspended()
    initially_suspended_tag = InitiallySuspendedLabel()
    resource_monitor = ResourceMonitor()
    resource_monitor_tag = ResourceMonitorLabel()
    comment = Comment()
    comment_tag = CommentLabel()
    tag = Tag()
    tag_tag = TagLabel()
    enable_query_acceleration = EnableQueryAcceleration()
    enable_query_acceleration_tag = EnableQueryAccelerationLabel()
    query_acceleration_max_scale_factor = QueryAccelerationMaxScaleFactor()
    query_acceleration_max_scale_factor_tag = QueryAccelerationMaxScaleFactorLabel()
    max_concurrency_level = MaxConcurrencyLevel()
    max_concurrency_level_tag = MaxConcurrencyLevelLabel()
    statement_queued_timeout_in_seconds = StatementQueuedTimeoutInSeconds()
    statement_queued_timeout_in_seconds_tag = StatementQueuedTimeoutInSecondsLabel()
    statement_timeout_in_seconds = StatementTimeoutInSeconds()
    statement_timeout_in_seconds_tag = StatementTimeoutInSecondsLabel()



class Warehouse:
    def __init__(self,session):
        self.attr = WarehouseAttrs(self)
        self.session =  session
        self.qry = ""

    def set_name(self, value):
        self.attr.name = value

    def set_name_tag(self, value):
        self.attr.name_tag = value

    def set_warehouse_size(self, value):
        self.attr.warehouse_size = value

    def set_warehouse_size_tag(self, value):
        self.attr.warehouse_size_tag = value

    def set_warehouse_type(self, value):
        self.attr.warehouse_type = value

    def set_warehouse_type_tag(self, value):
        self.attr.warehouse_type_tag = value

    def set_resource_constraint(self, value):
        self.attr.resource_constraint = value

    def set_resource_constraint_tag(self, value):
        self.attr.resource_constraint_tag = value

    def set_max_cluster_count(self, value):
        self.attr.max_cluster_count = value

    def set_max_cluster_count_tag(self, value):
        self.attr.max_cluster_count_tag = value

    def set_min_cluster_count(self, value):
        self.attr.min_cluster_count = value

    def set_min_cluster_count_tag(self, value):
        self.attr.min_cluster_count_tag = value

    def set_scaling_policy(self, value):
        self.attr.scaling_policy = value

    def set_scaling_policy_tag(self, value):
        self.attr.scaling_policy_tag = value

    def set_auto_suspend(self, value):
        self.attr.auto_suspend = value

    def set_auto_suspend_tag(self, value):
        self.attr.auto_suspend_tag = value

    def set_auto_resume(self, value):
        self.attr.auto_resume = value

    def set_auto_resume_tag(self, value):
        self.attr.auto_resume_tag = value

    def set_initially_suspended(self, value):
        self.attr.initially_suspended = value

    def set_initially_suspended_tag(self, value):
        self.attr.initially_suspended_tag = value

    def set_resource_monitor(self, value):
        self.attr.resource_monitor = value

    def set_resource_monitor_tag(self, value):
        self.attr.resource_monitor_tag = value

    def set_comment(self, value):
        self.attr.comment = value

    def set_comment_tag(self, value):
        self.attr.comment_tag = value

    def set_tag(self, value):
        self.attr.tag = value

    def set_tag_tag(self, value):
        self.attr.tag_tag = value

    def set_enable_query_acceleration(self, value):
        self.attr.enable_query_acceleration = value

    def set_enable_query_acceleration_tag(self, value):
        self.attr.enable_query_acceleration_tag = value

    def set_query_acceleration_max_scale_factor(self, value):
        self.attr.query_acceleration_max_scale_factor = value

    def set_query_acceleration_max_scale_factor_tag(self, value):
        self.attr.query_acceleration_max_scale_factor_tag = value

    def set_max_concurrency_level(self, value):
        self.attr.max_concurrency_level = value

    def set_max_concurrency_level_tag(self, value):
        self.attr.max_concurrency_level_tag = value

    def set_statement_queued_timeout_in_seconds(self, value):
        self.attr.statement_queued_timeout_in_seconds = value

    def set_statement_queued_timeout_in_seconds_tag(self, value):
        self.attr.statement_queued_timeout_in_seconds_tag = value

    def set_statement_timeout_in_seconds(self, value):
        self.attr.statement_timeout_in_seconds = value

    def set_statement_timeout_in_seconds_tag(self, value):
        self.attr.statement_timeout_in_seconds_tag = value
        

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv._name_tag,"_name")
        set_flag(gv._warehouse_size_tag,"_warehouse_size")
        set_flag(gv._warehouse_type_tag,"_warehouse_type")
        set_flag(gv._resource_constraint_tag,"_resource_constraint")
        set_flag(gv._max_cluster_count_tag,"_max_cluster_count")
        set_flag(gv._min_cluster_count_tag,"_min_cluster_count")
        set_flag(gv._scaling_policy_tag,"_scaling_policy")
        set_flag(gv._auto_suspend_tag,"_auto_suspend")
        set_flag(gv._auto_resume_tag,"_auto_resume")
        set_flag(gv._initially_suspended_tag,"_initially_suspended")
        set_flag(gv._resource_monitor_tag,"_resource_monitor")
        set_flag(gv._comment_tag,"_comment")
        set_flag(gv._tag_tag,"_tag")
        set_flag(gv._enable_query_acceleration_tag,"_enable_query_acceleration")
        set_flag(gv._query_acceleration_max_scale_factor_tag,"_query_acceleration_max_scale_factor")
        set_flag(gv._max_concurrency_level_tag,"_max_concurrency_level")
        set_flag(gv._statement_queued_timeout_in_seconds_tag,"_statement_queued_timeout_in_seconds")
        set_flag(gv._statement_timeout_in_seconds_tag,"_statement_timeout_in_seconds")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_warehouse_qry(self):
        self.qry = f"CREATE WAREHOUSE IF NOT EXISTS {self.attr.name} "


    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            self.qry = f"{self.qry} WITH "
            for prop in self.property_lst:
                if prop == 'warehouse_type':
                    self.qry = f" {self.qry} {self.attr.warehouse_type_tag}  = {self.attr.warehouse_type} "
                if prop == 'warehouse_size':
                    self.qry = f" {self.qry} {self.attr.warehouse_size_tag} = {self.attr.warehouse_size} "
                if prop == 'resource_constraint':
                    self.qry = f" {self.qry} {self.attr.resource_constraint_tag} = {self.attr.resource_constraint} "
                if prop == 'max_cluster_count':
                    self.qry = f" {self.qry} {self.attr.max_cluster_count_tag} = {self.attr.max_cluster_count} "
                if prop == 'min_cluster_count':
                    self.qry = f" {self.qry} {self.attr.min_cluster_count_tag} = {self.attr.min_cluster_count} "
                if prop == 'scaling_policy':
                    self.qry = f" {self.qry} {self.attr.scaling_policy_tag} = {self.attr.scaling_policy} "
                if prop == 'auto_suspend':
                    self.qry = f" {self.qry} {self.attr.auto_suspend_tag} = {self.attr.auto_suspend} "
                if prop == 'auto_resume':
                    self.qry = f" {self.qry} {self.attr.auto_resume_tag} = {self.attr.auto_resume} "
                if prop == 'initially_suspended':
                    self.qry = f" {self.qry} {self.attr.initially_suspended_tag} = {self.attr.initially_suspended} "
                if prop == 'resource_monitor':
                    self.qry = f" {self.qry} {self.attr.resource_monitor_tag} = {self.attr.resource_monitor} "
                if prop == 'comment':
                    self.qry = f" {self.qry} {self.attr.comment_tag} = {self.attr.comment} "
                if prop == 'tag':
                    self.qry = f" {self.qry} {self.attr.tag_tag} = {self.attr.tag} "
                if prop == 'enable_query_acceleration':
                    self.qry = f" {self.qry} {self.attr.enable_query_acceleration_tag} = {self.attr.enable_query_acceleration} "
                if prop == 'query_acceleration_max_scale_factor':
                    self.qry = f" {self.qry} {self.attr.query_acceleration_max_scale_factor_tag} = {self.attr.query_acceleration_max_scale_factor} "
                if prop == 'max_concurrency_level':
                    self.qry = f" {self.qry} {self.attr.max_concurrency_level_tag} = {self.attr.max_concurrency_level} "
                if prop == 'statement_queued_timeout_in_seconds':
                    self.qry = f" {self.qry} {self.attr.statement_queued_timeout_in_seconds_tag} = {self.attr.statement_queued_timeout_in_seconds} "
                if prop == 'statement_timeout_in_seconds':
                    self.qry = f" {self.qry} {self.attr.statement_timeout_in_seconds_tag} = {self.attr.statement_timeout_in_seconds} "


    def prepare_create_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_warehouse_qry()
        self.add_properties_to_query()
    
    def create_warehouse(self):
        self.session.sql(self.qry)                    

    def create_object(session,**kwargs):
        wh = Warehouse(session)
        wh.set_name(kwargs[gv._name_tag])
        wh.set_name_tag(gv._name_tag)
        wh.set_warehouse_type(kwargs[gv._warehouse_type_tag])
        wh.set_warehouse_type_tag(gv._warehouse_type_tag)
        wh.set_warehouse_size(kwargs[gv._warehouse_size_tag])
        wh.set_warehouse_size_tag(gv._warehouse_size_tag)
        wh.set_auto_resume(kwargs[gv._auto_resume_tag])
        wh.set_auto_resume_tag(gv._auto_resume_tag)
        wh.set_auto_suspend(kwargs[gv._auto_suspend_tag])
        wh.set_auto_suspend_tag(gv._auto_suspend_tag)
        wh.set_comment(kwargs[gv._comment_tag])
        wh.set_comment_tag(gv._comment_tag)
        wh.set_enable_query_acceleration(kwargs[gv._enable_query_acceleration_tag])
        wh.set_enable_query_acceleration_tag(gv._enable_query_acceleration_tag)
        wh.set_initially_suspended(kwargs[gv._initially_suspended_tag])
        wh.set_initially_suspended_tag(gv._initially_suspended_tag)
        wh.set_max_cluster_count(kwargs[gv._max_cluster_count_tag])
        wh.set_max_cluster_count_tag(gv._max_cluster_count_tag)
        wh.set_resource_constraint(kwargs[gv._resource_constraint_tag])
        wh.set_resource_constraint_tag(gv._resource_constraint_tag)
        wh.set_max_concurrency_level(kwargs[gv._max_concurrency_level_tag])
        wh.set_max_concurrency_level_tag(gv._max_concurrency_level_tag)
        wh.set_min_cluster_count(kwargs[gv._min_cluster_count_tag])
        wh.set_min_cluster_count_tag(gv._min_cluster_count_tag)
        wh.set_query_acceleration_max_scale_factor(gv._query_acceleration_max_scale_factor_tag)
        wh.set_query_acceleration_max_scale_factor_tag(gv._query_acceleration_max_scale_factor_tag)
        wh.set_resource_monitor(kwargs[gv._resource_monitor_tag])
        wh.set_resource_monitor_tag(gv._resource_monitor_tag)
        wh.set_scaling_policy(kwargs[gv._scaling_policy_tag])
        wh.set_scaling_policy_tag(gv._scaling_policy_tag)
        wh.set_statement_timeout_in_seconds(kwargs[gv._statement_timeout_in_seconds_tag])
        wh.set_statement_timeout_in_seconds_tag(gv._statement_timeout_in_seconds_tag)
        wh.set_statement_queued_timeout_in_seconds(gv._statement_queued_timeout_in_seconds_tag)
        wh.set_statement_queued_timeout_in_seconds_tag(gv._statement_queued_timeout_in_seconds_tag)
        wh.set_tag(gv._tag_tag)
        wh.set_tag_tag(gv._tag_tag)
        wh.prepare_create_query()     
        wh.create_warehouse()
