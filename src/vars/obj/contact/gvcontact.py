import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class ContactTag(BaseTag):
    NAME = "NAME"
    USERS = "USERS"
    EMAIL_DISTRIBUTION_LIST = "EMAIL_DISTRIBUTION_LIST"
    URL = "URL"
    COMMENT = "COMMENT"
    IS_CREATE = "IS_CREATE"

    @classmethod
    def get_attributes_with_description(cls):
        attr_dict=super().get_attributes_with_description()
        attr_dict["USERS"]="List of Snowflake users who can be contacted, specified by the name of their user objects. Pass this as a list [user1,user2] Default is NONE"
        attr_dict["EMAIL_DISTRIBUTION_LIST"]="A valid email address, which can be a distribution list if you want users to be able to contact more than one individual. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["URL"]="A URL that can be used to contact people about an object.. if value is not provided by user, DEFAULT value is set to NONE"
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