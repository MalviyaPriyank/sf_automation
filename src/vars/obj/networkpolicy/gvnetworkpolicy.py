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
    NETWORK_RULE_DATABASE="NETWORK_RULE_DATABASE"
    NETWORK_RULE_SCHEMA="NETWORK_RULE_SCHEMA"
    COMMENT = "COMMENT"
    TAG = "TAG"
    IS_CREATE = "IS_CREATE"

    @classmethod
    def get_attributes_with_description(cls):
        return {
            "NAME":"This is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. "
                    "This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO; "
                    "these are to be taken from user. The format is a dictionary with key 'NAME' for the name, "
                    "and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
            "ALLOWED_NETWORK_RULE_LIST":"Specifies a list of network rules that contain the network identifiers that are allowed access to Snowflake. There is no limit on the number of network rules in the list.",
            "BLOCKED_NETWORK_RULE_LIST":"Specifies a list of network rules that contain the network identifiers that are denied access to Snowflake. There is no limit on the number of network rules in the list.",
            "ALLOWED_IP_LIST":"""
            Specifies a list of IPv4 addresses that are allowed access to your Snowflake account. This is referred to as the allowed list.
            Snowflake recommends using network rules in conjunction with network policies rather than using this property.
            """,
            "BLOCKED_IP_LIST":"""
            Specifies a list of IPv4 addresses that are denied access to your Snowflake account. This is referred to as the blocked list. To unset this parameter, specify a different CIDR block range, a series of IPv4 addresses, or a single IPv4 address.
            Snowflake recommends using network rules in conjunction with network policies rather than using this parameter.
            """,
            "NETWORK_RULE_DATABASE":"Database of the network rule to be used.",
            "NETWORK_RULE_SCHEMA":"Schema of the network rule to be used.",
            "COMMENT":"This will be user defined comment for the object. If user does not define one add a proper comment as per your understanding and inform the user.",
            "IS_CREATE":"Set this to 'TRUE' if create object. set to 'FALSE' if alter object."
        }

    @classmethod
    def allowed_value_list(cls):
        pass
    
    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
