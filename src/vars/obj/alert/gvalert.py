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
    def get_attributes_with_description(cls):
        attr_dict=super().get_attributes_with_description()
        attr_dict["IF"]="The SQL statement that represents the condition for the alert."
        attr_dict["THEN"]="The SQL statement that should be executed if the condition returns one or more rows."
        attr_dict["WAREHOUSE"]="user provided value of Warhouse for alert object."
        attr_dict["SCHEDULE"]="user provided value for SCHEDULE for alert object. This is a required attribute."
        attr_dict["COMMENT"]="user provided value for CATALOG for database object. if value is not provided by user, DEFAULT value is set to NONE."
        return attr_dict
    @classmethod
    def allowed_value_list(cls):
        pass

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass