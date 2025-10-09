import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class RowAccessPolicyTag(BaseTag):
    NAME = "NAME"
    SIGNATURE = "SIGNATURE"
    RETURNS = "RETURNS"
    EXPRESSION = "EXPRESSION"
    COMMENT = "COMMENT"
    TAG_CLAUSE = "TAG_CLAUSE"
    IS_CREATE = "IS_CREATE"

    @classmethod
    def allowed_value_list(cls):
        return {
            "RETURNS": ["BOOLEAN"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
