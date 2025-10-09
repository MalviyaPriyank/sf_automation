import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class FailoverGroupTag(BaseTag):
    NAME = "NAME"
    OBJECT_TYPES = "OBJECT_TYPES"
    ALLOWED_DATABASES = "ALLOWED_DATABASES"
    ALLOWED_SHARES = "ALLOWED_SHARES"
    ALLOWED_ACCOUNTS = "ALLOWED_ACCOUNTS"
    REPLICATION_SCHEDULE = "REPLICATION_SCHEDULE"
    IS_CREATE = "IS_CREATE"

    @classmethod
    def allowed_value_list(cls):
        return {
            "OBJECT_TYPES": ["DATABASES", "SHARES"],
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
