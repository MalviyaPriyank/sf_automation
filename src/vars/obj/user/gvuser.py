import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class UserTag(BaseTag):
    PASSWORD="PASSWORD"
    LOGIN_NAME="LOGIN_NAME"
    DISPLAY_NAME="DISPLAY_NAME"
    FIRST_NAME="FIRST_NAME"
    LAST_NAME="LAST_NAME"
    EMAIL="EMAIL"
    MUST_CHANGE_PASSWORD="MUST_CHANGE_PASSWORD"
    DISABLED="DISABLED"
    DAYS_TO_EXPIRY="DAYS_TO_EXPIRY"
    MINS_TO_UNLOCK="MINS_TO_UNLOCK"
    DEFAULT_WAREHOUSE="DEFAULT_WAREHOUSE"
    DEFAULT_ROLE="DEFAULT_ROLE"
    DEFAULT_SECONDARY_ROLES="DEFAULT_SECONDARY_ROLES"
    MINS_TO_BY_PASS_MFA="MINS_TO_BY_PASS_MFA"
    RSA_PUBLIC_KEY="RSA_PUBLIC_KEY"
    RSA_PUBLIC_KEY_FP="RSA_PUBLIC_KEY_FP"
    RSA_PUBLIC_KEY_2="RSA_PUBLIC_KEY_2"
    RSA_PUBLIC_KEY_2_FP="RSA_PUBLIC_KEY_2_FP"
    TYPE="TYPE"
    ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR="ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR"
    

    @classmethod
    def allowed_value_list(cls):
        return {
            "TYPE":['PERSON','SERVICE','LEGACY_SERVICE','NULL'],
            "DEFAULT_SECONDARY_ROLES":['ALL']
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
          
