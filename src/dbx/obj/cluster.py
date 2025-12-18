import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from src.dbx.vars.obj.gvcluster import Cluster_Tags as tags
from src.validation.validatevalue import ValidateValue as vv
from src.validation.validateobject import ValidateObject as vo
from src.usr.user import ChatHistory


class Apply_Policy_:
    def __get__(self, instance, owner):
        return instance._auto_stop_mins
    
    def __set__(self, instance, value):
        instance._auto_stop_mins=value

    def __delete__(self, instance):
        del instance._auto_stop_mins

class ChannelDBSqlVersion:
    def __get__(self, instance, owner):
        return instance._dbsql_version
    
    def __set__(self, instance, value):
        instance._dbsql_version=value

    def __delete__(self, instance):
        del instance._dbsql_version


class ChannelName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name=value

    def __delete__(self, instance):
        del instance._name

class ClusterSize:
    def __get__(self, instance, owner):
        return instance._cluster_size
    
    def __set__(self, instance, value):
        instance._cluster_size=value

    def __delete__(self, instance):
        del instance._cluster_size

class CreatorName:
    def __get__(self, instance, owner):
        return instance._creator_name
    
    def __set__(self, instance, value):
        instance._creator_name=value

    def __delete__(self, instance):
        del instance._creator_name


class EnablePhoton:
    def __get__(self, instance, owner):
        return instance._enable_photon
    
    def __set__(self, instance, value):
        instance._enable_photon=value

    def __delete__(self, instance):
        del instance._enable_photon

class EnableServerlessCompute:
    def __get__(self, instance, owner):
        return instance._enable_serverless_compute
    
    def __set__(self, instance, value):
        instance._enable_serverless_compute=value

    def __delete__(self, instance):
        del instance._enable_serverless_compute

class InstanceProfileARN:
    def __get__(self, instance, owner):
        return instance._instance_profile_arn
    
    def __set__(self, instance, value):
        instance._instance_profile_arn=value

    def __delete__(self, instance):
        del instance._instance_profile_arn

class MaxNumClusters:
    def __get__(self, instance, owner):
        return instance._max_num_clusters
    
    def __set__(self, instance, value):
        instance._max_num_clusters=value

    def __delete__(self, instance):
        del instance._max_num_clusters

class MinNumClusters:
    def __get__(self, instance, owner):
        return instance._min_num_clusters
    
    def __set__(self, instance, value):
        instance._min_num_clusters=value

    def __delete__(self, instance):
        del instance._min_num_clusters

class Name:
    def __get__(self, instance, owner):
        return instance._name
    
    def __set__(self, instance, value):
        instance._name=value

    def __delete__(self, instance):
        del instance._name

class SpotInstancePolicy:
    def __get__(self, instance, owner):
        return instance._spot_instance_policy
    
    def __set__(self, instance, value):
        instance._spot_instance_policy=value

    def __delete__(self, instance):
        del instance._spot_instance_policy

class Tags:
    def __get__(self, instance, owner):
        return instance._tags
    
    def __set__(self, instance, value):
        instance._tags=value

    def __delete__(self, instance):
        del instance._tags


class WarehouseType:
    def __get__(self, instance, owner):
        return instance._warehouse_type
    
    def __set__(self, instance, value):
        instance._warehouse_type=value

    def __delete__(self, instance):
        del instance._warehouse_type


class WarehouseAttrs:
    def __init__(self,parent):
        self.parent=parent

    auto_stop_mins=AutoStopMins()
    channel_dbsql_version=ChannelDBSqlVersion()
    channel_name=ChannelName()
    cluster_size=ClusterSize()
    creator_name=CreatorName()
    enable_photon=EnablePhoton()
    enable_serverless_compute=EnableServerlessCompute()
    instance_profile_arn=InstanceProfileARN()
    max_num_clusters=MaxNumClusters()
    min_num_clusters=MinNumClusters()
    name=Name()
    spot_instance_policy=SpotInstancePolicy()
    tags=Tags()
    warehouse_type=WarehouseType()
    

