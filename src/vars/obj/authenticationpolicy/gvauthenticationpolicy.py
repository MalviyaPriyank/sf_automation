import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class AuthenticationPolicyTag(BaseTag):
    NAME = "NAME"
    AUTHENTICATION_METHODS = "AUTHENTICATION_METHODS"
    #MFA_AUTHENTICATION_METHODS = "MFA_AUTHENTICATION_METHODS"
    MFA_ENROLLMENT = "MFA_ENROLLMENT"
    MFA_POLICY = "MFA_POLICY"
    CLIENT_TYPES = "CLIENT_TYPES"
    CLIENT_POLICY = "CLIENT_POLICY"
    SECURITY_INTEGRATIONS = "SECURITY_INTEGRATIONS"
    PAT_POLICY = "PAT_POLICY"
    WORKLOAD_IDENTITY_POLICY = "WORKLOAD_IDENTITY_POLICY"
    COMMENT="COMMENT"


    @classmethod
    def get_attributes_with_description(cls):
        return {
            "NAME":"this is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO, these are to be taken from user. the format is a dictionary with key 'NAME' for the name, and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
            "AUTHENTICATION_METHODS":"A list of authentication methods that are allowed during login. Pass value as a list",
            "MFA_ENROLLMENT":"Determines whether a user must enroll in multi-factor authentication.",
        }

    @classmethod
    def allowed_value_list(cls):
        return {
            "AUTHENTICATION_METHODS": ["ALL","SAML","PASSWORD","OAUTH","KEYPAIR","PROGRAMMATIC_ACCESS_TOKEN","WORKLOAD_IDENTITY"],
            "MFA_AUTHENTICATION_METHODS": ["SAML", "PASSWORD"],
            "MFA_ENROLLMENT": ["OPTIONAL", "REQUIRED"],
            "MFA_POLICY":["ALL","PASSKEY","TOTP","DUO"],
            "CLIENT_TYPES":["ALL","SNOWFLAKE_UI","DRIVERS","SNOWFLAKE_CLI","SNOWSQL"]

        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
