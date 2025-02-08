import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
from src.utils import helper

ACCESS_KEY = 'AKIAUMYCH7Z6CF4OQXJT'
SECRET_KEY = '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'

TEMPERATURE = 0
REGION = 'us-west-2'
BEDROCK_RUNTIME_SERVICE = 'bedrock-runtime'
CHAT_MODEL_ID = 'us.anthropic.claude-3-5-sonnet-20241022-v2:0'#'anthropic.claude-3-5-sonnet-20241022-v2:0'#anthropic.claude-3-haiku-20240307-v1:0' #'anthropic.claude-3-sonnet-20240229-v1:0'
KB_MODEL_ID = 'us.anthropic.claude-3-5-sonnet-20241022-v2:0'#'anthropic.claude-3-5-sonnet-20241022-v2:0'#'anthropic.claude-3-haiku-20240307-v1:0'
EMBEDDINGS_MODEL_ID = 'amazon.titan-embed-text-v1'

ALLOWED_OBJS = helper.get_obj_names()

tools = {
    "tools": [
        {
            "toolSpec": {
                "name":"addition",
                "description":"perform addition of two numbers",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "num1": {
                                "type":"string",
                                "description":"User to provide value for first number"
                            },
                            "num2": {
                                "type":"string",
                                "description":"User to provide value for second number"
                            }
                        },
                        "required":[
                            "num1","num2"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_database_object",
                "description":"creates a snowflake database object for the user. NAME is a required input to be taken from user. Only use user provided inputs",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "NAME": {
                                "type":"string",
                                "description":"user to provide value for NAME for database object. This is to be taken as input from user. do not assume a value."
                            },
                            "REPLACE_INVALID_CHARACTERS": {
                                "type":"string",
                                "description":"user provided value for REPLACE_INVALID_CHARACTERS for database object"
                            },
                        "DATA_RETENTION_TIME_IN_DAYS": {
                                "type":"string",
                                "description":"user provided value for DATA_RETENTION_TIME_IN_DAYS for database object"
                            },
                        "MAX_DATA_EXTENSION_TIME_IN_DAYS": {
                                "type":"string",
                                "description":"user provided value for MAX_DATA_EXTENSION_TIME_IN_DAYS for database object"
                            },
                        "EXTERNAL_VOLUME": {
                                "type":"string",
                                "description":"user provided value for EXTERNAL_VOLUME for database object"
                            },
                        "CATALOG": {
                                "type":"string",
                                "description":"user provided value for CATALOG for database object"
                            },
                        "DEFAULT_DDL_COLLATION": {
                                "type":"string",
                                "description":"user provided value for DEFAULT_DDL_COLLATION for database object"
                            },
                        "DATA_RETENTION_TIME_IN_DAYS": {
                                "type":"string",
                                "description":"user provided value for DATA_RETENTION_TIME_IN_DAYS for database object"
                            },
                        "STORAGE_SERIALIZATION_POLICY": {
                                "type":"string",
                                "description":"user provided value for STORAGE_SERIALIZATION_POLICY for database object"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object"
                            },
                        },
                        "required":[
                            "NAME"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_account_object",
                "description":"creates a snowflake account admin object for the user. ACCOUNT, ADMIN_NAME, and ADMIN_PASSWORD are required inputs to be taken from user. Only use user provided inputs",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "ACCOUNT": {
                                "type":"string",
                                "description":"user to provide value for ACCOUNT for database object. This is to be taken as input from user. do not assume a value."
                            },
                            "ADMIN_NAME": {
                                "type":"string",
                                "description":"user provided value for ADMIN_NAME for database object"
                            },
                        "ADMIN_PASSWORD": {
                                "type":"string",
                                "description":"user provided value for ADMIN_PASSWORD for database object"
                            },
                        "ADMIN_USER_TYPE": {
                                "type":"string",
                                "description":"user provided value for ADMIN_USER_TYPE for database object"
                            },
                        "FIRST_NAME": {
                                "type":"string",
                                "description":"user provided value for FIRST_NAME for database object"
                            },
                        "LAST_NAME": {
                                "type":"string",
                                "description":"user provided value for LAST_NAME for database object"
                            },
                        "EMAIL": {
                                "type":"string",
                                "description":"user provided value for EMAIL for database object"
                            },
                        "MUST_CHANGE_PASSWORD": {
                                "type":"string",
                                "description":"user provided value for MUST_CHANGE_PASSWORD for database object"
                            },
                        "EDITION": {
                                "type":"string",
                                "description":"user provided value for EDITION for database object"
                            },
                        "REGION_GROUP": {
                                "type":"string",
                                "description":"user provided value for REGION_GROUP for database object"
                            },
                        "REGION": {
                                "type":"string",
                                "description":"user provided value for REGION for database object"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object"
                            },
                        "POLARIS": {
                                "type":"string",
                                "description":"user provided value for POLARIS for database object"
                            },
                        },
                        "required":[
                            "ACCOUNT","ADMIN_NAME","ADMIN_PASSWORD"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_externalstage_object",
                "description":"creates a snowflake external stage object for the user. NAME and FILE_FORMAT are required inputs to be taken from user. Only use user provided inputs",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "NAME": {
                                "type":"string",
                                "description":"user to provide value for NAME for database object. This is to be taken as input from user. do not assume a value."
                            },
                            "FILE_FORMAT": {
                                "type":"string",
                                "description":"user provided value for FILE_FORMAT for database object"
                            },
                        "TAG": {
                                "type":"string",
                                "description":"user provided value for TAG for database object"
                            },
                        "URL": {
                                "type":"string",
                                "description":"user provided value for URL for database object"
                            },
                        "STORAGE_INTEGRATION": {
                                "type":"string",
                                "description":"user provided value for STORAGE_INTEGRATION for database object"
                            },
                        "AWS_KEY_ID": {
                                "type":"string",
                                "description":"user provided value for AWS_KEY_ID for database object"
                            },
                        "AWS_SECRET_KEY": {
                                "type":"string",
                                "description":"user provided value for AWS_SECRET_KEY for database object"
                            },
                        "AWS_TOKEN": {
                                "type":"string",
                                "description":"user provided value for AWS_TOKEN for database object"
                            },
                        "AZURE_SAS_TOKEN": {
                                "type":"string",
                                "description":"user provided value for AZURE_SAS_TOKEN for database object"
                            },
                        "AWS_ROLE": {
                                "type":"string",
                                "description":"user provided value for AWS_ROLE for database object"
                            },
                        "ENCRYPTION": {
                                "type":"string",
                                "description":"user provided value for ENCRYPTION for database object"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object"
                            },
                        "ENCRYPTION_TYPE": {
                                "type":"string",
                                "description":"user provided value for ENCRYPTION_TYPE for database object"
                            },
                        "ENCRYPTION_MASTER_KEY": {
                                "type":"string",
                                "description":"user provided value for ENCRYPTION_MASTER_KEY for database object"
                            },
                        "ENCRYPTION_KMS_KEY_ID": {
                                "type":"string",
                                "description":"user provided value for ENCRYPTION_KMS_KEY_ID for database object"
                            },
                        "USE_PRIVATELINK_ENDPOINT": {
                                "type":"string",
                                "description":"user provided value for USE_PRIVATELINK_ENDPOINT for database object"
                            },
                        "DIRECTORY": {
                                "type":"string",
                                "description":"user provided value for DIRECTORY for database object"
                            },
                        "REFRESH_ON_CREATE": {
                                "type":"string",
                                "description":"user provided value for REFRESH_ON_CREATE for database object"
                            },
                        "AUTO_REFRESH": {
                                "type":"string",
                                "description":"user provided value for AUTO_REFRESH for database object"
                            },
                        "NOTIFICATION_INTEGRATION": {
                                "type":"string",
                                "description":"user provided value for NOTIFICATION_INTEGRATION for database object"
                            },
                        },
                        "required":[
                            "NAME","FILE_FORMAT"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_fileformat_object",
                "description":"creates a snowflake fileformat object for the user. DATABASE, SCHEMA, FILE_FORMAT is a required input to be taken from user. Only use user provided inputs",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                			"DATABASE": {
                                "type":"string",
                                "description":"user provided value for DATABASE for database object"
                            },
                			"SCHEMA": {
                                "type":"string",
                                "description":"user provided value for SCHEMA for database object"
                            },
                            "FILE_FORMAT": {
                                "type":"string",
                                "description":"user provided value for FILE_FORMAT for database object"
                            },
                        "TYPE": {
                                "type":"string",
                                "description":"user provided value for TYPE for database object"
                            },
                        "PARSE_HEADER": {
                                "type":"string",
                                "description":"user provided value for PARSE_HEADER for database object"
                            },
                        "SKIP_HEADER": {
                                "type":"string",
                                "description":"user provided value for SKIP_HEADER for database object"
                            },
                        "SKIP_BLANK_LINES": {
                                "type":"string",
                                "description":"user provided value for SKIP_BLANK_LINES for database object"
                            },
                        "DATE_FORMAT": {
                                "type":"string",
                                "description":"user provided value for DATE_FORMAT for database object"
                            },
                        "TIME_FORMAT": {
                                "type":"string",
                                "description":"user provided value for TIME_FORMAT for database object"
                            },
                        "TIMESTAMP_FORMAT": {
                                "type":"string",
                                "description":"user provided value for TIMESTAMP_FORMAT for database object"
                            },
                        "BINARY_FORMAT": {
                                "type":"string",
                                "description":"user provided value for BINARY_FORMAT for database object"
                            },
                        "ESCAPE": {
                                "type":"string",
                                "description":"user provided value for ESCAPE for database object"
                            },
                        "ESCAPE_UNENCLOSED_FIELD": {
                                "type":"string",
                                "description":"user provided value for ESCAPE_UNENCLOSED_FIELD for database object"
                            },
                        "TRIM_SPACE": {
                                "type":"string",
                                "description":"user provided value for TRIM_SPACE for database object"
                            },
                        "FIELD_OPTIONALLY_ENCLOSED_BY": {
                                "type":"string",
                                "description":"user provided value for FIELD_OPTIONALLY_ENCLOSED_BY for database object"
                            },
                        "NULL_IF": {
                                "type":"string",
                                "description":"user provided value for NULL_IF for database object"
                            },
                        "ERROR_ON_COLUMN_COUNT_MISMATCH": {
                                "type":"string",
                                "description":"user provided value for ERROR_ON_COLUMN_COUNT_MISMATCH for database object"
                            },
                        "REPLACE_INVALID_CHARACTERS": {
                                "type":"string",
                                "description":"user provided value for REPLACE_INVALID_CHARACTERS for database object"
                            },
                        "EMPTY_FIELD_AS_NULL": {
                                "type":"string",
                                "description":"user provided value for EMPTY_FIELD_AS_NULL for database object"
                            },
                        "SKIP_BYTE_ORDER_MARK": {
                                "type":"string",
                                "description":"user provided value for SKIP_BYTE_ORDER_MARK for database object"
                            },
                        "ENCODING": {
                                "type":"string",
                                "description":"user provided value for ENCODING for database object"
                            },
                        "ENABLE_OCTAL": {
                                "type":"string",
                                "description":"user provided value for ENABLE_OCTAL for database object"
                            },
                        "ALLOW_DUPLICATE": {
                                "type":"string",
                                "description":"user provided value for ALLOW_DUPLICATE for database object"
                            },
                        "STRIP_OUTER_ARRAY": {
                                "type":"string",
                                "description":"user provided value for STRIP_OUTER_ARRAY for database object"
                            },
                        "STRIP_NULL_VALUES": {
                                "type":"string",
                                "description":"user provided value for STRIP_NULL_VALUES for database object"
                            },
                        "IGNORE_UTF8_ERRORS": {
                                "type":"string",
                                "description":"user provided value for IGNORE_UTF8_ERRORS for database object"
                            },
                        "SNAPPY_COMPRESSION": {
                                "type":"string",
                                "description":"user provided value for SNAPPY_COMPRESSION for database object"
                            },
                        "BINARY_AS_TEXT": {
                                "type":"string",
                                "description":"user provided value for BINARY_AS_TEXT for database object"
                            },
                        "USE_LOGICAL_TYPE": {
                                "type":"string",
                                "description":"user provided value for USE_LOGICAL_TYPE for database object"
                            },
                        "USE_VECTORIZED_SCANNER": {
                                "type":"string",
                                "description":"user provided value for USE_VECTORIZED_SCANNER for database object"
                            },
                        "PRESERVE_SPACE": {
                                "type":"string",
                                "description":"user provided value for PRESERVE_SPACE for database object"
                            },
                        "STRIP_OUTER_ELEMENT": {
                                "type":"string",
                                "description":"user provided value for STRIP_OUTER_ELEMENT for database object"
                            },
                        "DISABLE_SNOWFLAKE_DATA": {
                                "type":"string",
                                "description":"user provided value for DISABLE_SNOWFLAKE_DATA for database object"
                            },
                        "DISABLE_AUTO_CONVERT": {
                                "type":"string",
                                "description":"user provided value for DISABLE_AUTO_CONVERT for database object"
                            },
                            
                        },
                        "required":[
                            "FILE_FORMAT","DATABASE","SCHEMA"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_internalstage_object",
                "description":"creates a snowflake internal stage object for the user. DATABASE is a required input to be taken from user. Only use user provided inputs",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "DATABASE": {
                                "type":"string",
                                "description":"user provided value for DATABASE for database object"
                            },
                        "SCHEMA": {
                                "type":"string",
                                "description":"user provided value for SCHEMA for database object"
                            },
                        "NAME": {
                                "type":"string",
                                "description":"user provided value for NAME for database object"
                            },
                        "FILE_FORMAT": {
                                "type":"string",
                                "description":"user provided value for FILE_FORMAT for database object"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object"
                            },
                        "TAG": {
                                "type":"string",
                                "description":"user provided value for TAG for database object"
                            },
                        "ENCRYPTION": {
                                "type":"string",
                                "description":"user provided value for ENCRYPTION for database object"
                            },
                        "DIRECTORY": {
                                "type":"string",
                                "description":"user provided value for DIRECTORY for database object"
                            },
                        "REFRESH_ON_CREATE": {
                                "type":"string",
                                "description":"user provided value for REFRESH_ON_CREATE for database object"
                            },
                            
                        },
                        "required":[
                            "NAME",
                            "DATABASE",
                            "SCHEMA"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_resourcemonitor_object",
                "description":"creates a snowflake resource monitor object for the user. NAME is a required input to be taken from user. Only use user provided inputs",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "NAME": {
                                "type":"string",
                                "description":"user provided value for NAME for database object"
                            },
                        "CREDIT_QUOTA": {
                                "type":"string",
                                "description":"user provided value for CREDIT_QOUTA for database object"
                            },
                        "FREQUENCY": {
                                "type":"string",
                                "description":"user provided value for FREQUENCY for database object"
                            },
                        "START_TIMESTAMP": {
                                "type":"string",
                                "description":"user provided value for START_TIMESTAMP for database object"
                            },
                        "END_TIMESTAMP": {
                                "type":"string",
                                "description":"user provided value for END_TIMESTAMP for database object"
                            },
                        "NOTIFY_USERS": {
                                "type":"string",
                                "description":"user provided value for NOTIFY_USERS for database object"
                            },
                        "TRIGGERS_ON": {
                                "type":"string",
                                "description":"user provided value for TRIGGERS_ON for database object"
                            },
                        "DO": {
                                "type":"string",
                                "description":"user provided value for DO for database object"
                            },
                            
                        },
                        "required":[
                            "NAME"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_role_object",
                "description":"creates a snowflake role object for the user. NAME is a required input to be taken from user. Only use user provided inputs",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "NAME": {
                                "type":"string",
                                "description":"user provided value for NAME for database object"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object"
                            },
                            
                        },
                        "required":[
                            "NAME"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_schema_object",
                "description":"creates a snowflake schema object for the user. DATABASE and NAME are required inputs to be taken from user. Only use user provided inputs",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "DATABASE": {
                                "type":"string",
                                "description":"user provided value for DATABASE for database object"
                            },
                        "NAME": {
                                "type":"string",
                                "description":"user provided value for NAME for database object"
                            },
                        "WITH_MANAGED_ACCESS": {
                                "type":"string",
                                "description":"user provided value for WITH_MANAGED_ACCESS for database object"
                            },
                        "DATA_RETENTION_TIME_IN_DAYS": {
                                "type":"string",
                                "description":"user provided value for DATA_RETENTION_TIME_IN_DAYS for database object"
                            },
                        "MAX_DATA_EXTENSION_TIME_IN_DAYS": {
                                "type":"string",
                                "description":"user provided value for MAX_DATA_EXTENSION_TIME_IN_DAYS for database object"
                            },
                        "EXTERNAL_VOLUME": {
                                "type":"string",
                                "description":"user provided value for EXTERNAL_VOLUME for database object"
                            },
                        "CATALOG": {
                                "type":"string",
                                "description":"user provided value for CATALOG for database object"
                            },
                        "REPLACE_INVALID_CHARACTERS": {
                                "type":"string",
                                "description":"user provided value for REPLACE_INVALID_CHARACTERS for database object"
                            },
                        "DEFAULT_DDL_COLLATION": {
                                "type":"string",
                                "description":"user provided value for DEFAULT_DDL_COLLATION for database object"
                            },
                        "LOG_LEVEL": {
                                "type":"string",
                                "description":"user provided value for LOG_LEVEL for database object"
                            },
                        "TRACE_LEVEL": {
                                "type":"string",
                                "description":"user provided value for TRACE_LEVEL for database object"
                            },
                        "STORAGE_SERIALIZATION_POLICY": {
                                "type":"string",
                                "description":"user provided value for STORAGE_SERIALIZATION_POLICY for database object"
                            },
                        "CLASSIFICATION_PROFILE": {
                                "type":"string",
                                "description":"user provided value for CLASSIFICATION_PROFILE for database object"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object"
                            },
                        "TAG": {
                                "type":"string",
                                "description":"user provided value for TAG for database object"
                            },
                            
                        },
                        "required":[
                            "DATABASE","NAME"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_share_object",
                "description":"creates a snowflake share object for the user. NAME is a required input to be taken from user. Only use user provided inputs",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "NAME": {
                                "type":"string",
                                "description":"user provided value for NAME for database object"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object"
                            },
                            
                        },
                        "required":[
                            "NAME"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_user_object",
                "description":"creates a snowflake user object for the user. NAME and PASSWORD are required inputs to be taken from user. Only use user provided inputs",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "NAME": {
                                "type":"string",
                                "description":"user provided value for NAME for database object"
                            },
                        "PASSWORD": {
                                "type":"string",
                                "description":"user provided value for PASSWORD for database object"
                            },
                        "LOGIN_NAME": {
                                "type":"string",
                                "description":"user provided value for LOGIN_NAME for database object"
                            },
                        "DISPLAY_NAME": {
                                "type":"string",
                                "description":"user provided value for DISPLAY_NAME for database object"
                            },
                        "FIRST_NAME": {
                                "type":"string",
                                "description":"user provided value for FIRST_NAME for database object"
                            },
                        "LAST_NAME": {
                                "type":"string",
                                "description":"user provided value for LAST_NAME for database object"
                            },
                        "EMAIL": {
                                "type":"string",
                                "description":"user provided value for EMAIL for database object"
                            },
                        "MUST_CHANGE_PASSWORD": {
                                "type":"string",
                                "description":"user provided value for MUST_CHANGE_PASSWORD for database object"
                            },
                        "DISABLED": {
                                "type":"string",
                                "description":"user provided value for DISABLED for database object"
                            },
                        "DAYS_TO_EXPIRY": {
                                "type":"string",
                                "description":"user provided value for DAYS_TO_EXPIRY for database object"
                            },
                        "MINS_TO_UNLOCK": {
                                "type":"string",
                                "description":"user provided value for MINS_TO_UNLOCK for database object"
                            },
                        "DEFAULT_WAREHOUSE": {
                                "type":"string",
                                "description":"user provided value for DEFAULT_WAREHOUSE for database object"
                            },
                        "DEAFULT_ROLE": {
                                "type":"string",
                                "description":"user provided value for DEFAULT_ROLE for database object"
                            },
                        "DEFAULT_SECONDARY_ROLES": {
                                "type":"string",
                                "description":"user provided value for DEFAULT_SECONDARY_ROLES for database object"
                            },
                        "MINS_TO_BY_PASS_MFA": {
                                "type":"string",
                                "description":"user provided value for MINS_TO_BY_PASS_MFA for database object"
                            },
                        "RSA_PUBLIC_KEY": {
                                "type":"string",
                                "description":"user provided value for RSA_PUBLIC_KEY for database object"
                            },
                        "RSA_PUBLIC_KEY_FP": {
                                "type":"string",
                                "description":"user provided value for RSA_PUBLIC_KEY_FP for database object"
                            },
                        "RSA_PUBLIC_KEY_2": {
                                "type":"string",
                                "description":"user provided value for RSA_PUBLIC_KEY_2 for database object"
                            },
                        "RSA_PUBLIC_KEY_2_FP": {
                                "type":"string",
                                "description":"user provided value for RSA_PUBLIC_KEY_2_FP for database object"
                            },
                        "TYPE": {
                                "type":"string",
                                "description":"user provided value for TYPE for database object"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object"
                            },
                        "ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR": {
                                "type":"string",
                                "description":"user provided value for ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR for database object"
                            },
                            
                        },
                        "required":[
                            "NAME"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_warehouse_object",
                "description":"creates a snowflake warehouse object for the user. NAME is a required input to be taken from user. Only use user provided inputs",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "NAME": {
                                "type":"string",
                                "description":"user provided value for NAME for database object"
                            },
                        "WAREHOUSE_SIZE": {
                                "type":"string",
                                "description":"user provided value for WAREHOUSE_SIZE for database object"
                            },
                        "WAREHOUSE_TYPE": {
                                "type":"string",
                                "description":"user provided value for WAREHOUSE_TYPE for database object"
                            },
                        "RESOURCE_CONSTRAINT": {
                                "type":"string",
                                "description":"user provided value for RESOURCE_CONSTRAINT for database object"
                            },
                        "MAX_CLUSTER_COUNT": {
                                "type":"string",
                                "description":"user provided value for MAX_CLUSTER_COUNT for database object"
                            },
                        "MIN_CLUSTER_COUNT": {
                                "type":"string",
                                "description":"user provided value for MIN_CLUSTER_COUNT for database object"
                            },
                        "SCALING_POLICY": {
                                "type":"string",
                                "description":"user provided value for SCALING_POLICY for database object"
                            },
                        "AUTO_SUSPEND": {
                                "type":"string",
                                "description":"user provided value for AUTO_SUSPEND for database object"
                            },
                        "AUTO_RESUME": {
                                "type":"string",
                                "description":"user provided value for AUTO_RESUME for database object"
                            },
                        "INITIALLY_SUSPENDED": {
                                "type":"string",
                                "description":"user provided value for INTITIALLY_SUSPENDED for database object"
                            },
                        "RESOURCE_MONITOR": {
                                "type":"string",
                                "description":"user provided value for RESOURCE_MONITOR for database object"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object"
                            },
                        "TAG": {
                                "type":"string",
                                "description":"user provided value for TAG for database object"
                            },
                        "ENABLE_QUERY_ACCELERATION": {
                                "type":"string",
                                "description":"user provided value for ENABLE_QUERY_ACCELERATION for database object"
                            },
                        "QUERY_ACCELERATION_MAX_SCALE_FACTOR": {
                                "type":"string",
                                "description":"user provided value for QUERY_ACCELERATION_MAX_SCALE_FACTOR for database object"
                            },
                        "MAX_CONCURRENCY_LEVEL": {
                                "type":"string",
                                "description":"user provided value for MAX_CONCURRENCY_LEVEL for database object"
                            },
                        "STATEMENT_QUEUED_TIMEOUT_IN_SECONDS": {
                                "type":"string",
                                "description":"user provided value for STATEMENT_QUEUED_TIMEOUT_IN_SECONDS for database object"
                            },
                        "STATEMENT_TIMEOUT_IN_SECONDS": {
                                "type":"string",
                                "description":"user provided value for STATEMENT_TIMEOUT_IN_SECONDS for database object"
                            },
                        },
                        "required":[
                            "NAME"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_multiple_table_object",
                "description":"creates multiple snowflake table objects in bulk for the user. DATABASE and SCHEMA are required inputs from user. this function already has the table names, so user does not have to provide it.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "database": {
                                "type":"string",
                                "description":"database object name"
                            },
                        "schema": {
                                "type":"string",
                                "description":"schema object name"
                            },
                        },
                        "required":[
                            "database","schema"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_single_table_object",
                "description":"create one snowflake table object for the user. name is a required input from user.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "name": {
                                "type":"string",
                                "description":"user provided name for table object"
                            }
                        },
                        "required":[
                            "name"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_copyinto_object",
                "description":"creates a snowflake copyinto object for the user.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "DATABASE": {
                                "type":"string",
                                "description":"user provided value for DATABASE for copying object"
                            },
			"SCHEMA": {
                                "type":"string",
                                "description":"user provided value for SCHEMA for copying object"
                            },
			"TABLE": {
                                "type":"string",
                                "description":"user provided list for TABLE nameS for copying object"
                            },
			"STAGE": {
                                "type":"string",
                                "description":"user provided value for STAGE name for copying object"
                            },
			"FILE_FORMAT": {
                                "type":"string",
                                "description":"user provided value for FILE_FORMAT for copying object"
                            },
			"ON_ERROR": {
                                "type":"string",
                                "description":"user provided value for ON_ERROR for copying object"
                            },
			"SIZE_LIMIT": {
                                "type":"string",
                                "description":"user provided value for SIZE_LIMIT for copying object"
                            },
			"PURGE": {
                                "type":"string",
                                "description":"user provided value for PURGE for copying object"
                            },
			"RETURN_FAILED_ONLY": {
                                "type":"string",
                                "description":"user provided value for RETURN_FAILED_ONLY for copying object"
                            },
			"MATCH_BY_COLUMN_NAME": {
                                "type":"string",
                                "description":"user provided value for MATCH_BY_COLUMN_NAME for copying object"
                            },
			"INCLUDE_METADATA": {
                                "type":"string",
                                "description":"user provided value for INCLUDE_METADATA for copying object"
                            },
			"ENFORCE_LENGTH": {
                                "type":"string",
                                "description":"user provided value for ENFORCE_LENGTH for copying object"
                            },
			"TRUNCATECOLUMNS": {
                                "type":"string",
                                "description":"user provided value for TRUNCATECOLUMNS for copying object"
                            },
			"FORCE": {
                                "type":"string",
                                "description":"user provided value for FORCE for copying object"
                            },
			"LOAD_UNCERTAIN_FILES": {
                                "type":"string",
                                "description":"user provided value for LOAD_UNCERTAIN_FILES for copying object"
                            },
			"FILE_PROCESSOR": {
                                "type":"string",
                                "description":"user provided value for FILE_PROCESSOR for copying object"
                            },
			"LOAD_MODE": {
                                "type":"string",
                                "description":"user provided value for LOAD_MODE for copying object"
                            },
                        },
                        "required":[
                            "DATABASE","SCHEMA","TABLE","FILE_FORMAT","STAGE"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"get_workflow",
                "description":"retrieves the workflow setup instructions",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "query": {
                                "type":"string",
                                "description":"user query"
                            }
                        },
                        "required":[
                            "query"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"deploy_all_dev_to_test",
                "description":"deploys all objects from dev environment to test environment.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "query": {
                                "type":"string",
                                "description":"user query"
                            }
                        },
                        "required":[
                            "query"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"sf_setup",
                "description":"performs snowflake setup for user. do this if user specifies it is their first time and explicitly ask for the setup. Does not have to tell user how to do it, instead this function does it all for the user.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "query": {
                                "type":"string",
                                "description":"user query"
                            }
                        },
                        "required":[
                            "query"
                        ]
                    }
                }
            }
        }
    ]
}