import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class ContactTag(BaseTag):
    NAME = "NAME"
    USERS = "USERS"
    EMAIL_DISTRIBUTION_LIST = "EMAIL_DISTRIBUTION_LIST"
    URL = "URL"
    COMMENT = "COMMENT"
    IS_CREATE = "IS_CREATE"

    @classmethod
    def allowed_value_list(cls):
        pass

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass