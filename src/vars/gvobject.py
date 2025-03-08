


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
    _replace_invalid_characters_tag = "REPLACE_INVALID_CHARACTERS"
    _data_retention_time_in_days_tag = "DATA_RETENTION_TIME_IN_DAYS"
    _max_data_extension_time_in_days_tag = "MAX_DATA_EXTENSION_TIME_IN_DAYS"
    _external_volume_tag = "EXTERNAL_VOLUME"
    _catalog_tag = "CATALOG"
    _default_ddl_collation_tag = "DEFAULT_DDL_COLLATION"
    _log_level_tag="LOG_LEVEL"
    _trace_level_tag="TRACE_LEVEL"
    _storage_serialization_policy_tag = "STORAGE_SERIALIZATION_POLICY"
    _comment_tag = "COMMENT"
    _allowed_values_storage_serialization_policy = ["COMPATIBLE","OPTIMIZED"]
    _max_allowed_value_data_retention_time_in_days=1
    _min_allowed_value_data_retention_time_in_days=0
    _max_allowed_value_max_data_extension_time_in_days=1
    _min_allowed_value_max_data_extension_time_in_days=0
    _allowed_values_log_level=['TRACE','DEBUG','INFO','WARN','ERROR','FATAL','OFF']
    _allowed_values_trace_level=['ALWAYS','ON_EVENT','OFF']
    _allowed_collation_specifiers=['de','ci','pi','en','en_US','fr','fr_CA','cs','ci','as','ai','ps','pi','fl','fu','upper','lower','trim','ltrim','rtrim']

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
    _database_tag = "DATABASE"
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
    _min_allowed_value_data_retention_time_in_days=0
    _max_allowed_value_data_retention_time_in_days=1
    _min_allowed_value_max_data_extension_time_in_days=0
    _max_allowed_value_max_data_extension_time_in_days=90
    _allowed_collation_specifiers=['de','ci','pi','en','en_US','fr','fr_CA','cs','ci','as','ai','ps','pi','fl','fu','upper','lower','trim','ltrim','rtrim']


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

    _database_tag = "DATABASE"
    _schema_tag = "SCHEMA"
    _name_tag = "NAME"
    _file_format_tag = "FILE_FORMAT"
    _comment_tag = "COMMENT"
    _tag_tag = "TAG"
    _encryption_tag = "ENCRYPTION"
    _enable_tag="ENABLE"
    _refresh_on_create_tag = "REFRESH_ON_CREATE"
    _allowed_values_encryption = ["SNOWFLAKE_FULL","SNOWFLAKE_SSE"]

class ExternalStage:
    def __init__(self):
        pass
    _database_tag="DATABASE"
    _schema_tag="SCHEMA"
    _name_tag = "NAME"
    _file_format_tag = "FILE_FORMAT"
    _comment_tag = "COMMENT"
    _tag_tag = "TAG"
    _url_tag = "URL"
    _aws_access_point_arn_tag="AWS_ACCESS_POINT_ARN"
    _storage_integration_tag = "STORAGE_INTEGRATION"
    _aws_key_id_tag = "AWS_KEY_ID"
    _aws_secret_key_tag = "AWS_SECRET_KEY"
    _aws_token_tag = "AWS_TOKEN"
    _azure_sas_token_tag = "AZURE_SAS_TOKEN"
    _aws_role_tag = "AWS_ROLE"
    _encryption_type_tag = "ENCRYPTION"
    _encryption_master_key_tag = "ENCRYPTION_MASTER_KEY"
    _encryption_kms_key_id_tag ="ENCRYPTION_KMS_KEY_ID"
    _use_privatelink_endpoint_tag = "USE_PRIVATELINK_ENDPOINT"
    _enable_tag="ENABLE"
    _refresh_on_create_tag = "REFRESH_ON_CREATE"
    _auto_refresh_tag = "AUTO_REFRESH"
    _notification_integration_tag = "NOTIFICATION_INTEGRATION"
    _allowed_values_encryption = ["SNOWFLAKE_FULL","SNOWFLAKE_SSE","DEF"]
    _allowed_values_protocols=['s3','s3china','s3gov','gcs','azure']
    _allowed_values_s3_encryption_type=['AWS_CSE','AWS_SSE_S3','AWS_SSE_KMS']
    _allowed_values_gcs_encyption_type=['GCS_SSE_KMS']
    _allowed_values_azure_encyption_type=['AZURE_CSE']


