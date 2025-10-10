import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseMethod,BaseTag

class AlertTag(BaseTag,BaseMethod):
    SCHEDULE="SCHEDULE"
    IF="IF"
    THEN="THEN"
    ACTION_TYPE="ACTION_TYPE"
    ACTION_SQL="ACTION_SQL"
    INTEGRATION_NAME="INTEGRATION_NAME"
    EMAIL_ADDRESS="EMAIL_ADDRESS"
    EMAIL_CONTENT="EMAIL_CONTENT"
    EMAIL_SUBJECT="EMAIL_SUBJECT"
    WAREHOUSE="WAREHOUSE"

    @classmethod
    def allowed_value_list(cls):
        pass

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass