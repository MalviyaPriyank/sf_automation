import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
from src.utils import helper

ACCESS_KEY = 'AKIAUMYCH7Z6CF4OQXJT'
SECRET_KEY = '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'

TEMPERATURE = 0
REGION = 'us-west-2'
BEDROCK_RUNTIME_SERVICE = 'bedrock-runtime'
CHAT_MODEL_ID = 'anthropic.claude-3-haiku-20240307-v1:0' #'anthropic.claude-3-sonnet-20240229-v1:0'
KB_MODEL_ID = 'anthropic.claude-3-haiku-20240307-v1:0'
EMBEDDINGS_MODEL_ID = 'anthropic.claude-3-haiku-20240307-v1:0'

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
                            "query": {
                                "type":"string",
                                "description":"User input for two numbers"
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
                "name":"create_sf_object",
                "description":"creates a snowflake object for the user. allowed objects are "+str(ALLOWED_OBJS),
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "obj_name": {
                                "type":"string",
                                "description":"name of object type"
                            }
                        },
                        "required":[
                            "obj_name"
                        ]
                    }
                }
            }
        },
        {
            "toolSpec": {
                "name":"initial_sf_setup",
                "description":"performs initial snowflake setup for user. do this if user specifies it is their first time and explicitly ask for initial setup",
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