ACCESS_KEY = 'AKIAUMYCH7Z6CF4OQXJT'
SECRET_KEY = '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'

TEMPERATURE = 0
REGION = 'us-west-2'
BEDROCK_RUNTIME_SERVICE = 'bedrock-runtime'
CHAT_MODEL_ID = 'anthropic.claude-3-haiku-20240307-v1:0' #'anthropic.claude-3-sonnet-20240229-v1:0'
KB_MODEL_ID = 'anthropic.claude-3-haiku-20240307-v1:0'
EMBEDDINGS_MODEL_ID = 'anthropic.claude-3-haiku-20240307-v1:0'

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
                "description":"creates a snowflake object.",
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
        }
    ]
}