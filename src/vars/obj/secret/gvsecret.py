import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class SecretTag(BaseTag):
    TYPE="TYPE"
    API_AUTHENTICATION="API_AUTHENTICATION"
    OAUTH_SCOPES="OAUTH_SCOPES"
    OAUTH_REFRESH_TOKEN="OAUTH_REFRESH_TOKEN"
    OAUTH_REFRESH_TOKEN_EXPIRY_TIME="OAUTH_REFRESH_TOKEN_EXPIRY_TIME"
    ENABLED="ENABLED"
    USERNAME="USERNAME"
    PASSWORD="PASSWORD"
    SECRET_STRING="SECRET_STRING"
    ALGORITHM="ALGORITHM"
    SECRET_OPTION="SECRET_OPTION"


    

    @classmethod
    def allowed_value_list(cls):
        return {
            "TYPE":["OAUTH2","CLOUD_PROVIDER_TOKEN","PASSWORD","GENERIC_STRING","SYMMETRIC_KEY"],
            "SECRET_OPTION":["OAUTH_WITH_CLIENT_CREDENTIALS","OAUTH_WITH_AUTH_CODE_GRANT_FLOW","CLOUD_PROVIDER","BASIC_AUTHENTICATION","GENERIC_STRING","SYMMETRIC_KEY"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass
    @classmethod
    def min_allowed_value(cls):
        pass
          
