import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class SchemaTag(BaseTag):
    TYPE="TYPE"
    DATA_RETENTION_TIME_IN_DAYS="DATA_RETENTION_TIME_IN_DAYS"
    MAX_DATA_EXTENSION_TIME_IN_DAYS="MAX_DATA_EXTENSION_TIME_IN_DAYS"
    EXTERNAL_VOLUME="EXTERNAL_VOLUME"
    CATALOG="CATALOG"
    DEFAULT_DDL_COLLATION="DEFAULT_DDL_COLLATION"
    REPLACE_INVALID_CHARACTERS="REPLACE_INVALID_CHARACTERS"
    LOG_LEVEL="LOG_LEVEL"
    TRACE_LEVEL="TRACE_LEVEL"
    STORAGE_SERIALIZATION_POLICY="STORAGE_SERIALIZATION_POLICY"
    CLASSIFICATION_PROFILE="CLASSIFICATION_PROFILE"
    

    @classmethod
    def allowed_value_list(cls):
        return {
            "TYPE":["OAUTH2","CLOUD_PROVIDER_TOKEN","PASSWORD","GENERIC_STRING","SYMMETRIC_KEY"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass
    @classmethod
    def min_allowed_value(cls):
        pass
          
