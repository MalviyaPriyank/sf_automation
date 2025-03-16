import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag

class StoredProcedureTag(BaseTag):
    LOGIC="LOGIC"
    LANGUAGE="LANGUAGE"
    RETURNS="RETURNS"
    PACKAGES="PACKAGES"
    HANDLER="HANDLER"   

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
          
