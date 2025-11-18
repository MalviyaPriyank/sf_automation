import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseMethod,BaseTag

class ExternalAccessIntegration(BaseTag,BaseMethod):
    ALLOWED_NETWORK_RULES="ALLOWED_NETWORK_RULES"
    ENABLED="ENABLED"
    ALLOWED_API_AUTHENTICATION_INTEGRATIONS="ALLOWED_API_AUTHENTICATION_INTEGRATIONS"
    ALLOWED_AUTHENTICATION_SECRETS="ALLOWED_AUTHENTICATION_SECRETS"
    COMMENT="COMMENT"

    @classmethod
    def get_attributes_with_description(cls):
        return {
            "NAME":"this is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO, these are to be taken from user. the format is a dictionary with key 'NAME' for the name, and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
            "IS_CREATE":"Set this to 'TRUE' if create object. set to 'FALSE' if alter object.",
            "ALLOWED_NETWORK_RULES":"Specifies the allowed network rules. Only egress rules may be specified.",
            "ENABLED": "Specifies whether this integration is enabled or disabled. If the integration is disabled, any handler code that relies on it will be unable to reach the external network location.",
            "ALLOWED_API_AUTHENTICATION_INTEGRATIONS": """
            Specifies the security integrations whose OAuth authorization server issued the secret used by the UDF or procedure. 
            The security integration must be the type used for external API integration.
            This parameters value must be one of the following:
            One or more Snowflake security integration names to allow any of the listed integrations.
            none to allow no integrations.
            Security integrations specified by this parameter  as well as secrets specified by the 
            ALLOWED_AUTHENTICATION_SECRETS parameter are ways to allow secrets for use in a UDF or procedure that 
            uses this external access integration.
            """,
            "ALLOWED_AUTHENTICATION_SECRETS": """
            Specifies the secrets that UDF or procedure handler code can use when accessing the external network locations referenced in allowed network rules.
            This parameters value must be one of the following: 
            One or more Snowflake secret names to allow any of the listed secrets.
            all to allow any secret.
            none to allow no secrets.
            The ALLOWED_API_AUTHENTICATION_INTEGRATIONS parameter can also specify allowed secrets. 
            """,
            "COMMENT": "Specifies a comment for the external access integration."
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