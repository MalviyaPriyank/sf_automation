import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class RoleTag(BaseTag):
    NAME="NAME"
    COMMENT="COMMENT"

    @classmethod
    def allowed_value_list(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass

    @classmethod
    def max_allowed_value(cls):
        pass