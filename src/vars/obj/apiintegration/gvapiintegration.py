import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class ComputePoolTag(BaseTag):
    NAME = "NAME"
    IS_CREATE = "IS_CREATE"
    API_TYPE="API_TYPE"
    API_PROVIDER="API_PROVIDER"
    API_AWS_ROLE_ARN="API_AWS_ROLE_ARN"
    API_KEY="API_KEY"
    API_ALLOWED_PREFIXES="API_ALLOWED_PREFIXES"
    AZURE_TENANT_ID="AZURE_TENANT_ID"
    AZURE_AD_APPLICATION_ID="AZURE_AD_APPLICATION_ID"
    GOOGLE_AUDIENCE="GOOGLE_AUDIENCE"
    ENABLED="ENABLED"
    API_BLOCKED_PREFIXES="API_BLOCKED_PREFIXES"
    ALLOWED_AUTHENTICATION_SECRETS="ALLOWED_AUTHENTICATION_SECRETS"

    @classmethod
    def get_attributes_with_description(cls):
        return {
            "NAME":"this is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO, these are to be taken from user. the format is a dictionary with key 'NAME' for the name, and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
            "API_TYPE":"Specifies if the api integration is for AZURE, AMAZON, GOOGLE or GIT",
            "DATABASE":"Only required for GIT API Integration.",
            "SCHEMA":"Only required for GIT API Integration",
            "COMMENT":"Comment for the API Integration.",
            "IS_CREATE":"Set this to 'TRUE' if create object. set to 'FALSE' if alter object.",
            "API_PROVIDER":"""
            It can have different values for differnt API TYPE.
            For API_TYPE = AMAZON valid values are :
                - aws_api_gateway : for Amazon API Gateway using regional endpoints.
                - aws_private_api_gateway : for Amazon API Gateway using private endpoints.
                - aws_gov_api_gateway : for Amazon API Gateway using U.S. government GovCloud endpoints.
                - aws_gov_private_api_gateway : for Amazon API Gateway using U.S. government GovCloud endpoints that are also private endpoints.
            
            For API_TYPE = AZURE : azure_api_management
            For API_TYPE = GOOGLE : google_api_gateway
            For API_TYPE = GIT : git_https_api
            """,
            "API_AWS_ROLE_ARN":"This is only required when API_TYPE is AMAZON. This is the ARN (Amazon resource name) of a cloud platform role. Default is NONE.",
            "API_KEY":"The API key (also called a 'subscription key').",
            "API_ALLOWED_PREFIXES":"""
            Explicitly limits external functions that use the integration to reference one or more HTTPS proxy service endpoints and resources within those proxies.
            Each URL in API_ALLOWED_PREFIXES = (...) is treated as a prefix. 
            For example, if you specify:
            https://my-external-function-demo.azure-api.net/my-function-app-name
            that means all resources under https://my-external-function-demo.azure-api.net/my-function-app-name are allowed. Pass it as a comma separated list of URLs.
            """,
            "AZURE_TENANT_ID":"""
            Specifies the ID for the Office 365 tenant that all Azure API Management instances belong to. 
            An API integration can authenticate to only one tenant, and so the allowed and blocked locations must 
            refer to API Management instances that all belong to this tenant.To find your tenant ID, sign in to 
            the Azure portal and select Azure Active Directory » Properties. The tenant ID is displayed in the Tenant ID field.
            """,
            "AZURE_AD_APPLICATION_ID":"""
            The “Application (client) id” of the Azure AD (Active Directory) app for your remote service.
            """,
            "API_BLOCKED_PREFIXES":"""
            Lists the endpoints and resources in the HTTPS proxy service that are not allowed to be called from Snowflake.
            The possible values for locations follow the same rules as for API_ALLOWED_PREFIXES above.
            API_BLOCKED_PREFIXES takes precedence over API_ALLOWED_PREFIXES. If a prefix matches both, then it is blocked. In other words, Snowflake allows all values that match API_ALLOWED_PREFIXES except values that also match API_BLOCKED_PREFIXES.
            If a value is outside API_ALLOWED_PREFIXES, you do not need to explicitly block it. Pass it as a comma separated list of URLs.
            """,
            "GOOGLE_AUDIENCE":"""
            This is used as the audience claim when generating the JWT (JSON Web Token) to authenticate to the Google API Gateway. 
            If the user want more information share the link : https://docs.cloud.google.com/api-gateway/docs/authenticate-service-account#configure_auth
            """,
            "ALLOWED_AUTHENTICATION_SECRETS":"""
            Specifies the secrets that UDF or procedure handler code can use when accessing the Git repository at 
            the API_ALLOWED_PREFIXES value. IT must be one of the following values:
                - One or more fully-qualified Snowflake secret names to allow any of the listed secrets.
                - Default : all to allow any secret.
                - none to allow no secrets.        
            """,
            "ENABLED":"Specifies whether the integration is enabled on creation or not. Pass this as a string."
        }

    @classmethod
    def allowed_value_list(cls):
        return {
            "API_TYPE": ["AZURE", "AMAZON","GOOGLE","GIT"],
            "API_PROVIDER":{
                "AMAZON":["aws_api_gateway","aws_private_api_gateway","aws_gov_api_gateway","aws_gov_private_api_gateway"]
            }
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
