import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class SnowpipeTag(BaseTag):
    AUTO_INGEST="AUTO_INGEST"
    ERROR_INTEGRATION="ERROR_INTEGRATION"
    AWS_SNS_TOPIC="AWS_SNS_TOPIC"
    INTEGRATION="INTEGRATION"
    FILE_TYPE="FILE_TYPE"
    COPYINTO_QUERY="COPYINTO_QUERY"
    

    @classmethod
    def allowed_value_list(cls):
        pass

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
          
