import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class TaskTag(BaseTag):
    SQL="SQL"
    WAREHOUSE="WAREHOUSE"
    USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE="USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE"
    SCHEDULE="SCHEDULE"   
    CONFIG="CONFIG"
    ALLOW_OVERLAPPING_EXECUTION="ALLOW_OVERLAPPING_EXECUTION"
    USER_TASK_TIMEOUT_MS="USER_TASK_TIMEOUT_MS"
    SUSPEND_TASK_AFTER_NUM_FAILURES="SUSPEND_TASK_AFTER_NUM_FAILURES"
    ERROR_INTEGRATION="ERROR_INTEGRATION"
    SUCCESS_INTEGRATION="SUCCESS_INTEGRATION"
    AFTER="AFTER"
    WHEN="WHEN"
    FINALIZE="FINALIZE"
    TASK_AUTO_RETRY_ATTEMPTS="TASK_AUTO_RETRY_ATTEMPTS"
    USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS="USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS"
    TARGET_COMPLETION_INTERVAL="TARGET_COMPLETION_INTERVAL"
    SERVERLESS_TASK_MIN_STATEMENT_SIZE="SERVERLESS_TASK_MIN_STATEMENT_SIZE"
    SERVERLESS_TASK_MAX_STATEMENT_SIZE="SERVERLESS_TASK_MAX_STATEMENT_SIZE"
    SECONDS="SECONDS"
    MINUTE="MINUTE"
    HOUR="HOUR"
    LOG_LEVEL="LOG_LEVEL"

    @classmethod
    def allowed_value_list(cls):
        return {
            "USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE":["XSMALL","SMALL","MEDIUM","LARGE","XLARGE","XXLARGE"],
            "LOG_LEVEL":["TRACE","DEBUG","INFO","WARN","ERROR","FATAL","OFF"]
        }

    @classmethod
    def min_allowed_value(cls):
        return {
            "USER_TASK_TIMEOUT_MS":0,
            "SCHEDULE":{
                "SECONDS":10,
                "MINUTE":1,
                "HOUR":1
            },
            "TASK_AUTO_RETRY_ATTEMPTS":0,
            "USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS":10,
            "TARGET_COMPLETION_INTERVAL":{
                "SECONDS":10,
                "MINUTE":1,
                "HOUR":1
            }
        }
    
    @classmethod
    def max_allowed_value(cls):
        return {
            "USER_TASK_TIMEOUT_MS":604800000,
            "SCHEDULE":{
                "SECONDS":691200,
                "MINUTE":11520,
                "HOUR":192
            },
            "TASK_AUTO_RETRY_ATTEMPTS":30,
            "USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS":604800000,
            "TARGET_COMPLETION_INTERVAL":{
                "SECONDS":86400,
                "MINUTE":1440,
                "HOUR":24
            }
        }
          
