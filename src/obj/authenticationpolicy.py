import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.authenticationpolicy.gvauthenticationpolicy import AuthenticationPolicyTag as tags

# ========== Descriptors ==========

class AuthName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class AuthComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = f"COMMENT = '{value}'"
    def __delete__(self, instance):
        del instance._comment

class AuthSamlIdp:
    def __get__(self, instance, owner):
        return instance._saml_idp
    def __set__(self, instance, value):
        instance._saml_idp = f"SAML_IDENTITY_PROVIDER = '{value}'"
    def __delete__(self, instance):
        del instance._saml_idp

class AuthSamlSpInit:
    def __get__(self, instance, owner):
        return instance._saml_sp_init
    def __set__(self, instance, value):
        instance._saml_sp_init = f"SAML_ENABLE_SP_INITIATED = {value}"
    def __delete__(self, instance):
        del instance._saml_sp_init

class AuthSamlIdpInit:
    def __get__(self, instance, owner):
        return instance._saml_idp_init
    def __set__(self, instance, value):
        instance._saml_idp_init = f"SAML_ENABLE_IDP_INITIATED = {value}"
    def __delete__(self, instance):
        del instance._saml_idp_init

class AuthOauthClientId:
    def __get__(self, instance, owner):
        return instance._oauth_client_id
    def __set__(self, instance, value):
        instance._oauth_client_id = f"OAUTH_CLIENT_ID = '{value}'"
    def __delete__(self, instance):
        del instance._oauth_client_id

class AuthOauthClientSecret:
    def __get__(self, instance, owner):
        return instance._oauth_client_secret
    def __set__(self, instance, value):
        instance._oauth_client_secret = f"OAUTH_CLIENT_SECRET = '{value}'"
    def __delete__(self, instance):
        del instance._oauth_client_secret

class AuthOauthRedirectUri:
    def __get__(self, instance, owner):
        return instance._oauth_redirect_uri
    def __set__(self, instance, value):
        instance._oauth_redirect_uri = f"OAUTH_REDIRECT_URI = '{value}'"
    def __delete__(self, instance):
        del instance._oauth_redirect_uri

class AuthMfaEnrollment:
    def __get__(self, instance, owner):
        return instance._mfa_enrollment
    def __set__(self, instance, value):
        instance._mfa_enrollment = f"MFA_ENROLLMENT = {value}"
    def __delete__(self, instance):
        del instance._mfa_enrollment

class AuthMfaEnrollmentGrace:
    def __get__(self, instance, owner):
        return instance._mfa_enrollment_grace
    def __set__(self, instance, value):
        instance._mfa_enrollment_grace = f"MFA_ENROLLMENT_GRACE_PERIOD_DAYS = {value}"
    def __delete__(self, instance):
        del instance._mfa_enrollment_grace

class AuthTagClause:
    def __get__(self, instance, owner):
        return instance._tag_clause
    def __set__(self, instance, value):
        if isinstance(value, dict):
            clause = ", ".join(f"{k} = '{v}'" for k, v in value.items())
        else:
            k, v = next(iter(value.items()))
            clause = f"{k} = '{v}'"
        instance._tag_clause = f"TAG {clause}"
    def __delete__(self, instance):
        del instance._tag_clause


# ========== Attr container ==========

class AuthenticationPolicyAttrs:
    name = AuthName()
    saml_idp = AuthSamlIdp()
    saml_sp_init = AuthSamlSpInit()
    saml_idp_init = AuthSamlIdpInit()
    oauth_client_id = AuthOauthClientId()
    oauth_client_secret = AuthOauthClientSecret()
    oauth_redirect_uri = AuthOauthRedirectUri()
    mfa_enrollment = AuthMfaEnrollment()
    mfa_enrollment_grace = AuthMfaEnrollmentGrace()
    comment = AuthComment()
    tag_clause = AuthTagClause()


# ========== Main Object ==========

