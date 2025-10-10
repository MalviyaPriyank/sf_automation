import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class StorageIntegrationTag(BaseTag):
    TYPE="TYPE"
    ENABLED="ENABLED"
    STORAGE_PROVIDER="STORAGE_PROVIDER"
    STORAGE_AWS_ROLE_ARN="STORAGE_AWS_ROLE_ARN"
    STORAGE_AWS_EXTERNAL_ID="STORAGE_AWS_EXTERNAL_ID"
    STORAGE_AWS_OBJECT_ACL="STORAGE_AWS_OBJECT_ACL"
    USE_PRIVATE_LINK_ENDPOINT="USE_PRIVATE_LINK_ENDPOINT"
    AZURE_TENANT_ID="AZURE_TENANT_ID"
    STORAGE_ALLOWED_LOCATIONS="STORAGE_ALLOWED_LOCATIONS"
    STORAGE_BLOCKED_LOCATIONS="STORAGE_BLOCKED_LOCATIONS"
    
    

    @classmethod
    def allowed_value_list(cls):
        pass

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
          
