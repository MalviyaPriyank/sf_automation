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