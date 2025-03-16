# The Snowpark package is required for Python Worksheets. 
# You can add more packages by selecting them using the Packages control and then importing them.

import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))



from vars.gvobject import Warehouse as gv,Config as cfg
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from exception.valueexception import InvalidParamForObject
from dep.deploy import Deploy
from .baseobj import BaseObject 

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

class WarehouseType:
    def __get__(self,instance,owner):
        return instance._warehouse_type

    def __set__(self,instance,value):
        if value=="NONE":
            instance._warehouse_type=value
        else:
            vv.is_allowed_value(value,gv._allowed_values_warehouse_type,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._warehouse_type = f"'{value}'"

    def __delete__(self,instance):
        del instance._warehouse_type

class WarehouseSize:
    def __get__(self,instance,owner):
        return instance._warehouse_size

    def __set__(self,instance,value):
        if value=="NONE":
            instance._warehouse_size=value
        else:
            vv.is_allowed_value(value,gv._allowed_values_warehouse_size,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._warehouse_size = f"'{value}'"

    def __delete__(self,instance):
        del instance._warehouse_size

class ResourceConstraint:
    def __get__(self,instance,owner):
        return instance._resource_constraint

    def __set__(self,instance,value):
        if value == "NONE":
            instance._resource_constraint = "NONE"
        elif instance._warehouse_type == 'SNOWPARK-OPTIMIZED': 
            instance._resource_constraint = value
        else:
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f"for {instance._warehouse_type} warehouse")

    def __delete__(self,instance):
        del instance._resource_constraint

class MaxClusterCount:
    def __get__(self,instance,owner):
        return instance._max_cluster_count

    def __set__(self,instance,value):
        if value=="NONE":
            instance._max_cluster_count=value
        else:
            vv.is_positive_number(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_between(value,1,gv._allowed_max_cluster_size_for_warehouse_type[instance._warehouse_size],instance.parent.__class__.__name__,self.__class__.__name__)
            instance._max_cluster_count = value

    def __delete__(self,instance):
        del instance._max_cluster_count

class MinClusterCount:
    def __get__(self,instance,owner):
        return instance._min_cluster_count

    def __set__(self,instance,value):
        if value=="NONE":
            instance._min_cluster_count=value
        else:
            vv.is_positive_number(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_less_than_or_equal_to(value_base=instance._max_cluster_count,value_ref=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._min_cluster_count=value

    def __delete__(self,instance):
        del instance._min_cluster_count

class ScalingPolicy:
    def __get__(self,instance,owner):
        return instance._scaling_policy

    def __set__(self,instance,value):
        if value=="NONE":
            instance._scaling_policy=value
        else:
            vv.is_allowed_value(value,gv._allowed_values_scaling_policy,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._scaling_policy = value   


    def __delete__(self,instance):
        del instance._scaling_policy

class AutoSuspend:
    def __get__(self,instance,owner):
        return instance._auto_suspend

    def __set__(self,instance,value):
        if value=="NONE":
            instance._auto_suspend=value
        else:
            vv.is_positive_number(value,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._auto_suspend = value

    def __delete__(self,instance):
        del instance._auto_suspend

class AutoResume:
    def __get__(self,instance,owner):
        return instance._auto_resume

    def __set__(self,instance,value):
        if value=="NONE":
            instance._auto_resume=value
        else:
            vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._auto_resume = value

    def __delete__(self,instance):
        del instance._auto_resume

class InitiallySuspended:
    def __get__(self,instance,owner):
        return instance._initially_suspended

    def __set__(self,instance,value):
        if value=="NONE":
            instance._initially_suspended=value
        else:
            vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._initially_suspended = value

    def __delete__(self,instance):
        del instance._initially_suspended

class ResourceMonitor:
    def __get__(self,instance,owner):
        return instance._resource_monitor

    def __set__(self,instance,value):
        if value=="NONE":
            instance._resource_monitor=value
        else:
            vo.resource_monitor_exist(session=instance.parent.session,resource_monitor_name=value)
            instance._resource_monitor = value

    def __delete__(self,instance):
        del instance._resource_monitor

class Comment:
    def __get__(self,instance,owner):
        return instance._comment

    def __set__(self,instance,value):
        if value == "NONE":
            instance._comment = value
        else:
            instance._comment = f"'{value}'"

    def __delete__(self,instance):
        del instance._comment


class EnableQueryAcceleration:
    def __get__(self,instance,owner):
        return instance._enable_query_acceleration

    def __set__(self,instance,value):
        if value=="NONE":
            instance._enable_query_acceleration=value
        else:
            vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._enable_query_acceleration = value

    def __delete__(self,instance):
        del instance._enable_query_acceleration

class QueryAccelerationMaxScaleFactor:
    def __get__(self,instance,owner):
        return instance._query_acceleration_max_scale_factor

    def __set__(self,instance,value):
        if value=="NONE":
            instance._query_acceleration_max_scale_factor=value
        else:
            vv.is_between(value=value,num1=gv._min_value_query_acceleration_max_scale_factor,num2=gv._max_value_query_acceleration_max_scale_factor,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._query_acceleration_max_scale_factor = value

    def __delete__(self,instance):
        del instance._query_acceleration_max_scale_factor

class MaxConcurrencyLevel:
    def __get__(self,instance,owner):
        return instance._max_concurrency_level

    def __set__(self,instance,value):
        if value=="NONE":
            instance._max_concurrency_level=value
        else:
            instance._max_concurrency_level = gv._max_concurrency_level_tag

    def __delete__(self,instance):
        del instance._max_concurrency_level

class StatementQueuedTimeoutInSeconds:
    def __get__(self,instance,owner):
        return instance._statement_queued_timeout_in_seconds

    def __set__(self,instance,value):
        if value=="NONE":
            instance._statement_queued_timeout_in_seconds=value
        else:
            vv.is_positive_number(value,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._statement_queued_timeout_in_seconds = value

    def __delete__(self,instance):
        del instance._statement_queued_timeout_in_seconds

class StatementTimeoutInSeconds:
    def __get__(self,instance,owner):
        return instance._statement_timeout_in_seconds

    def __set__(self,instance,value):
        if value=="NONE":
            instance._statement_timeout_in_seconds=value
        else:
            vv.is_between(value=value,num1=gv._min_value_statement_timeout_in_seconds,num2=gv._max_value_statement_timeout_in_seconds,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._statement_timeout_in_seconds = value

    def __delete__(self,instance):
        del instance._statement_timeout_in_seconds


class WarehouseAttrs:
    def __init__(self,parent):
        self.parent = parent

    name = Name()
    warehouse_size = WarehouseSize()
    warehouse_type = WarehouseType()
    resource_constraint = ResourceConstraint()
    max_cluster_count = MaxClusterCount()
    min_cluster_count = MinClusterCount()
    scaling_policy = ScalingPolicy()
    auto_suspend = AutoSuspend()
    auto_resume = AutoResume()
    initially_suspended = InitiallySuspended()
    resource_monitor = ResourceMonitor()
    comment = Comment()
    enable_query_acceleration = EnableQueryAcceleration()
    query_acceleration_max_scale_factor = QueryAccelerationMaxScaleFactor()
    max_concurrency_level = MaxConcurrencyLevel()
    statement_queued_timeout_in_seconds = StatementQueuedTimeoutInSeconds()
    statement_timeout_in_seconds = StatementTimeoutInSeconds()

class Warehouse(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session, user_id, logger)
        self.attr = WarehouseAttrs(self)

    def set_name(self, value):
        self.attr.name = value

    def set_warehouse_size(self, value):
        self.attr.warehouse_size = value

    def set_warehouse_type(self, value):
        self.attr.warehouse_type = value

    def set_resource_constraint(self, value):
        self.attr.resource_constraint = value

    def set_max_cluster_count(self, value):
        self.attr.max_cluster_count = value

    def set_min_cluster_count(self, value):
        self.attr.min_cluster_count = value

    def set_scaling_policy(self, value):
        self.attr.scaling_policy = value

    def set_auto_suspend(self, value):
        self.attr.auto_suspend = value

    def set_auto_resume(self, value):
        self.attr.auto_resume = value

    def set_initially_suspended(self, value):
        self.attr.initially_suspended = value

    def set_resource_monitor(self, value):
        self.attr.resource_monitor = value

    def set_comment(self, value):
        self.attr.comment = f"'{value}'" 

    def set_enable_query_acceleration(self, value):
        self.attr.enable_query_acceleration = value

    def set_query_acceleration_max_scale_factor(self, value):
        self.attr.query_acceleration_max_scale_factor = value

    def set_max_concurrency_level(self, value):
        self.attr.max_concurrency_level = value

    def set_statement_queued_timeout_in_seconds(self, value):
        self.attr.statement_queued_timeout_in_seconds = value

    def set_statement_timeout_in_seconds(self, value):
        self.attr.statement_timeout_in_seconds = value       

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
            for prop in self.property_lst:
                if prop == gv._warehouse_type_tag:
                    self.qry = f" {self.qry} {gv._warehouse_type_tag}  = {self.attr.warehouse_type} "
                if prop == gv._warehouse_size_tag:
                    self.qry = f" {self.qry} {gv._warehouse_size_tag} = {self.attr.warehouse_size} "
                if prop == gv._resource_constraint_tag:
                    self.qry = f" {self.qry} {gv._resource_constraint_tag} = {self.attr.resource_constraint} "
                if prop == gv._max_cluster_count_tag:
                    self.qry = f" {self.qry} {gv._max_cluster_count_tag} = {self.attr.max_cluster_count} "
                if prop == gv._min_cluster_count_tag:
                    self.qry = f" {self.qry} {gv._min_cluster_count_tag} = {self.attr.min_cluster_count} "
                if prop == gv._scaling_policy_tag:
                    self.qry = f" {self.qry} {gv._scaling_policy_tag} = {self.attr.scaling_policy} "
                if prop == gv._auto_suspend_tag:
                    self.qry = f" {self.qry} {gv._auto_suspend_tag} = {self.attr.auto_suspend} "
                if prop == gv._auto_resume_tag:
                    self.qry = f" {self.qry} {gv._auto_resume_tag} = {self.attr.auto_resume} "
                if prop == gv._initially_suspended_tag:
                    self.qry = f" {self.qry} {gv._initially_suspended_tag} = {self.attr.initially_suspended} "
                if prop == gv._resource_monitor_tag:
                    self.qry = f" {self.qry} {gv._resource_monitor_tag} = {self.attr.resource_monitor} "
                if prop == gv._comment_tag:
                    self.qry = f" {self.qry} {gv._comment_tag} = {self.attr.comment} "
                if prop == gv._enable_query_acceleration_tag:
                    self.qry = f" {self.qry} {gv._enable_query_acceleration_tag} = {self.attr.enable_query_acceleration} "
                if prop == gv._query_acceleration_max_scale_factor_tag:
                    self.qry = f" {self.qry} {gv._query_acceleration_max_scale_factor_tag} = {self.attr.query_acceleration_max_scale_factor} "
                if prop == gv._max_concurrency_level_tag:
                    self.qry = f" {self.qry} {gv._max_concurrency_level_tag} = {self.attr.max_concurrency_level} "
                if prop == gv._statement_queued_timeout_in_seconds_tag:
                    self.qry = f" {self.qry} {gv._statement_queued_timeout_in_seconds_tag} = {self.attr.statement_queued_timeout_in_seconds} "
                if prop == gv._statement_timeout_in_seconds_tag:
                    self.qry = f" {self.qry} {gv._statement_timeout_in_seconds_tag} = {self.attr.statement_timeout_in_seconds} "


    def prepare_create_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_warehouse_qry()
        self.add_properties_to_query()
    
    def create_warehouse(self,*largs):
        self.execute_final_query()         

    def create_object(self,*largs,**kwargs):
        self.set_name(kwargs[gv._name_tag])
        self.set_warehouse_type(kwargs[gv._warehouse_type_tag])
        self.set_warehouse_size(kwargs[gv._warehouse_size_tag])
        self.set_auto_resume(kwargs[gv._auto_resume_tag])
        self.set_auto_suspend(kwargs[gv._auto_suspend_tag])
        self.set_comment(kwargs[gv._comment_tag])
        self.set_enable_query_acceleration(kwargs[gv._enable_query_acceleration_tag])
        self.set_initially_suspended(kwargs[gv._initially_suspended_tag])
        self.set_max_cluster_count(kwargs[gv._max_cluster_count_tag])
        self.set_resource_constraint(kwargs[gv._resource_constraint_tag])
        self.set_max_concurrency_level(kwargs[gv._max_concurrency_level_tag])
        self.set_min_cluster_count(kwargs[gv._min_cluster_count_tag])
        self.set_query_acceleration_max_scale_factor(kwargs[gv._query_acceleration_max_scale_factor_tag])
        self.set_resource_monitor(kwargs[gv._resource_monitor_tag])
        self.set_scaling_policy(kwargs[gv._scaling_policy_tag])
        self.set_statement_timeout_in_seconds(kwargs[gv._statement_timeout_in_seconds_tag])
        self.set_statement_queued_timeout_in_seconds(kwargs[gv._statement_queued_timeout_in_seconds_tag])
        self.prepare_create_query()     
        self.logger.info(f"creating warehouse {self.attr.name}")
        self.create_warehouse()
        if len(largs) == 0:
            self.create_deployment_entry()

    def create_deployment_entry(self):
        deploy_inst = Deploy(self.attr.session)
        self.logger.info(f"Tracking for deployment warehouse object : {self.attr.name}")
        deploy_inst.insert_into_deployment_script_table(qry=self.qry, user_id=self.user_id)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database('NA')
        deploy_inst.set_object_schema('NA')
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()
