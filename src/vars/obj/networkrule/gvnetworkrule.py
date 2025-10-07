import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag,BaseMethod

class NetworkRuleTag(BaseTag,BaseMethod):
    TYPE="TYPE"
    VALUE_LIST="VALUE_LIST"
    MODE="MODE"    
    COMMENT="COMMENT"
    
    @classmethod
    def allowed_value_list(cls):
        return {
            "TYPE":["IPV4","AWSVPCEID","AZURELINKID","HOST_PORT","PRIVATE_HOST_PORT"],
            "MODE":["INGRESS","INTERNAL_STAGE","EGRESS"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
          
