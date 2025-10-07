import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag,BaseMethod

class MaskingPolicyTag(BaseTag,BaseMethod):
    ARGUMENTS="AS"
    RETURNS="RETURNS"
    EXEMPT_OTHER_POLICIES="EXEMPT_OTHER_POLICIES"    
    @classmethod
    def allowed_value_list(cls):
        pass

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
          
