import os
import sys
import time
from langchain_aws import ChatBedrock
from botocore.exceptions import ClientError

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../conf'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../schema'))
from conf import llm_config, readconf
from schema import llm_chat_schema as lcs
from src.obj import connection,schema,account,database,share,internalstage,externalstage,role,fileformat,resourcemonitor,user,warehouse,session

from valueexception import (
    AttributeValidationError,
    InvalidPassword
)

class LLMTools:
    def __init__(self,
                 logger,
                 sf_session,
                 region=llm_config.REGION,
                 temperature=llm_config.TEMPERATURE,
                 chat_model_id=llm_config.CHAT_MODEL_ID):
        self.sf_session = sf_session
        self.region = region
        self.logger = logger
        self.chat_llm = ChatBedrock(model_id=chat_model_id,
                                    model_kwargs=dict(temperature=temperature),
                                    aws_access_key_id=llm_config.ACCESS_KEY,
                                    aws_secret_access_key=llm_config.SECRET_KEY,
                                    region_name=self.region)

    def addition(self, num1, num2):
        return int(num1) + int(num2)


    def create_sf_object(self, obj_name):
        data_dict = readconf.main(obj_name)
        try:
            qry = database.Database.create_object(self.sf_session, **data_dict)
            self.logger.info(f"query returned {qry}")
            self.logger.info(f'Object {obj_name} created successfully')
            #self.sf_session.sql(qry)
        except AttributeValidationError as e:
            return(e)
        #sql_query = schema.main(**data_dict)
        #print(query)
        return(f'Object {obj_name} created successfully')


    def tool_call(self, content, tool_result):
        func_name = content[lcs.TOOL_USE][lcs.NAME]
        params = content[lcs.TOOL_USE][lcs.INPUT]
        result = getattr(self, func_name)(**params)
        tool_result.append({lcs.TOOL_RESULT:{
            lcs.TOOL_USE_ID: content[lcs.TOOL_USE][lcs.TOOL_USE_ID],
            lcs.CONTENT: [{lcs.JSON: {lcs.RESULT: result}}]
        }})
        return tool_result
        