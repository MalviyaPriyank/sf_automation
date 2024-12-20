class DatabaseTags:
    def __init__(self):
        self._account_name_tag = "ACCOUNT"
        self._admin_name_tag = "ADMIN_NAME"
        self._admin_password_tag = "ADMIN_PASSWORD"
        self._admin_user_type_tag = "ADMIN_USER_TYPE"
        self._allowed_values_admin_user_type = ["PERSON","SERVICE","LEGACY_SERVICE","NULL"]
        self._first_name_tag = "FIRST_NAME"
        self._last_name_tag = "LAST_NAME"
        self._email_tag = "EMAIL"
        self._must_change_password_tag = "MUST_CHANGE_PASSWORD"
        self._allowed_values_must_change_password = ["TRUE","FALSE"]
        self._edition_tag = "EDITION"
        self._allowed_values_edition = ["STANDARD","ENTERPRISE","BUSINESS_CRITICAL"]
        self._region_group_tag = "REGION_GROUP"
        self._region_tag = "REGION"
        self._comment_tag = "COMMENT"
        self._polaris_tag = "POLARIS"
        self._allowed_values_polaris = ["TRUE","FALSE"]