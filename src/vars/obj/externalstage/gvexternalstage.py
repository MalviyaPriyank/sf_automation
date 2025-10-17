import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag,BaseMethod

class ExternalStageTag(BaseTag,BaseMethod):
    FILE_FORMAT="FILE_FORMAT"
    URL="URL"
    AWS_ACCESS_POINT_ARN="AWS_ACCESS_POINT_ARN"
    STORAGE_INTEGRATION="STORAGE_INTEGRATION"   
    AWS_KEY_ID="AWS_KEY_ID"
    AWS_SECRET_KEY="AWS_SECRET_KEY"
    AWS_TOKEN="AWS_TOKEN"
    AZURE_SAS_TOKEN="AZURE_SAS_TOKEN"
    AWS_ROLE="AWS_ROLE"
    ENCRYPTION_TYPE="ENCRYPTION_TYPE"
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
    def get_attributes_with_description(cls):
        attr_dict = super().get_attributes_with_description()
        attr_dict["FILE_FORMAT"] = "user provided value for FILE_FORMAT for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["URL"] = "user provided value for URL for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["AWS_ACCESS_POINT_ARN"] = "user provided value for AWS_ACCESS_POINT_ARN for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["STORAGE_INTEGRATION"] = "user provided value for STORAGE_INTEGRATION for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["AWS_KEY_ID"] = "user provided value for AWS_KEY_ID for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["AWS_SECRET_KEY"] = "user provided value for AWS_SECRET_KEY for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["AWS_TOKEN"] = "user provided value for AWS_TOKEN for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["AZURE_SAS_TOKEN"] = "user provided value for AZURE_SAS_TOKEN for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["AWS_ROLE"] = "user provided value for AWS_ROLE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["ENCRYPTION_TYPE"] = "user provided value for ENCRYPTION_TYPE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["ENCRYPTION_MASTER_KEY"] = "user provided value for ENCRYPTION_MASTER_KEY for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["ENCRYPTION_KMS_KEY_ID"] = "user provided value for ENCRYPTION_KMS_KEY_ID for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["USE_PRIVATELINK_ENDPOINT"] = "user provided value for USE_PRIVATELINK_ENDPOINT for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["ENABLE"] = "user provided value for ENABLE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["REFRESH_ON_CREATE"] = "user provided value for REFRESH_ON_CREATE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["AUTO_REFRESH"] = "user provided value for AUTO_REFRESH for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["NOTIFICATION_INTEGRATION"] = "user provided value for NOTIFICATION_INTEGRATION for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["PROTOCOLS"] = "user provided value for PROTOCOLS for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["S3_ENCRYPTION_TYPE"] = "user provided value for S3_ENCRYPTION_TYPE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["GCS_ENCRYPTION_TYPE"] = "user provided value for GCS_ENCRYPTION_TYPE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["AZURE_ENCRYPTION_TYPE"] = "user provided value for AZURE_ENCRYPTION_TYPE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        return attr_dict


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
          
