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
    ALLOWED_DRIVERS="ALLOWED_DRIVERS"


    @classmethod
    def get_attributes_with_description(cls):
        return {
            "NAME":"this is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO, these are to be taken from user. the format is a dictionary with key 'NAME' for the name, and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
            "COMMENT":"Comment for the API Integration.",
            "IS_CREATE":"Set this to 'TRUE' if create object. set to 'FALSE' if alter object.",
            "AUTHENTICATION_METHODS":"""
            A list of authentication methods that are allowed during login. Pass value as a list
            One of following values allowed:
                - ALL
                - SAML
                - PASSWORD
                - OAUTH
                - KEYPAIR
                - PROGRAMMATIC_ACCESS_TOKEN
                - WORKLOAD_IDENTITY
            """,
            "MFA_ENROLLMENT":"""
            Determines whether a user must enroll in multi-factor authentication. Following values allowed:
                - REQUIRED
                - REQUIRED_PASSWORD_ONLY
                - OPTIONAL
            """,
            "MFA_POLICY":"""
            Specifies the policies that affect how multi-factor authentication (MFA) is enforced. 
            You can specify more than one of following values, as a comma separated list:
                - ALL
                - PASSKEY
                - TOTP
                - OTP
                - DUO
            """,
            "CLIENT_TYPES":"""
            Optional value.
            A list of clients that can authenticate with Snowflake. 
            You can specify more than one of following values, as a comma separated list:
                - ALL
                - SNOWFLAKE_UI
                - DRIVERS
                - SNOWFLAKE_CLI
                - SNOWSQL
            Pass this as a list.
            """,
            "CLIENT_POLICY":"""
            Optional Value.
            Specifies a policy within the authentication policy that sets the minimum version allowed for each specified client type.

            If CLIENT_TYPES is empty, contains ALL, or contains DRIVERS, the CLIENT_POLICY parameter accepts one or more of the 
            following driver clients (and a specific version string). For any driver client that is not specified, 
            the policy implicitly allows any version of that client.

            If CLIENT_TYPES contains another value, such as SNOWFLAKE_CLI, and does not also contain DRIVERS, 
            specifying any of the following client types results in an error. You cannot create (or alter) an authentication policy 
            such that the CLIENT_TYPES and CLIENT_POLICY parameters are not compatible.

            Always pass this as a dictionary of Drivers as keys and their minimum version as its value.
            """,
            "SECURITY_INTEGRATIONS":"""
            A list of security integrations the authentication policy is associated with. This parameter has no effect when SAML or OAUTH are not in the AUTHENTICATION_METHODS list.
            All values in the SECURITY_INTEGRATIONS list must be compatible with the values in the AUTHENTICATION_METHODS list. 
            For example, if SECURITY_INTEGRATIONS contains a SAML security integration, 
            and AUTHENTICATION_METHODS contains OAUTH, then you cannot create the authentication policy.
            """,
            "PAT_POLICY":"""
            Specifies the policies for programmatic access tokens.
            """,
            "WORKLOAD_IDENTITY_POLICY":"""
            Specifies the policies for workload identity federation.
            """
        }

    @classmethod
    def allowed_value_list(cls):
        return {
            "AUTHENTICATION_METHODS": ["ALL","SAML","PASSWORD","OAUTH","KEYPAIR","PROGRAMMATIC_ACCESS_TOKEN","WORKLOAD_IDENTITY"],
            "MFA_AUTHENTICATION_METHODS": ["SAML", "PASSWORD"],
            "MFA_ENROLLMENT": ["OPTIONAL", "REQUIRED"],
            "MFA_POLICY":["ALL","PASSKEY","TOTP","DUO"],
            "CLIENT_TYPES":["ALL","SNOWFLAKE_UI","DRIVERS","SNOWFLAKE_CLI","SNOWSQL"],
            "ALLOWED_DRIVERS":["JDBC_DRIVER","ODBC_DRIVER","PYTHON_DRIVER","JAVASCRIPT_DRIVER","C_DRIVER","GO_DRIVER","PHP_DRIVER","DOTNET_DRIVER","SQL_API","SNOWPIPE_STREAMING_CLIENT_SDK","PY_CORE","SPROC_PYTHON","PYTHON_SNOWPARK","SQL_ALCHEMY","SNOWPARK","SNOWFLAKE_CLIENT"]

        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
