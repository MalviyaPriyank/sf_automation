import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class FailoverGroupTag(BaseTag):
    NAME = "NAME"
    OBJECT_TYPES = "OBJECT_TYPES"
    ALLOWED_DATABASES = "ALLOWED_DATABASES"
    ALLOWED_SHARES = "ALLOWED_SHARES"
    ALLOWED_EXTERNAL_VOLUMES="ALLOWED_EXTERNAL_VOLUMES"
    ALLOWED_INTEGRATION_TYPES="ALLOWED_INTEGRATION_TYPES"
    ALLOWED_ACCOUNTS = "ALLOWED_ACCOUNTS"
    REPLICATION_SCHEDULE = "REPLICATION_SCHEDULE"
    IS_CREATE = "IS_CREATE"
    ERROR_INTEGRATION="ERROR_INTEGRATION"

    @classmethod
    def get_attributes_with_description(cls):
        return {
        "NAME":"this is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO, these are to be taken from user. the format is a dictionary with key 'NAME' for the name, and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
        "COMMENT":"This will be user defined comment for the object. If user does not define one add a proper comment as per your understanding and inform the user.",
        "IS_CREATE":"Set this to 'TRUE' if create object. set to 'FALSE' if alter object.",
        "OBJECT_TYPES":"Specifies the Type(s) of objects for which you are enabling replication and failover from the source account to the target account. Default is NONE.",
        "ALLOWED_DATABASES":"Specifies the database or list of databases for which you are enabling replication and failover from the source account to the target account. In order for you to set this parameter, the OBJECT_TYPES list must include DATABASES. Default is NONE.",
        "ALLOWED_SHARES":"Specifies the share or list of shares for which you are enabling replication and failover from the source account to the target account. For you to set this parameter, the OBJECT_TYPES list must include SHARES. Default is NONE.",
        "ALLOWED_EXTERNAL_VOLUMES":"Specifies the external volume or list of external volumes for which you are enabling replication and failover from the source account to the target account. For you to set this parameter, the OBJECT_TYPES list must include EXTERNAL VOLUMES. Default is NONE.",
        "ALLOWED_INTEGRATION_TYPES":"""
        Type(s) of integrations for which you are enabling replication and failover from the source account to the target account.
        This property requires that the OBJECT_TYPES list include INTEGRATIONS to set this parameter.
        Default is NONE.
        """,
        "ALLOWED_ACCOUNTS":"Specifies the target account or list of target accounts to which replication and failover of specified objects from the source account is enabled. Secondary failover groups in the target accounts in this list can be promoted to serve as the primary failover group in case of failover. Default is NONE.",
        "REPLICATION_SCHEDULE":"Specifies the schedule for refreshing secondary failover groups.Default is NONE.",
        "ERROR_INTEGRATION":"Specifies the name of the notification integration to use to send notifications when refresh errors occur for the failover group. Strongly recommended."
        }


    @classmethod
    def allowed_value_list(cls):
        return {
            "OBJECT_TYPES": ["DATABASES", "SHARES","ACCOUNT PARAMETERS","INTEGRATIONS","NETWORK POLICIES","RESOURCE MONITORS","ROLES","SHARES","USERS","WAREHOUSES"],
            "REPLICATION_SCHEDULE": [
                "<n> MINUTE",
                "USING CRON <cron_expression> UTC"
            ]
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
