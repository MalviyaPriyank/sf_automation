import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class ExternalVolumeTag(BaseTag):
    NAME = "NAME"
    STORAGE_LOCATION_NAME = "STORAGE_LOCATION_NAME"
    ALLOW_WRITES = "ALLOW_WRITES"
    COMMENT = "COMMENT"
    IS_CREATE = "IS_CREATE"
    STORAGE_PROVIDER="STORAGE_PROVIDER"
    STORAGE_AWS_ROLE_ARN="STORAGE_AWS_ROLE_ARN"
    STORAGE_BASE_URL="STORAGE_BASE_URL"
    ENCRYPTION_TYPE="ENCRYPTION_TYPE"
    KMS_KEY_ID="KMS_KEY_ID"
    AZURE_TENANT_ID="AZURE_TENANT_ID"
    AWS_KEY_ID="AWS_KEY_ID"
    AWS_SECRET_KEY="AWS_SECRET_KEY"
    STORAGE_ENDPOINT="STORAGE_ENDPOINT"
    STORAGE_AWS_ACCESS_POINT_ARN="STORAGE_AWS_ACCESS_POINT_ARN"
    STORAGE_AWS_EXTERNAL_ID="STORAGE_AWS_EXTERNAL_ID"
    USE_PRIVATELINK_ENDPOINT="USE_PRIVATELINK_ENDPOINT"

    @classmethod
    def get_attributes_with_description(cls):
        return {
        "NAME":"this is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO, these are to be taken from user. the format is a dictionary with key 'NAME' for the name, and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
        "COMMENT":"This will be user defined comment for the object. If user does not define one add a proper comment as per your understanding and inform the user.",
        "IS_CREATE":"Set this to 'TRUE' if create object. set to 'FALSE' if alter object.",
        "STORAGE_PROVIDER":"Specifies the cloud storage provider that stores your data files.Default is NONE.",
        "STORAGE_AWS_ROLE_ARN":"Specifies the case-sensitive Amazon Resource Name (ARN) of the AWS identity and access management (IAM) role that grants privileges on the S3 bucket containing your data files.",
        "STORAGE_BASE_URL":"Specifies the base URL for your cloud storage location",
        "STORAGE_AWS_ACCESS_POINT_ARN":"Specifies the Amazon resource name (ARN) for your S3 access point. Required only when you specify an S3 access point alias for your storage STORAGE_BASE_URL.",
        "STORAGE_AWS_EXTERNAL_ID":"""
        Optionally specifies an external ID that Snowflake uses to establish a trust relationship with AWS. 
        You must specify the same external ID in the trust policy of the IAM role that you configured for 
        this external volume. Default is NONE.
        """,
        "USE_PRIVATELINK_ENDPOINT":"Specifies whether to use outbound private connectivity to harden your security posture. Default is NONE.",
        "AZURE_TENANT_ID":"Specifies the ID for your Office 365 tenant that the storage location belongs to. An external volume can authenticate to only one tenant, so the storage location must refer to a storage account that belongs to this tenant.Default is NONE.",
        "AWS_KEY_ID":"Specifies the security credentials for connecting to and accessing your S3-compatible storage location. Default is NONE.",
        "AWS_SECRET_KEY":"Specifies the security credentials for connecting to and accessing your S3-compatible storage location. Default is NONE.",
        "ENCRYPTION_TYPE":"Specifies the encryption type used.Default is NONE.",
        "KMS_KEY_ID":"Optionally specifies the ID for the AWS KMS-managed key used to encrypt files written to the bucket. If no value is provided, default KMS key is used to encrypt files for writing data.Default is NONE.",
        "STORAGE_AWS_ROLE_ARN":"Specifies the case-sensitive Amazon Resource Name (ARN) of the AWS identity and access management (IAM) role that grants privileges on the S3 bucket containing your data files. Default is NONE.",
        "STORAGE_LOCATION_NAME":"Set of named cloud storage locations in different regions and, optionally, cloud platforms.",
        }

    @classmethod
    def allowed_value_list(cls):
        return {
            "STORAGE_LOCATIONS": ["aws", "azure", "gcs", "s3compat"],
            "ALLOW_WRITES": ["TRUE", "FALSE"],
            "STORAGE_PROVIDER":["S3","S3GOV","GCS","AZURE","S3COMPAT"],
            "ENCRYPTION_TYPE":{
                "GCS":['GCS_SSE_KMS'],
                "S3":['AWS_SSE_S3','AWS_SSE_KMS']
            }
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
