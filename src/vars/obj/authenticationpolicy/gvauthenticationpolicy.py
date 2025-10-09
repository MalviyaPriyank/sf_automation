import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class AuthenticationPolicyTag(BaseTag):
    NAME = "NAME"
    SAML_IDENTITY_PROVIDER = "SAML_IDENTITY_PROVIDER"
    SAML_ENABLE_SP_INITIATED = "SAML_ENABLE_SP_INITIATED"
    SAML_ENABLE_IDP_INITIATED = "SAML_ENABLE_IDP_INITIATED"
    OAUTH_CLIENT_ID = "OAUTH_CLIENT_ID"
    OAUTH_CLIENT_SECRET = "OAUTH_CLIENT_SECRET"
    OAUTH_REDIRECT_URI = "OAUTH_REDIRECT_URI"
    MFA_ENROLLMENT = "MFA_ENROLLMENT"
    MFA_ENROLLMENT_GRACE_PERIOD_DAYS = "MFA_ENROLLMENT_GRACE_PERIOD_DAYS"
    COMMENT = "COMMENT"
    TAG_CLAUSE = "TAG_CLAUSE"
    IS_CREATE = "IS_CREATE"

    @classmethod
    def allowed_value_list(cls):
        return {
            "SAML_ENABLE_SP_INITIATED": ["TRUE", "FALSE"],
            "SAML_ENABLE_IDP_INITIATED": ["TRUE", "FALSE"],
            "MFA_ENROLLMENT": ["OPTIONAL", "REQUIRED", "DISABLED"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