class FileFormat:
    def __init__(self):
        pass
    _database_tag = "DATABASE"
    _schema_tag = "SCHEMA"
    _name_tag = "FILE_FORMAT"
    _type_tag = "TYPE"
    _compression_tag="COMPRESSION"
    _record_delimiter_tag="RECORD_DELIMITER"
    _field_delimiter_tag="FIELD_DELIMITER"
    _multi_line_tag="MULTI_LINE"
    _file_extension_tag="FILE_EXTENSION"
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
    _allowed_values_compression_for_csv=["AUTO","GZIP","BZ2","BROTLI","ZSTD","DEFLATE","RAW_DEFLATE"]
    _allowed_values_compression_for_json=["AUTO","GZIP","BZ2","BROTLI","ZSTD","DEFLATE","RAW_DEFLATE"]  
    _allowed_values_compression_for_avro=["AUTO","GZIP","BROTLI","ZSTD","DEFLATE","RAW_DEFLATE"]  
    _allowed_values_compression_for_parquet=["AUTO","LZO","SNAPPY"]
    _allowed_values_compression_for_xml=["AUTO","GZIP","BZ2","BROTLI","ZSTD","DEFLATE","RAW_DEFLATE"]
    _allowed_values_encoding=["BIG5","EUCJP","EUCKR","GB18030","IBM420","IBM424","IBM949","ISO2022CN","ISO2022JP","ISO2022KR","ISO88591","ISO88592","ISO88595","ISO88596","ISO88597","ISO88598","ISO88599","ISO885915","KOI8R","SHIFTJIS","UTF8","UTF16","UTF16BE","UTF16LE","UTF32","UTF32BE","UTF32LE","WINDOWS874","WINDOWS949","WINDOWS1250","WINDOWS1251","WINDOWS1252","WINDOWS1253","WINDOWS1254","WINDOWS1255","WINDOWS1256"]

class Snowpipe:
    def __init__(self):
        pass
    _database_tag = "DATABASE"
    _schema_tag = "SCHEMA"
    _name_tag = "NAME"
    _auto_ingest_tag = "AUTO_INGEST"
    _error_integration_tag = "ERROR_INTEGRATION"
    _aws_sns_topic_tag = "AWS_SNS_TOPIC"
    _integration_tag =  "INTEGRATION"
    _comment_tag = "COMMENT"
    _file_type_tag = "FILE_TYPE"

class Stream:
    def __init__(self):
        pass
    _database_tag="DATABASE"
    _schema_tag="SCHEMA"
    _name_tag="NAME"
    _table_name_tag="TABLE_NAME"
    _tag_tag="TAG"
    _at_tag="AT"
    _append_only_tag="APPEND_ONLY"
    _insert_only_tag="INSERT_ONLY"
    _show_initial_rows_tag="SHOW_INITIAL_ROWS"
    _comment_tag="COMMENT"

