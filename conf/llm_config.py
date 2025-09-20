import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
from src.utils import helper

ACCESS_KEY = 'AKIARSK3TK3YS2J5WLVZ' #'AKIAUMYCH7Z6CF4OQXJT'
SECRET_KEY = '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' #'ys7JM4BClYXWTpjzOv1C2aGZbIMltlHu9UJsq/oY'

TEMPERATURE = 0
REGION = 'us-west-2'
BEDROCK_RUNTIME_SERVICE = 'bedrock-runtime'
CHAT_MODEL_ID = 'us.anthropic.claude-3-7-sonnet-20250219-v1:0'#'global.anthropic.claude-sonnet-4-20250514-v1:0'#'us.anthropic.claude-3-5-sonnet-20241022-v2:0'#'anthropic.claude-3-5-sonnet-20241022-v2:0'#anthropic.claude-3-haiku-20240307-v1:0' #'anthropic.claude-3-sonnet-20240229-v1:0' #'us.anthropic.claude-3-7-sonnet-20250219-v1:0'
KB_MODEL_ID = 'us.anthropic.claude-3-7-sonnet-20250219-v1:0'#'global.anthropic.claude-sonnet-4-20250514-v1:0'#'us.anthropic.claude-3-5-sonnet-20241022-v2:0'#'anthropic.claude-3-5-sonnet-20241022-v2:0'#'anthropic.claude-3-haiku-20240307-v1:0' #'us.anthropic.claude-3-7-sonnet-20250219-v1:0'
EMBEDDINGS_MODEL_ID = 'amazon.titan-embed-text-v1'

ALLOWED_OBJS = helper.get_obj_names()

