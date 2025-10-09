import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class ExternalVolumeTag(BaseTag):
    NAME = "NAME"
    STORAGE_LOCATIONS = "STORAGE_LOCATIONS"
    ALLOW_WRITES = "ALLOW_WRITES"
    COMMENT = "COMMENT"
    TAG_CLAUSE = "TAG_CLAUSE"
    IS_CREATE = "IS_CREATE"

    @classmethod
    def allowed_value_list(cls):
        return {
            "STORAGE_LOCATIONS": ["aws", "azure", "gcs", "s3compat"],
            "ALLOW_WRITES": ["TRUE", "FALSE"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
