import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class ImageRepositoryTag(BaseTag):
    NAME = "NAME"
    ENCRYPTION="ENCRYPTION"

    @classmethod
    def get_attributes_with_description(cls):
        attr_dict=super().get_attributes_with_description()
        attr_dict["ENCRYPTION"]="Specifies the type of encryption to use for binaries stored in the image repository. You cannot change the encryption type after you create the image repository."

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