import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class ReplicationGroupTag(BaseTag):
    NAME = "NAME"
    OBJECT_TYPES = "OBJECT_TYPES"
    ALLOWED_DATABASES = "ALLOWED_DATABASES"
    ALLOWED_SHARES = "ALLOWED_SHARES"
    ALLOWED_INTEGRATION_TYPES = "ALLOWED_INTEGRATION_TYPES"
    ALLOWED_ACCOUNTS = "ALLOWED_ACCOUNTS"
    REPLICATION_SCHEDULE = "REPLICATION_SCHEDULE"
    IGNORE_EDITION_CHECK = "IGNORE_EDITION_CHECK"
    ERROR_INTEGRATION = "ERROR_INTEGRATION"
    TAG_CLAUSE = "TAG"
    IS_CREATE = "IS_CREATE"

    @classmethod
    def get_attributes_with_description(cls):
        return {
            "NAME":"this is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO, these are to be taken from user. the format is a dictionary with key 'NAME' for the name, and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
            "OBJECT_TYPES":"Type(s) of objects for which user is enabling replication from the source account to the target account. Pass this as a list. If user wants to enable replication for DATABASES and WAREHOUSES then the value would be ['DATABASES','WAREHOUSES']",
            "ALLOWED_DATABASES":"Specifies the database or list of databases for which you are enabling replication from the source account to the target account. This should be passed as list of databases. Example ['DB1','DB2']",
            
        }

    @classmethod
    def allowed_value_list(cls):
        return {
            "OBJECT_TYPES": [
                "ACCOUNT PARAMETERS",
                "DATABASES",
                "INTEGRATIONS",
                "NETWORK POLICIES",
                "RESOURCE MONITORS",
                "ROLES",
                "SHARES",
                "USERS",
                "WAREHOUSES"
            ],
            "REPLICATION_SCHEDULE": [
                "<n> MINUTE",
                "USING CRON <expr> <time_zone>"
            ]
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass