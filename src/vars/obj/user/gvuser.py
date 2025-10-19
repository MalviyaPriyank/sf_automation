import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag, BaseMethod

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
    def get_attributes_with_description(cls):
        return {
            "NAME":"this is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO, these are to be taken from user. the format is a dictionary with key 'NAME' for the name, and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
            "PASSWORD": "Initial password for the user. User must change this upon first login.",
            "LOGIN_NAME": "Login name for the user (unique within the account).",
            "DISPLAY_NAME": "Display name for the user, visible in Snowsight and the UI.",
            "FIRST_NAME": "First name of the user.",
            "LAST_NAME": "Last name of the user.",
            "EMAIL": "Email address associated with the user account.",
            "MUST_CHANGE_PASSWORD": "If TRUE, user must change the password at the next login.",
            "DISABLED": "If TRUE, disables the user so they cannot log in.",
            "DAYS_TO_EXPIRY": "Number of days until the user password expires.",
            "MINS_TO_UNLOCK": "Number of minutes until a locked user account automatically unlocks.",
            "DEFAULT_WAREHOUSE": "Default warehouse automatically used in sessions for this user.",
            "DEFAULT_ROLE": "Default role granted to the user upon login.",
            "DEFAULT_SECONDARY_ROLES": "Secondary roles automatically enabled for the user on login.",
            "MINS_TO_BY_PASS_MFA": "Number of minutes to bypass multi-factor authentication after a successful login.",
            "RSA_PUBLIC_KEY": "First RSA public key for key pair authentication.",
            "RSA_PUBLIC_KEY_FP": "Fingerprint for the first RSA public key.",
            "RSA_PUBLIC_KEY_2": "Second RSA public key for key pair authentication rotation.",
            "RSA_PUBLIC_KEY_2_FP": "Fingerprint for the second RSA public key.",
            "TYPE": "Type of user (e.g., 'LOCAL' or 'FEDERATED').",
            "ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR": "If TRUE, shows full unredacted query text in syntax error messages.",
            "IS_CREATE":"Set this to 'TRUE' if create object. set to 'FALSE' if alter object."
        }

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
          
