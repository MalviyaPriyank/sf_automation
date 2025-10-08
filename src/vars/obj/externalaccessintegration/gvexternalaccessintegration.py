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
    def allowed_value_list(cls):
        pass

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass