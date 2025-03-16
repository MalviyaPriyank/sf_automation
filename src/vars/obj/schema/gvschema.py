import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class SchemaTag(BaseTag):
    WITH_MANAGED_ACCESS="WITH MANAGED ACCESS"
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
            "STORAGE_SERIALIZATION_POLICY":["COMPATIBLE","OPTIMIZED"],
            "LOG_LEVEL":['TRACE','DEBUG','INFO','WARN','ERROR','FATAL','OFF'],
            "TRACE_LEVEL":['ALWAYS','ON_EVENT','OFF'],
            "DEFAULT_DDL_COLLATION":['de','ci','pi','en','en_US','fr','fr_CA','cs','ci','as','ai','ps','pi','fl','fu','upper','lower','trim','ltrim','rtrim']
    
        }

    @classmethod
    def max_allowed_value(cls):
        return {
            "DATA_RETENTION_TIME_IN_DAYS":1,
            "MAX_DATA_EXTENSION_TIME_IN_DAYS":1
        }

    @classmethod
    def min_allowed_value(cls):
        return {
            "DATA_RETENTION_TIME_IN_DAYS":0,
            "MAX_DATA_EXTENSION_TIME_IN_DAYS":0
        }
          
