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
    def get_attributes_with_description(cls):
        attr_dict = super().get_attributes_with_description()
        attr_dict["WITH_MANAGED_ACCESS"] = "user provided value for WITH_MANAGED_ACCESS for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["DATA_RETENTION_TIME_IN_DAYS"] = "user provided value for DATA_RETENTION_TIME_IN_DAYS for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["MAX_DATA_EXTENSION_TIME_IN_DAYS"] = "user provided value for MAX_DATA_EXTENSION_TIME_IN_DAYS for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["EXTERNAL_VOLUME"] = "user provided value for EXTERNAL_VOLUME for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["CATALOG"] = "user provided value for CATALOG for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["DEFAULT_DDL_COLLATION"] = "user provided value for DEFAULT_DDL_COLLATION for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["REPLACE_INVALID_CHARACTERS"] = "user provided value for REPLACE_INVALID_CHARACTERS for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["LOG_LEVEL"] = "user provided value for LOG_LEVEL for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["TRACE_LEVEL"] = "user provided value for TRACE_LEVEL for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["STORAGE_SERIALIZATION_POLICY"] = "user provided value for STORAGE_SERIALIZATION_POLICY for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["CLASSIFICATION_PROFILE"] = "user provided value for CLASSIFICATION_PROFILE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        return attr_dict

    

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
          
