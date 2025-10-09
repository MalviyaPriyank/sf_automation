import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class PasswordPolicyTag(BaseTag):
    NAME = "NAME"
    PASSWORD_MIN_LENGTH = "PASSWORD_MIN_LENGTH"
    PASSWORD_MAX_LENGTH = "PASSWORD_MAX_LENGTH"
    PASSWORD_MIN_UPPER_CASE_CHARS = "PASSWORD_MIN_UPPER_CASE_CHARS"
    PASSWORD_MIN_LOWER_CASE_CHARS = "PASSWORD_MIN_LOWER_CASE_CHARS"
    PASSWORD_MIN_NUMERIC_CHARS = "PASSWORD_MIN_NUMERIC_CHARS"
    PASSWORD_MIN_SPECIAL_CHARS = "PASSWORD_MIN_SPECIAL_CHARS"
    PASSWORD_MIN_AGE_DAYS = "PASSWORD_MIN_AGE_DAYS"
    PASSWORD_MAX_AGE_DAYS = "PASSWORD_MAX_AGE_DAYS"
    PASSWORD_MAX_RETRIES = "PASSWORD_MAX_RETRIES"
    PASSWORD_LOCKOUT_TIME_MINS = "PASSWORD_LOCKOUT_TIME_MINS"
    PASSWORD_HISTORY = "PASSWORD_HISTORY"
    COMMENT = "COMMENT"
    TAG_CLAUSE = "TAG_CLAUSE"
    IS_CREATE = "IS_CREATE"

    @classmethod
    def allowed_value_list(cls):
        return {
            # You can enforce integer ranges based on Snowflake docs
            "PASSWORD_MIN_LENGTH": list(range(8, 257)),
            "PASSWORD_MAX_LENGTH": list(range(8, 257)),
            # similarly, other numeric parameters could have ranges
        }

    @classmethod
    def max_allowed_value(cls):
        return {}

    @classmethod
    def min_allowed_value(cls):
        return {}
