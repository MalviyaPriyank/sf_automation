import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class ComputePoolTag(BaseTag):
    NAME = "NAME"
    FOR_APPLICATION="FOR_APPLICATION"
    MIN_NODES = "MIN_NODES"
    MAX_NODES = "MAX_NODES"
    INSTANCE_FAMILY = "INSTANCE_FAMILY"
    AUTO_RESUME = "AUTO_RESUME"
    INITIALLY_SUSPENDED = "INITIALLY_SUSPENDED"
    AUTO_SUSPEND_SECS = "AUTO_SUSPEND_SECS"
    COMMENT = "COMMENT"
    IS_CREATE = "IS_CREATE"

    @classmethod
    def get_attributes_with_description(cls):
        return {
            "NAME":"this is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO, these are to be taken from user. the format is a dictionary with key 'NAME' for the name, and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
            "FOR_APPLICATION":"Specifies the Snowflake Native App name. If specified, the compute pool can only be used by the native app.",
            "MIN_NODES":"Specifies the minimum number of nodes for the compute pool. This value must be greater than 0.",
            "MAX_NODES":"Specifies the maximum number of nodes for the compute pool.",
            "INSTANCE_FAMILY":"Identifies the type of machine you want to provision for the nodes in the compute pool. The machine type determines the amount of compute resources in the compute pool and, therefore, the number of credits consumed while the compute pool is running.",
            "AUTO_RESUME":"Specifies whether to automatically resume a compute pool when a service or job is submitted to it.If AUTO_RESUME is FALSE, user need to explicitly resume the compute pool (using ALTER COMPUTE POOL RESUME) before user can start a service or job on the compute pool.",
            "INITIALLY_SUSPENDED":"Specifies whether the compute pool is created initially in the suspended state. If you create a compute pool with INITIALLY_SUSPENDED set to TRUE, Snowflake will not provision any nodes requested for the compute pool at the compute pool creation time. User can start the suspended compute pool using ALTER COMPUTE POOL … RESUME.",
            "AUTO_SUSPEND_SECS":"Number of seconds of inactivity after which you want Snowflake to automatically suspend the compute pool. An inactive compute pool is one in which no services or jobs are currently active on any node in the pool. If auto_suspend_secs is set to 0, Snowflake does not suspend the compute pool automatically.",
            "COMMENT":"Comment for the compute pool.",
            "IS_CREATE":"Set this to 'TRUE' if create object. set to 'FALSE' if alter object."
        }

    @classmethod
    def allowed_value_list(cls):
        return {
            "AUTO_RESUME": ["TRUE", "FALSE"],
            "INITIALLY_SUSPENDED": ["TRUE", "FALSE"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
