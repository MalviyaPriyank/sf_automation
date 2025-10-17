import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
from src.utils import helper

ACCESS_KEY = 'AKIARSK3TK3YS2J5WLVZ' #'AKIAUMYCH7Z6CF4OQXJT'
SECRET_KEY = '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' #'ys7JM4BClYXWTpjzOv1C2aGZbIMltlHu9UJsq/oY'

TEMPERATURE = 0
REGION = 'us-west-2'
BEDROCK_RUNTIME_SERVICE = 'bedrock-runtime'
CHAT_MODEL_ID ='us.anthropic.claude-3-5-sonnet-20241022-v2:0'
KB_MODEL_ID ='us.anthropic.claude-3-5-sonnet-20241022-v2:0'
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
    ]
}