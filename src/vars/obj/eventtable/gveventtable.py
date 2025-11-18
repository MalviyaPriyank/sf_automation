import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseMethod,BaseTag

class EventTableTag(BaseTag,BaseMethod):
    CLUSTER_BY="CLUSTER BY"
    DATA_RETENTION_TIME_IN_DAYS="DATA_RETENTION_TIME_IN_DAYS"
    MAX_DATA_EXTENSION_TIME_IN_DAYS="MAX_DATA_EXTENSION_TIME_IN_DAYS"
    CHANGE_TRACKING="CHANGE_TRACKING"
    DEFAULT_DDL_COLLATION="DEFAULT_DDL_COLLATION"

    @classmethod
    def get_attributes_with_description(cls):
        attr_dict=super().get_attributes_with_description()
        attr_dict["CLUSTER_BY"]="Specifies one or more columns or column expressions in the table as the clustering key. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["DATA_RETENTION_TIME_IN_DAYS"]="Specifies the retention period for the table so that Time Travel actions (SELECT, CLONE, UNDROP) can be performed on historical data in the table. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["MAX_DATA_EXTENSION_TIME_IN_DAYS"]="Object parameter that specifies the maximum number of days for which Snowflake can extend the data retention period for the table to prevent streams on the table from becoming stale. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["CHANGE_TRACKING"]="""
        Specifies whether to enable change tracking on the table.
        TRUE : enables change tracking on the table. This setting adds a pair of hidden columns to the source table 
        and begins storing change tracking metadata in the columns. These columns consume a small amount of storage.
        """
        attr_dict["DEFAULT_DDL_COLLATION"]="user provided value for DEFAULT_DDL_COLLATION of columns in the table . if value is not provided by user, DEFAULT value is set to NONE"
        return attr_dict

    @classmethod
    def allowed_value_list(cls):
        return {
            "CLUSTER_BY":["TIMESTAMP","START_TIMESTAMP","OBSERVED_TIMESTAMP","TRACE","RESOURCE","RESOURCE_ATTRIBUTES","SCOPE","SCOPE_ATTRIBUTES","RECORD_TYPE","RECORD","RECORD_ATTRIBUTES","VALUE","EXEMPLARS"],
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