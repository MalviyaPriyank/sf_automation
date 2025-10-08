import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class SecurityIntegrationTag(BaseTag):
    TYPE="TYPE"
    AUTH_TYPE="AUTH_TYPE"
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
    def allowed_value_list(cls):
        return {
            "OAUTH_CLIENT_AUTH_METHOD":["CLIENT_SECRET_BASIC","CLIENT_SECRET_POST"],
            "OAUTH_GRANT":["CLIENT_CREDENTIALS","AUTHORIZATION_CODE","JWT_BEARER"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass
    @classmethod
    def min_allowed_value(cls):
        pass
          
