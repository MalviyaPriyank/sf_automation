import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class ProvisionedThroughputTag(BaseTag):
    NAME = "NAME"
    CLOUD_PROVIDER = "CLOUD_PROVIDER"
    MODEL = "MODEL"
    PTUS = "PTUS"
    TERM_START = "TERM_START"
    TERM_END = "TERM_END"
    COMMENT = "COMMENT"
    TAG_CLAUSE = "TAG_CLAUSE"
    IS_CREATE = "IS_CREATE"

    @classmethod
    def allowed_value_list(cls):
        return {
            "CLOUD_PROVIDER": ["aws", "azure"],
            "MODEL": [
                "Mistral Large 2",
                "Llama 3.1-405B",
                "Llama 3.1-70B",
                "Llama 3.1-8B",
                "Snowflake-Llama3.3-70B",
                "Snowflake-Llama3.3-405B"
            ]
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
