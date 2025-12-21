import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from src.dbx.vars.obj.gvcluster import ClusterTags as tags
from src.validation.validatevalue import ValidateValue as vv
from src.validation.validateobject import ValidateObject as vo
from src.usr.user import ChatHistory


class ClusterType:
    def __get__(self, instance, owner):
        return instance._cluster_type
    
    def __set__(self, instance, value):
        # Bot should first ask for what type of cluster user wants to create.
        vv.is_allowed_value(value=value,
                            allowed_list=tags.allowed_value_list().get(tags.CLUSTER_TYPE),
                            object_type=instance.parent.__class__.__name__,
                            attr_name=self.__class__.__name__
                            )
        instance._cluster_type=value

    def __delete__(self, instance):
        del instance._cluster_type

class ApplyPolicyDefaultValues:
    def __get__(self, instance, owner):
        return instance._apply_policy_default_values
    
    def __set__(self, instance, value):
        instance._apply_policy_default_values=value

    def __delete__(self, instance):
        del instance._apply_policy_default_values


class AutoScaleMaxWorkers:
    def __get__(self, instance, owner):
        return instance._auto_scale_max_workers
    
    def __set__(self, instance, value):
        vv.is_greater_than_or_equal_to(value_base=value,
                                    value_ref=instance._auto_scale_min_workers,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        instance._auto_scale_max_workers=value

    def __delete__(self, instance):
        del instance._auto_scale_max_workers


class AutoScaleMinWorkers:
    def __get__(self, instance, owner):
        return instance._auto_scale_min_workers
    
    def __set__(self, instance, value):
        if instance._cluster_type=='AUTO_SCALING':
            vv.required_attribute_check(value=value,
                                        object_type=instance.parent.__class__.__name__,
                                        attr_name=self.__class__.__name__)
            
            instance._auto_scale_min_workers=value

    def __delete__(self, instance):
        del instance._auto_scale_min_workers


class AutoterminationMinutes:
    def __get__(self, instance, owner):
        return instance._autotermination_minutes
    
    def __set__(self, instance, value):
        instance._autotermination_minutes=value

    def __delete__(self, instance):
        del instance._autotermination_minutes

class AwsAttributesAvailability:
    def __get__(self, instance, owner):
        return instance._aws_attributes_availability
    
    def __set__(self, instance, value):
        instance._aws_attributes_availability=value

    def __delete__(self, instance):
        del instance._aws_attributes_availability

class AwsAttributesEbsVolumeCount:
    def __get__(self, instance, owner):
        return instance._aws_attributes_ebs_volume_count
    
    def __set__(self, instance, value):
        instance._aws_attributes_ebs_volume_count=value

    def __delete__(self, instance):
        del instance._aws_attributes_ebs_volume_count


class AwsAttributesEbsVolumeIops:
    def __get__(self, instance, owner):
        return instance._aws_attributes_ebs_volume_iops
    
    def __set__(self, instance, value):
        instance._aws_attributes_ebs_volume_iops=value

    def __delete__(self, instance):
        del instance._aws_attributes_ebs_volume_iops

class AwsAttributesEbsVolumeSize:
    def __get__(self, instance, owner):
        return instance._aws_attributes_ebs_volume_size
    
    def __set__(self, instance, value):
        instance._aws_attributes_ebs_volume_size=value

    def __delete__(self, instance):
        del instance._aws_attributes_ebs_volume_size

class AwsAttributesEbsVolumeThroughput:
    def __get__(self, instance, owner):
        return instance._aws_attributes_ebs_volume_throughput
    
    def __set__(self, instance, value):
        instance._aws_attributes_ebs_volume_throughput=value

    def __delete__(self, instance):
        del instance._aws_attributes_ebs_volume_throughput

class AwsAttributesEbsVolumeType:
    def __get__(self, instance, owner):
        return instance._aws_attributes_ebs_volume_type
    
    def __set__(self, instance, value):
        instance._aws_attributes_ebs_volume_type=value

    def __delete__(self, instance):
        del instance._aws_attributes_ebs_volume_type

class AwsAttributesFirstOnDemand:
    def __get__(self, instance, owner):
        return instance._aws_attributes_first_on_demand
    
    def __set__(self, instance, value):
        instance._aws_attributes_first_on_demand=value

    def __delete__(self, instance):
        del instance._aws_attributes_first_on_demand

class AwsAttributesInstanceProfileArn:
    def __get__(self, instance, owner):
        return instance._aws_attributes_instance_profile_arn
    
    def __set__(self, instance, value):
        instance._aws_attributes_instance_profile_arn=value

    def __delete__(self, instance):
        del instance._aws_attributes_instance_profile_arn

class AwsAttributesSpotBidPricePercent:
    def __get__(self, instance, owner):
        return instance._aws_attributes_spot_bid_price_percent
    
    def __set__(self, instance, value):
        instance._aws_attributes_spot_bid_price_percent=value

    def __delete__(self, instance):
        del instance._aws_attributes_spot_bid_price_percent

class AwsAttributesZoneID:
    def __get__(self, instance, owner):
        return instance._aws_attributes_zone_id
    
    def __set__(self, instance, value):
        instance._aws_attributes_zone_id=value

    def __delete__(self, instance):
        del instance._aws_attributes_zone_id


class CloneFromSourceClusterID:
    def __get__(self, instance, owner):
        return instance._clone_from_source_cluster_id
    
    def __set__(self, instance, value):
        instance._clone_from_source_cluster_id=value

    def __delete__(self, instance):
        del instance._clone_from_source_cluster_id

class ClusterLogConfDbfs:
    def __get__(self, instance, owner):
        return instance._cluster_log_conf_dbfs
    
    def __set__(self, instance, value):
        instance._cluster_log_conf_dbfs=value

    def __delete__(self, instance):
        del instance._cluster_log_conf_dbfs

class ClusterLogConfS3:
    def __get__(self, instance, owner):
        return instance._cluster_log_conf_s3
    
    def __set__(self, instance, value):
        instance._cluster_log_conf_s3=value

    def __delete__(self, instance):
        del instance._cluster_log_conf_s3

class ClusterLogConfVolumesDestinations:
    def __get__(self, instance, owner):
        return instance._cluster_log_conf_volumes_destinations
    
    def __set__(self, instance, value):
        instance._cluster_log_conf_volumes_destinations=value

    def __delete__(self, instance):
        del instance._cluster_log_conf_volumes_destinations

class ClusterName:
    def __get__(self, instance, owner):
        return instance._cluster_name
    
    def __set__(self, instance, value):
        # vo.cluster_exist() TBA
        instance._cluster_name=value

    def __delete__(self, instance):
        del instance._cluster_name

class CustomTagsResourceClass:
    def __get__(self, instance, owner):
        return instance._custom_tags_resourceclass
    
    def __set__(self, instance, value):
        instance._custom_tags_resourceclass=value

    def __delete__(self, instance):
        del instance._custom_tags_resourceclass

class DataSecurityMode:
    def __get__(self, instance, owner):
        return instance._data_security_mode
    
    def __set__(self, instance, value):
        instance._data_security_mode=value

    def __delete__(self, instance):
        del instance._data_security_mode

class DockerImageBasicAuth:
    def __get__(self, instance, owner):
        return instance._docker_image_basic_auth
    
    def __set__(self, instance, value):
        instance._docker_image_basic_auth=value

    def __delete__(self, instance):
        del instance._docker_image_basic_auth

class DockerImageURL:
    def __get__(self, instance, owner):
        return instance._docker_image_url
    
    def __set__(self, instance, value):
        instance._docker_image_url=value

    def __delete__(self, instance):
        del instance._docker_image_url


class DriverInstancePoolID:
    def __get__(self, instance, owner):
        return instance._driver_instance_pool_id
    
    def __set__(self, instance, value):
        instance._driver_instance_pool_id=value

    def __delete__(self, instance):
        del instance._driver_instance_pool_id


class DriverNodeTypeID:
    def __get__(self, instance, owner):
        return instance._driver_node_type_id
    
    def __set__(self, instance, value):
        instance._driver_node_type_id=value

    def __delete__(self, instance):
        del instance._driver_node_type_id


class EnableElasticDisk:
    def __get__(self, instance, owner):
        return instance._enable_elastic_disk
    
    def __set__(self, instance, value):
        instance._enable_elastic_disk=value

    def __delete__(self, instance):
        del instance._enable_elastic_disk


class EnableLocalDiskEncryption:
    def __get__(self, instance, owner):
        return instance._enable_local_disk_encryption
    
    def __set__(self, instance, value):
        instance._enable_local_disk_encryption=value

    def __delete__(self, instance):
        del instance._enable_local_disk_encryption


class InitScriptsAbfssDestination:
    def __get__(self, instance, owner):
        return instance._init_scripts_abfss_destination
    
    def __set__(self, instance, value):
        instance._init_scripts_abfss_destination=value

    def __delete__(self, instance):
        del instance._init_scripts_abfss_destination


class InitScriptsDbfsDestination:
    def __get__(self, instance, owner):
        return instance._init_scripts_dbfs_destination
    
    def __set__(self, instance, value):
        instance._init_scripts_dbfs_destination=value

    def __delete__(self, instance):
        del instance._init_scripts_dbfs_destination


class InitScriptsFileDestination:
    def __get__(self, instance, owner):
        return instance._init_scripts_file_destination
    
    def __set__(self, instance, value):
        instance._init_scripts_file_destination=value

    def __delete__(self, instance):
        del instance._init_scripts_file_destination


class InitScriptsGcsDestination:
    def __get__(self, instance, owner):
        return instance._init_scripts_gcs_destination
    
    def __set__(self, instance, value):
        instance._init_scripts_gcs_destination=value

    def __delete__(self, instance):
        del instance._init_scripts_gcs_destination


class InitScriptsS3CannedAcl:
    def __get__(self, instance, owner):
        return instance._init_scripts_s3_canned_acl
    
    def __set__(self, instance, value):
        instance._init_scripts_s3_canned_acl=value

    def __delete__(self, instance):
        del instance._init_scripts_s3_canned_acl


class InitScriptsS3Destination:
    def __get__(self, instance, owner):
        return instance._init_scripts_s3_destination
    
    def __set__(self, instance, value):
        instance._init_scripts_s3_destination=value

    def __delete__(self, instance):
        del instance._init_scripts_s3_destination


class InitScriptsS3EnableEncryption:
    def __get__(self, instance, owner):
        return instance._init_scripts_s3_enable_encryption
    
    def __set__(self, instance, value):
        instance._init_scripts_s3_enable_encryption=value

    def __delete__(self, instance):
        del instance._init_scripts_s3_enable_encryption


class InitScriptsS3EncryptionType:
    def __get__(self, instance, owner):
        return instance._init_scripts_s3_encryption_type
    
    def __set__(self, instance, value):
        instance._init_scripts_s3_encryption_type=value

    def __delete__(self, instance):
        del instance._init_scripts_s3_encryption_type


class InitScriptsS3Endpoint:
    def __get__(self, instance, owner):
        return instance._init_scripts_s3_endpoint
    
    def __set__(self, instance, value):
        instance._init_scripts_s3_endpoint=value

    def __delete__(self, instance):
        del instance._init_scripts_s3_endpoint


class InitScriptsS3KMSKey:
    def __get__(self, instance, owner):
        return instance._init_scripts_s3_kms_key
    
    def __set__(self, instance, value):
        instance._init_scripts_s3_kms_key=value

    def __delete__(self, instance):
        del instance._init_scripts_s3_kms_key


class InitScriptsS3Region:
    def __get__(self, instance, owner):
        return instance._init_scripts_s3_region
    
    def __set__(self, instance, value):
        instance._init_scripts_s3_region=value

    def __delete__(self, instance):
        del instance._init_scripts_s3_region


class InitScriptsVolumesDestination:
    def __get__(self, instance, owner):
        return instance._init_scripts_volumes_destination
    
    def __set__(self, instance, value):
        instance._init_scripts_volumes_destination=value

    def __delete__(self, instance):
        del instance._init_scripts_volumes_destination


class InitScriptsWorkspaceDestination:
    def __get__(self, instance, owner):
        return instance._init_scripts_workspace_destination
    
    def __set__(self, instance, value):
        instance._init_scripts_workspace_destination=value

    def __delete__(self, instance):
        del instance._init_scripts_workspace_destination
    

class InstancePoolID:
    def __get__(self, instance, owner):
        return instance._instance_pool_id
    
    def __set__(self, instance, value):
        instance._instance_pool_id=value

    def __delete__(self, instance):
        del instance._instance_pool_id


class IsSingleNode:
    def __get__(self, instance, owner):
        return instance._is_single_node
    
    def __set__(self, instance, value):
        instance._is_single_node=value

    def __delete__(self, instance):
        del instance._is_single_node


class Kind:
    def __get__(self, instance, owner):
        return instance._kind
    
    def __set__(self, instance, value):
        instance._kind=value

    def __delete__(self, instance):
        del instance._kind


class NodeTypeID:
    def __get__(self, instance, owner):
        return instance._node_type_id
    
    def __set__(self, instance, value):
        instance._node_type_id=value

    def __delete__(self, instance):
        del instance._node_type_id


class NumWorkers:
    def __get__(self, instance, owner):
        return instance._num_workers
    
    def __set__(self, instance, value):
        instance._num_workers=value

    def __delete__(self, instance):
        del instance._num_workers


class PolicyID:
    def __get__(self, instance, owner):
        return instance._policy_id
    
    def __set__(self, instance, value):
        instance._policy_id=value

    def __delete__(self, instance):
        del instance._policy_id


class RuntimeEngine:
    def __get__(self, instance, owner):
        return instance._runtime_engine
    
    def __set__(self, instance, value):
        instance._runtime_engine=value

    def __delete__(self, instance):
        del instance._runtime_engine


class SingleUserName:
    def __get__(self, instance, owner):
        return instance._single_user_name
    
    def __set__(self, instance, value):
        instance._single_user_name=value

    def __delete__(self, instance):
        del instance._single_user_name


class SparkConfSparkDatabricksClusterProfile:
    def __get__(self, instance, owner):
        return instance._spark_conf_spark_databricks_cluster_profile
    
    def __set__(self, instance, value):
        instance._spark_conf_spark_databricks_cluster_profile=value

    def __delete__(self, instance):
        del instance._spark_conf_spark_databricks_cluster_profile


class SparkConfMaster:
    def __get__(self, instance, owner):
        return instance._spark_conf_master
    
    def __set__(self, instance, value):
        instance._spark_conf_master=value

    def __delete__(self, instance):
        del instance._spark_conf_master


class SparkEnvVarsSparkWorkerMemory:
    def __get__(self, instance, owner):
        return instance._spark_env_vars_spark_worker_memory
    
    def __set__(self, instance, value):
        instance._spark_env_vars_spark_worker_memory=value

    def __delete__(self, instance):
        del instance._spark_env_vars_spark_worker_memory


class SparkEnvVarsSparkDaemonJavaOpts:
    def __get__(self, instance, owner):
        return instance._spark_env_vars_spark_daemon_java_opts
    
    def __set__(self, instance, value):
        instance._spark_env_vars_spark_daemon_java_opts=value

    def __delete__(self, instance):
        del instance._spark_env_vars_spark_daemon_java_opts


class SparkVersion:
    def __get__(self, instance, owner):
        return instance._spark_version
    
    def __set__(self, instance, value):
        instance._spark_version=value

    def __delete__(self, instance):
        del instance._spark_version


class SSHPublicKeys:
    def __get__(self, instance, owner):
        return instance._ssh_public_keys
    
    def __set__(self, instance, value):
        instance._ssh_public_keys=value

    def __delete__(self, instance):
        del instance._ssh_public_keys


class UseMLRuntime:
    def __get__(self, instance, owner):
        return instance._use_ml_runtime
    
    def __set__(self, instance, value):
        instance._use_ml_runtime=value

    def __delete__(self, instance):
        del instance._use_ml_runtime


class WorkloadTypeClientsJobs:
    def __get__(self, instance, owner):
        return instance._workload_type_clients_jobs
    
    def __set__(self, instance, value):
        instance._workload_type_clients_jobs=value

    def __delete__(self, instance):
        del instance._workload_type_clients_jobs


class WorkloadTypeClientsNotebooks:
    def __get__(self, instance, owner):
        return instance._workload_type_clients_notebooks
    
    def __set__(self, instance, value):
        instance._workload_type_clients_notebooks=value

    def __delete__(self, instance):
        del instance._workload_type_clients_notebooks



class ClusterAttrs:
    def __init__(self,parent):
        self.parent=parent
    
    cluster_type=ClusterType()
    apply_policy_default_values=ApplyPolicyDefaultValues()
    auto_scale_max_workers=AutoScaleMaxWorkers()
    auto_scale_min_workers=AutoScaleMinWorkers()
    autotermination_minutes=AutoterminationMinutes()
    aws_attributes_availability=AwsAttributesAvailability()
    aws_attributes_ebs_volume_count=AwsAttributesEbsVolumeCount()
    aws_attributes_ebs_volume_iops=AwsAttributesEbsVolumeIops()
    aws_attributes_ebs_volume_size=AwsAttributesEbsVolumeSize()
    aws_attributes_ebs_volume_throughput=AwsAttributesEbsVolumeThroughput
    aws_attributes_ebs_volume_type=AwsAttributesEbsVolumeType()
    aws_attributes_first_on_demand=AwsAttributesFirstOnDemand()
    aws_attributes_instance_profile_arn=AwsAttributesInstanceProfileArn()
    aws_attributes_spot_bid_price_percent=AwsAttributesSpotBidPricePercent()
    aws_attributes_zone_id=AwsAttributesZoneID()
    clone_from_source_cluster_id=CloneFromSourceClusterID()
    cluster_log_conf_dbfs=ClusterLogConfDbfs()
    cluster_log_conf_s3=ClusterLogConfS3()
    cluster_log_conf_volumes_destinations=ClusterLogConfVolumesDestinations()
    cluster_name=ClusterName()
    custom_tags_resourceclass=CustomTagsResourceClass()
    data_security_mode=DataSecurityMode()
    docker_image_basic_auth=DockerImageBasicAuth()
    docker_image_url=DockerImageURL()
    driver_instance_pool_id=DriverInstancePoolID()
    driver_node_type_id=DriverNodeTypeID()
    enable_elastic_disk=EnableElasticDisk()
    enable_local_disk_encryption=EnableLocalDiskEncryption()
    init_scripts_abfss_destination=InitScriptsAbfssDestination()
    init_scripts_dbfs_destination=InitScriptsDbfsDestination()
    init_scripts_file_destination=InitScriptsFileDestination()
    init_scripts_gcs_destination=InitScriptsGcsDestination()
    init_scripts_s3_canned_acl=InitScriptsS3CannedAcl()
    init_scripts_s3_destination=InitScriptsS3Destination()
    init_scripts_s3_enable_encryption=InitScriptsS3EnableEncryption()
    init_scripts_s3_encryption_type=InitScriptsS3EncryptionType()
    init_scripts_s3_endpoint=InitScriptsS3Endpoint()
    init_scripts_s3_kms_key=InitScriptsS3KMSKey()
    init_scripts_s3_region=InitScriptsS3Region()
    init_scripts_volumes_destination=InitScriptsVolumesDestination()
    init_scripts_workspace_destination=InitScriptsWorkspaceDestination()
    instance_pool_id=InstancePoolID()
    is_single_node=IsSingleNode()
    kind=Kind()
    node_type_id=NodeTypeID()
    num_workers=NumWorkers()
    policy_id=PolicyID()
    runtime_engine=RuntimeEngine()
    single_user_name=SingleUserName()
    spark_conf_spark_databricks_cluster_profile=SparkConfSparkDatabricksClusterProfile()
    spark_conf_master=SparkConfMaster()
    spark_env_vars_spark_worker_memory=SparkEnvVarsSparkWorkerMemory()
    spark_env_vars_spark_daemon_java_opts=SparkEnvVarsSparkDaemonJavaOpts()
    spark_version=SparkVersion()
    ssh_public_keys=SSHPublicKeys()
    use_ml_runtime=UseMLRuntime()
    workload_type_clients_jobs=WorkloadTypeClientsJobs()
    workload_type_clients_notebooks=WorkloadTypeClientsNotebooks()


class Cluster():
    def __init__(self, session, user_id, logger):
        super().__init__(session=session,user_id=user_id,logger=logger)
        self.attr = ClusterAttrs(self)
        self.logger = logger.getChild(self.__class__.__name__)

    def cluster_type(self,v): self.attr.cluster_type=v
    def set_apply_policy_default_values(self, v): self.attr.apply_policy_default_values = v
    def set_auto_scale_min_workers(self, v): self.attr.auto_scale_min_workers = v
    def set_auto_scale_max_workers(self, v): self.attr.auto_scale_max_workers = v
    def set_autotermination_minutes(self, v): self.attr.autotermination_minutes = v
    def set_aws_attributes_availability(self, v): self.attr.aws_attributes_availability = v
    def set_aws_attributes_ebs_volume_count(self, v): self.attr.aws_attributes_ebs_volume_count = v
    def set_aws_attributes_ebs_volume_iops(self, v): self.attr.aws_attributes_ebs_volume_iops = v
    def set_aws_attributes_ebs_volume_size(self, v): self.attr.aws_attributes_ebs_volume_size = v
    def set_aws_attributes_ebs_volume_throughput(self, v): self.attr.aws_attributes_ebs_volume_throughput = v
    def set_aws_attributes_ebs_volume_type(self, v): self.attr.aws_attributes_ebs_volume_type = v
    def set_aws_attributes_first_on_demand(self, v): self.attr.aws_attributes_first_on_demand = v
    def set_aws_attributes_instance_profile_arn(self, v): self.attr.aws_attributes_instance_profile_arn = v
    def set_aws_attributes_spot_bid_price_percent(self, v): self.attr.aws_attributes_spot_bid_price_percent = v
    def set_aws_attributes_zone_id(self, v): self.attr.aws_attributes_zone_id = v
    def set_clone_from_source_cluster_id(self, v): self.attr.clone_from_source_cluster_id = v
    def set_cluster_log_conf_dbfs(self, v): self.attr.cluster_log_conf_dbfs = v
    def set_cluster_log_conf_s3(self, v): self.attr.cluster_log_conf_s3 = v
    def set_cluster_log_conf_volumes_destinations(self, v): self.attr.cluster_log_conf_volumes_destinations = v
    def set_cluster_name(self, v): self.attr.cluster_name = v
    def set_custom_tags_resourceclass(self, v): self.attr.custom_tags_resourceclass = v
    def set_data_security_mode(self, v): self.attr.data_security_mode = v
    def set_docker_image_basic_auth(self, v): self.attr.docker_image_basic_auth = v
    def set_docker_image_url(self, v): self.attr.docker_image_url = v
    def set_driver_instance_pool_id(self, v): self.attr.driver_instance_pool_id = v
    def set_driver_node_type_id(self, v): self.attr.driver_node_type_id = v
    def set_enable_elastic_disk(self, v): self.attr.enable_elastic_disk = v
    def set_enable_local_disk_encryption(self, v): self.attr.enable_local_disk_encryption = v
    def set_init_scripts_abfss_destination(self, v): self.attr.init_scripts_abfss_destination = v
    def set_init_scripts_dbfs_destination(self, v): self.attr.init_scripts_dbfs_destination = v
    def set_init_scripts_file_destination(self, v): self.attr.init_scripts_file_destination = v
    def set_init_scripts_gcs_destination(self, v): self.attr.init_scripts_gcs_destination = v
    def set_init_scripts_s3_canned_acl(self, v): self.attr.init_scripts_s3_canned_acl = v
    def set_init_scripts_s3_destination(self, v): self.attr.init_scripts_s3_destination = v
    def set_init_scripts_s3_enable_encryption(self, v): self.attr.init_scripts_s3_enable_encryption = v
    def set_init_scripts_s3_encryption_type(self, v): self.attr.init_scripts_s3_encryption_type = v
    def set_init_scripts_s3_endpoint(self, v): self.attr.init_scripts_s3_endpoint = v
    def set_init_scripts_s3_kms_key(self, v): self.attr.init_scripts_s3_kms_key = v
    def set_init_scripts_s3_region(self, v): self.attr.init_scripts_s3_region = v
    def set_init_scripts_volumes_destination(self, v): self.attr.init_scripts_volumes_destination = v
    def set_init_scripts_workspace_destination(self, v): self.attr.init_scripts_workspace_destination = v
    def set_instance_pool_id(self, v): self.attr.instance_pool_id = v
    def set_is_single_node(self, v): self.attr.is_single_node = v
    def set_kind(self, v): self.attr.kind = v
    def set_node_type_id(self, v): self.attr.node_type_id = v
    def set_num_workers(self, v): self.attr.num_workers = v
    def set_policy_id(self, v): self.attr.policy_id = v
    def set_runtime_engine(self, v): self.attr.runtime_engine = v
    def set_single_user_name(self, v): self.attr.single_user_name = v
    def set_spark_conf_spark_databricks_cluster_profile(self, v): self.attr.spark_conf_spark_databricks_cluster_profile = v
    def set_spark_conf_master(self, v): self.attr.spark_conf_master = v
    def set_spark_env_vars_spark_worker_memory(self, v): self.attr.spark_env_vars_spark_worker_memory = v
    def set_spark_env_vars_spark_daemon_java_opts(self, v): self.attr.spark_env_vars_spark_daemon_java_opts = v
    def set_spark_version(self, v): self.attr.spark_version = v
    def set_ssh_public_keys(self, v): self.attr.ssh_public_keys = v
    def set_use_ml_runtime(self, v): self.attr.use_ml_runtime = v
    def set_workload_type_clients_jobs(self, v): self.attr.workload_type_clients_jobs = v
    def set_workload_type_clients_notebooks(self, v): self.attr.workload_type_clients_notebooks = v

    # Object property flags
    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.APPLY_POLICY_DEFAULT_VALUES, "apply_policy_default_values")
        set_flag(tags.AUTO_SCALE_MAX_WORKERS,"auto_scale_max_workers")
        set_flag(tags.AUTO_SCALE_MIN_WORKERS,"auto_scale_min_workers")
        set_flag(tags.AUTOTERMINATION_MINUTES,"autotermination_minutes")
        set_flag(tags.AWS_ATTRIBUTES_AVAILABILITY,"aws_attributes_availability")
        set_flag(tags.AWS_ATTRIBUTES_EBS_VOLUME_COUNT,"aws_attributes_ebs_volume_count")
        set_flag(tags.AWS_ATTRIBUTES_EBS_VOLUME_IOPS,"aws_attributes_ebs_volume_iops")
        set_flag(tags.AWS_ATTRIBUTES_EBS_VOLUME_SIZE,"aws_attributes_ebs_volume_size")
        set_flag(tags.AWS_ATTRIBUTES_EBS_VOLUME_THROUGHPUT,"aws_attributes_ebs_volume_throughput")
        set_flag(tags.AWS_ATTRIBUTES_EBS_VOLUME_TYPE,"aws_attributes_ebs_volume_type")
        set_flag(tags.AWS_ATTRIBUTES_FIRST_ON_DEMAND,"aws_attributes_first_on_demand")
        set_flag(tags.AWS_ATTRIBUTES_INSTANCE_PROFILE_ARN,"aws_attributes_instance_profile_arn")
        set_flag(tags.AWS_ATTRIBUTES_SPOT_BID_PRICE_PERCENT,"aws_attributes_spot_bid_price_percent")
        set_flag(tags.AWS_ATTRIBUTES_ZONE_ID,"aws_attributes_zone_id")
        set_flag(tags.CLONE_FROM_SOURCE_CLUSTER_ID,"clone_from_source_cluster_id")
        set_flag(tags.CLUSTER_LOG_CONF_DBFS,"cluster_log_conf_dbfs")
        set_flag(tags.CLUSTER_LOG_CONF_S3,"cluster_log_conf_s3")
        set_flag(tags.CLUSTER_LOG_CONF_VOLUMES_DESTINATIONS,"cluster_log_conf_volumes_destinations")
        set_flag(tags.CLUSTER_NAME,"cluster_name")
        set_flag(tags.CUSTOM_TAGS_RESOURCECLASS,"custom_tags_resourceclass")
        set_flag(tags.DATA_SECURITY_MODE,"data_security_mode")
        set_flag(tags.DOCKER_IMAGE_BASIC_AUTH,"docker_image_basic_auth")
        set_flag(tags.DOCKER_IMAGE_URL,"docker_image_url")
        set_flag(tags.DRIVER_INSTANCE_POOL_ID,"driver_instance_pool_id")
        set_flag(tags.DRIVER_NODE_TYPE_ID,"driver_node_type_id")
        set_flag(tags.ENABLE_ELASTIC_DISK,"enable_elastic_disk")
        set_flag(tags.ENABLE_LOCAL_DISK_ENCRYPTION,"enable_local_disk_encryption")
        set_flag(tags.INIT_SCRIPTS_ABFSS_DESTINATION,"init_scripts_abfss_destination")
        set_flag(tags.INIT_SCRIPTS_DBFS_DESTINATION,"init_scripts_dbfs_destination")
        set_flag(tags.INIT_SCRIPTS_FILE_DESTINATION,"init_scripts_file_destination")
        set_flag(tags.INIT_SCRIPTS_GCS_DESTINATION,"init_scripts_gcs_destination")
        set_flag(tags.INIT_SCRIPTS_S3_CANNED_ACL,"init_scripts_s3_canned_acl")
        set_flag(tags.INIT_SCRIPTS_S3_DESTINATION,"init_scripts_s3_destination")
        set_flag(tags.INIT_SCRIPTS_S3_ENABLE_ENCRYPTION,"init_scripts_s3_enable_encryption")
        set_flag(tags.INIT_SCRIPTS_S3_ENCRYPTION_TYPE,"init_scripts_s3_encryption_type")
        set_flag(tags.INIT_SCRIPTS_S3_ENDPOINT,"init_scripts_s3_endpoint")
        set_flag(tags.INIT_SCRIPTS_S3_KMS_KEY,"init_scripts_s3_kms_key")
        set_flag(tags.INIT_SCRIPTS_S3_REGION,"init_scripts_s3_region")
        set_flag(tags.INIT_SCRIPTS_VOLUMES_DESTINATION,"init_scripts_volumes_destination")
        set_flag(tags.INIT_SCRIPTS_WORKSPACE_DESTINATION,"init_scripts_workspace_destination")
        set_flag(tags.INSTANCE_POOL_ID,"instance_pool_id")
        set_flag(tags.IS_SINGLE_NODE,"is_single_node")
        set_flag(tags.KIND,"kind")
        set_flag(tags.NODE_TYPE_ID,"node_type_id")
        set_flag(tags.NUM_WORKERS,"num_workers")
        set_flag(tags.POLICY_ID,"policy_id")
        set_flag(tags.RUNTIME_ENGINE,"runtime_engine")
        set_flag(tags.SINGLE_USER_NAME,"single_user_name")
        set_flag(tags.SPARK_CONF_SPARK_DATABRICKS_CLUSTER_PROFILE,"spark_conf_spark_databricks_cluster_profile")
        set_flag(tags.SPARK_CONF_MASTER,"spark_conf_master")
        set_flag(tags.SPARK_ENV_VARS_SPARK_WORKER_MEMORY,"spark_env_vars_spark_worker_memory")
        set_flag(tags.SPARK_ENV_VARS_SPARK_DAEMON_JAVA_OPTS,"spark_env_vars_spark_daemon_java_opts")
        set_flag(tags.SPARK_VERSION,"spark_version")
        set_flag(tags.SSH_PUBLIC_KEYS,"ssh_public_keys")
        set_flag(tags.USE_ML_RUNTIME,"use_ml_runtime")
        set_flag(tags.WORKLOAD_TYPE_CLIENTS_JOBS,"workload_type_clients_jobs")
        set_flag(tags.WORKLOAD_TYPE_CLIENTS_NOTEBOOKS,"workload_type_clients_notebooks")


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
    
