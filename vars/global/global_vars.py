
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

class Schema:
    def __init__(self):
        pass
    _name_tag = "NAME"
    _with_managed_access_tag = "WITH MANAGED ACCESS"
    _data_retention_time_in_days_tag = "DATA_RETENTION_TIME_IN_DAYS"
    _max_data_extension_time_in_days_tag = "MAX_DATA_EXTENSION_TIME_IN_DAYS"
    _external_volume_tag = "EXTERNAL_VOLUME"
    _catalog_tag = "CATALOG"
    _replace_invalid_characters_tag = "REPLACE_INVALID_CHARACTERS"
    _default_ddl_collation_tag = "DEFAULT_DDL_COLLATION"
    _log_level_tag = "LOG_LEVEL"
    _trace_level_tag = "TRACE_LEVEL"
    _storage_serialization_policy_tag = "STORAGE_SERIALIZATION_POLICY"
    _classification_profile_tag = "CLASSIFICATION_PROFILE"
    _comment_tag = "COMMENT"
    _tag_tag = "TAG"
    _allowed_values_log_level = ["TRACE","DEBUG","INFO","WARN","ERROR","FATAL","OFF"]
    _allowed_values_trace_level = ["ALWAYS","ON_EVENT","OFF"]
    _allowed_values_storage_serialization_policy = ["COMPATIBLE","OPTIMIZED"]

class Share:
    def __init__(self):
        pass
    _name_tag = "NAME"
    _with_managed_access_tag = "WITH MANAGED ACCESS"
    _data_retention_time_in_days_tag = "DATA_RETENTION_TIME_IN_DAYS"
    _max_data_extension_time_in_days_tag = "MAX_DATA_EXTENSION_TIME_IN_DAYS"
    _external_volume_tag = "EXTERNAL_VOLUME"
    _catalog_tag = "CATALOG"
    _replace_invalid_characters_tag = "REPLACE_INVALID_CHARACTERS"
    _default_ddl_collation_tag = "DEFAULT_DDL_COLLATION"
    _log_level_tag = "LOG_LEVEL"
    _trace_level_tag = "TRACE_LEVEL"
    _storage_serialization_policy_tag = "STORAGE_SERIALIZATION_POLICY"
    _classification_profile_tag = "CLASSIFICATION_PROFILE"
    _comment_tag = "COMMENT"
    _tag_tag = "TAG"
    _allowed_values_log_level = ["TRACE","DEBUG","INFO","WARN","ERROR","FATAL","OFF"]
    _allowed_values_trace_level = ["ALWAYS","ON_EVENT","OFF"]
    _allowed_values_storage_serialization_policy = ["COMPATIBLE","OPTIMIZED"]


class InternalStage:
    def __init__(self):
        pass
    _name_tag = "NAME"
    _file_format_tag = "FILE_FORMAT"
    _comment_tag = "COMMENT"
    _tag_tag = "TAG"
    _encryption_tag = "ENCRYPTION"
    _directory_tag = "DIRECTORY"
    _refresh_on_create_tag = "REFRESH_ON_CREATE"
    _allowed_values_encryption = ["SNOWFLAKE_FULL","SNOWFLAKE_SSE"]

class ExternalStage:
    def __init__(self):
        pass
    _name_tag = "NAME"
    _file_format_tag = "FILE_FORMAT"
    _comment_tag = "COMMENT"
    _tag_tag = "TAG"
    _url_tag = "URL"
    _storage_integration_tag = "STORAGE_INTEGRATION"
    _aws_key_id_tag = "AWS_KEY_ID"
    _aws_secret_key_tag = "AWS_SECRET_KEY"
    _aws_token_tag = "AWS_TOKEN"
    _azure_sas_token_tag = "AZURE_SAS_TOKEN"
    _aws_role_tag = "AWS_ROLE"
    _encryption_tag = "ENCRYPTION"
    _encryption_type_tag = "ENCRYPTION_TYPE"
    _encryption_master_key_tag = "ENCRYPTION_MASTER_KEY"
    _encryption_kms_key_id_tag ="ENCRYPTION_KMS_KEY_ID"
    _use_privatelink_endpoint_tag = "USE_PRIVATELINK_ENDPOINT"
    _directory_tag = "DIRECTORY"
    _refresh_on_create_tag = "REFRESH_ON_CREATE"
    _auto_refresh_tag = "AUTO_REFRESH"
    _notification_integration_tag = "NOTIFICATION_INTEGRATION"
    _allowed_values_encryption = ["SNOWFLAKE_FULL","SNOWFLAKE_SSE","DEF"]

class FileFormat:
    def __init__(self):
        pass
    _name_tag = "FILE_FORMAT"
    _type_tag = "TYPE"
    _parse_header_tag = "PARSE_HEADER"
    _skip_header_tag = "SKIP_HEADER"
    _skip_blank_lines_tag = "SKIP_BLANK_LINES"
    _date_format_tag = "DATE_FORMAT"
    _time_format_tag = "TIME_FORMAT"
    _timestamp_format_tag = "TIMESTAMP_FORMAT"
    _binary_format_tag = "BINARY_FORMAT"
    _escape_tag = "ESCAPE"
    _escape_unenclosed_field_tag = "ESCAPE_UNENCLOSED_FIELD"
    _trim_space_tag = "TRIM_SPACE"
    _field_optionally_enclosed_by_tag = "FIELD_OPTIONALLY_ENCLOSED_BY"
    _null_if_tag = "NULL_IF"
    _error_on_column_count_mismatch_tag = "ERROR_ON_COLUMN_COUNT_MISMATCH"
    _replace_invalid_characters_tag = "REPLACE_INVALID_CHARACTERS"
    _empty_field_as_null_tag = "EMPTY_FIELD_AS_NULL"
    _skip_byte_order_mark_tag = "SKIP_BYTE_ORDER_MARK"
    _encoding_tag = "ENCODING"
    _enable_octal_tag = "ENABLE_OCTAL"
    _allow_duplicate_tag = "ALLOW_DUPLICATE"
    _strip_outer_array_tag = "STRIP_OUTER_ARRAY"
    _strip_null_values_tag = "STRIP_NULL_VALUES"
    _ignore_utf8_errors_tag = "IGNORE_UTF8_ERRORS"
    _snappy_compression_tag = "SNAPPY_COMPRESSION"
    _binary_as_text_tag = "BINARY_AS_TEXT"
    _use_logical_type_tag = "USE_LOGICAL_TYPE"
    _use_vectorized_scanner_tag = "USE_VECTORIZED_SCANNER"
    _preserve_space_tag = "PRESERVE_SPACE"
    _strip_outer_element_tag = "STRIP_OUTER_ELEMENT"
    _disable_snowflake_data_tag = "DISABLE_SNOWFLAKE_DATA"
    _disable_auto_convert_tag = "DISABLE_AUTO_CONVERT"
    _allowed_values_type = ["CSV","JSON","AVRO","ORC","PARQUET","XML","DEFAULT"]
    _allowed_values_binary_format = ["HEX","BASE64","UTF8"]    