class Warehouse():
    def __init__(self, session, user_id, logger):
        super().__init__(session=session,user_id=user_id,logger=logger)
        self.attr = WarehouseAttrs(self)
        self.logger = logger.getChild(self.__class__.__name__)


    def set_auto_stop_mins(self, v): self.attr.auto_stop_mins = v
    def set_channel_dbsql_version(self, v): self.attr.channel_dbsql_version = v
    def set_channel_name(self, v): self.attr.channel_name = v
    def set_cluster_size(self, v): self.attr.cluster_size = v
    def set_creator_name(self, v): self.attr.creator_name = v
    def set_enable_photon(self, v): self.attr.enable_photon = v
    def set_enable_serverless_compute(self, v): self.attr.enable_serverless_compute = v
    def set_instance_profile_arn(self, v): self.attr.instance_profile_arn = v
    def set_max_num_clusters(self, v): self.attr.max_num_clusters = v
    def set_min_num_clusters(self, v): self.attr.min_num_clusters = v
    def set_name(self, v): self.attr.name = v
    def set_spot_instance_policy(self, v): self.attr.spot_instance_policy = v
    def set_tags(self, v): self.attr.tags = v
    def set_warehouse_type(self, v): self.attr.warehouse_type = v

    # Object property flags
    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.AUTO_STOP_MINS,"auto_stop_mins")
        #set_flag(tags.CHANNEL_DBSQL_VERSION,"channel_dbsql_version")
        #set_flag(tags.CHANNEL_NAME,"channel_name")
        set_flag(tags.CLUSTER_SIZE,"cluster_size")
        set_flag(tags.CREATOR_NAME,"creator_name")
        set_flag(tags.ENABLE_PHOTON,"enable_photon")
        set_flag(tags.ENABLE_SERVERLESS_COMPUTE,"enables_serverless_compute")
        set_flag(tags.INSTANCE_PROFILE_ARN,"instance_profile_arn")
        set_flag(tags.MAX_NUM_CLUSTERS,"max_num_clusters")
        set_flag(tags.MIN_NUM_CLUSTERS,"min_num_clusters")
        set_flag(tags.NAME,"name")
        set_flag(tags.SPOT_INSTANCE_POLICY,"spot_instance_policy")
        set_flag(tags.TAGS,"tags")
        set_flag(tags.WAREHOUSE_TYPE,"warehouse_type")
        

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

# Different payload specs
#     class Autoscaling_Cluster_Tags:
#     AUTO_SCALE_MAX_WORKERS="AUTO_SCALE_MAX_WORKERS"
#     AUTO_SCALE_MIN_WORKERS="AUTO_SCALE_MIN_WORKERS"
#     AWS_ATTRIBUTES_AVAILABILITY="AWS_ATTRIBUTES_AVAILABILITY"
#     AWS_ATTRIBUTES_EBS_VOLUME_COUNT="AWS_ATTRIBUTES_EBS_VOLUME_COUNT"
#     AWS_ATTRIBUTES_FIRST_ON_DEMAND="AWS_ATTRIBUTES_FIRST_ON_DEMAND"
#     AWS_ATTRIBUTES_SPOT_BID_PRICE_PERCENT="AWS_ATTRIBUTES_SPOT_BID_PRICE_PERCENT"
#     AWS_ATTRIBUTES_ZONE_ID="AWS_ATTRIBUTES_ZONE_ID"
#     CLUSTER_NAME="CLUSTER_NAME"
#     NODE_TYPE_ID="NODE_TYPE_ID"
#     SPARK_VERSION="SPARK_VERSION"

# class Machine_Learning_Runtime_With_Kind_Cluster_Tags:
#     AWS_ATTRIBUTES_AVAILABILITY="AWS_ATTRIBUTES_AVAILABILITY"
#     AWS_ATTRIBUTES_EBS_VOLUME_COUNT="AWS_ATTRIBUTES_EBS_VOLUME_COUNT"
#     AWS_ATTRIBUTES_FIRST_ON_DEMAND="AWS_ATTRIBUTES_FIRST_ON_DEMAND"
#     AWS_ATTRIBUTES_SPOT_BID_PRICE_PERCENT="AWS_ATTRIBUTES_SPOT_BID_PRICE_PERCENT"
#     AWS_ATTRIBUTES_ZONE_ID="AWS_ATTRIBUTES_ZONE_ID"
#     CLUSTER_NAME="CLUSTER_NAME"
#     KIND="KIND"
#     NODE_TYPE_ID="NODE_TYPE_ID"
#     NUM_WORKERS="NUM_WORKERS"
#     SPARK_VERSION="SPARK_VERSION"
#     USE_ML_RUNTIME="USE_ML_RUNTIME"

