import os
import sys
import time
from langchain_aws import ChatBedrock
from botocore.exceptions import ClientError

sys.path.append(os.path.join(os.path.dirname(__file__),'../conf'))
from conf import llm_config, readconf

class LLMTools:
    def __init__(self,
                 temperature=llm_config.TEMPERATURE,
                 chat_model_id=llm_config.CHAT_MODEL_ID):
        self.chat_llm = ChatBedrock(model_id=chat_model_id,
                                    model_kwargs=dict(temperature=temperature))

    def addition(num1, num2):
        return int(num1) + int(num2)


    def create_sf_object(obj_name):
        data_dict = readconf.main(obj_name)
        print(data_dict)
        print(type(data_dict))
        sql_query = schema.main(**data_dict)
        print(query)
        