class User:
    def __init__(self):
        pass
    _name_tag = "NAME"
    _password_tag = "PASSWORD"
    _login_name_tag = "LOGIN_NAME"
    _display_name_tag = "DISPLAY_NAME"
    _first_name_tag = "FIRST_NAME"
    _last_name_tag = "LAST_NAME"
    _email_tag = "EMAIL"
    _must_change_password_tag = "MUST_CHANGE_PASSWORD"
    _disabled_tag = "DISABLED"
    _days_to_expiry_tag = "DAYS_TO_EXPIRY"
    _mins_to_unlock_tag = "MINS_TO_UNLOCK"
    _default_warehouse_tag = "DEFAULT_WAREHOUSE"
    _default_role_tag = "DEFAULT_ROLE"
    _default_secondary_roles_tag = "DEFAULT_SECONDARY_ROLES"
    _mins_to_by_pass_mfa_tag = "MINS_TO_BY_PASS_MFA"
    _rsa_public_key_tag = "RSA_PUBLIC_KEY"
    _rsa_public_key_fp_tag = "RSA_PUBLIC_KEY_FP"
    _rsa_public_key_2_tag = "RSA_PUBLIC_KEY_2"
    _rsa_public_key_2_fp_tag = "RSA_PUBLIC_KEY_2_FP"
    _type_tag = "TYPE"
    _comment_tag = "COMMENT"
    _enable_unredacted_query_syntax_error_tag = "ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR"
    _allowed_values_display_name = ['PERSON','SERVICE','LEGACY_SERVICE','NULL']
    _allowed_values_type = ['PERSON','SERVICE','LEGACY_SERVICE','NULL']
    _allowed_values_default_secondary_roles = ['ALL',{}]


class Task:
    def __init__(self):
        pass
    _database_tag="DATABASE"
    _schema_tag="SCHEMA"
    _name_tag="NAME"
    _sql_tag="SQL"
    _warehouse_tag="WAREHOUSE"
    _user_task_managed_initial_warehouse_size_tag="USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE"
    _schedule_tag="SCHEDULE"
    _config_tag="CONFIG"
    _allow_overlapping_execution_tag="ALLOW_OVERLAPPING_EXECUTION"
    _user_task_timeout_ms_tag="USER_TASK_TIMEOUT_MS"
    _suspend_task_after_num_failures_tag="SUSPEND_TASK_AFTER_NUM_FAILURES"
    _error_integration_tag="ERROR_INTEGRATION"
    _success_integration_tag="SUCCESS_INTEGRATION"
    _comment_tag="COMMENT"
    _after_tag="AFTER"
    _when_tag="WHEN"
    _tag_tag="TAG"
    _finalize_tag="FINALIZE"
    _task_auto_retry_attempts_tag="TASK_AUTO_RETRY_ATTEMPTS"
    _user_task_minimum_trigger_interval_in_seconds_tag="USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS"
    _target_completion_interval_tag="TARGET_COMPLETION_INTERVAL"
    _serverless_task_min_statement_size_tag="SERVERLESS_TASK_MIN_STATEMENT_SIZE"
    _serverless_task_max_statement_size_tag="SERVERLESS_TASK_MAX_STATEMENT_SIZE"
    _allowed_min_user_task_timeout_ms=0
    _allowed_max_user_task_timeout_ms=604800000


