import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class ExternalStageTag(BaseTag):
    FILE_FORMAT="FILE_FORMAT"
    URL="URL"
    AWS_ACCESS_POINT_ARN="AWS_ACCESS_POINT_ARN"
    STORAGE_INTEGRATION="STORAGE_INTEGRATION"   
    AWS_KEY_ID="AWS_KEY_ID"
    AWS_SECRET_KEY="AWS_SECRET_KEY"
    AWS_TOKEN="AWS_TOKEN"
    AZURE_SAS_TOKEN="AZURE_SAS_TOKEN"
    AWS_ROLE="AWS_ROLE"
    ENCRYPTION="ENCRYPTION"
    ENCRYPTION_MASTER_KEY="ENCRYPTION_MASTER_KEY"
    ENCRYPTION_KMS_KEY_ID="ENCRYPTION_KMS_KEY_ID"
    USE_PRIVATELINK_ENDPOINT="USE_PRIVATELINK_ENDPOINT"
    ENABLE="ENABLE"
    REFRESH_ON_CREATE="REFRESH_ON_CREATE"
    AUTO_REFRESH="AUTO_REFRESH"
    NOTIFICATION_INTEGRATION="NOTIFICATION_INTEGRATION"
    PROTOCOLS="PROTOCOLS"
    S3_ENCRYPTION_TYPE="S3_ENCRYPTION_TYPE"
    GCS_ENCRYPTION_TYPE="GCS_ENCRYPTION_TYPE"
    AZURE_ENCRYPTION_TYPE="AZURE_ENCRYPTION_TYPE"

    @classmethod
    def allowed_value_list(cls):
        return {
            "ENCRYPTION":["SNOWFLAKE_FULL","SNOWFLAKE_SSE"],
            "PROTOCOLS":['s3','s3china','s3gov','gcs','azure'],
            "S3_ENCRYPTION_TYPE":['AWS_CSE','AWS_SSE_S3','AWS_SSE_KMS'],
            "GCS_ENCRYPTION_TYPE":['GCS_SSE_KMS'],
            "AZURE_ENCRYPTION_TYPE":['AZURE_CSE']

        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
          
