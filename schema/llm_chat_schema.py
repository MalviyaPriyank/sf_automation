NAME = 'name'
JSON = 'json'
INPUT = 'input'
RESULT = 'result'
CONTENT = 'content'
TOOL_USE = 'toolUse'
OBJ_NAME = 'obj_name'
TOOL_USE_ID = 'toolUseId'
TOOL_RESULT = 'toolResult'
RETRIEVAL_WORKFLOW = 'retrieval_workflow'

CREATE_SF_OBJ = 'create_sf_object'

SYSTEM_PROMPT_USER = 'You are an assistant named Frosty to help user build on snowflake platform. Only answer questions related to snowflake. Start by retrieving the workflow provided as tool. Always provide a link to snowflake documentation if you pull information from the web.'

OBJ_PROMPTS = {
'What are the attributes to create snowflake database object?':'NAME is a required attribute to create snowflake database object. Optional attributes for snowflake database object are REPLACE_INVALID_CHARACTERS, DATA_RETENTION_TIME_IN_DAYS, MAX_DATA_EXTENSION_TIME_IN_DAYS, EXTERNAL_VOLUME, CATALOG, DEFAULT_DDL_COLLATION, DATA_RETENTION_TIME_IN_DAYS, STORAGE_SERIALIZATION_POLICY, COMMENT',
'What are the attributes to create snowflake external stage (externalstage) object':'NAME and FILE_FORMAT are the required attributes to create snowflake external stage object. Optional attributes include COMMENT, TAG, URL, STORAGE_INTEGRATION, AWS_KEY_ID, AWS_SECRET_KEY, AWS_TOKEN, AZURE_SAS_TOKEN, AWS_ROLE, ENCRYPTION, ENCRYPTION_TYPE, ENCRYPTION_MASTER_KEY, ENCRYPTION_KMS_KEY_ID, USE_PRIVATELINK_ENDPOINT, DIRECTORY, REFRESH_ON_CREATE, AUTO_REFRESH, NOTIFICATION_INTEGRATION',
'What are the required attributes to create snowflake file format object': 'FILE_FORMAT is a required attribute. Optional attributes include TYPE, PARSE_HEADER, SKIP_HEADER, SKIP_BLANK_LINES, DATE_FORMAT, TIME_FORMAT, TIMESTAMP_FORMAT, BINARY_FORMAT, ESCAPE, ESCAPE_UNENCLOSED_FIELD, SNOWFLAKE_FULL, TRIM_SPACE, FIELD_OPTIONALLY_ENCLOSED_BY, NULL_IF, ERROR_ON_COLUMN_COUNT_MISMATCH, REPLACE_INVALID_CHARACTERS, EMPTY_FIELD_AS_NULL, SKIP_BYTE_ORDER_MARK, ENCODING, ENABLE_OCTAL, ALLOW_DUPLICATE, STRIP_OUTER_ARRAY, STRIP_NULL_VALUES, IGNORE_UTF8_ERROR, SNAPPY_COMPRESSION, BINARY_AS_TEXT, USE_LOGICAL_TYPE, USE_VECTORIZED_SCANNER, PRESERVE_SPACE, STRIP_OUTER_ELEMENT, DISABLE_SNOWFLAKE_DATA, DISABLE_AUTO_CONVERT',
'What are the attributes to create snowflake internal stage (internalstage) object':'DATABASE is the required attribute. SCHEMA, NAME, FILE_FORMAT, COMMENT, TAG, ENCRYPTION, DIRECTORY, REFRESH_ON_CREATE are optional attributes',
'What are the attributes for resource monitor object':'NAME is a required attribute. CREDIT_QUOTA, FREQUENCY, START_TIMESTAMP, END_TIMESTAMP, NOTIFY_USERS, TRIGGERS_ON, DO are optional attributes',
'What are the attributes to create snowflake role object':'NAME is a required attribute and COMMENT is an optional attribute',
'What are the attributes for schema object':'DATABASE and NAME are required attributes. Optional attributes include WITH_MANAGED_ACCESS, DATA_RETENTION_TIME_IN_DAYS, MAX_DATA_EXTENSION_TIME_IN_DAYS, EXTERNAL_VOLUME, CATALOG, REPLACE_INVALID_CHARACTERS, DEFAULT_DDL_COLLATION, LOG_LEVEL, TRACE_LEVEL, STORAGE_SERIALIZATION_POLICY, CLASSIFICATION_PROFILE, COMMENT, TAG',
'What are the attributes to create snowflake share object':'NAME is a required attribute, and COMMENT is an optional attribute',
'What are the attributes to create snowflake user object':'NAME and PASSWORD are required attributes. Optional attributes include LOGIN_NAME, DISPLAY_NAME, FIRST_NAME, LAST_NAME, EMAIL, MUST_CHANGE_PASSWORD, DISABLED, DAYS_TO_EXPIRY, MINS_TO_UNLOCK, DEFAULT_WAREHOUSE, DEFAULT_ROLE, DEFAULT_SECONDARY_ROLES, MINS_TO_BY_PASS_MFA, RSA_PUBLIC_KEY, RSA_PUBLIC_KEY_FP, RSA_PUBLIC_KEY_2, RSA_PUBLIC_KEY_2_FP, TYPE, COMMENT, ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR',
'What are the attributes to create snowflake warehouse object':'NAME is a required attribute. Optional attributes include WAREHOUSE_SIZE, WAREHOUSE_TYPE, RESOURCE_CONSTRAINT, MAX_CLUSTER_COUNT, MIN_CLUSTER_COUNT, SCALING_POLICY, AUTO_SUSPEND, AUTO_RESUME, INITIALLY_SUSPENDED, RESOURCE_MONITOR, COMMENT, TAG, ENABLE_QUERY_ACCELERATION, QUERY_ACCELERATION_MAX_SCALE_FACTOR, MAX_CONCURRENCY_LEVEL, STATEMENT_QUEUED_TIMEOUT_IN_SECONDS, STATEMENT_TIMEOUT_IN_SECONDS'
}

SYSTEM_PROMPT_ASST = 'Understood. How can I help?'

JSON_UPLOAD_GREETING = 'Please upload the json with required attributes'