class Warehouse:
    def __init__(self):
        pass
    _name_tag = "NAME"
    _warehouse_size_tag = "WAREHOUSE_SIZE"
    _warehouse_type_tag = "WAREHOUSE_TYPE"
    _resource_constraint_tag = "RESOURCE_CONSTRAINT"
    _max_cluster_count_tag = "MAX_CLUSTER_COUNT"
    _min_cluster_count_tag = "MIN_CLUSTER_COUNT"
    _scaling_policy_tag = "SCALING_POLICY"
    _auto_suspend_tag = "AUTO_SUSPEND"
    _auto_resume_tag = "AUTO_RESUME"
    _initially_suspended_tag = "INITIALLY_SUSPENDED"
    _resource_monitor_tag = "RESOURCE_MONITOR"
    _comment_tag = "COMMENT"
    _tag_tag = "TAG"
    _enable_query_acceleration_tag = "ENABLE_QUERY_ACCELERATION"
    _query_acceleration_max_scale_factor_tag = "QUERY_ACCELERATION_MAX_SCALE_FACTOR"
    _max_concurrency_level_tag = "MAX_CONCURRENCY_LEVEL"
    _statement_queued_timeout_in_seconds_tag = "STATEMENT_QUEUED_TIMEOUT_IN_SECONDS"
    _statement_timeout_in_seconds_tag = "STATEMENT_TIMEOUT_IN_SECONDS"
    _allowed_values_scaling_policy = ["STANDARD","ECONOMY"]
    _allowed_values_warehouse_type = ["STANDARD","SNOWPARK-OPTIMIZED"]
    _allowed_values_warehouse_size = ["XSMALL","SMALL","MEDIUM","LARGE","XLARGE","XXLARGE","XXXLARGE","X4LARGE","X5LARGE","X6LARGE"]
    _min_value_query_acceleration_max_scale_factor=0
    _max_value_query_acceleration_max_scale_factor=100
    _default_value_max_concurrency_level=8
    _min_value_statement_timeout_in_seconds=0
    _max_value_statement_timeout_in_seconds=604800
    _allowed_max_cluster_size_for_warehouse_type={
        "XSMALL":300,
        "SMALL":300,
        "MEDIUM":300,
        "LARGE":160,
        "XLARGE":80,
        "2XLARGE":40,
        "3XLARGE":20,
        "4XLARGE":10,
        "5XLARGE":10,
        "6XLARGE":10
    }

class CopyInto:
    _table_tag = "TABLE"
    _schema_tag = "SCHEMA"
    _db_tag = "DATABASE"
    _stage_tag = "STAGE"
    _file_format_tag = "FILE_FORMAT"
    _on_error_tag = "ON_ERROR"
    _size_limit_tag = "SIZE_LIMIT"
    _purge_tag = "PURGE"
    _return_failed_only_tag = "RETURN_FAILED_ONLY"
    _match_by_column_name_tag = "MATCH_BY_COLUMN_NAME"
    _include_metadata_tag = "INCLUDE_METADATA"
    _enforce_length_tag = "ENFORCE_LENGTH"
    _truncatecolumns_tag = "TRUNCATECOLUMNS"
    _force_tag = "FORCE"
    _load_uncertain_files_tag = "LOAD_UNCERTAIN_FILES"
    _file_processor_tag = "FILE_PROCESSOR"
    _load_mode_tag = "LOAD_MODE"
    _allowed_values_on_error = ["CONTINUE","SKIP_FILE"]
    _allowed_values_match_by_column_name = ["CASE_SENSITIVE","CASE_INSENSITIVE","NONE"]
    _allowed_values_load_mode = ["FULL_INGEST","ADD_FILES_COPY"]

class NotificationIntegrationEmail:
    _name_tag = "NAME"
    _enabled_tag = "ENABLED"
    _type_tag = "TYPE"
    _allowed_recepients_tag = "ALLOWED_RECIPIENTS"
    _default_recepients_tag = "DEFAULT_RECIPIENTS"
    _default_subject_tag = "DEFAULT_SUBJECT"
    _comment_tag = "COMMENT"
    _allowed_number_of_recipients = 50
    _allowed_values_type=["EMAIL"]
    _max_allowed_recepients=50
    _allowed_length_subject=256

class Alert:
    _name_tag="NAME"
    _schedule_tag="SCHEDULE"
    _if_tag="IF"
    _then_tag="THEN"


class StorageIntegrationAws:
    _name_tag="NAME"
    _type_tag="TYPE"
    _enabled_tag="ENABLED"
    _storage_allowed_locations_tag="STORAGE_ALLOWED_LOCATIONS"
    _storage_blocked_locations_tag="STORAGE_BLOCKED_LOCATIONS"
    _storage_provider_tag="STORAGE_PROVIDER"
    _storage_aws_role_arn_tag="STORAGE_AWS_ROLE_ARN"
    _storage_aws_external_id_tag="STORAGE_AWS_EXTERNAL_ID"
    _storage_aws_object_acl_tag="STORAGE_AWS_OBJECT_ACL"
    _allowed_value_type="EXTERNAL_STAGE"
    _allowed_value_storage_provider=['S3','S3CHINA','S3GOV']
    _comment_tag="COMMENT"
    _use_private_link_endpoint_tag="USE_PRIVATELINK_ENDPOINT"

