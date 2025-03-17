import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag,BaseMethod

class InternalStageTag(BaseTag,BaseMethod):
    FILE_FORMAT="FILE_FORMAT"
    ENCRYPTION="ENCRYPTION"
    ENABLE="ENABLE"
    REFRESH_ON_CREATE="REFRESH_ON_CREATE"    

    @classmethod
    def allowed_value_list(cls):
        return {
            "ENCRYPTION":["SNOWFLAKE_FULL","SNOWFLAKE_SSE"]  
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
          
