import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
from src.utils import helper

ACCESS_KEY = 'AKIARSK3TK3YS2J5WLVZ' #'AKIAUMYCH7Z6CF4OQXJT'
SECRET_KEY = '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' #'ys7JM4BClYXWTpjzOv1C2aGZbIMltlHu9UJsq/oY'

TEMPERATURE = 0
REGION = 'us-west-2'
BEDROCK_RUNTIME_SERVICE = 'bedrock-runtime'
CHAT_MODEL_ID ='us.anthropic.claude-3-5-sonnet-20241022-v2:0'#'us.anthropic.claude-3-7-sonnet-20250219-v1:0'#'global.anthropic.claude-sonnet-4-20250514-v1:0'#'us.anthropic.claude-3-5-sonnet-20241022-v2:0'
KB_MODEL_ID ='us.anthropic.claude-3-5-sonnet-20241022-v2:0'#'us.anthropic.claude-3-7-sonnet-20250219-v1:0'#'global.anthropic.claude-sonnet-4-20250514-v1:0'#'us.anthropic.claude-3-5-sonnet-20241022-v2:0'
EMBEDDINGS_MODEL_ID ='us.anthropic.claude-3-5-sonnet-20241022-v2:0'

ALLOWED_OBJS = helper.get_obj_names()


tools = {
    "tools": [
        {
            "toolSpec": {
                "name":"create_object",
                "description":"Use this tool to create an object. ALWAYS use the get_object_params tool before this tool FOR EACH OBJECT, to get the dictionary keys and their description for data_dict attribute.",
                "inputSchema": {
                    "json":{ 
                        "type":"object",
                        "properties": {
                            "obj_type": {
                                "type":"string",
                                "description":f"type of object to create. allowed values are {ALLOWED_OBJS}"
                            },
                            "data_dict": {
                                "type":"string",
                                "description":"use the get_object_params tool to get the dictionary keys and their description. pass key value pair for the dictionary from the allowed keys"
                            }
                        },
                        "required":[
                            "obj_type","data_dict"
                        ]
                    }
                }
            },
        },
        {
            "toolSpec": {
                "name":"get_object_params",
                "description":"Use this tool to create an object.",
                "inputSchema": {
                    "json":{ 
                        "type":"object",
                        "properties": {
                            "obj_type": {
                                "type":"string",
                                "description":f"allowed values are {ALLOWED_OBJS}"
                            },
                        },
                        "required":[
                            "obj_type"
                        ]
                    }
                }
            },
        },
        {
            "toolSpec": {
                "name":"get_salesforce_cols",
                "description":"Use this tool to retrieve data columns from salesforce. it returns column list, you then cconfirm with user the columns they want to keep.",
                "inputSchema": {
                    "json":{ 
                        "type":"object",
                        "properties": {
                            "object_type": {
                                "type":"string",
                                "description":"user provided type of object"
                            },
                            "object_identifier": {
                                "type":"string",
                                "description":"user provided identifier for the object"
                            },
                        },
                        "required":[
                            "object_type","object_identifier"
                        ]
                    }
                }
            },
        },
        {
            "toolSpec": {
                "name":"get_salesforce_data_into_table",
                "description":"Use this tool to load data from salesforce into snowflake table.",
                "inputSchema": {
                    "json":{ 
                        "type":"object",
                        "properties": {
                            "object_type": {
                                "type":"string",
                                "description":"user provided type of object"
                            },
                            "object_identifier": {
                                "type":"string",
                                "description":"user provided identifier for the object"
                            },
                            "database": {
                                "type":"string",
                                "description":"user provided database name"
                            },
                            "schema": {
                                "type":"string",
                                "description":"user provided schema name"
                            },
                            "table": {
                                "type":"string",
                                "description":"user provided table name"
                            },
                            "columns_list": {
                                "type":"string",
                                "description":"user provided list of columns. this should be in the format ['col1','col2']"
                            },
                        },
                        "required":[
                            "object_type","object_identifier"
                        ]
                    }
                }
            },
        },
        {
            "toolSpec": {
                "name":"ingestion_pipeline_instructions",
                "description":"Use this tool to get instructions and dependencies for creating ingestion pipeline.",
                "inputSchema": {
                    "json":{ 
                        "type":"object",
                        "properties": {
                            "question": {
                                "type":"string",
                                "description":"user question"
                            },
                        },
                        "required":[
                            "question"
                        ]
                    }
                }
            },
        },
        {
            "toolSpec": {
                "name":"find_privileges",
                "description":"retrieves list of allowed privileges on an object",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "object_type": {
                                "type":"string",
                                "description":"alowed values are DATABASE, SCHEMA, WAREHOUSE, STAGE, TABLE, FILEFORMAT, SNOWPIPE, STREAM, TASK, USER"
                            },
                            "object_identifier": {
                                "type":"string",
                                "description":"name for the object"
                            },
                          "database": {
                                "type":"string",
                                "description":"name for the database. Default value is NONE"
                            },
                          "schema": {
                                "type":"string",
                                "description":"name for the schema. Default value is NONE"
                            },
                        },
                        "required":[
                            "object_type","object_identifier","database","schema"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"grant_privilege_on_object",
                "description":"grants privileges on an object. use find_privileges tool to get the list of allowed privileges on the object. you then choose from the retrieved list of allowed privileges by interpreting user request. for example if user request interprets to USAGE privilege, you select USAGE, you dont select the entire list of privileges returned from find_privileges tool but select one from the list that applies.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "object_type": {
                                "type":"string",
                                "description":"alowed values are DATABASE, SCHEMA, WAREHOUSE, STAGE, TABLE, FILEFORMAT, SNOWPIPE, STREAM, TASK, USER"
                            },
                            "object_identifier": {
                                "type":"string",
                                "description":"name for the object"
                            },
                            "role": {
                                "type":"string",
                                "description":"role to grant privileges to"
                            },
                            "privilege": {
                                "type":"string",
                                "description":"one privilege to be granted from the list of allowed privileges"
                            },
                            "database_name": {
                                "type":"string",
                                "description":"name of database. this is set to 'None' if object type is DATABASE, otherwise request it from user."
                            },
                            "schema": {
                                "type":"string",
                                "description":"name for the schema. Default value is NONE"
                            },
                        },
                        "required":[
                            "object_type","object_identifier","role","privilege","database_name","schema"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"create_cdc",
                "description":"pull incremental data from SQL Server to Snowflake, one-time load not a pipeline.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "db": {
                                "type":"string",
                                "description":"user provided database name"
                            },
                            "table_name": {
                                "type":"string",
                                "description":"user provided table name"
                            },
                        },
                        "required":[
                            "db","table_name"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"get_deployable_objects",
                "description":"returns a list of objects in development that are allowed for deployment. always check this list before executing deployment. use the list to check with user to select objects for deployment from this list.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "src_db": {
                                "type":"string",
                                "description":"source database name"
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
                "name":"deploy_objects",
                "description":"always check list of allowed objects from get_deployable_objects tool, share the list with user to pick subset of objects. then use this tool to deploy objects.",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "src_db": {
                                "type":"string",
                                "description":"source database name"
                            },
                            "tgt_db": {
                                "type":"string",
                                "description":"target database name"
                            },
                            "object_list": {
                                "type":"string",
                                "description":"user provided subset of objects from allowed objects of deployment list retrieved from get_deployable_objects tool"
                            },
                        },
                        "required":[
                            "src_db", "tgt_db"
                        ]
                    }
                }
            }
        },
    ]
}