import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class WarehouseTag(BaseTag):
    WAREHOUSE_SIZE="WAREHOUSE_SIZE"
    WAREHOUSE_TYPE="WAREHOUSE_TYPE"
    RESOURCE_CONSTRAINT="RESOURCE_CONSTRAINT"
    MAX_CLUSTER_COUNT="MAX_CLUSTER_COUNT"
    MIN_CLUSTER_COUNT="MIN_CLUSTER_COUNT"
    SCALING_POLICY="SCALING_POLICY"
    AUTO_SUSPEND="AUTO_SUSPEND"
    AUTO_RESUME="AUTO_RESUME"
    INITIALLY_SUSPENDED="INITIALLY_SUSPENDED"
    RESOURCE_MONITOR="RESOURCE_MONITOR"
    COMMENT="COMMENT"
    TAG="TAG"
    ENABLE_QUERY_ACCELERATION="ENABLE_QUERY_ACCELERATION"
    QUERY_ACCELERATION_MAX_SCALE_FACTOR="QUERY_ACCELERATION_MAX_SCALE_FACTOR"
    MAX_CONCURRENCY_LEVEL="MAX_CONCURRENCY_LEVEL"
    STATEMENT_QUEUED_TIMEOUT_IN_SECONDS="STATEMENT_QUEUED_TIMEOUT_IN_SECONDS"
    STATEMENT_TIMEOUT_IN_SECONDS="STATEMENT_TIMEOUT_IN_SECONDS"
    RSA_PUBLIC_KEY_2_FP="RSA_PUBLIC_KEY_2_FP"
    TYPE="TYPE"
    ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR="ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR"

    @classmethod
    def get_attributes_with_description(cls):
        return {
            "WAREHOUSE_SIZE": "Specifies the size of the warehouse (XSMALL, SMALL, MEDIUM, LARGE, XLARGE, etc.). Determines compute resources and cost. (str)",
            "WAREHOUSE_TYPE": "Specifies the warehouse type. 'STANDARD' for general-purpose, 'SNOWPARK-OPTIMIZED' for compute-intensive Snowpark workloads. (str)",
            "RESOURCE_CONSTRAINT": "Controls whether queries are queued or fail immediately when resources are insufficient (e.g., 'SOFT' or 'HARD'). (str)",
            "MAX_CLUSTER_COUNT": "Maximum number of clusters allowed when multi-cluster mode is enabled. (int)",
            "MIN_CLUSTER_COUNT": "Minimum number of clusters allowed when multi-cluster mode is enabled. (int)",
            "SCALING_POLICY": "Determines how additional clusters are added under load — 'STANDARD' (default) or 'ECONOMY'. (str)",
            "AUTO_SUSPEND": "Specifies the number of seconds of inactivity after which the warehouse is automatically suspended. (int)",
            "AUTO_RESUME": "If TRUE, resumes the warehouse automatically when a query is submitted. (bool)",
            "INITIALLY_SUSPENDED": "If TRUE, creates the warehouse in a suspended state. (bool)",
            "RESOURCE_MONITOR": "Name of the resource monitor that manages this warehouse’s credit usage. (str)",
            "COMMENT": "Optional description or comment for the warehouse. (str)",
            "TAG": "Specifies one or more tags (key-value pairs) for warehouse metadata. (dict or list)",
            "ENABLE_QUERY_ACCELERATION": "If TRUE, enables query acceleration for eligible queries. (bool)",
            "QUERY_ACCELERATION_MAX_SCALE_FACTOR": "Maximum scale factor for compute resources used by query acceleration (1–8). (int)",
            "MAX_CONCURRENCY_LEVEL": "Maximum number of concurrent SQL statements allowed on the warehouse. (int)",
            "STATEMENT_QUEUED_TIMEOUT_IN_SECONDS": "Maximum time, in seconds, a SQL statement can be queued before timing out. (int)",
            "STATEMENT_TIMEOUT_IN_SECONDS": "Maximum time, in seconds, before a running SQL statement times out. (int)",
            "TYPE": "Warehouse type classification (usually 'WAREHOUSE'). Not typically modified. (str)",
            "ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR": "If TRUE, shows full unredacted query text in syntax error messages. (bool)"
        }
    

    @classmethod
    def allowed_value_list(cls):
        return {
            "SCALING_POLICY":["STANDARD","ECONOMY"],
            "WAREHOUSE_TYPE":["STANDARD","SNOWPARK-OPTIMIZED"],
            "WAREHOUSE_SIZE":["XSMALL","SMALL","MEDIUM","LARGE","XLARGE","XXLARGE","XXXLARGE","X4LARGE","X5LARGE","X6LARGE"],
        }

    @classmethod
    def max_allowed_value(cls):
        return {
            "QUERY_ACCELERATION_MAX_SCALE_FACTOR":100,
            "STATEMENT_TIMEOUT_IN_SECONDS":604800

        }

    @classmethod
    def min_allowed_value(cls):
        return {
            "STATEMENT_TIMEOUT_IN_SECONDS":0,
            "QUERY_ACCELERATION_MAX_SCALE_FACTOR":0
        }
          
    



