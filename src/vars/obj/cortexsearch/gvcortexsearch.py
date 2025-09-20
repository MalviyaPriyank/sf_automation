import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseMethod,BaseTag

class CortexSearchTag(BaseTag,BaseMethod):
    ATTRIBUTES="ATTRIBUTES"
    WAREHOUSE="WAREHOUSE"
    ON="ON"
    TARGET_LAG="TARGET_LAG"
    EXTERNAL_VOLUME="EXTERNAL_VOLUME"
    EMBEDDING_MODEL="EMBEDDING_MODEL"
    INITIALIZE="INITIALIZE"
    QUERY="QUERY"

    @classmethod
    def allowed_value_list(cls):
        return {
            "EMBEDDING_MODEL":["snowflake-arctic-embed-m-v1.5."],
            "INITIALIZE":["ON_CREATE","ON_SCHEDULE"]   
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass