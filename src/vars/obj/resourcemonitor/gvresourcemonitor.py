import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class ResourceMonitorTag(BaseTag):
    NAME="NAME"
    CREDIT_QUOTA="CREDIT_QUOTA"
    FREQUENCY="FREQUENCY"
    START_TIMESTAMP="START_TIMESTAMP"
    END_TIMESTAMP="END_TIMESTAMP"
    NOTIFY_USERS="NOTIFY_USERS"
    TRIGGERS="TRIGGERS"
    THRESHOLD="THRESHOLD"
    ACTION="ACTION"

    @classmethod
    def allowed_value_list(cls):
        return {
            "FREQUENCY":["MONTHLY","DAILY","WEEKLY","YEARLY","NEVER"],
            "TRIGGERS":["SINGLE","MULTIPLE"],
            "ACTION":["SUSPEND","SUSPEND_IMMEDIATE","NOTIFY"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
          