class Privilege:
    _allowed_object_type = ["USER","ROLE","WAREHOUSE","DATABASE","SCHEMA","TABLE","FILE FORMAT","PIPE","TASK","STAGE","STREAM"]
    _allowed_privileges = {
        "USER": ["MONITOR","OWNERSHIP","ALL"],
        "ROLE": ["OWNERSHIP"],
        "STAGE":["READ","WRITE","OWNERSHIP"],
        "WAREHOUSE": ["APPLYBUDGET","MODIFY","MONITOR","OPERATE","USAGE","OWNERSHIP","ALL"],
        "DATABASE": ["APPLYBUDGET","MODIFY","MONITOR","USAGE","REFERENCE_USAGE","CREATE DATABASE ROLE","CREATE SCHEMA","IMPORTED PRIVILEGES","OWNERSHIP","ALL"],
        "SCHEMA": ["APPLYBUDGET","MODIFY","MONITOR","USAGE","CREATE AUTHENTICATION POLICY","CREATE DATA METRIC FUNCTION","CREATE TABLE","CREATE DYNAMIC TABLE","CREATE EVENT TABLE",
                          "CREATE EXTERNAL TABLE","CREATE GIT REPOSITORY","CREATE ICEBERG TABLE","CREATE VIEW","CREATE MASKING POLICY","CREATE MATERIALIZED VIEW","CREATE NETWORK RULE",
                          "CREATE NOTEBOOK","CREATE ROW ACCESS POLICY","CREATE SECRET","CREATE SESSION POLICY","CREATE STAGE","CREATE STREAMLIT","CREATE FILE FORMAT",
                          "CREATE SEQUENCE","CREATE FUNCTION","CREATE PACKAGES POLICY","CREATE PASSWORD POLICY","CREATE PIPE","CREATE STREAM","CREATE TAG","CREATE TASK","CREATE PROCEDURE",
                          "CREATE ALERT","CREATE CORTEX SEARCH SERVICE","CREATE SNOWFLAKE.CORE.BUDGET","CREATE SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE","CREATE SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER",
                          "CREATE SNOWFLAKE.ML.ANOMALY_DETECTION","CREATE SNOWFLAKE.ML.CLASSIFICATION","CREATE SNOWFLAKE.ML.FORECAST","CREATE SNOWFLAKE.ML.TOP_INSIGHTS","CREATE SNOWFLAKE.ML.DOCUMENT_INTELLIGENCE",
                          "CREATE MODEL","CREATE MODEL MONITOR","CREATE IMAGE REPOSITORY","CREATE SERVICE","CREATE SNAPSHOT","ADD SEARCH OPTIMIZATION","OWNERSHIP","ALL"],
        "TABLE": ["SELECT","INSERT","UPDATE","TRUNCATE","DELETE","EVOLVE SCHEMA","REFERENCES","APPLYBUDGET","OWNERSHIP","ALL"],
        "FILE FORMAT": ["USAGE","OWNERSHIP","ALL"],
        "PIPE": ["APPLYBUDGET","MONITOR","OPERATE","OWNERSHIP","ALL"],
        "STREAM":["SELECT","OWNERSHIP","ALL"],
        "TASK": ["APPLYBUDGET","MONITOR","OPERATE","OWNERSHIP","ALL"]
    }


