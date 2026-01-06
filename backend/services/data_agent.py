from src.model.tools_new import LLMTools
from src.model.bedrock import Bedrock
from src.usr.user import User,ChatHistory,Session
import logging
import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../conf'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../schema'))

from snowchainexception import (
    SnowchainException
)
class DataAgent:
    def __init__(self,session_state,user_name,logger,root):
        self.logger=logger.getChild(self.__class__.__name__)
        self.logger.setLevel(logging.ERROR)
        logger.setLevel(logging.ERROR)
        self.bedrock_obj=Bedrock()
        self.session_state=session_state
        self.user=User(user_name=user_name)
        self.user_session=Session()
        self.user_session.register_session(user=self.user,snowflake_session=session_state)
        self.user_chat_inst=ChatHistory(user=self.user,session=self.user_session)
        self.tools=LLMTools(logger=logger,
                            sf_session=session_state,
                            root=root,
                            bedrock_obj=Bedrock(),
                            user_chat_inst=self.user_chat_inst)
        self.chat_history=[]

    def initialize_chat_history(self, prompt):
        if isinstance(prompt, str):
            prompt = [{'role': 'user', 'content': prompt}]

        self.chat_history = []
        last_user_prompt = None

        for msg in prompt:
            role = msg.get('role', 'user')
            content = msg.get('content', '')
            if isinstance(content, str):
                content = [{'text': content}]
            self.chat_history.append({'role': role, 'content': content})
            if role == 'user':
                # store the last user text for ChatHistory logging
                for part in content:
                    if 'text' in part:
                        last_user_prompt = part['text']

        if last_user_prompt:
            self.user_chat_inst.add_prompt(prompt=last_user_prompt)
        # self.logger.info(f"chat history initialized: {self.chat_history}")
        # self.user_chat_inst.add_prompt(prompt=prompt)
        # self.chat_history.append({'role':'user',
        #                           'content':[{'text':prompt}]})
        # self.logger.info(f"chat history initialized: {self.chat_history}")
        
    def add_user_message(self,prompt):
        self.chat_history.append({'role':'user',
                                  'content':prompt})
        
    def add_assistant_message(self,prompt):
        self.chat_history.append({'role': 'assistant',
                                    'content': prompt})
        
    def converse(self):
        response = self.bedrock_obj.converse(messages=self.chat_history)
        self.chat_history.append({'role':'assistant',
                                  'content':response})
        for content in response:
            if 'text' in content:
                reply = json.dumps({"reply": content['text']}).encode("utf-8")
        while len(response)>0:
            # self.logger.info(self.chat_history)
            tool_result = []
            done_tool_call = False
            for content in response:
                if ('text' in content) and (len(response)==1): 
                    done_tool_call = True
                    if self.tools.query_count !=0:
                        self.user_chat_inst.store_chat_history(snowflake_session=self.session_state)
                    break
                if 'toolUse' in content:
                    try:
                        tool_result = self.tools.tool_call(content, tool_result)                            
                    except SnowchainException as e:
                        self.logger.info('attr-error')
                        tool_result.append({'toolResult':{
                            'toolUseId': content['toolUse']['toolUseId'],
                            'content': [{'json': {'result': "Error raised due to invalid input"}}]
                        }})
                        self.add_user_message(prompt=tool_result)
                        done_tool_call=True
                        break
                    self.add_user_message(prompt=tool_result)
                
                    response = self.bedrock_obj.converse(messages=self.chat_history)
                    self.add_assistant_message(prompt=response)
                        
                    
                    for content in response:
                        if 'text' in content:
                            reply = json.dumps({"reply": content['text']}).encode("utf-8")
        
        
            if done_tool_call: 
                break 
        return reply