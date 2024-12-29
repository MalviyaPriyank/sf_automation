TEMPERATURE = 0
CHAT_MODEL_ID = 'anthropic.claude-3-sonnet-20240229-v1:0'

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
                "description":"creates a snowflake object based on user request",
                "inputSchema": {
                    "json":{
                        "type":"object",
                        "properties": {
                            "query": {
                                "type":"string",
                                "description":"User input for object type"
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