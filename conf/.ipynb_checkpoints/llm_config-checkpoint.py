import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
from src.utils import helper

ACCESS_KEY = 'AKIAUMYCH7Z6CF4OQXJT'
SECRET_KEY = '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'

TEMPERATURE = 0
REGION = 'us-west-2'
BEDROCK_RUNTIME_SERVICE = 'bedrock-runtime'
CHAT_MODEL_ID = 'us.anthropic.claude-3-7-sonnet-20250219-v1:0' #'us.anthropic.claude-3-5-sonnet-20241022-v2:0'#'anthropic.claude-3-5-sonnet-20241022-v2:0'#anthropic.claude-3-haiku-20240307-v1:0' #'anthropic.claude-3-sonnet-20240229-v1:0'
KB_MODEL_ID = 'us.anthropic.claude-3-7-sonnet-20250219-v1:0' #'us.anthropic.claude-3-5-sonnet-20241022-v2:0'#'anthropic.claude-3-5-sonnet-20241022-v2:0'#'anthropic.claude-3-haiku-20240307-v1:0'
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
                        "STORAGE_SERIALIZATION_POLICY": {
                                "type":"string",
                                "description":"user provided value for STORAGE_SERIALIZATION_POLICY for database object"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object"
                            },
                            "LOG_LEVEL": {
                                "type":"string",
                                "description":"user provided value for LOG_LEVEL for database object"
                            },
                            "TRACE_LEVEL": {
                                "type":"string",
                                "description":"user provided value for TRACE_LEVEL for database object"
                            }
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
                "description":"creates a snowflake external stage object for the user. NAME, DATABASE, SCHEMA are required inputs to be taken from user. Only use user provided inputs. While fileformat is not required, recommend creating file format to save rework in the future.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "NAME": {
                                "type":"string",
                                "description":"user to provide value for NAME for external stage object. This is to be taken as input from user. do not assume a value."
                            },
                            "DATABASE": {
                                "type":"string",
                                "description":"user to provide value for DATABASE for external stage object. This is to be taken as input from user. do not assume a value."
                            },
                            "SCHEMA": {
                                "type":"string",
                                "description":"user to provide value for SCHEMA for external stage object. This is to be taken as input from user. do not assume a value."
                            },
                            "FILE_FORMAT": {
                                "type":"string",
                                "description":"user provided value for FILE_FORMAT for external stage object"
                            },
                        "URL": {
                                "type":"string",
                                "description":"user provided value for URL for external stage object"
                            },
                        "AWS_ACCESS_POINT_ARN": {
                                "type":"string",
                                "description":"user provided value for AWS ACCESS POINT ARN for external stage object"
                            },
                        "STORAGE_INTEGRATION": {
                                "type":"string",
                                "description":"user provided value for STORAGE_INTEGRATION for external stage object"
                            },
                        
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for external stage object"
                            },
                        "ENCRYPTION_TYPE": {
                                "type":"string",
                                "description":"user provided value for ENCRYPTION_TYPE for external stage object"
                            },
                        "ENCRYPTION_MASTER_KEY": {
                                "type":"string",
                                "description":"user provided value for ENCRYPTION_MASTER_KEY for external stage object"
                            },
                        "ENCRYPTION_KMS_KEY_ID": {
                                "type":"string",
                                "description":"user provided value for ENCRYPTION_KMS_KEY_ID for external stage object"
                            },
                        "USE_PRIVATELINK_ENDPOINT": {
                                "type":"string",
                                "description":"user provided value for USE_PRIVATELINK_ENDPOINT for external stage object"
                            },
                        "ENABLE": {
                                "type":"string",
                                "description":"user provided value for DIRECTORY for external stage object"
                            },
                        "REFRESH_ON_CREATE": {
                                "type":"string",
                                "description":"user provided value for REFRESH_ON_CREATE for external stage object"
                            },
                        "AUTO_REFRESH": {
                                "type":"string",
                                "description":"user provided value for AUTO_REFRESH for external stage object"
                            },
                        "NOTIFICATION_INTEGRATION": {
                                "type":"string",
                                "description":"user provided value for NOTIFICATION_INTEGRATION for external stage object"
                            },
                        },
                        "required":[
                            "NAME","DATABASE","SCHEMA"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_fileformat_object",
                "description":"creates a snowflake fileformat object for the user. DATABASE, SCHEMA, FILE_FORMAT is a required input to be taken from user. Only use user provided inputs. Do not refer snowflake documentation for attributes.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                			"DATABASE": {
                                "type":"string",
                                "description":"user provided value for DATABASE for file format object"
                            },
                			"SCHEMA": {
                                "type":"string",
                                "description":"user provided value for SCHEMA for file format object"
                            },
                            "FILE_FORMAT": {
                                "type":"string",
                                "description":"user provided value for FILE_FORMAT for file format object"
                            },
                            "MULTI_LINE": {
                                "type":"string",
                                "description":"user provided value for MULTI_LINE for file format object"
                            },
                        "TYPE": {
                                "type":"string",
                                "description":"user provided value for TYPE for file format object"
                            },
                        "PARSE_HEADER": {
                                "type":"string",
                                "description":"user provided value for PARSE_HEADER for file format object"
                            },
                        "SKIP_HEADER": {
                                "type":"string",
                                "description":"user provided value for SKIP_HEADER for file format object"
                            },
                        "SKIP_BLANK_LINES": {
                                "type":"string",
                                "description":"user provided value for SKIP_BLANK_LINES for file format object"
                            },
                        "DATE_FORMAT": {
                                "type":"string",
                                "description":"user provided value for DATE_FORMAT for file format object"
                            },
                        "TIME_FORMAT": {
                                "type":"string",
                                "description":"user provided value for TIME_FORMAT for file format object"
                            },
                        "TIMESTAMP_FORMAT": {
                                "type":"string",
                                "description":"user provided value for TIMESTAMP_FORMAT for file format object"
                            },
                        "BINARY_FORMAT": {
                                "type":"string",
                                "description":"user provided value for BINARY_FORMAT for file format object"
                            },
                        "ESCAPE": {
                                "type":"string",
                                "description":"user provided value for ESCAPE for file format object"
                            },
                        "ESCAPE_UNENCLOSED_FIELD": {
                                "type":"string",
                                "description":"user provided value for ESCAPE_UNENCLOSED_FIELD for file format object"
                            },
                        "TRIM_SPACE": {
                                "type":"string",
                                "description":"user provided value for TRIM_SPACE for file format object"
                            },
                        "FIELD_OPTIONALLY_ENCLOSED_BY": {
                                "type":"string",
                                "description":"user provided value for FIELD_OPTIONALLY_ENCLOSED_BY for file format object"
                            },
                        "NULL_IF": {
                                "type":"string",
                                "description":"user provided value for NULL_IF for file format object"
                            },
                        "ERROR_ON_COLUMN_COUNT_MISMATCH": {
                                "type":"string",
                                "description":"user provided value for ERROR_ON_COLUMN_COUNT_MISMATCH for file format object"
                            },
                        "REPLACE_INVALID_CHARACTERS": {
                                "type":"string",
                                "description":"user provided value for REPLACE_INVALID_CHARACTERS for file format object"
                            },
                        "EMPTY_FIELD_AS_NULL": {
                                "type":"string",
                                "description":"user provided value for EMPTY_FIELD_AS_NULL for file format object"
                            },
                        "SKIP_BYTE_ORDER_MARK": {
                                "type":"string",
                                "description":"user provided value for SKIP_BYTE_ORDER_MARK for file format object"
                            },
                        "ENCODING": {
                                "type":"string",
                                "description":"user provided value for ENCODING for file format object"
                            },
                        "ENABLE_OCTAL": {
                                "type":"string",
                                "description":"user provided value for ENABLE_OCTAL for file format object"
                            },
                        "ALLOW_DUPLICATE": {
                                "type":"string",
                                "description":"user provided value for ALLOW_DUPLICATE for file format object"
                            },
                        "STRIP_OUTER_ARRAY": {
                                "type":"string",
                                "description":"user provided value for STRIP_OUTER_ARRAY for file format object"
                            },
                        "STRIP_NULL_VALUES": {
                                "type":"string",
                                "description":"user provided value for STRIP_NULL_VALUES for file format object"
                            },
                        "IGNORE_UTF8_ERRORS": {
                                "type":"string",
                                "description":"user provided value for IGNORE_UTF8_ERRORS for file format object"
                            },
                        "SNAPPY_COMPRESSION": {
                                "type":"string",
                                "description":"user provided value for SNAPPY_COMPRESSION for file format object"
                            },
                        "BINARY_AS_TEXT": {
                                "type":"string",
                                "description":"user provided value for BINARY_AS_TEXT for file format object"
                            },
                        "USE_LOGICAL_TYPE": {
                                "type":"string",
                                "description":"user provided value for USE_LOGICAL_TYPE for file format object"
                            },
                        "USE_VECTORIZED_SCANNER": {
                                "type":"string",
                                "description":"user provided value for USE_VECTORIZED_SCANNER for file format object"
                            },
                        "PRESERVE_SPACE": {
                                "type":"string",
                                "description":"user provided value for PRESERVE_SPACE for file format object"
                            },
                        "STRIP_OUTER_ELEMENT": {
                                "type":"string",
                                "description":"user provided value for STRIP_OUTER_ELEMENT for file format object"
                            },
                        "DISABLE_SNOWFLAKE_DATA": {
                                "type":"string",
                                "description":"user provided value for DISABLE_SNOWFLAKE_DATA for file format object"
                            },
                        "DISABLE_AUTO_CONVERT": {
                                "type":"string",
                                "description":"user provided value for DISABLE_AUTO_CONVERT for file format object"
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
                "description":"creates a snowflake internal stage object for the user. DATABASE is a required input to be taken from user. Only use user provided inputs. While fileformat is not required, recommend creating file format to save rework in the future.",
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
                "description":"creates a snowflake copyinto and snowpipe objects for the user. Do not use pattern attribute and on_error attribute. After creating snowpipe, recommend user to create error integration which would alert them in case of failures in snowpipe.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "DATABASE": {
                                "type":"string",
                                "description":"user provided value for DATABASE for copyinto object"
                            },
			"SCHEMA": {
                                "type":"string",
                                "description":"user provided value for SCHEMA for copyinto object"
                            },
			"TABLE": {
                                "type":"string",
                                "description":"user provided list for TABLE names for copyinto object"
                            },
			"STAGE": {
                                "type":"string",
                                "description":"user provided value for STAGE name for copyinto object"
                            },
			"FILE_FORMAT": {
                                "type":"string",
                                "description":"user provided value for FILE_FORMAT for copyinto object"
                            },
			"ON_ERROR": {
                                "type":"string",
                                "description":"user provided value for ON_ERROR for copyinto object"
                            },
			"SIZE_LIMIT": {
                                "type":"string",
                                "description":"user provided value for SIZE_LIMIT for copyinto object"
                            },
			"PURGE": {
                                "type":"string",
                                "description":"user provided value for PURGE for copyinto object"
                            },
			"RETURN_FAILED_ONLY": {
                                "type":"string",
                                "description":"user provided value for RETURN_FAILED_ONLY for copyinto object"
                            },
			"MATCH_BY_COLUMN_NAME": {
                                "type":"string",
                                "description":"user provided value for MATCH_BY_COLUMN_NAME for copyinto object"
                            },
			"INCLUDE_METADATA": {
                                "type":"string",
                                "description":"user provided value for INCLUDE_METADATA for copyinto object"
                            },
			"ENFORCE_LENGTH": {
                                "type":"string",
                                "description":"user provided value for ENFORCE_LENGTH for copyinto object"
                            },
			"TRUNCATECOLUMNS": {
                                "type":"string",
                                "description":"user provided value for TRUNCATECOLUMNS for copyinto object"
                            },
			"FORCE": {
                                "type":"string",
                                "description":"user provided value for FORCE for copyinto object"
                            },
			"LOAD_UNCERTAIN_FILES": {
                                "type":"string",
                                "description":"user provided value for LOAD_UNCERTAIN_FILES for copyinto object"
                            },
			"FILE_PROCESSOR": {
                                "type":"string",
                                "description":"user provided value for FILE_PROCESSOR for copyinto object"
                            },
			"LOAD_MODE": {
                                "type":"string",
                                "description":"user provided value for LOAD_MODE for copyinto object"
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
                "name":"create_task_object",
                "description":"creates a snowflake task object for the user. DATABASE, SCHEMA, NAME, SQL, WAREHOUSE are required parameters. ask user if they want to leverage the serverless compute of snowflake or they want to go with an existing warehouse. If they say existing warehouse then pass WAREHOUSE name else pass set WAREHOUSE to NONE. Recommend to create notification integration to alert if the task fails.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "DATABASE": {
                                "type":"string",
                                "description":"user provided value for DATABASE for task object"
                            },
			"SCHEMA": {
                                "type":"string",
                                "description":"user provided value for SCHEMA for task object"
                            },
			"NAME": {
                                "type":"string",
                                "description":"user provided value for NAME for task object"
                            },
			"SQL": {
                                "type":"string",
                                "description":"user provided value for SQL query for task object"
                            },
			"WAREHOUSE": {
                                "type":"string",
                                "description":"user provided value for WAREHOUSE for task object. ask user if they want to leverage the serverless compute of snowflake or they want to go with an existing warehouse. If they say existing warehouse then pass WAREHOUSE name else pass set WAREHOUSE to NONE"
                            },
			"USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE": {
                                "type":"string",
                                "description":"user provided value for USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE for task object"
                            },
			"SCHEDULE": {
                                "type":"string",
                                "description":"user provided value for SCHEDULE for task object"
                            },
			"CONFIG": {
                                "type":"string",
                                "description":"user provided value for CONFIG for task object"
                            },
			"ALLOW_OVERLAPPING_EXECUTION": {
                                "type":"string",
                                "description":"user provided value for ALLOW_OVERLAPPING_EXECUTION for task object"
                            },
			"USER_TASK_TIMEOUT_MS": {
                                "type":"string",
                                "description":"user provided value for USER_TASK_TIMEOUT_MS for task object"
                            },
			"SUSPEND_TASK_AFTER_NUM_FAILURES": {
                                "type":"string",
                                "description":"user provided value for SUSPEND_TASK_AFTER_NUM_FAILURES for task object"
                            },
			"ERROR_INTEGRATION": {
                                "type":"string",
                                "description":"user provided value for ERROR_INTEGRATION for task object"
                            },
			"SUCCESS_INTEGRATION": {
                                "type":"string",
                                "description":"user provided value for SUCCESS_INTEGRATION for task object"
                            },
			"COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for task object"
                            },
			"AFTER": {
                                "type":"string",
                                "description":"user provided value for AFTER for task object"
                            },
			"WHEN": {
                                "type":"string",
                                "description":"user provided value for WHEN for task object"
                            },
			"TAG": {
                                "type":"string",
                                "description":"user provided value for TAG for task object"
                            },
                        },
                        "FINALIZE": {
                                "type":"string",
                                "description":"user provided value for FINALIZE for task object"
                            },
                        "TASK_AUTO_RETRY_ATTEMPTS": {
                                "type":"string",
                                "description":"user provided value for TASK_AUTO_RETRY_ATTEMPTS for task object"
                            },
                        "USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS": {
                                "type":"string",
                                "description":"user provided value for USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS for task object"
                            },
                        "SERVERLESS_TASK_MIN_STATEMENT_SIZE": {
                                "type":"string",
                                "description":"user provided value for SERVERLESS_TASK_MIN_STATEMENT_SIZE for task object"
                            },
                        "SERVERLESS_TASK_MAX_STATEMENT_SIZE": {
                                "type":"string",
                                "description":"user provided value for SERVERLESS_TASK_MAX_STATEMENT_SIZE for task object"
                            },
                        "required":[
                            "DATABASE","SCHEMA","NAME","SQL","WAREHOUSE"
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
                "description":"if user explicitly asks for initial setup with snowflake. such that user specifies it is their first time.",
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
                "name":"get_history_for_pipe",
                "description":"If user ask if the data was loaded in the table, or when was the data loaded. user wants to provide details of snowpipe that is linked to the table",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "pipe_db": {
                                "type":"string",
                                "description":"database for snowpipe object"
                            },
                            "pipe_schema": {
                                "type":"string",
                                "description":"schema for snowpipe object"
                            },
                            "pipe_name": {
                                "type":"string",
                                "description":"name for snowpipe object"
                            }
                        },
                        "required":[
                            "pipe_db","pipe_schema","pipe_name"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"get_history_for_table",
                "description":"If user ask if the data was loaded in the table, or when was the data loaded. if user wants to give the name of table and schema and db",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "table_db": {
                                "type":"string",
                                "description":"database for table object"
                            },
                            "table_schema": {
                                "type":"string",
                                "description":"schema for table object"
                            },
                            "table_name": {
                                "type":"string",
                                "description":"name for table object"
                            }
                        },
                        "required":[
                            "table_db","table_schema","table_name"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_stream_object",
                "description":"creates snowflake stream object for the user. DATABSE, SCHEMA, NAME, and TABLE_NAME are the required parameters",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "DATABASE": {
                                "type":"string",
                                "description":"DATABASE for stream object"
                            },
                            "SCHEMA": {
                                "type":"string",
                                "description":"SCHEMA for stream object"
                            },
                            "NAME": {
                                "type":"string",
                                "description":"NAME for stream object"
                            },
                            "TABLE_NAME": {
                                "type":"string",
                                "description":"TABLE for stream object"
                            },
                            "TAG": {
                                "type":"string",
                                "description":"TAG for stream object"
                            },
                            "AT": {
                                "type":"string",
                                "description":"AT value for stream object"
                            },
                            "APPEND_ONLY": {
                                "type":"string",
                                "description":"APPEND_ONLY value for stream object"
                            },
                            "INSERT_ONLY": {
                                "type":"string",
                                "description":"INSERT_ONLY value for stream object"
                            },
                            "SHOW_INITIAL_ROWS": {
                                "type":"string",
                                "description":"SHOW_INITIAL_ROWS for stream object"
                            },
                            "COMMENT": {
                                "type":"string",
                                "description":"COMMENT for stream object"
                            }
                        },
                        "required":[
                            "DATABSE","SCHEMA","NAME","TABLE_NAME"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_alert_object",
                "description":"creates snowflake alert object for the user. NAME and SCHEDULE are the required parameters. depends on notification object. notification object has to be created before creating alert object.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "NAME": {
                                "type":"string",
                                "description":"NAME for alert object"
                            },
                            "SCHEDULE": {
                                "type":"string",
                                "description":"SCHEDULE for alert object"
                            },
                            "IF": {
                                "type":"string",
                                "description":"SQL query for alert object"
                            },
                            "THEN": {
                                "type":"string",
                                "description":"NOTIFICATION object name for alert object"
                            },
                            "WAREHOUSE": {
                                "type":"string",
                                "description":"WAREHOUSE for alert object"
                            },
                            "COMMENT": {
                                "type":"string",
                                "description":"COMMENT for alert object"
                            }
                        },
                        "required":[
                            "NAME","SCHEDULE","IF","THEN"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_notification_object",
                "description":"creates snowflake notification integration object for the user. NAME and ENABLED are the required parameters.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "NAME": {
                                "type":"string",
                                "description":"NAME for notification object"
                            },
                            "ENABLED": {
                                "type":"string",
                                "description":"ENABLED value for notification object"
                            },
                            "TYPE": {
                                "type":"string",
                                "description":"TYPE value for notification object"
                            },
                            "ALLOWED_RECIPIENTS": {
                                "type":"string",
                                "description":"ALLOWED_RECIPIENTS value for notification object"
                            },
                            "DEFAULT_RECIPIENTS": {
                                "type":"string",
                                "description":"DEFAULT_RECIPIENTS value for notification object"
                            },
                            "DEFAULT_SUBJECT": {
                                "type":"string",
                                "description":"DEFAULT_SUBJECT value for notification object"
                            },
                            "COMMENT": {
                                "type":"string",
                                "description":"COMMENT for notification object"
                            }
                        },
                        "required":[
                            "NAME","ENABLED"
                        ]
                    }
                }
            }
        }
    ]
}