class Config:
    def __init__(self):
        pass
    _config_database = "DB_CONFIG"
    _config_schema = "SCH_CONFIG"
    _config_stage = "STG_INT_CONFIG"
    _deployment_stage = "STG_INT_DEPLOY"
    _deployment_control_table = "DEPLOYMENT_CONTROL"
    _deployment_scripts_table = "DEPLOYMENT_SCRIPTS"
    _deployment_log_table = "DEPLOYMENT_LOG"
    _deployment_reference_table = "DEPLOYMENT_REFERENCE"
    _deployment_history_table = "DEPLOYMENT_HISTORY"
    _default_privilege_set = ["OWNERSHIP","ALL","MONITOR","MODIFY","USAGE","OPERATE"]
    _default_warehouse = {
        "WH_XSMALL" : "XSMALL",
        "WH_SMALL" : "SMALL",
        "WH_MEDIUM" : "MEDIUM",
        "WH_LARGE" : "LARGE",
        "WH_XLARGE" : "XLARGE",
        "WH_XXLARGE" : "XXLARGE"
    }
    _default_role = {
        "RL_DEV_OWNER_EVERY_OBJ" : "'Default role to be the owner of all the objects within account'",
        "RL_DEV_ALL_EVERY_OBJ" : "'Default role to have all allowed privileges on all objects except ownership'",
    }

    _default_role_privilege_set = {
        "RL_DEV_OWNER_EVERY_OBJ": "OWNERSHIP",
        "RL_DEV_ALL_EVERY_OBJ": "ALL"
    }
    _deployment_scripts_table_column_list = ["SQL_TEXT","USER_ID"]
    _deployment_scripts_table_column_data_type_dict ={
        "SQL_TEXT" : "VARCHAR",
        "USER_ID" : "VARCHAR(50)"
    }
    _deployment_control_table_column_list = ["OBJECT_TYPE","OBJECT_DATABASE","OBJECT_SCHEMA","OBJECT_NAME","MODIFIED_BY","DEPLOYMENT_STATUS","DEPLOYMENT_ID"]
    _deployment_control_table_column_data_type_dict = {
        "OBJECT_TYPE" : "VARCHAR(50)",
        "OBJECT_DATABASE" : "VARCHAR(50)",
        "OBJECT_SCHEMA" : "VARCHAR(50)",
        "OBJECT_NAME" : "VARCHAR(100)",
        "MODIFIED_BY" : "VARCHAR(50)",
        "DEPLOYMENT_STATUS" : "VARCHAR(100)",
        "DEPLOYMENT_ID" : "VARCHAR(50)"
    }
    _deployment_log_table_column_list = ["DEPLOYMENT_ID","DEPLOYMENT_TIMESTAMP","DEPLOYMENT_STATUS"]
    _deployment_log_table_column_data_type_dict = {
        "DEPLOYMENT_ID" : "VARCHAR(50)",
        "DEPLOYMENT_TIMESTAMP" : "TIMESTAMP",
        "DEPLOYMENT_STATUS" : "VARCHAR(50)"
    }
    _deployment_history_table_column_list = ["OBJECT_TYPE","OBJECT_DATABASE","OBJECT_SCHEMA","OBJECT_NAME","MODIFIED_BY","DEPLOYMENT_STATUS","DEPLOYMENT_ID"]
    _deployment_history_table_column_data_type_dict = {
        "OBJECT_TYPE" : "VARCHAR(50)",
        "OBJECT_DATABASE" : "VARCHAR(50)",
        "OBJECT_SCHEMA" : "VARCHAR(50)",
        "OBJECT_NAME" : "VARCHAR(100)",
        "MODIFIED_BY" : "VARCHAR(50)",
        "DEPLOYMENT_STATUS" : "VARCHAR(100)",
        "DEPLOYMENT_ID" : "VARCHAR(50)"
    }    
    _deployment_reference_table_column_list = ["ENVIRONMENT_NAME","DATABASE_NAME"] 
    _deployment_reference_table_column_data_type_dict = {
        "ENVIRONMENT_NAME" : "VARCHAR(50)",
        "DATABASE_NAME" : "VARCHAR(50)"
    }
    _deployment_status_in_development = "IN DEVELOPMENT"
    _deployment_status_in_test = "DEPLOYED IN TEST"
    _deployment_status_in_prod = "DEPLOYED IN PROD"
        

