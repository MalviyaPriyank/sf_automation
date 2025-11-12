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
    def get_attributes_with_description(cls):
        attr_dict=super().get_attributes_with_description()
        attr_dict["TYPE"]="Specifies the type of network identifiers being allowed or blocked. A network rule can have only one type. Allowed values : IPV4, AWSVPCEID, AZURELINKID,HOST_PORT,PRIVATE_HOST_PORT."
        attr_dict["VALUE_LIST"]="Specifies the network identifiers that will be allowed or blocked. Valid values in the list are determined by the type of network rule"
        attr_dict["MODE"]="Specifies what is restricted by the network rule. Allowed values : INGRESS, EGRESS, INTERNAL_STAGE."
        return attr_dict
    
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
          