# class Single_Node_Cluster_Tags:
#     AWS_ATTRIBUTES_AVAILABILITY="AWS_ATTRIBUTES_AVAILABILITY"
#     AWS_ATTRIBUTES_EBS_VOLUME_COUNT="AWS_ATTRIBUTES_EBS_VOLUME_COUNT"
#     AWS_ATTRIBUTES_FIRST_ON_DEMAND="AWS_ATTRIBUTES_FIRST_ON_DEMAND"
#     AWS_ATTRIBUTES_SPOT_BID_PRICE_PERCENT="AWS_ATTRIBUTES_SPOT_BID_PRICE_PERCENT"
#     AWS_ATTRIBUTES_ZONE_ID="AWS_ATTRIBUTES_ZONE_ID"
#     CLUSTER_NAME="CLUSTER_NAME"
#     CUSTOMER_TAGS_RESOURCECLASS="CUSTOMER_TAGS_RESOURCECLASS"
#     NODE_TYPE_ID="NODE_TYPE_ID"
#     NUM_WORKERS="NUM_WORKERS"
#     SPARK_CONF_SPARK_DATABRICKS_CLUSTER_PROFILE="SPARK_CONF_SPARK_DATABRICKS_CLUSTER_PROFILE"
#     SPARK_CONF_MASTER="SPARK_CONF_MASTER"
#     SPARK_VERSION="SPARK_VERSION"
#     USE_ML_RUNTIME="USE_ML_RUNTIME"

# class Single_Node_With_Kind_Cluster_Tags:
#     AWS_ATTRIBUTES_AVAILABILITY="AWS_ATTRIBUTES_AVAILABILITY"
#     AWS_ATTRIBUTES_EBS_VOLUME_COUNT="AWS_ATTRIBUTES_EBS_VOLUME_COUNT"
#     AWS_ATTRIBUTES_FIRST_ON_DEMAND="AWS_ATTRIBUTES_FIRST_ON_DEMAND"
#     AWS_ATTRIBUTES_SPOT_BID_PRICE_PERCENT="AWS_ATTRIBUTES_SPOT_BID_PRICE_PERCENT"
#     AWS_ATTRIBUTES_ZONE_ID="AWS_ATTRIBUTES_ZONE_ID"
#     CLUSTER_NAME="CLUSTER_NAME"
#     IS_SINGLE_NODE="IS_SINGLE_NODE"
#     KIND="KIND"
#     NODE_TYPE_ID="NODE_TYPE_ID"
#     SPARK_VERSION="SPARK_VERSION"

