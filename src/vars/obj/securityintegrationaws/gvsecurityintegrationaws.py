import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class SecurityIntegrationAWSTag(BaseTag):
    TYPE="TYPE"
    AUTH_TYPE="AUTH_TYPE"
    ENABLED="ENABLED"
    AWS_ROLE_ARN="AWS_ROLE_ARN"
    COMMENT="COMMENT"


    @classmethod
    def get_attributes_with_description(cls):
        return {
            "NAME":"this is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO, these are to be taken from user. the format is a dictionary with key 'NAME' for the name, and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
            "IS_CREATE":"Set this to 'TRUE' if create object. set to 'FALSE' if alter object.",
            "TYPE": "Specifies that the security integration is an interface between Snowflake and one or more AWS services that use OAuth 2.0 or AWS IAM credentials. Always API_AUTHENTICATION",
            "AUTH_TYPE": "Specifies that the integration uses AWS IAM to authenticate to authenticate to one or more AWS services. Always AWS_IAM",
            "AWS_ROLE_ARN": "Specifies the Amazon Resource Name (ARN) of the AWS identity and access management (IAM) role that grants privileges for AWS resources.",
            "ENABLED": "Specifies whether this security integration is enabled or disabled.",
            "COMMENT": "Specifies a comment for the integration. Default value is NONE"        
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
          
