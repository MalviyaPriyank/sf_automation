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
            "TYPE": "Specifies that you are creating a security interface between Snowflake and an external service that uses OAuth 2.0 with External API Authentication. Always API_AUTHENTICATION",
            "AUTH_TYPE": "Specifies that the integration uses OAuth 2.0 to authenticate to the external service. Always OUATH2",
            "INTEGRATION_TYPE": "Specifies what type of security integration user is trying to create. Only one of following values allowed : CLIENT_CREDENTIALS, AUTHORIZATION_CODE, JWT_BEARER",
            "ENABLED": "Specifies whether this security integration is enabled or disabled.",
            "OAUTH_AUTHORIZATION_ENDPOINT": "Specifies the URL for authenticating to the external service. For example, to connect to the ServiceNow instance the URL should be in the following format : https://<instance_name>.service-now.com/oauth_token Where <instance_name> is the name of your ServiceNow instance.",
            "OAUTH_TOKEN_ENDPOINT": "Specifies the token endpoint used by the client to obtain an access token by presenting its authorization grant or refresh token. The token endpoint is used with every authorization grant except for the implicit grant type (since an access token is issued directly).",
            "OAUTH_CLIENT_AUTH_METHOD": "Controls how client credentials are sent to the external service. Only following values allowed : CLIENT_SECRET_BASIC, CLIENT_SECRET_POST",
            "OAUTH_CLIENT_ID": "Specifies the client ID for the OAuth application in the external service.",
            "OAUTH_CLIENT_SECRET":"Specifies the client secret for the OAuth application in the ServiceNow instance from the previous step. The connector uses this to request an access token from the ServiceNow instance."
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
          
