import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class TagTag(BaseTag):
    NAME = "NAME"
    ALLOWED_VALUES = "ALLOWED_VALUES"
    PROPAGATE = "PROPAGATE"
    ON_CONFLICT = "ON_CONFLICT"
    COMMENT = "COMMENT"
    TAG_CLAUSE = "TAG_CLAUSE"
    IS_CREATE = "IS_CREATE"

    @classmethod
    def allowed_value_list(cls):
        return {
            "PROPAGATE": [
                "ON_DEPENDENCY_AND_DATA_MOVEMENT",
                "ON_DEPENDENCY",
                "ON_DATA_MOVEMENT"
            ],
            # ON_CONFLICT can be a string or ALLOWED_VALUES_SEQUENCE
            # ALLOWED_VALUES is a list of string values
        }

    @classmethod
    def max_allowed_value(cls):
        return {}

    @classmethod
    def min_allowed_value(cls):
        return {}
