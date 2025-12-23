from dataclasses import dataclass
from base import BaseMethod

@dataclass(frozen=True)
class ClusterTags(BaseMethod):
    CLUSTER_TYPE='cluster_type'
    APPLY_POLICY_DEFAULT_VALUES="apply_policy_default_values"
    AUTO_SCALE_MAX_WORKERS="max_workers"
    AUTO_SCALE_MIN_WORKERS="min_workers"
    AUTOTERMINATION_MINUTES="autotermination_minutes"
    AWS_ATTRIBUTES_AVAILABILITY="availability"
    AWS_ATTRIBUTES_EBS_VOLUME_COUNT="ebs_volume_count"
    AWS_ATTRIBUTES_EBS_VOLUME_IOPS="ebs_volume_iops"
    AWS_ATTRIBUTES_EBS_VOLUME_SIZE="ebs_volume_size"
    AWS_ATTRIBUTES_EBS_VOLUME_THROUGHPUT="ebs_volume_throughput"
    AWS_ATTRIBUTES_EBS_VOLUME_TYPE="ebs_volume_type"
    AWS_ATTRIBUTES_FIRST_ON_DEMAND="first_on_demand"
    AWS_ATTRIBUTES_INSTANCE_PROFILE_ARN="instance_profile_arn"
    AWS_ATTRIBUTES_SPOT_BID_PRICE_PERCENT="spot_bid_price_percent"
    AWS_ATTRIBUTES_ZONE_ID="zone_id"
    CLONE_FROM_SOURCE_CLUSTER_ID="clone_from_source_cluster_id"
    CLUSTER_LOG_CONF_DBFS_Destination="destination"
    CLUSTER_LOG_CONF_S3_CANNED_ACL="canned_acl"
    CLUSTER_LOG_CONF_S3_DESTINATION="destination"
    CLUSTER_LOG_CONF_S3_ENABLE_ENCRYPTION="enable_encryption"
    CLUSTER_LOG_CONF_S3_ENCRYPTION_TYPE="encryption_type"
    CLUSTER_LOG_CONF_S3_ENDPOINT="endpoint"
    CLUSTER_LOG_CONF_S3_KMS_KEY="kms_key"
    CLUSTER_LOG_CONF_S3_REGION="region"
    CLUSTER_LOG_CONF_VOLUMES_DESTINATION="destination"
    CLUSTER_NAME="cluster_name"
    CUSTOM_TAGS_RESOURCECLASS="ResourceClass"
    DATA_SECURITY_MODE="data_security_mode"
    DOCKER_IMAGE_BASIC_AUTH_PASSWORD="password"
    DOCKER_IMAGE_BASIC_AUTH_USERNAME="username"
    DOCKER_IMAGE_URL="url"
    DRIVER_INSTANCE_POOL_ID="driver_instance_pool_id"
    DRIVER_NODE_TYPE_ID="driver_node_type_id"
    ENABLE_ELASTIC_DISK="enable_elastic_disk"
    ENABLE_LOCAL_DISK_ENCRYPTION="enable_local_disk_encryption"
    INIT_SCRIPTS_ABFSS_DESTINATION="destination"
    INIT_SCRIPTS_DBFS_DESTINATION="destination"
    INIT_SCRIPTS_FILE_DESTINATION="destination"
    INIT_SCRIPTS_GCS_DESTINATION="destination"
    INIT_SCRIPTS_S3_CANNED_ACL="canned_acl"
    INIT_SCRIPTS_S3_DESTINATION="destination"
    INIT_SCRIPTS_S3_ENABLE_ENCRYPTION="enable_encryption"
    INIT_SCRIPTS_S3_ENCRYPTION_TYPE="encryption_type"
    INIT_SCRIPTS_S3_ENDPOINT="endpoint"
    INIT_SCRIPTS_S3_KMS_KEY="kms_key"
    INIT_SCRIPTS_S3_REGION="region"
    INIT_SCRIPTS_VOLUMES_DESTINATION="destination"
    INIT_SCRIPTS_WORKSPACE_DESTINATION="destination"
    INSTANCE_POOL_ID="instance_pool_id"
    IS_SINGLE_NODE="is_single_node"
    KIND="kind"
    NODE_TYPE_ID="node_type_id"
    NUM_WORKERS="num_workers"
    POLICY_ID="policy_id"
    RUNTIME_ENGINE="runtime_engine"
    SINGLE_USER_NAME="single_user_name"
    SPARK_CONF_SPARK_DATABRICKS_CLUSTER_PROFILE="spark.databricks.cluster.profile"
    SPARK_CONF_SPARK_MASTER="spark.master"
    SPARK_CONF_SPARK_SPECULATION="spark.speculation"
    SPARK_CONF_SPARK_DRIVER_EXTRAJAVAOPTIONS="spark.driver.extraJavaOptions"
    SPARK_CONF_SPARK_EXECUTOR_EXTRAJAVAOPTIONS="spark.executor.extraJavaOptions"
    SPARK_ENV_VARS_SPARK_WORKER_MEMORY="spark_worker_memory"
    SPARK_ENV_VARS_SPARK_LOCAL_DIRS="spark_local_dirs"
    SPARK_ENV_VARS_SPARK_DAEMON_JAVA_OPTS="spark_daemon_java_opts"
    SPARK_VERSION="spark_version"
    SSH_PUBLIC_KEYS="ssh_public_keys"
    USE_ML_RUNTIME="use_ml_runtime"
    WORKLOAD_TYPE_CLIENTS_JOBS="jobs"
    WORKLOAD_TYPE_CLIENTS_NOTEBOOKS="notebooks"

    @classmethod
    def allowed_value_list(cls):
        return {
            "CLUSTER_TYPE": ["AUTOSCALING", "ML_WITH_KIND","SINGLE_NODE","SINGLE_NODE_WITH_KIND","SPOT_INSTANCES"],
            "API_PROVIDER":{
                "AMAZON":["aws_api_gateway","aws_private_api_gateway","aws_gov_api_gateway","aws_gov_private_api_gateway"]
            }
        }