#5 payloads could be required depending on type of cluster
    def prepare_payload(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.payload={}
        for prop in self.property_lst:
            if self.attr.cluster_type=="AUTO_SCALE":
                if prop==tags.AUTO_SCALE_MAX_WORKERS:
                    self.payload[tags.AUTO_SCALE_MAX_WORKERS]=self.attr.auto_scale_max_workers
                if prop==tags.AUTO_SCALE_MIN_WORKERS:
                    self.payload[tags.AUTO_SCALE_MIN_WORKERS]=self.attr.auto_scale_min_workers

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
        obj_inst=Cluster(session=session,
                         user_id=user_id,
                         logger=logger)
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')

        if tags.APPLY_POLICY_DEFAULT_VALUES in kwargs.keys():
            obj_inst.set_apply_policy_default_values(kwargs[tags.APPLY_POLICY_DEFAULT_VALUES])
        else:
            obj_inst.set_apply_policy_default_values('NONE')
        obj_inst.logger.info(f"set apply_policy_default_values {obj_inst.attr.apply_policy_default_values}")

        
        if tags.AUTO_SCALE_MAX_WORKERS in kwargs.keys():
            obj_inst.set_auto_scale_max_workers(kwargs[tags.AUTO_SCALE_MAX_WORKERS])
        else:
            obj_inst.set_auto_scale_max_workers('NONE')
        obj_inst.logger.info(f"set auto_scale_max_workers {obj_inst.attr.auto_scale_max_workers}")

        
        if tags.AUTO_SCALE_MIN_WORKERS in kwargs.keys():
            obj_inst.set_auto_scale_min_workers(kwargs[tags.AUTO_SCALE_MIN_WORKERS])
        else:
            obj_inst.set_auto_scale_min_workers('NONE')
        obj_inst.logger.info(f"set auto_scale_min_workers {obj_inst.attr.auto_scale_min_workers}")

        
        if tags.AUTOTERMINATION_MINUTES in kwargs.keys():
            obj_inst.set_autotermination_minutes(kwargs[tags.AUTOTERMINATION_MINUTES])
        else:
            obj_inst.set_autotermination_minutes('NONE')
        obj_inst.logger.info(f"set autotermination_minutes {obj_inst.attr.autotermination_minutes}")


        if tags.AWS_ATTRIBUTES_AVAILABILITY in kwargs.keys():
            obj_inst.set_aws_attributes_availability(kwargs[tags.AWS_ATTRIBUTES_AVAILABILITY])
        else:
            obj_inst.set_aws_attributes_availability('NONE')
        obj_inst.logger.info(f"set aws_attributes_availability {obj_inst.attr.aws_attributes_availability}")


        if tags.AWS_ATTRIBUTES_EBS_VOLUME_COUNT in kwargs.keys():
            obj_inst.set_aws_attributes_ebs_volume_count(kwargs[tags.AWS_ATTRIBUTES_EBS_VOLUME_COUNT])
        else:
            obj_inst.set_aws_attributes_ebs_volume_count('NONE')
        obj_inst.logger.info(f"set aws_attributes_ebs_volume_count {obj_inst.attr.aws_attributes_ebs_volume_count}")

        
        if tags.AWS_ATTRIBUTES_EBS_VOLUME_IOPS in kwargs.keys():
            obj_inst.set_aws_attributes_ebs_volume_iops(kwargs[tags.AWS_ATTRIBUTES_EBS_VOLUME_IOPS])
        else:
            obj_inst.set_aws_attributes_ebs_volume_iops('NONE')
        obj_inst.logger.info(f"set aws_attributes_ebs_volume_iops {obj_inst.attr.aws_attributes_ebs_volume_iops}")

        
        if tags.AWS_ATTRIBUTES_EBS_VOLUME_SIZE in kwargs.keys():
            obj_inst.set_aws_attributes_ebs_volume_size(kwargs[tags.AWS_ATTRIBUTES_EBS_VOLUME_SIZE])
        else:
            obj_inst.set_aws_attributes_ebs_volume_size('NONE')
        obj_inst.logger.info(f"set aws_attributes_ebs_volume_size {obj_inst.attr.aws_attributes_ebs_volume_size}")


        if tags.AWS_ATTRIBUTES_EBS_VOLUME_THROUGHPUT in kwargs.keys():
            obj_inst.set_aws_attributes_ebs_volume_throughput(kwargs[tags.AWS_ATTRIBUTES_EBS_VOLUME_THROUGHPUT])
        else:
            obj_inst.set_aws_attributes_ebs_volume_throughput('NONE')
        obj_inst.logger.info(f"set aws_attributes_ebs_volume_throughput {obj_inst.attr.aws_attributes_ebs_volume_throughput}")

        
        if tags.AWS_ATTRIBUTES_EBS_VOLUME_TYPE in kwargs.keys():
            obj_inst.set_aws_attributes_ebs_volume_type(kwargs[tags.AWS_ATTRIBUTES_EBS_VOLUME_TYPE])
        else:
            obj_inst.set_aws_attributes_ebs_volume_type('NONE')
        obj_inst.logger.info(f"set aws_attributes_ebs_volume_type {obj_inst.attr.aws_attributes_ebs_volume_type}")

        
        if tags.AWS_ATTRIBUTES_FIRST_ON_DEMAND in kwargs.keys():
            obj_inst.set_aws_attributes_first_on_demand(kwargs[tags.AWS_ATTRIBUTES_FIRST_ON_DEMAND])
        else:
            obj_inst.set_aws_attributes_first_on_demand('NONE')
        obj_inst.logger.info(f"set aws_attributes_first_on_demand {obj_inst.attr.aws_attributes_first_on_demand}")


        if tags.AWS_ATTRIBUTES_INSTANCE_PROFILE_ARN in kwargs.keys():
            obj_inst.set_aws_attributes_instance_profile_arn(kwargs[tags.AWS_ATTRIBUTES_INSTANCE_PROFILE_ARN])
        else:
            obj_inst.set_aws_attributes_instance_profile_arn('NONE')
        obj_inst.logger.info(f"set aws_attributes_instance_profile_arn {obj_inst.attr.aws_attributes_instance_profile_arn}")


        if tags.AWS_ATTRIBUTES_SPOT_BID_PRICE_PERCENT in kwargs.keys():
            obj_inst.set_aws_attributes_spot_bid_price_percent(kwargs[tags.AWS_ATTRIBUTES_SPOT_BID_PRICE_PERCENT])
        else:
            obj_inst.set_aws_attributes_spot_bid_price_percent('NONE')
        obj_inst.logger.info(f"set aws_attributes_spot_bid_price_percent {obj_inst.attr.aws_attributes_spot_bid_price_percent}")

        
        if tags.AWS_ATTRIBUTES_ZONE_ID in kwargs.keys():
            obj_inst.set_aws_attributes_zone_id(kwargs[tags.AWS_ATTRIBUTES_ZONE_ID])
        else:
            obj_inst.set_aws_attributes_zone_id('NONE')
        obj_inst.logger.info(f"set aws_attributes_zone_id {obj_inst.attr.aws_attributes_zone_id}")


        if tags.CLONE_FROM_SOURCE_CLUSTER_ID in kwargs.keys():
            obj_inst.set_clone_from_source_cluster_id(kwargs[tags.CLONE_FROM_SOURCE_CLUSTER_ID])
        else:
            obj_inst.set_clone_from_source_cluster_id('NONE')
        obj_inst.logger.info(f"set clone_from_source_cluster_id {obj_inst.attr.clone_from_source_cluster_id}")

        
        if tags.CLUSTER_LOG_CONF_DBFS in kwargs.keys():
            obj_inst.set_cluster_log_conf_dbfs(kwargs[tags.CLUSTER_LOG_CONF_DBFS])
        else:
            obj_inst.set_cluster_log_conf_dbfs('NONE')
        obj_inst.logger.info(f"set cluster_log_conf_dbfs {obj_inst.attr.cluster_log_conf_dbfs}")

        
        if tags.CLUSTER_LOG_CONF_S3 in kwargs.keys():
            obj_inst.set_cluster_log_conf_s3(kwargs[tags.CLUSTER_LOG_CONF_S3])
        else:
            obj_inst.set_cluster_log_conf_s3('NONE')
        obj_inst.logger.info(f"set cluster_log_conf_s3 {obj_inst.attr.cluster_log_conf_s3}")

        
        if tags.CLUSTER_LOG_CONF_VOLUMES_DESTINATIONS in kwargs.keys():
            obj_inst.set_cluster_log_conf_volumes_destinations(kwargs[tags.CLUSTER_LOG_CONF_VOLUMES_DESTINATIONS])
        else:
            obj_inst.set_cluster_log_conf_volumes_destinations('NONE')
        obj_inst.logger.info(f"set cluster_log_conf_volumes_destinations {obj_inst.attr.cluster_log_conf_volumes_destinations}")


        if tags.CLUSTER_NAME in kwargs.keys():
            obj_inst.set_cluster_name(kwargs[tags.CLUSTER_NAME])
        else:
            obj_inst.set_cluster_name('NONE')
        obj_inst.logger.info(f"set cluster_name {obj_inst.attr.cluster_name}")


        if tags.CUSTOM_TAGS_RESOURCECLASS in kwargs.keys():
            obj_inst.set_custom_tags_resourceclass(kwargs[tags.CUSTOM_TAGS_RESOURCECLASS])
        else:
            obj_inst.set_custom_tags_resourceclass('NONE')
        obj_inst.logger.info(f"set custom_tags_resourceclass {obj_inst.attr.custom_tags_resourceclass}")

        
        if tags.DATA_SECURITY_MODE in kwargs.keys():
            obj_inst.set_data_security_mode(kwargs[tags.DATA_SECURITY_MODE])
        else:
            obj_inst.set_data_security_mode('NONE')
        obj_inst.logger.info(f"set data_security_mode {obj_inst.attr.data_security_mode}")

        
        if tags.DOCKER_IMAGE_BASIC_AUTH in kwargs.keys():
            obj_inst.set_docker_image_basic_auth(kwargs[tags.DOCKER_IMAGE_BASIC_AUTH])
        else:
            obj_inst.set_docker_image_basic_auth('NONE')
        obj_inst.logger.info(f"set docker_image_basic_auth {obj_inst.attr.docker_image_basic_auth}")


        if tags.DOCKER_IMAGE_URL in kwargs.keys():
            obj_inst.set_docker_image_url(kwargs[tags.DOCKER_IMAGE_URL])
        else:
            obj_inst.set_docker_image_url('NONE')
        obj_inst.logger.info(f"set docker_image_url {obj_inst.attr.docker_image_url}")

        
        if tags.DRIVER_INSTANCE_POOL_ID in kwargs.keys():
            obj_inst.set_driver_instance_pool_id(kwargs[tags.DRIVER_INSTANCE_POOL_ID])
        else:
            obj_inst.set_driver_instance_pool_id('NONE')
        obj_inst.logger.info(f"set driver_instance_pool_id {obj_inst.attr.driver_instance_pool_id}")

        
        if tags.DRIVER_NODE_TYPE_ID in kwargs.keys():
            obj_inst.set_driver_node_type_id(kwargs[tags.DRIVER_NODE_TYPE_ID])
        else:
            obj_inst.set_driver_node_type_id('NONE')
        obj_inst.logger.info(f"set driver_node_type_id {obj_inst.attr.driver_node_type_id}")


        if tags.ENABLE_ELASTIC_DISK in kwargs.keys():
            obj_inst.set_enable_elastic_disk(kwargs[tags.ENABLE_ELASTIC_DISK])
        else:
            obj_inst.set_enable_elastic_disk('NONE')
        obj_inst.logger.info(f"set enable_elastic_disk {obj_inst.attr.enable_elastic_disk}")


        if tags.ENABLE_LOCAL_DISK_ENCRYPTION in kwargs.keys():
            obj_inst.set_enable_local_disk_encryption(kwargs[tags.ENABLE_LOCAL_DISK_ENCRYPTION])
        else:
            obj_inst.set_enable_local_disk_encryption('NONE')
        obj_inst.logger.info(f"set enable_local_disk_encryption {obj_inst.attr.enable_local_disk_encryption}")

        
        if tags.INIT_SCRIPTS_ABFSS_DESTINATION in kwargs.keys():
            obj_inst.set_init_scripts_abfss_destination(kwargs[tags.INIT_SCRIPTS_ABFSS_DESTINATION])
        else:
            obj_inst.set_init_scripts_abfss_destination('NONE')
        obj_inst.logger.info(f"set init_scripts_abfss_destination {obj_inst.attr.init_scripts_abfss_destination}")


        if tags.INIT_SCRIPTS_DBFS_DESTINATION in kwargs.keys():
            obj_inst.set_init_scripts_dbfs_destination(kwargs[tags.INIT_SCRIPTS_DBFS_DESTINATION])
        else:
            obj_inst.set_init_scripts_dbfs_destination('NONE')
        obj_inst.logger.info(f"set init_scripts_dbfs_destination {obj_inst.attr.init_scripts_dbfs_destination}")

        
        if tags.INIT_SCRIPTS_FILE_DESTINATION in kwargs.keys():
            obj_inst.set_init_scripts_file_destination(kwargs[tags.INIT_SCRIPTS_FILE_DESTINATION])
        else:
            obj_inst.set_init_scripts_file_destination('NONE')
        obj_inst.logger.info(f"set init_scripts_file_destination {obj_inst.attr.init_scripts_file_destination}")

        
        if tags.INIT_SCRIPTS_GCS_DESTINATION in kwargs.keys():
            obj_inst.set_init_scripts_gcs_destination(kwargs[tags.INIT_SCRIPTS_GCS_DESTINATION])
        else:
            obj_inst.set_init_scripts_gcs_destination('NONE')
        obj_inst.logger.info(f"set init_scripts_gcs_destination {obj_inst.attr.init_scripts_gcs_destination}")

        
        if tags.INIT_SCRIPTS_S3_CANNED_ACL in kwargs.keys():
            obj_inst.set_init_scripts_s3_canned_acl(kwargs[tags.INIT_SCRIPTS_S3_CANNED_ACL])
        else:
            obj_inst.set_init_scripts_s3_canned_acl('NONE')
        obj_inst.logger.info(f"set init_scripts_s3_canned_acl {obj_inst.attr.init_scripts_s3_canned_acl}")


        if tags.INIT_SCRIPTS_S3_DESTINATION in kwargs.keys():
            obj_inst.set_init_scripts_s3_destination(kwargs[tags.INIT_SCRIPTS_S3_DESTINATION])
        else:
            obj_inst.set_init_scripts_s3_destination('NONE')
        obj_inst.logger.info(f"set init_scripts_s3_destination {obj_inst.attr.init_scripts_s3_canned_acl}")


        if tags.INIT_SCRIPTS_S3_ENABLE_ENCRYPTION in kwargs.keys():
            obj_inst.set_init_scripts_s3_enable_encryption(kwargs[tags.INIT_SCRIPTS_S3_ENABLE_ENCRYPTION])
        else:
            obj_inst.set_init_scripts_s3_enable_encryption('NONE')
        obj_inst.logger.info(f"set init_scripts_s3_enable_encryption {obj_inst.attr.init_scripts_s3_enable_encryption}")

        
        if tags.INIT_SCRIPTS_S3_ENCRYPTION_TYPE in kwargs.keys():
            obj_inst.set_init_scripts_s3_encryption_type(kwargs[tags.INIT_SCRIPTS_S3_ENCRYPTION_TYPE])
        else:
            obj_inst.set_init_scripts_s3_encryption_type('NONE')
        obj_inst.logger.info(f"set init_scripts_s3_encryption_type {obj_inst.attr.init_scripts_s3_encryption_type}")

        
        if tags.INIT_SCRIPTS_S3_ENDPOINT in kwargs.keys():
            obj_inst.set_init_scripts_s3_endpoint(kwargs[tags.INIT_SCRIPTS_S3_ENDPOINT])
        else:
            obj_inst.set_init_scripts_s3_endpoint('NONE')
        obj_inst.logger.info(f"set init_scripts_s3_endpoint {obj_inst.attr.init_scripts_s3_endpoint}")


        if tags.INIT_SCRIPTS_S3_KMS_KEY in kwargs.keys():
            obj_inst.set_init_scripts_s3_kms_key(kwargs[tags.INIT_SCRIPTS_S3_KMS_KEY])
        else:
            obj_inst.set_init_scripts_s3_kms_key('NONE')
        obj_inst.logger.info(f"set init_scripts_s3_kms_key {obj_inst.attr.init_scripts_s3_kms_key}")

        
        if tags.INIT_SCRIPTS_S3_REGION in kwargs.keys():
            obj_inst.set_init_scripts_s3_region(kwargs[tags.INIT_SCRIPTS_S3_REGION])
        else:
            obj_inst.set_init_scripts_s3_region('NONE')
        obj_inst.logger.info(f"set init_scripts_s3_region {obj_inst.attr.init_scripts_s3_region}")

        
        if tags.INIT_SCRIPTS_VOLUMES_DESTINATION in kwargs.keys():
            obj_inst.set_init_scripts_volumes_destination(kwargs[tags.INIT_SCRIPTS_VOLUMES_DESTINATION])
        else:
            obj_inst.set_init_scripts_volumes_destination('NONE')
        obj_inst.logger.info(f"set init_scripts_volumes_destination {obj_inst.attr.init_scripts_volumes_destination}")


        if tags.INIT_SCRIPTS_WORKSPACE_DESTINATION in kwargs.keys():
            obj_inst.set_init_scripts_workspace_destination(kwargs[tags.INIT_SCRIPTS_WORKSPACE_DESTINATION])
        else:
            obj_inst.set_init_scripts_workspace_destination('NONE')
        obj_inst.logger.info(f"set init_scripts_workspace_destination {obj_inst.attr.init_scripts_workspace_destination}")


        if tags.INSTANCE_POOL_ID in kwargs.keys():
            obj_inst.set_instance_pool_id(kwargs[tags.INSTANCE_POOL_ID])
        else:
            obj_inst.set_instance_pool_id('NONE')
        obj_inst.logger.info(f"set instance_pool_id {obj_inst.attr.instance_pool_id}")

        
        if tags.IS_SINGLE_NODE in kwargs.keys():
            obj_inst.set_is_single_node(kwargs[tags.IS_SINGLE_NODE])
        else:
            obj_inst.set_is_single_node('NONE')
        obj_inst.logger.info(f"set is_single_node {obj_inst.attr.is_single_node}")


        if tags.KIND in kwargs.keys():
            obj_inst.set_kind(kwargs[tags.KIND])
        else:
            obj_inst.set_kind('NONE')
        obj_inst.logger.info(f"set kind {obj_inst.attr.kind}")

        
        if tags.NODE_TYPE_ID in kwargs.keys():
            obj_inst.set_node_type_id(kwargs[tags.NODE_TYPE_ID])
        else:
            obj_inst.set_node_type_id('NONE')
        obj_inst.logger.info(f"set node_type_id {obj_inst.attr.node_type_id}")

        
        if tags.NUM_WORKERS in kwargs.keys():
            obj_inst.set_num_workers(kwargs[tags.NUM_WORKERS])
        else:
            obj_inst.set_num_workers('NONE')
        obj_inst.logger.info(f"set num_workers {obj_inst.attr.num_workers}")

        
        if tags.POLICY_ID in kwargs.keys():
            obj_inst.set_policy_id(kwargs[tags.POLICY_ID])
        else:
            obj_inst.set_policy_id('NONE')
        obj_inst.logger.info(f"set policy_id {obj_inst.attr.policy_id}")


        if tags.RUNTIME_ENGINE in kwargs.keys():
            obj_inst.set_runtime_engine(kwargs[tags.RUNTIME_ENGINE])
        else:
            obj_inst.set_runtime_engine('NONE')
        obj_inst.logger.info(f"set runtime_engine {obj_inst.attr.runtime_engine}")


        if tags.SINGLE_USER_NAME in kwargs.keys():
            obj_inst.set_single_user_name(kwargs[tags.SINGLE_USER_NAME])
        else:
            obj_inst.set_single_user_name('NONE')
        obj_inst.logger.info(f"set single_user_name {obj_inst.attr.single_user_name}")

        
        if tags.SPARK_CONF_SPARK_DATABRICKS_CLUSTER_PROFILE in kwargs.keys():
            obj_inst.set_spark_conf_spark_databricks_cluster_profile(kwargs[tags.SPARK_CONF_SPARK_DATABRICKS_CLUSTER_PROFILE])
        else:
            obj_inst.set_spark_conf_spark_databricks_cluster_profile('NONE')
        obj_inst.logger.info(f"set spark_conf_spark_databricks_cluster_profile {obj_inst.attr.spark_conf_spark_databricks_cluster_profile}")

        
        if tags.SPARK_CONF_MASTER in kwargs.keys():
            obj_inst.set_spark_conf_master(kwargs[tags.SPARK_CONF_MASTER])
        else:
            obj_inst.set_spark_conf_master('NONE')
        obj_inst.logger.info(f"set spark_conf_master {obj_inst.attr.spark_conf_master}")


        if tags.SPARK_ENV_VARS_SPARK_WORKER_MEMORY in kwargs.keys():
            obj_inst.set_spark_env_vars_spark_worker_memory(kwargs[tags.SPARK_ENV_VARS_SPARK_WORKER_MEMORY])
        else:
            obj_inst.set_spark_env_vars_spark_worker_memory('NONE')
        obj_inst.logger.info(f"set spark_env_vars_spark_worker_memory {obj_inst.attr.spark_env_vars_spark_worker_memory}")

        
        if tags.SPARK_ENV_VARS_SPARK_DAEMON_JAVA_OPTS in kwargs.keys():
            obj_inst.set_spark_env_vars_spark_daemon_java_opts(kwargs[tags.SPARK_ENV_VARS_SPARK_DAEMON_JAVA_OPTS])
        else:
            obj_inst.set_spark_env_vars_spark_daemon_java_opts('NONE')
        obj_inst.logger.info(f"set spark_env_vars_spark_daemon_java_opts {obj_inst.attr.spark_env_vars_spark_daemon_java_opts}")

        
        if tags.SPARK_VERSION in kwargs.keys():
            obj_inst.set_spark_version(kwargs[tags.SPARK_VERSION])
        else:
            obj_inst.set_spark_version('NONE')
        obj_inst.logger.info(f"set spark_version {obj_inst.attr.spark_version}")


        if tags.SSH_PUBLIC_KEYS in kwargs.keys():
            obj_inst.set_ssh_public_keys(kwargs[tags.SSH_PUBLIC_KEYS])
        else:
            obj_inst.set_ssh_public_keys('NONE')
        obj_inst.logger.info(f"set ssh_public_keys {obj_inst.attr.ssh_public_keys}")


        if tags.USE_ML_RUNTIME in kwargs.keys():
            obj_inst.set_use_ml_runtime(kwargs[tags.USE_ML_RUNTIME])
        else:
            obj_inst.set_use_ml_runtime('NONE')
        obj_inst.logger.info(f"set use_ml_runtime {obj_inst.attr.use_ml_runtime}")

        
        if tags.WORKLOAD_TYPE_CLIENTS_JOBS in kwargs.keys():
            obj_inst.set_workload_type_clients_jobs(kwargs[tags.WORKLOAD_TYPE_CLIENTS_JOBS])
        else:
            obj_inst.set_workload_type_clients_jobs('NONE')
        obj_inst.logger.info(f"set workload_type_clients_jobs {obj_inst.attr.workload_type_clients_jobs}")


        if tags.WORKLOAD_TYPE_CLIENTS_NOTEBOOKS in kwargs.keys():
            obj_inst.set_workload_type_clients_notebooks(kwargs[tags.WORKLOAD_TYPE_CLIENTS_NOTEBOOKS])
        else:
            obj_inst.set_workload_type_clients_notebooks('NONE')
        obj_inst.logger.info(f"set workload_type_clients_notebooks {obj_inst.attr.workload_type_clients_notebooks}")

   

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