# class Cluster_With_Spot_Instances_Tags:
#     AWS_ATTRIBUTES_AVAILABILITY="AWS_ATTRIBUTES_AVAILABILITY"
#     AWS_ATTRIBUTES_FIRST_ON_DEMAND="AWS_ATTRIBUTES_FIRST_ON_DEMAND"
#     AWS_ATTRIBUTES_ZONE_ID="AWS_ATTRIBUTES_ZONE_ID"
#     CLUSTER_NAME="CLUSTER_NAME"
#     NODE_TYPE_ID="NODE_TYPE_ID"
#     NUM_WORKERS="NUM_WORKERS"
#     SPARK_CONF_SPARK_SPECULATION="SPARK_CONF_SPARK_SPECULATION"
#     SPARK_VERSION="SPARK_VERSION"
    

    def prepare_payload(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.payload={}
        for prop in self.property_lst:
            if prop == tags.AUTO_STOP_MINS:
                self.payload[tags.AUTO_STOP_MINS] = self.attr.auto_stop_mins
            if prop==tags.CLUSTER_SIZE:
                self.payload[tags.CLUSTER_SIZE]=self.attr.cluster_size
            if prop == tags.CREATOR_NAME:
                self.payload[tags.CREATOR_NAME] = self.attr.creator_name
            if prop==tags.ENABLE_PHOTON:
                self.payload[tags.ENABLE_PHOTON]=self.attr.enable_photon
            if prop == tags.ENABLE_SERVERLESS_COMPUTE:
                self.payload[tags.ENABLE_SERVERLESS_COMPUTE] = self.attr.enable_serverless_compute
            if prop==tags.INSTANCE_PROFILE_ARN:
                self.payload[tags.INSTANCE_PROFILE_ARN]=self.attr.instance_profile_arn
            if prop == tags.MAX_NUM_CLUSTERS:
                self.payload[tags.MAX_NUM_CLUSTERS] = self.attr.max_num_clusters
            if prop==tags.MIN_NUM_CLUSTERS:
                self.payload[tags.MIN_NUM_CLUSTERS]=self.attr.min_num_clusters
            if prop == tags.NAME:
                self.payload[tags.NAME] = self.attr.name
            if prop==tags.SPOT_INSTANCE_POLICY:
                self.payload[tags.SPOT_INSTANCE_POLICY]=self.attr.spot_instance_policy
            if prop==tags.WAREHOUSE_TYPE:
                self.payload[tags.WAREHOUSE_TYPE] = self.attr.warehouse_type

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=Warehouse(session=session,
                         user_id=user_id,
                         logger=logger)
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')

        if tags.AUTO_STOP_MINS in kwargs.keys():
            obj_inst.set_auto_stop_mins(kwargs[tags.AUTO_STOP_MINS])
        else:
            obj_inst.set_auto_stop_mins('NONE')
        obj_inst.logger.info(f"set set_auto_stop_mins {obj_inst.attr.auto_stop_mins}")

        #channel_dbsql_version and channel_name
        
        if tags.CLUSTER_SIZE in kwargs.keys():
            obj_inst.set_cluster_size(kwargs[tags.CLUSTER_SIZE])
        else:
            obj_inst.set_cluster_size('NONE')
        obj_inst.logger.info(f"set cluster_size {obj_inst.attr.cluster_size}")

        
        if tags.CREATOR_NAME in kwargs.keys():
            obj_inst.set_creator_name(kwargs[tags.CREATOR_NAME])
        else:
            obj_inst.set_creator_name('NONE')
        obj_inst.logger.info(f"set creator_name {obj_inst.attr.creator_name}")

        
        if tags.ENABLE_PHOTON in kwargs.keys():
            obj_inst.set_enable_photon(kwargs[tags.ENABLE_PHOTON])
        else:
            obj_inst.set_enable_photon('NONE')
        obj_inst.logger.info(f"set enable_photon {obj_inst.attr.enable_photon}")


        if tags.ENABLE_SERVERLESS_COMPUTE in kwargs.keys():
            obj_inst.set_enable_serverless_compute(kwargs[tags.ENABLE_SERVERLESS_COMPUTE])
        else:
            obj_inst.set_enable_serverless_compute('NONE')
        obj_inst.logger.info(f"set enable_serverless_compute {obj_inst.attr.enable_serverless_compute}")


        if tags.INSTANCE_PROFILE_ARN in kwargs.keys():
            obj_inst.set_instance_profile_arn(kwargs[tags.INSTANCE_PROFILE_ARN])
        else:
            obj_inst.set_instance_profile_arn('NONE')
        obj_inst.logger.info(f"set instance_profile_arn {obj_inst.attr.instance_profile_arn}")

        
        if tags.MAX_NUM_CLUSTERS in kwargs.keys():
            obj_inst.set_max_num_clusters(kwargs[tags.MAX_NUM_CLUSTERS])
        else:
            obj_inst.set_max_num_clusters('NONE')
        obj_inst.logger.info(f"set max_num_clusters {obj_inst.attr.max_num_clusters}")

        
        if tags.MIN_NUM_CLUSTERS in kwargs.keys():
            obj_inst.set_min_num_clusters(kwargs[tags.MIN_NUM_CLUSTERS])
        else:
            obj_inst.set_min_num_clusters('NONE')
        obj_inst.logger.info(f"set min_num_clusters {obj_inst.attr.min_num_clusters}")


        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')
        obj_inst.logger.info(f"set name {obj_inst.attr.name}")

        
        if tags.SPOT_INSTANCE_POLICY in kwargs.keys():
            obj_inst.set_spot_instance_policy(kwargs[tags.SPOT_INSTANCE_POLICY])
        else:
            obj_inst.set_spot_instance_policy('NONE')
        obj_inst.logger.info(f"set spot_instance_policy {obj_inst.attr.spot_instance_policy}")

        
        if tags.TAGS in kwargs.keys():
            obj_inst.set_tags(kwargs[tags.TAGS])
        else:
            obj_inst.set_tags('NONE')
        obj_inst.logger.info(f"set tags {obj_inst.attr.tags}")


        if tags.WAREHOUSE_TYPE in kwargs.keys():
            obj_inst.set_warehouse_type(kwargs[tags.WAREHOUSE_TYPE])
        else:
            obj_inst.set_warehouse_type('NONE')
        obj_inst.logger.info(f"set warehouse_type {obj_inst.attr.warehouse_type}")



        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        obj_inst.print_query()
        
        obj_inst.logger.info('execute query')
        obj_inst.execute_final_query()

        obj_inst.logger.info('create deployment entry')
        obj_inst.create_deployment_entry()
        
        obj_inst.write_file_to_git()

        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                           object_identifier=obj_inst.attr.name[0],
                                           qry=obj_inst.qry)


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()


