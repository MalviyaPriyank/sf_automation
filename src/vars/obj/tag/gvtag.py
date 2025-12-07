import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class TagTag(BaseTag):
    NAME = "NAME"
    ALLOWED_VALUES = "ALLOWED_VALUES"

    @classmethod
    def get_attributes_with_description(cls):
        attr_dict=super().get_attributes_with_description()
        attr_dict["ALLOWED_VALUES"]="Specifies a comma-separated list of the possible string values that can be assigned to the tag when the tag is set on an object.Pass it as a list."        
        return attr_dict

    @classmethod
    def allowed_value_list(cls):
        return {
            "PROPAGATE": [
                "ON_DEPENDENCY_AND_DATA_MOVEMENT",
                "ON_DEPENDENCY",
                "ON_DATA_MOVEMENT"
            ],
            # ON_CONFLICT can be a string or ALLOWED_VALUES_SEQUENCE
            # ALLOWED_VALUES is a list of string values
        }

    @classmethod
    def max_allowed_value(cls):
        return {}

    @classmethod
    def min_allowed_value(cls):
        return {}
