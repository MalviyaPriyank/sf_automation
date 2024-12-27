
class Account:
    def __init__(self):
        pass

    _account_name_tag = "ACCOUNT"
    _admin_name_tag = "ADMIN_NAME"
    _admin_password_tag = "ADMIN_PASSWORD"
    _admin_user_type_tag = "ADMIN_USER_TYPE"
    _allowed_values_admin_user_type = ["PERSON","SERVICE","LEGACY_SERVICE","NULL"]
    _first_name_tag = "FIRST_NAME"
    _last_name_tag = "LAST_NAME"
    _email_tag = "EMAIL"
    _must_change_password_tag = "MUST_CHANGE_PASSWORD"
    _allowed_values_must_change_password = ["TRUE","FALSE"]
    _edition_tag = "EDITION"
    _allowed_values_edition = ["STANDARD","ENTERPRISE","BUSINESS_CRITICAL"]
    _region_group_tag = "REGION_GROUP"
    _region_tag = "REGION"
    _comment_tag = "COMMENT"
    _polaris_tag = "POLARIS"
    _allowed_values_polaris = ["TRUE","FALSE"]

class Database:
    def __init__(self):
        pass

    _name_tag = "NAME"
    _data_retention_time_in_days_tag = "DATA_RETENTION_TIME_IN_DAYS"
    _max_data_extension_time_in_days_tag = "MAX_DATA_EXTENSION_TIME_IN_DAYS"
    _external_volume_tag = "EXTERNAL_VOLUME"
    _catalog_tag = "CATALOG"
    _default_ddl_collation_tag = "DEFAULT_DDL_COLLATION"
    _storage_serialization_policy_tag = "STORAGE_SERIALIZATION_POLICY"
    _comment_tag = "COMMENT"

class Role:
    def __init__(self):
        pass

    _name_tag = "NAME"
    _comment_tag = "COMMENT"

class ResourceMonitor:
    def __init__(self):
        pass

    _name_tag = "NAME"
    _credit_quota_tag = "CREDIT_QUOTA"
    _frequency_tag = "FREQUENCY"
    _allowed_values_frequency = ["MONTHLY","DAILY","WEEKLY","YEARLY","NEVER"]
    _start_timestamp_tag = "START_TIMESTAMP"
    _end_timestamp_tag = "END_TIMESTAMP"
    _notify_users_tag = "NOTIFY_USERS"
    _triggers_on_tag = "TRIGGERS ON"
    _do_tag = "DO"
    _allowed_values_do = ["SUSPEND","SUSPEND_IMMEDIATE","NOTIFY"]