tools = {
    "tools": [
        {
            "toolSpec": {
                "name":"create_database_object",
                "description":"Use this tool to create a database. NAME is a required input to be taken from user, other values are NONE if not provided by the user. Only use user provided inputs",
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
                                "description":"user provided value for REPLACE_INVALID_CHARACTERS for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "DATA_RETENTION_TIME_IN_DAYS": {
                                "type":"string",
                                "description":"user provided value for DATA_RETENTION_TIME_IN_DAYS for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "MAX_DATA_EXTENSION_TIME_IN_DAYS": {
                                "type":"string",
                                "description":"user provided value for MAX_DATA_EXTENSION_TIME_IN_DAYS for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "EXTERNAL_VOLUME": {
                                "type":"string",
                                "description":"user provided value for EXTERNAL_VOLUME for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "CATALOG": {
                                "type":"string",
                                "description":"user provided value for CATALOG for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "DEFAULT_DDL_COLLATION": {
                                "type":"string",
                                "description":"user provided value for DEFAULT_DDL_COLLATION for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "STORAGE_SERIALIZATION_POLICY": {
                                "type":"string",
                                "description":"user provided value for STORAGE_SERIALIZATION_POLICY for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "LOG_LEVEL": {
                                "type":"string",
                                "description":"user provided value for LOG_LEVEL for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "TRACE_LEVEL": {
                                "type":"string",
                                "description":"user provided value for TRACE_LEVEL for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            }
                        },
                        "required":[
                            "NAME"
                        ]
                    }
                }
            },
        "toolSpec": {
                "name":"create_stored_procedure_object",
                "description":"creates a  stored procedure object for the user. DATABASE, SCHEMA, NAME, LOGIC, RETURN_TYPE, LANGUAGE, HANDLER, PACKAGES is a required input to be taken from user. Only use user provided inputs",
                "inputSchema": {
                    "json":{   
                        "type":"object",
                        "properties": {
                            "DATABASE": {
                                "type":"string",
                                "description":"user to provide value for DATABASE for stored procedure object."
                            },
                            "SCHEMA": {
                                "type":"string",
                                "description":"user provided value for SCHEMA for stored procedure object"
                            },
                        "NAME": {
                                "type":"string",
                                "description":"user provided value for NAME for stored procedure object"
                            },
                        "LOGIC": {
                                "type":"string",
                                "description":"user provided value for LOGIC for stored procedure object. This would be the script that user wants to be executed inside the sproc."
                            },
                        "RETURN_TYPE": {
                                "type":"string",
                                "description":"user provided value for RETURN_TYPE for stored procedure object. This would be the return type of the value that sproc would return"
                            },
                        "LANGUAGE": {
                                "type":"string",
                                "description":"user provided value for LANGUAGE for stored procedure object. This would be the language that the sproc would be in. Pytho,Java,Javascript,Scala or SQL"
                            },
                        "HANDLER": {
                                "type":"string",
                                "description":"user provided value for HANDLER for stored procedure object. This would be the entry point of sproc."
                            },
                        "PACKAGES": {
                                "type":"string",
                                "description":"user provided value for PACKAGES for stored procedure object. This would be packages to be imported if any.(Should be passed as a tuple each value enclosed in single quotes and separated by comma)"
                            },
                        },
                        "required":[
                            "DATABASE","SCHEMA","NAME","LOGIC","RETURN_TYPE","LANGUAGE","HANDLER","PACKAGES"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_externalstage_object",
                "description":"creates a snowflake external stage object for the user. NAME, DATABASE, SCHEMA, URL, STORAGE_INTEGRATION are required inputs to be taken from user. Only use user provided inputs, DO NOT assume values.  DO NOT use the generic s3://your-bucket-name/path/. user needs to provide with the url path. While fileformat is not required, recommend creating file format to save rework in the future.",
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
                                "description":"user provided value for FILE_FORMAT for external stage object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "URL": {
                                "type":"string",
                                "description":"user provided value for URL for external stage object. DO NOT ASSUME VALUE. ask user explicitly for the URL. DO NOT use the generic s3://your-bucket-name/path/. user needs to provide with the url path."
                            },
                        "AWS_ACCESS_POINT_ARN": {
                                "type":"string",
                                "description":"user provided value for AWS ACCESS POINT ARN for external stage object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "STORAGE_INTEGRATION": {
                                "type":"string",
                                "description":"user provided value for STORAGE_INTEGRATION for external stage object.E"
                            },
                        
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for external stage object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "ENCRYPTION_TYPE": {
                                "type":"string",
                                "description":"user provided value for ENCRYPTION_TYPE for external stage object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "ENCRYPTION_MASTER_KEY": {
                                "type":"string",
                                "description":"user provided value for ENCRYPTION_MASTER_KEY for external stage object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "ENCRYPTION_KMS_KEY_ID": {
                                "type":"string",
                                "description":"user provided value for ENCRYPTION_KMS_KEY_ID for external stage object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "USE_PRIVATELINK_ENDPOINT": {
                                "type":"string",
                                "description":"user provided value for USE_PRIVATELINK_ENDPOINT for external stage object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "ENABLE": {
                                "type":"string",
                                "description":"user provided value for DIRECTORY for external stage object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "REFRESH_ON_CREATE": {
                                "type":"string",
                                "description":"user provided value for REFRESH_ON_CREATE for external stage object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "AUTO_REFRESH": {
                                "type":"string",
                                "description":"user provided value for AUTO_REFRESH for external stage object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "NOTIFICATION_INTEGRATION": {
                                "type":"string",
                                "description":"user provided value for NOTIFICATION_INTEGRATION for external stage object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        },
                        "required":[
                            "NAME","DATABASE","SCHEMA","URL","STORAGE_INTEGRATION"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_fileformat_object",
                "description":"creates a snowflake fileformat object for the user. DATABASE, SCHEMA, NAME is a required input to be taken from user. Only use user provided inputs. Do not refer snowflake documentation for attributes.",
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
                            "NAME": {
                                "type":"string",
                                "description":"user provided name for FILE_FORMAT for file format object"
                            },
                            "MULTI_LINE": {
                                "type":"string",
                                "description":"user provided value for MULTI_LINE for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "TYPE": {
                                "type":"string",
                                "description":"user provided value for TYPE for file format object. if value is not provided by user, DEFAULT value is set to CSV"
                            },
                        "PARSE_HEADER": {
                                "type":"string",
                                "description":"user provided value for PARSE_HEADER for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "SKIP_HEADER": {
                                "type":"string",
                                "description":"user provided value for SKIP_HEADER for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "SKIP_BLANK_LINES": {
                                "type":"string",
                                "description":"user provided value for SKIP_BLANK_LINES for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "DATE_FORMAT": {
                                "type":"string",
                                "description":"user provided value for DATE_FORMAT for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "TIME_FORMAT": {
                                "type":"string",
                                "description":"user provided value for TIME_FORMAT for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "TIMESTAMP_FORMAT": {
                                "type":"string",
                                "description":"user provided value for TIMESTAMP_FORMAT for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "BINARY_FORMAT": {
                                "type":"string",
                                "description":"user provided value for BINARY_FORMAT for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "ESCAPE": {
                                "type":"string",
                                "description":"user provided value for ESCAPE for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "ESCAPE_UNENCLOSED_FIELD": {
                                "type":"string",
                                "description":"user provided value for ESCAPE_UNENCLOSED_FIELD for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "TRIM_SPACE": {
                                "type":"string",
                                "description":"user provided value for TRIM_SPACE for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "FIELD_OPTIONALLY_ENCLOSED_BY": {
                                "type":"string",
                                "description":"user provided value for FIELD_OPTIONALLY_ENCLOSED_BY for file format object.If user does not provide a value then default value is NONE. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "NULL_IF": {
                                "type":"string",
                                "description":"user provided value for NULL_IF for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "ERROR_ON_COLUMN_COUNT_MISMATCH": {
                                "type":"string",
                                "description":"user provided value for ERROR_ON_COLUMN_COUNT_MISMATCH for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "REPLACE_INVALID_CHARACTERS": {
                                "type":"string",
                                "description":"user provided value for REPLACE_INVALID_CHARACTERS for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "EMPTY_FIELD_AS_NULL": {
                                "type":"string",
                                "description":"user provided value for EMPTY_FIELD_AS_NULL for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "SKIP_BYTE_ORDER_MARK": {
                                "type":"string",
                                "description":"user provided value for SKIP_BYTE_ORDER_MARK for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "ENCODING": {
                                "type":"string",
                                "description":"user provided value for ENCODING for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "ENABLE_OCTAL": {
                                "type":"string",
                                "description":"user provided value for ENABLE_OCTAL for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "ALLOW_DUPLICATE": {
                                "type":"string",
                                "description":"user provided value for ALLOW_DUPLICATE for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "STRIP_OUTER_ARRAY": {
                                "type":"string",
                                "description":"user provided value for STRIP_OUTER_ARRAY for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "STRIP_NULL_VALUES": {
                                "type":"string",
                                "description":"user provided value for STRIP_NULL_VALUES for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "IGNORE_UTF8_ERRORS": {
                                "type":"string",
                                "description":"user provided value for IGNORE_UTF8_ERRORS for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "SNAPPY_COMPRESSION": {
                                "type":"string",
                                "description":"user provided value for SNAPPY_COMPRESSION for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "BINARY_AS_TEXT": {
                                "type":"string",
                                "description":"user provided value for BINARY_AS_TEXT for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "USE_LOGICAL_TYPE": {
                                "type":"string",
                                "description":"user provided value for USE_LOGICAL_TYPE for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "USE_VECTORIZED_SCANNER": {
                                "type":"string",
                                "description":"user provided value for USE_VECTORIZED_SCANNER for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "PRESERVE_SPACE": {
                                "type":"string",
                                "description":"user provided value for PRESERVE_SPACE for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "STRIP_OUTER_ELEMENT": {
                                "type":"string",
                                "description":"user provided value for STRIP_OUTER_ELEMENT for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "DISABLE_SNOWFLAKE_DATA": {
                                "type":"string",
                                "description":"user provided value for DISABLE_SNOWFLAKE_DATA for file format object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "DISABLE_AUTO_CONVERT": {
                                "type":"string",
                                "description":"user provided value for DISABLE_AUTO_CONVERT for file format object. if value is not provided by user, DEFAULT value is set to NONE"
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
                                "description":"user provided value for SCHEMA for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "NAME": {
                                "type":"string",
                                "description":"user provided value for NAME for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "FILE_FORMAT": {
                                "type":"string",
                                "description":"user provided value for FILE_FORMAT for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "TAG": {
                                "type":"string",
                                "description":"user provided value for TAG for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "ENCRYPTION": {
                                "type":"string",
                                "description":"user provided value for ENCRYPTION for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "DIRECTORY": {
                                "type":"string",
                                "description":"user provided value for DIRECTORY for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "REFRESH_ON_CREATE": {
                                "type":"string",
                                "description":"user provided value for REFRESH_ON_CREATE for database object. if value is not provided by user, DEFAULT value is set to NONE"
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
                                "description":"user provided value for NAME for resource monitor object"
                            },
                        "CREDIT_QUOTA": {
                                "type":"string",
                                "description":"user provided value for CREDIT_QOUTA for resource monitor object. if value is not provided by user, DEFAULT value is set to 75"
                            },
                        "FREQUENCY": {
                                "type":"string",
                                "description":"user provided value for FREQUENCY for resource monitor object. if value is not provided by user, DEFAULT value is set to DAILY"
                            },
                        "START_TIMESTAMP": {
                                "type":"string",
                                "description":"user provided value for START_TIMESTAMP for resource monitor object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "END_TIMESTAMP": {
                                "type":"string",
                                "description":"user provided value for END_TIMESTAMP for resource monitor object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "NOTIFY_USERS": {
                                "type":"string",
                                "description":"user provided value for NOTIFY_USERS for resource monitor object. if value is not provided by user, DEFAULT value is set to ADMIN"
                            },
                        "TRIGGERS": {
                                "type":"string",
                                "description":"user provided value for TRIGGERS for resource monitor object.  ask user if they want to setup single action or multiple based on which values passed should be either 'SINGLE' or 'MULTIPLE' or NONE"
                            },
                        "THRESHOLD": {
                                "type":"string",
                                "description":"user provided value for THRESHOLD for resource monitor object. If TRIGGERS parameter value is 'MULTIPLE', sets list of numbers having threshold values for each action. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "ACTION": {
                                "type":"string",
                                "description":"user provided value for ACTION for resource monitor object. list of actions to be taken against each THRESHOLD. List can only be [SUSPEND, SUSPEND_IMMEDIATE, NOTIFY]"
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
                                "description":"user provided value for COMMENT for database object. if value is not provided by user, DEFAULT value is set to NONE"
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
                "name":"transfer_tables_across_stage",
                "description":"performs a data load (transfer or deployment) of tables from one stage to another",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "SRC_DATABASE": {
                                "type":"string",
                                "description":"user provided value for source database"
                            },
                            "SRC_SCHEMA": {
                                "type":"string",
                                "description":"user provided value for source schema"
                            },
                            "SRC_TABLE": {
                                "type":"string",
                                "description":"user provided value for source table"
                            },
                            "TGT_DATABASE": {
                                "type":"string",
                                "description":"user provided value for target database"
                            },
                            "TGT_SCHEMA": {
                                "type":"string",
                                "description":"user provided value for target schema"
                            },
                            "TGT_TABLE": {
                                "type":"string",
                                "description":"user provided value for target table"
                            },
                            
                        },
                        "required":[
                            "SRC_DATABASE", "SRC_SCHEMA", "SRC_TABLE", "TGT_DATABASE", "TGT_SCHEMA", "TGT_TABLE"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_cortex_search_object",
                "description":"creates a cortex search object for snowflake",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "ON": {
                                "type":"string",
                                "description":"user provided value for the base table name that you wish to search on."
                            },
                            "ATTRIBUTES": {
                                "type":"string",
                                "description":"comma-separated list of columns in the base table that you wish to filter on when issuing queries to the service."
                            },
                            "WAREHOUSE": {
                                "type":"string",
                                "description":"warehouse to use for running the source query, building the search index, and keeping it refreshed per the TARGET_LAG target."
                            },
                            "TARGET_LAG": {
                                "type":"string",
                                "description":"Specifies the maximum amount of time that the Cortex Search service content should lag behind updates to the base tables specified in the source query."
                            },
                            "EXTERNAL_VOLUME": {
                                "type":"string",
                                "description":"user provided value for external volume"
                            },
                            "EMBEDDING_MODEL": {
                                "type":"string",
                                "description":"user provided value for embedding model"
                            },
                            "INITIALIZE": {
                                "type":"string",
                                "description":"user provided value for the behavior of the initial refresh of the Cortex Search Service"
                            },
                            "QUERY": {
                                "type":"string",
                                "description":"user provided value for query"
                            },
                            
                        },
                        "required":[
                            "ON","ATTRIBUTES","WAREHOUSE","TARGET_LAG","EXTERNAL_VOLUME","EMBEDDING_MODEL","INITIALIZE","QUERY"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_schema_object",
                "description":"Use this tool to create Schema.DATABASE and NAME are required inputs to be taken from user. Only use user provided inputs",
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
                                "description":"user provided value for WITH_MANAGED_ACCESS for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "DATA_RETENTION_TIME_IN_DAYS": {
                                "type":"string",
                                "description":"user provided value for DATA_RETENTION_TIME_IN_DAYS for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "MAX_DATA_EXTENSION_TIME_IN_DAYS": {
                                "type":"string",
                                "description":"user provided value for MAX_DATA_EXTENSION_TIME_IN_DAYS for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "EXTERNAL_VOLUME": {
                                "type":"string",
                                "description":"user provided value for EXTERNAL_VOLUME for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "CATALOG": {
                                "type":"string",
                                "description":"user provided value for CATALOG for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "REPLACE_INVALID_CHARACTERS": {
                                "type":"string",
                                "description":"user provided value for REPLACE_INVALID_CHARACTERS for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "DEFAULT_DDL_COLLATION": {
                                "type":"string",
                                "description":"user provided value for DEFAULT_DDL_COLLATION for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "LOG_LEVEL": {
                                "type":"string",
                                "description":"user provided value for LOG_LEVEL for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "TRACE_LEVEL": {
                                "type":"string",
                                "description":"user provided value for TRACE_LEVEL for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "STORAGE_SERIALIZATION_POLICY": {
                                "type":"string",
                                "description":"user provided value for STORAGE_SERIALIZATION_POLICY for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "CLASSIFICATION_PROFILE": {
                                "type":"string",
                                "description":"user provided value for CLASSIFICATION_PROFILE for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object. if value is not provided by user, DEFAULT value is set to NONE"
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
                                "description":"user provided value for LOGIN_NAME for database object. if value is not provided by user, DEFAULT value is set to DEFAULT"
                            },
                        "DISPLAY_NAME": {
                                "type":"string",
                                "description":"user provided value for DISPLAY_NAME for database object. if value is not provided by user, DEFAULT value is set to PERSON"
                            },
                        "FIRST_NAME": {
                                "type":"string",
                                "description":"user provided value for FIRST_NAME for database object. if value is not provided by user, DEFAULT value is set to DEFAULT"
                            },
                        "LAST_NAME": {
                                "type":"string",
                                "description":"user provided value for LAST_NAME for database object. if value is not provided by user, DEFAULT value is set to DEFAULT"
                            },
                        "EMAIL": {
                                "type":"string",
                                "description":"user provided value for EMAIL for database object. if value is not provided by user, DEFAULT value is set to DEFAULT"
                            },
                        "MUST_CHANGE_PASSWORD": {
                                "type":"string",
                                "description":"user provided value for MUST_CHANGE_PASSWORD for database object. if value is not provided by user, DEFAULT value is set to TRUE"
                            },
                        "DISABLED": {
                                "type":"string",
                                "description":"user provided value for DISABLED for database object. if value is not provided by user, DEFAULT value is set to FALSE"
                            },
                        "DAYS_TO_EXPIRY": {
                                "type":"string",
                                "description":"user provided value for DAYS_TO_EXPIRY for database object. if value is not provided by user, DEFAULT value is set to 20"
                            },
                        "MINS_TO_UNLOCK": {
                                "type":"string",
                                "description":"user provided value for MINS_TO_UNLOCK for database object. if value is not provided by user, DEFAULT value is set to 20"
                            },
                        "DEFAULT_WAREHOUSE": {
                                "type":"string",
                                "description":"user provided value for DEFAULT_WAREHOUSE for database object. if value is not provided by user, DEFAULT value is set to DEFAULT"
                            },
                        "DEAFULT_ROLE": {
                                "type":"string",
                                "description":"user provided value for DEFAULT_ROLE for database object. if value is not provided by user, DEFAULT value is set to DEFAULT"
                            },
                        "DEFAULT_SECONDARY_ROLES": {
                                "type":"string",
                                "description":"user provided value for DEFAULT_SECONDARY_ROLES for database object. if value is not provided by user, DEFAULT value is set to ALL"
                            },
                        "MINS_TO_BY_PASS_MFA": {
                                "type":"string",
                                "description":"user provided value for MINS_TO_BY_PASS_MFA for database object. if value is not provided by user, DEFAULT value is set to 20"
                            },
                        "RSA_PUBLIC_KEY": {
                                "type":"string",
                                "description":"user provided value for RSA_PUBLIC_KEY for database object. if value is not provided by user, DEFAULT value is set to DEFAULT"
                            },
                        "RSA_PUBLIC_KEY_FP": {
                                "type":"string",
                                "description":"user provided value for RSA_PUBLIC_KEY_FP for database object. if value is not provided by user, DEFAULT value is set to DEFAULT"
                            },
                        "RSA_PUBLIC_KEY_2": {
                                "type":"string",
                                "description":"user provided value for RSA_PUBLIC_KEY_2 for database object. if value is not provided by user, DEFAULT value is set to KEY2"
                            },
                        "RSA_PUBLIC_KEY_2_FP": {
                                "type":"string",
                                "description":"user provided value for RSA_PUBLIC_KEY_2_FP for database object. if value is not provided by user, DEFAULT value is set to DEFAULT"
                            },
                        "TYPE": {
                                "type":"string",
                                "description":"user provided value for TYPE for database object. if value is not provided by user, DEFAULT value is set to PERSON"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object. if value is not provided by user, DEFAULT value is set to DEFAULT"
                            },
                        "ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR": {
                                "type":"string",
                                "description":"user provided value for ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR for database object. if value is not provided by user, DEFAULT value is set to TRUE"
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
                                "description":"user provided value for WAREHOUSE_SIZE for database object. if value is not provided by user, DEFAULT value is set to SMALL"
                            },
                        "WAREHOUSE_TYPE": {
                                "type":"string",
                                "description":"user provided value for WAREHOUSE_TYPE for database object. if value is not provided by user, DEFAULT value is set to STANDARD"
                            },
                        "RESOURCE_CONSTRAINT": {
                                "type":"string",
                                "description":"user provided value for RESOURCE_CONSTRAINT for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "MAX_CLUSTER_COUNT": {
                                "type":"string",
                                "description":"user provided value for MAX_CLUSTER_COUNT for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "MIN_CLUSTER_COUNT": {
                                "type":"string",
                                "description":"user provided value for MIN_CLUSTER_COUNT for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "SCALING_POLICY": {
                                "type":"string",
                                "description":"user provided value for SCALING_POLICY for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "AUTO_SUSPEND": {
                                "type":"string",
                                "description":"user provided value for AUTO_SUSPEND for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "AUTO_RESUME": {
                                "type":"string",
                                "description":"user provided value for AUTO_RESUME for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "INITIALLY_SUSPENDED": {
                                "type":"string",
                                "description":"user provided value for INTITIALLY_SUSPENDED for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "RESOURCE_MONITOR": {
                                "type":"string",
                                "description":"user provided value for RESOURCE_MONITOR for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "TAG": {
                                "type":"string",
                                "description":"user provided value for TAG for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "ENABLE_QUERY_ACCELERATION": {
                                "type":"string",
                                "description":"user provided value for ENABLE_QUERY_ACCELERATION for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "QUERY_ACCELERATION_MAX_SCALE_FACTOR": {
                                "type":"string",
                                "description":"user provided value for QUERY_ACCELERATION_MAX_SCALE_FACTOR for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "MAX_CONCURRENCY_LEVEL": {
                                "type":"string",
                                "description":"user provided value for MAX_CONCURRENCY_LEVEL for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "STATEMENT_QUEUED_TIMEOUT_IN_SECONDS": {
                                "type":"string",
                                "description":"user provided value for STATEMENT_QUEUED_TIMEOUT_IN_SECONDS for database object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "STATEMENT_TIMEOUT_IN_SECONDS": {
                                "type":"string",
                                "description":"user provided value for STATEMENT_TIMEOUT_IN_SECONDS for database object. if value is not provided by user, DEFAULT value is set to NONE"
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
                "name":"create_table_object",
                "description":"creates snowflake table object for the user. database and schema are required inputs. tables csv and names are already provided, you need not ask user for this.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "database": {
                                "type":"string",
                                "description":"database name for table object"
                            },
                            "schema": {
                                "type":"string",
                                "description":"schema name for table object"
                            }
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
                "name":"create_storage_integration_object",
                "description":"creates storage integration object for the user. NAME, ENABLED, and STORAGE_PROVIDER are required inputs from user.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "NAME": {
                                "type":"string",
                                "description":"user provided NAME for storage integration object"
                            },
                            "ENABLED": {
                                "type":"string",
                                "description":"user provided ENABLED for storage integration object"
                            },
                            "STORAGE_PROVIDER": {
                                "type":"string",
                                "description":"user provided STORAGE_PROVIDER for storage integration object"
                            },
                            "TYPE": {
                                "type":"string",
                                "description":"user provided TYPE for storage integration object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "STORAGE_ALLOWED_LOCATIONS": {
                                "type":"string",
                                "description":"user provided STORAGE_ALLOWED_LOCATIONS for storage integration object. should be passed as a list with each value enclosed in single quote, example: STORAGE_ALLOWED_LOCATIONS=['val1','val2']"
                            },
                            "STORAGE_BLOCKED_LOCATIONS": {
                                "type":"string",
                                "description":"user provided STORAGE_BLOCKED_LOCATIONS for storage integration object. should be passed as a list with each value enclosed in single quote, example: STORAGE_BLOCKED_LOCATIONS=['val1','val2']"
                            },
                            "STORAGE_AWS_ROLE_ARN": {
                                "type":"string",
                                "description":"user provided STORAGE_AWS_ROLE_ARN for storage integration object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "STORAGE_AWS_EXTERNAL_ID": {
                                "type":"string",
                                "description":"user provided STORAGE_AWS_EXTERNAL_ID for storage integration object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "STORAGE_AWS_OBJECT_ACL": {
                                "type":"string",
                                "description":"user provided STORAGE_AWS_OBJECT_ACL for storage integration object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "COMMENT": {
                                "type":"string",
                                "description":"user provided COMMENT for storage integration object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "AZURE_TENANT_ID": {
                                "type":"string",
                                "description":"user provided AZURE_TENANT_ID for storage integration object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "USE_PRIVATELINK_ENDPOINT": {
                                "type":"string",
                                "description":"user provided USE_PRIVATELINK_ENDPOINT for storage integration object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        },
                        "required":[
                            "NAME","ENABLED","STORAGE_PROVIDER"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_snowpipe_object",
                "description":"creates a snowpipe object for the user. After creating snowpipe, recommend user to create error integration which would alert them in case of failures in snowpipe.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "DATABASE": {
                                "type":"string",
                                "description":"user provided value for DATABASE for snowpipe object"
                            },
                			"SCHEMA": {
                                "type":"string",
                                "description":"user provided value for SCHEMA for snowpipe object"
                            },
                			"TABLE": {
                                "type":"string",
                                "description":"user provided list for TABLE names for snowpipe object"
                            },
                			"COPYINTO_QUERY": {
                                "type":"string",
                                "description":"user provided list for COPYINTO names for snowpipe object"
                            },
                			"AUTO_INGEST": {
                                "type":"string",
                                "description":"user provided value for AUTO_INGEST for snowpipe object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                			"ERROR_INTEGRATION": {
                                "type":"string",
                                "description":"user provided value for ERROR_INTEGRATION for snowpipe object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                			"AWS_SNS_TOPIC": {
                                "type":"string",
                                "description":"user provided value for AWS_SNS_TOPIC for snowpipe object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                			"INTEGRATION": {
                                "type":"string",
                                "description":"user provided value for INTEGRATION for snowpipe object. If user does not provide a value then default value is NONE."
                            },
                			"COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        },
                        "required":[
                            "DATABASE","SCHEMA","TABLE","COPYINTO_QUERY"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_copyinto_object",
                "description":"creates a snowflake copyinto object for the user. Do not use pattern attribute and on_error attribute.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "SCANNER": {
                                "type":"string",
                                "description":"user provided value for SCANNER for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "PROJECT_NAME": {
                                "type":"string",
                                "description":"user provided value for PROJECT_NAME for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "MODEL_NAME": {
                                "type":"string",
                                "description":"user provided value for MODEL_NAME for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "MODEL_VERSION": {
                                "type":"string",
                                "description":"user provided value for MODEL_VERSION for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
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
                                "description":"user provided value for ON_ERROR for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"SIZE_LIMIT": {
                                "type":"string",
                                "description":"user provided value for SIZE_LIMIT for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"PURGE": {
                                "type":"string",
                                "description":"user provided value for PURGE for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"RETURN_FAILED_ONLY": {
                                "type":"string",
                                "description":"user provided value for RETURN_FAILED_ONLY for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"MATCH_BY_COLUMN_NAME": {
                                "type":"string",
                                "description":"user provided value for MATCH_BY_COLUMN_NAME for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"INCLUDE_METADATA": {
                                "type":"string",
                                "description":"user provided value for INCLUDE_METADATA for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"ENFORCE_LENGTH": {
                                "type":"string",
                                "description":"user provided value for ENFORCE_LENGTH for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"TRUNCATECOLUMNS": {
                                "type":"string",
                                "description":"user provided value for TRUNCATECOLUMNS for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"FORCE": {
                                "type":"string",
                                "description":"user provided value for FORCE for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"LOAD_UNCERTAIN_FILES": {
                                "type":"string",
                                "description":"user provided value for LOAD_UNCERTAIN_FILES for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"FILE_PROCESSOR": {
                                "type":"string",
                                "description":"user provided value for FILE_PROCESSOR for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"LOAD_MODE": {
                                "type":"string",
                                "description":"user provided value for LOAD_MODE for copyinto object. if value is not provided by user, DEFAULT value is set to NONE"
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
                "description":"creates a snowflake task object for the user. DATABASE, SCHEMA, NAME, SQL, WAREHOUSE are required parameters. ask user if they want to leverage the serverless compute of snowflake or they want to go with an existing warehouse. If they say existing warehouse then pass WAREHOUSE name else pass set WAREHOUSE to NONE. Recommend to create notification integration to alert if the task fails. While creating a task we need to know if the task is going to be using a WAREHOUSE or SERVERLESS COMPUTE (USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE parameter) of Snowflake.",
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
                                "description":"user provided value for USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE for task object. Specifies the size of the compute resources to provision for the first run of the task, before a task history is available for Snowflake to determine an ideal size. Once a task has successfully completed a few runs, Snowflake ignores this parameter setting. Snowchain for now will use MEDIUM by default for this param."
                            },
			"SCHEDULE": {
                                "type":"string",
                                "description":"user provided value for SCHEDULE for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"CONFIG": {
                                "type":"string",
                                "description":"user provided value for CONFIG for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"ALLOW_OVERLAPPING_EXECUTION": {
                                "type":"string",
                                "description":"user provided value for ALLOW_OVERLAPPING_EXECUTION for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"USER_TASK_TIMEOUT_MS": {
                                "type":"string",
                                "description":"user provided value for USER_TASK_TIMEOUT_MS for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"SUSPEND_TASK_AFTER_NUM_FAILURES": {
                                "type":"string",
                                "description":"user provided value for SUSPEND_TASK_AFTER_NUM_FAILURES for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"ERROR_INTEGRATION": {
                                "type":"string",
                                "description":"user provided value for ERROR_INTEGRATION for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"SUCCESS_INTEGRATION": {
                                "type":"string",
                                "description":"user provided value for SUCCESS_INTEGRATION for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"COMMENT": {
                                "type":"string",
                                "description":"user provided value for COMMENT for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"AFTER": {
                                "type":"string",
                                "description":"user provided value for AFTER for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"WHEN": {
                                "type":"string",
                                "description":"user provided value for WHEN for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
			"TAG": {
                                "type":"string",
                                "description":"user provided value for TAG for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        },
                        "FINALIZE": {
                                "type":"string",
                                "description":"user provided value for FINALIZE for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "TASK_AUTO_RETRY_ATTEMPTS": {
                                "type":"string",
                                "description":"user provided value for TASK_AUTO_RETRY_ATTEMPTS for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS": {
                                "type":"string",
                                "description":"user provided value for USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "SERVERLESS_TASK_MIN_STATEMENT_SIZE": {
                                "type":"string",
                                "description":"user provided value for SERVERLESS_TASK_MIN_STATEMENT_SIZE for task object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                        "SERVERLESS_TASK_MAX_STATEMENT_SIZE": {
                                "type":"string",
                                "description":"user provided value for SERVERLESS_TASK_MAX_STATEMENT_SIZE for task object. if value is not provided by user, DEFAULT value is set to NONE"
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
                "description":"creates snowflake stream object for the user. Streams can only be created for one of the following objects: Table, External Table, Views, DIRECTORY TABLE/Stage. DATABASE, SCHEMA, NAME, and TABLE_NAME are the required parameters. Inform user that Streams by default would start CDC from the moment they are created OR AT a specific point in time if they want OR BEFORE a specific point in time.",
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
                                "description":"TAG for stream object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "AT": {
                                "type":"string",
                                "description":"AT value for stream object. User can provide any one of the following: TIMESTAMP (timestamp at which they want it to start CDC), OFFSET (time difference from the current time at which they want CDC to start, the user should tell us how many minutes ago from now.), STATEMENT (query id of the query they want to use as a starting point not supported by SNOWCHAIN for now), STREAM (name of the stream NOT SUPPORTED by Snowchain right now)."
                            },
                            "APPEND_ONLY": {
                                "type":"string",
                                "description":"APPEND_ONLY value for stream object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "INSERT_ONLY": {
                                "type":"string",
                                "description":"INSERT_ONLY value for stream object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "SHOW_INITIAL_ROWS": {
                                "type":"string",
                                "description":"SHOW_INITIAL_ROWS for stream object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "COMMENT": {
                                "type":"string",
                                "description":"COMMENT for stream object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "BEFORE": {
                                "type":"string",
                                "description":"BEFORE for stream object. Allowed values are TIMESTAMP (timestamp at which they want it to start CDC), OFFSET (time difference from the current time at which they want CDC to start the user should tell us how many minutes ago from now.), STATEMENT (query id of the query they want to use as a starting point)"
                            },
                            "TIMESTAMP": {
                                "type":"string",
                                "description":"TIMESTAMP for stream object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "OFFSET": {
                                "type":"string",
                                "description":"OFFSET for stream object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "STATEMENT": {
                                "type":"string",
                                "description":"STATEMENT for stream object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "OBJECT_TYPE": {
                                "type":"string",
                                "description":"OBJECT TYPE for stream object. Possible values: TABLE, EXTERNAL TABLE, STAGE (If user says Directory table OR Stage, STAGE to be passed in both cases.), and VIEW"
                            },
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
                "description":"creates snowflake alert object for the user. NAME, SCHEDULE, DATABASE, and SCHEMA are the required parameters. depends on notification object. notification object has to be created before creating alert object. If user does not provide WAREHOUSE, Snowflake's serverless compute would be utilized.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "NAME": {
                                "type":"string",
                                "description":"NAME for alert object"
                            },
                            "CONDITION": {
                                "type":"string",
                                "description":"CONDITION for alert object. If CONDITION returns one or more rows then ACTION would be taken. Options for CONDITION are: SELECT statement, SHOW Objects, Stored procedure. If user wants a custom stored procedure to be used then they have to provide the definition of stored proc for example SP_CUSTOM_SPROC('VAR1','VAR2'). if they want to use SHOW Objects then they need to specify object name. if they want to use SELECT statement, there are two options Frosty can write a query for them if they describe the problem (and then pass it to create_object), or they can provide the select statement. This should be passed as a value to IF parameter. For select pass the select sql statement 'STATEMENT'. For show objects pass 'SHOW object name', For stored proc pass 'CALL SP_CUSTOM_SPROC('VAR1','VAR2')'"
                            },
                            "ACTION": {
                                "type":"string",
                                "description":"ACTION for alert object. For ACTION, if User wants to provide custom SQL or Wants to send out emails using notification integration email. (If they have existing one use it else follow the flow where we take them to create one.). If they are using notification integration, then we need integration_name, email_addresses, email_subject, email_content. This should be passed as a value to THEN parameter. For custom SQL pass sql: 'custom sql', pass all other params i.e integration_name, email_address, email_subject, email_content as NONE. For notification integration : pass sql:NONE, and values for integration_name, email_address, email_subject, email_content"
                            },
                            "ACTION_TYPE": {
                                "type":"string",
                                "description":"ACTION_TYPE for alert object"
                            },
                            "DATABASE": {
                                "type":"string",
                                "description":"DATABASE for alert object"
                            },
                            "SCHEMA": {
                                "type":"string",
                                "description":"SCHEMA for alert object"
                            },
                            "SCHEDULE": {
                                "type":"string",
                                "description":"SCHEDULE for alert object"
                            },
                            "IF": {
                                "type":"string",
                                "description":"SQL query for alert object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "THEN": {
                                "type":"string",
                                "description":"NOTIFICATION object name for alert object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "WAREHOUSE": {
                                "type":"string",
                                "description":"WAREHOUSE for alert object. If user does not provide WAREHOUSE, Snowflake's serverless compute would be utilized. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "COMMENT": {
                                "type":"string",
                                "description":"COMMENT for alert object. if value is not provided by user, DEFAULT value is set to NONE"
                            }
                        },
                        "required":[
                            "NAME","SCHEDULE","IF","THEN","DATABASE","SCHEMA"
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
                                "description":"TYPE value for notification object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "ALLOWED_RECIPIENTS": {
                                "type":"string",
                                "description":"ALLOWED_RECIPIENTS value for notification object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "DEFAULT_RECIPIENTS": {
                                "type":"string",
                                "description":"DEFAULT_RECIPIENTS value for notification object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "DEFAULT_SUBJECT": {
                                "type":"string",
                                "description":"DEFAULT_SUBJECT value for notification object. if value is not provided by user, DEFAULT value is set to NONE"
                            },
                            "COMMENT": {
                                "type":"string",
                                "description":"COMMENT for notification object. if value is not provided by user, DEFAULT value is set to NONE"
                            }
                        },
                        "required":[
                            "NAME","ENABLED"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"perform_data_analysis",
                "description":"this tool executes python code extract insights from table. it has the data definitions, sample data, among other details of the table. you need not ask them to the user. use this tools for any analysis to be performed on the data. you dont need the database and schema for this. This tool takes a while for completion, please let the user know.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "table_name": {
                                "type":"string",
                                "description":"table name to retrieve data"
                            },
                            "query": {
                                "type":"string",
                                "description":"user question about the data to extract insights"
                            },
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
                "name":"get_list_of_tables",
                "description":"retrieves list of onboarded tables for a given database and schema",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "database": {
                                "type":"string",
                                "description":"database name to retrieve list of tables"
                            },
                            "schema": {
                                "type":"string",
                                "description":"schema name to retrieve list of tables"
                            },
                        },
                        "required":[
                            "database","schema"
                        ]
                    }
                }
            }
        },
    ]
}