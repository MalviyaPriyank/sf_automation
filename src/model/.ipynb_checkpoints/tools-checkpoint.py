import os
import sys
import time
from langchain_aws import ChatBedrock
from botocore.exceptions import ClientError

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../conf'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../schema'))
from conf import llm_config, readconf
from schema import llm_chat_schema as lcs
from src.obj import account,database,share,internalstage,externalstage,role,fileformat,resourcemonitor,user,warehouse


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
        self.obj_class_mapping = {'account': account.Admin,
                                  'database': database.Database,
                                  'externalstage': externalstage.ExternalStage,
                                  'role': role.Role,
                                  'internalstage': internalstage.InternalStage,
                                  'fileformat': fileformat.FileFormat,
                                  'resourcemonitor': resourcemonitor.ResourceMonitor,
                                  'warehouse': warehouse.Warehouse,
                                  #'schema': schema.Schema,
                                  'share': share.Share,
                                  #'table': table.Table,
                                  #'task': task.Task,
                                  'user': user.User
                                  }

    def addition(self, num1, num2):
        return int(num1) + int(num2)


    def create_sf_object(self, obj_name):
        data_dict = readconf.main(obj_name)
        try:
            qry = self.obj_class_mapping[obj_name].create_object(self.sf_session, **data_dict)
            self.logger.info(f"For {obj_name}, query returned: {qry}")
            self.logger.info(f'Object {obj_name} created successfully')
        except AttributeValidationError as e:
            return(e)
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
        