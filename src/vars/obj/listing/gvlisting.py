import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class ListingTag(BaseTag):
    NAME = "NAME"
    SHARE = "SHARE"
    APPLICATION_PACKAGE = "APPLICATION_PACKAGE"
    YAML_MANIFEST = "YAML_MANIFEST"
    PUBLISH = "PUBLISH"
    REVIEW = "REVIEW"
    COMMENT = "COMMENT"
    IS_CREATE = "IS_CREATE"

    @classmethod
    def allowed_value_list(cls):
        pass

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass