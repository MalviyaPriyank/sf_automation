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
    def get_attributes_with_description(cls):
        return {
            "NAME":"this is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO, these are to be taken from user. the format is a dictionary with key 'NAME' for the name, and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
            "IS_CREATE":"Set this to 'TRUE' if create object. set to 'FALSE' if alter object.",
            "CREDIT_QUOTA": "Number of compute credits allocated to this resource monitor per frequency interval. Used to cap or track usage. (float or int)",
            "FREQUENCY": "Defines how often the monitor resets its credit quota. Possible values: 'DAILY', 'WEEKLY', 'MONTHLY', or 'YEARLY'. (str)",
            "START_TIMESTAMP": "Timestamp (UTC) when monitoring begins or the first interval starts. If omitted, starts immediately upon creation. (datetime str or ISO 8601 format)",
            "END_TIMESTAMP": "Optional timestamp (UTC) when monitoring ends. After this time, the monitor stops tracking usage. (datetime str or ISO 8601 format)",
            "NOTIFY_USERS": "List of user names or email addresses to notify when a trigger condition is met. (list[str])",
            "TRIGGERS": "List of threshold-action pairs defining what happens at specific usage levels. Each trigger includes THRESHOLD (%) and ACTION ('NOTIFY', 'SUSPEND', or 'SUSPEND_IMMEDIATE'). (list[dict])",
            "THRESHOLD": "Percentage of credit quota consumed that activates a trigger. Typically 50, 75, 100, etc. (float or int)",
            "ACTION": "Action to take when the threshold is reached. Options: 'NOTIFY' (send alert), 'SUSPEND' (pause warehouses), or 'SUSPEND_IMMEDIATE' (halt all usage immediately). (str)"
        }

    @classmethod
    def allowed_value_list(cls):
        return {
            "FREQUENCY":["MONTHLY","DAILY","WEEKLY","YEARLY","NEVER"],
            "ACTION":["SUSPEND","SUSPEND_IMMEDIATE","NOTIFY"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
          
