import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class NetworkPolicyTag(BaseTag):
    NAME = "NAME"
    ALLOWED_NETWORK_RULE_LIST = "ALLOWED_NETWORK_RULE_LIST"
    BLOCKED_NETWORK_RULE_LIST = "BLOCKED_NETWORK_RULE_LIST"
    ALLOWED_IP_LIST = "ALLOWED_IP_LIST"
    BLOCKED_IP_LIST = "BLOCKED_IP_LIST"
    COMMENT = "COMMENT"
    TAG = "TAG"
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
