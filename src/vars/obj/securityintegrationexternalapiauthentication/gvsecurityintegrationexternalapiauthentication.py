import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class SecurityIntegrationExternalApiAuthentication(BaseTag):
    API_TYPE="API_TYPE"
    TYPE="TYPE"
    AUTH_TYPE="AUTH_TYPE"
    INTEGRATION_TYPE="INTEGRATION_TYPE"
    ENABLED="ENABLED"
    OAUTH_AUTHORIZATION_ENDPOINT="OAUTH_AUTHORIZATION_ENDPOINT"
    OAUTH_TOKEN_ENDPOINT="OAUTH_TOKEN_ENDPOINT"
    OAUTH_CLIENT_AUTH_METHOD="OAUTH_CLIENT_AUTH_METHOD"
    OAUTH_CLIENT_ID="OAUTH_CLIENT_ID"
    OAUTH_CLIENT_SECRET="OAUTH_CLIENT_SECRET"
    OAUTH_GRANT="OAUTH_GRANT"
    OAUTH_ACCESS_TOKEN_VALIDITY="OAUTH_ACCESS_TOKEN_VALIDITY"
    OAUTH_REFRESH_TOKEN_VALIDITY="OAUTH_REFRESH_TOKEN_VALIDITY"
    OAUTH_ALLOWED_SCOPES="OAUTH_ALLOWED_SCOPES"

    @classmethod
    def get_attributes_with_description(cls):
        return {
            "NAME":"this is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO, these are to be taken from user. the format is a dictionary with key 'NAME' for the name, and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
            "IS_CREATE":"Set this to 'TRUE' if create object. set to 'FALSE' if alter object.",
            "API_TYPE":"Specifies the type of service for which integration is being setup. Allowed values : 'AUTHORIZATION_CODE','JWT_BEARER','CLIENT_CREDENTIALS'.",
            "TYPE": "Specifies that you are creating a security interface between Snowflake and an external service that uses OAuth 2.0 with External API Authentication. Always API_AUTHENTICATION",
            "AUTH_TYPE": "Specifies that the integration uses OAuth 2.0 to authenticate to the external service. Always OUATH2",
            "ENABLED": "Specifies whether this security integration is enabled or disabled.",
            "OAUTH_TOKEN_ENDPOINT": "Specifies the token endpoint used by the client to obtain an access token by presenting its authorization grant or refresh token. The token endpoint is used with every authorization grant except for the implicit grant type (since an access token is issued directly).",
            "OAUTH_CLIENT_AUTH_METHOD": "Controls how client credentials are sent to the external service. Only following values allowed : CLIENT_SECRET_BASIC, CLIENT_SECRET_POST",
            "OAUTH_CLIENT_ID": "Specifies the client ID for the OAuth application in the external service.",
            "OAUTH_CLIENT_SECRET":"""
            It is the OAuth application password issued by the external identity provider. 
            Snowflake uses this secret to authenticate itself to the external OAuth token endpoint so it can request access tokens.
            """,
            "OAUTH_GRANT":"""
            Specifies the type of OAuth flow. Allowed values:
            'AUTHORIZATION_CODE' : when the integration will use an authorization code.
            'CLIENT_CREDENTIALS':  when the integration will use client credentials.
            'JWT_BEARER' : when the integration will use a JWT Token.
            """,
            "OAUTH_ACCESS_TOKEN_VALIDITY":"""
            Specifies the default lifetime of the OAuth access token (in seconds) issued by an OAuth server. The value set in this property 
            is used if the access token lifetime is not returned as part of OAuth token response. When both values are available, 
            the smaller of the two values will be used to refresh the access token.
            """,
            "OAUTH_ALLOWED_SCOPES":"""
            Specifies a comma-separated list of scopes, with single quotes surrounding each scope, 
            to use when making a request from the OAuth by a role with USAGE on the integration during 
            the OAuth client credentials flow.
            """,
            "OAUTH_AUTHORIZATION_ENDPOINT": """
            Specifies the URL for authenticating to the external service. For example, to connect to the ServiceNow 
            instance the URL should be in the following format : https://<instance_name>.service-now.com/oauth_token 
            Where <instance_name> is the name of your ServiceNow instance.""",
            "OAUTH_REFRESH_TOKEN_VALIDITY":"""
            Specifies the value to determine the validity of the refresh token obtained from the OAuth server.
            """
        }

    @classmethod
    def allowed_value_list(cls):
        return {
            "OAUTH_CLIENT_AUTH_METHOD":["CLIENT_SECRET_BASIC","CLIENT_SECRET_POST"],
            "OAUTH_GRANT":["CLIENT_CREDENTIALS","AUTHORIZATION_CODE","JWT_BEARER"],
            "INTEGRATION_TYPE":["CLIENT_CREDENTIALS","AUTHORIZATION_CODE","JWT_BEARER"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass
    @classmethod
    def min_allowed_value(cls):
        pass
          