class AuthenticationPolicy(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = AuthenticationPolicyAttrs()
        self.session = session
        self.user_id = user_id
        self.logger = logger

    # setters
    def set_name(self, v): self.attr.name = v
    def set_saml_idp(self, v): self.attr.saml_idp = v
    def set_saml_sp_init(self, v): self.attr.saml_sp_init = v
    def set_saml_idp_init(self, v): self.attr.saml_idp_init = v
    def set_oauth_client_id(self, v): self.attr.oauth_client_id = v
    def set_oauth_client_secret(self, v): self.attr.oauth_client_secret = v
    def set_oauth_redirect_uri(self, v): self.attr.oauth_redirect_uri = v
    def set_mfa_enrollment(self, v): self.attr.mfa_enrollment = v
    def set_mfa_enrollment_grace(self, v): self.attr.mfa_enrollment_grace = v
    def set_comment(self, v): self.attr.comment = v
    def set_tag_clause(self, v): self.attr.tag_clause = v

    def set_object_properties_flag(self):
        self.flag_dic = {}
        def set_flag(tag, attrname):
            self.flag_dic[tag] = 1 if getattr(self.attr, attrname, None) is not None else 0

        set_flag(tags.SAML_IDENTITY_PROVIDER, "saml_idp")
        set_flag(tags.SAML_ENABLE_SP_INITIATED, "saml_sp_init")
        set_flag(tags.SAML_ENABLE_IDP_INITIATED, "saml_idp_init")
        set_flag(tags.OAUTH_CLIENT_ID, "oauth_client_id")
        set_flag(tags.OAUTH_CLIENT_SECRET, "oauth_client_secret")
        set_flag(tags.OAUTH_REDIRECT_URI, "oauth_redirect_uri")
        set_flag(tags.MFA_ENROLLMENT, "mfa_enrollment")
        set_flag(tags.MFA_ENROLLMENT_GRACE_PERIOD_DAYS, "mfa_enrollment_grace")
        set_flag(tags.COMMENT, "comment")
        set_flag(tags.TAG_CLAUSE, "tag_clause")

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_auth_policy_qry(self):
        self.qry = f"CREATE AUTHENTICATION POLICY {self.attr.name[0]}"

    def add_properties_to_query(self):
        for prop in self.property_lst:
            self.qry += f" {getattr(self.attr, prop.lower())}"

    def alter_object(self):
        for prop in self.property_lst:
            self.qry = f"ALTER AUTHENTICATION POLICY {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_auth_policy_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        """
        kwargs expects:
          tags.IS_CREATE : "TRUE" / "FALSE"
          tags.NAME : [name, new_name?]
          tags.SAML_IDENTITY_PROVIDER
          tags.SAML_ENABLE_SP_INITIATED
          tags.SAML_ENABLE_IDP_INITIATED
          tags.OAUTH_CLIENT_ID
          tags.OAUTH_CLIENT_SECRET
          tags.OAUTH_REDIRECT_URI
          tags.MFA_ENROLLMENT
          tags.MFA_ENROLLMENT_GRACE_PERIOD_DAYS
          tags.COMMENT
          tags.TAG_CLAUSE
        """
        self.logger.info(f"Operating on {self.__class__.__name__} create flag {kwargs.get(tags.IS_CREATE)}")
        self.is_create = kwargs.get(tags.IS_CREATE)

        self.set_name(kwargs.get(tags.NAME))
        self.set_saml_idp(kwargs.get(tags.SAML_IDENTITY_PROVIDER))
        self.set_saml_sp_init(kwargs.get(tags.SAML_ENABLE_SP_INITIATED))
        self.set_saml_idp_init(kwargs.get(tags.SAML_ENABLE_IDP_INITIATED))
        self.set_oauth_client_id(kwargs.get(tags.OAUTH_CLIENT_ID))
        self.set_oauth_client_secret(kwargs.get(tags.OAUTH_CLIENT_SECRET))
        self.set_oauth_redirect_uri(kwargs.get(tags.OAUTH_REDIRECT_URI))
        self.set_mfa_enrollment(kwargs.get(tags.MFA_ENROLLMENT))
        self.set_mfa_enrollment_grace(kwargs.get(tags.MFA_ENROLLMENT_GRACE_PERIOD_DAYS))
        self.set_comment(kwargs.get(tags.COMMENT))
        self.set_tag_clause(kwargs.get(tags.TAG_CLAUSE))

        self.prepare_query()
        self.execute_final_query()
