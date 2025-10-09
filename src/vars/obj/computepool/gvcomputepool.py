import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class ComputePoolTag(BaseTag):
    NAME = "NAME"
    MIN_NODES = "MIN_NODES"
    MAX_NODES = "MAX_NODES"
    INSTANCE_FAMILY = "INSTANCE_FAMILY"
    AUTO_RESUME = "AUTO_RESUME"
    INITIALLY_SUSPENDED = "INITIALLY_SUSPENDED"
    AUTO_SUSPEND_SECS = "AUTO_SUSPEND_SECS"
    COMMENT = "COMMENT"
    TAG_CLAUSE = "TAG_CLAUSE"
    IS_CREATE = "IS_CREATE"

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
