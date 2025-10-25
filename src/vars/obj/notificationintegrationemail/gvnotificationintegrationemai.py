import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../base'))

from base.basetag import BaseTag

class NotificationIntegrationEmailTag(BaseTag):
    NAME = "NAME"
    ENABLED = "ENABLED"
    TYPE="TYPE"
    ALLOWED_RECIPIENTS = "ALLOWED_RECIPIENTS"
    COMMENT = "COMMENT"

    @classmethod
    def get_attributes_with_description(cls):
        return {
            "NAME": "This is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. "
                    "This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO; "
                    "these are to be taken from user. The format is a dictionary with key 'NAME' for the name, "
                    "and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
            "ENABLED": "Specifies whether the notification integration is enabled or disabled. "
                       "Valid values: TRUE | FALSE. Default: TRUE.(str)",
            "TYPE":"Type of integration. This value is always 'EMAIL'.",
            "ALLOWED_RECIPIENTS": "Specifies one or more email addresses that are allowed to receive notifications "
                                  "from this integration. The value must be a list of valid email addresses or domains. "
                                  "For example: ['user@example.com', 'team@company.com'].",
            "DEAFULT_RECIPIENTS":"Specifies one or more email addresses that are default recipients to receive notifications "
                                  "from this integration. The value must be a list of valid email addresses or domains. "
                                  "For example: ['user@example.com', 'team@company.com'].",
            "DEFAULT_SUBJECT":"Specifies the default subject line for messages sent with this integration",
            "COMMENT": "Optional description or comment for the notification integration. (str)",
            "IS_CREATE": "Set this to 'TRUE' if creating the object. Set to 'FALSE' if altering the object."
        }

    @classmethod
    def allowed_value_list(cls):
        return {
            "ENABLED": ["TRUE", "FALSE"]
        }

    @classmethod
    def max_allowed_value(cls):
        # No numeric max values for this object
        return {}

    @classmethod
    def min_allowed_value(cls):
        # No numeric min values for this object
        return {}
