import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class RoleTag(BaseTag):
    @classmethod
    def get_attributes_with_description(cls):
        return {
            "NAME":"this is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO, these are to be taken from user. the format is a dictionary with key 'NAME' for the name, and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
            "IS_CREATE":"Set this to 'TRUE' if create object. set to 'FALSE' if alter object."
            "COMMENT": "comment for the role"
        }

    @classmethod
    def allowed_value_list(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass

    @classmethod
    def max_allowed_value(cls):
        pass