import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class StreamTag(BaseTag):
    TABLE_NAME="TABLE_NAME"
    AT="AT"
    APPEND_ONLY="APPEND_ONLY"
    INSERT_ONLY="INSERT_ONLY"
    SHOW_INITIAL_ROWS="SHOW_INITIAL_ROWS"
    OBJECT_TYPE="OBJECT_TYPE"
    BEFORE="BEFORE"
    TIMESTAMP="TIMESTAMP"
    OFFSET="OFFSET"
    OBJECT_TYPE="OBJECT_TYPE"
    

    @classmethod
    def allowed_value_list(cls):
        return {
            "OBJECT_TYPE":["TABLE","EXTERNAL TABLE","STAGE","VIEW"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
          
