import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class StoredProcedureTag(BaseTag):
    NAME="NAME"
    LOGIC="LOGIC"
    LANGUAGE="LANGUAGE"
    RETURNS="RETURNS"

    @classmethod
    def get_attributes_with_description(cls):
        attr_dict=super().get_attributes_with_description()
        attr_dict['LOGIC']=""" SQL expression to implement the logic for the problem described by the user.
        If there are multiple SQLs required to implement the logic use Common Table Expression"""
        attr_dict['LANGUAGE']="""Language of the stored procedure logic. Always SQL"""
        attr_dict['RETURNS']="""Data type that the stored procedure will return. Always VARCHAR."""
        return attr_dict

    @classmethod
    def allowed_value_list(cls):
        return {
            "LANGUAGE":["JAVA","PYTHON","JAVASCRIPT","SCALA","SQL"]
        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
          
