from src.model.tools_new import LLMTools
from src.model.bedrock import Bedrock
from src.usr.user import User,ChatHistory,Session
import json

class DataAgent:
    def __init__(self,session_state,user_name,logger,root):
        self.logger=logger.getChild(self.__class__.__name__)
        self.user_chat_inst=ChatHistory(user=self.user,session=self.user_session)
        self.bedrock_obj=Bedrock()
        self.tools=LLMTools(logger=logger,
                            sf_session=session_state,
                            root=root,
                            bedrock_obj=Bedrock(),
                            user_chat_inst=self.user_chat_inst)
        self.user=User(user_name=user_name)
        self.user_session=Session()
        self.user_session.register_session(user=self.user,snowflake_session=session_state)
        self.chat_history=[]

    def initialize_chat_history(self,prompt):
        self.user_chat_inst.add_prompt(prompt=prompt)
        self.chat_history.append({'role':'user',
                'content':[{'text':prompt}]})
        
    def converse(self):
        response = self.bedrock_obj.converse(messages=self.chat_history)
        self.chat_history.append({'role':'assistant',
                                  'content':response})
        for content in response:
            if 'text' in content:
                reply = json.dumps({"reply": content['text']}).encode("utf-8")
        while len(response)>0:
            self.logger.info(self.chat_history)
            tool_result = []
            done_tool_call = False
            for content in response:
                if ('text' in content) and (len(response)==1): 
                    done_tool_call = True
                    if self.tools.query_count !=0:
                        self.user_chat_inst.store_chat_history(snowflake_session=session_state)
                    break
                if 'toolUse' in content:
                    try:
                        tool_result = self.tools.tool_call(content, tool_result)                            
                    except SnowchainException as e:
                        self.logger.info('attr-error')
                        tool_result.append({lcs.TOOL_RESULT:{
                            lcs.TOOL_USE_ID: content[lcs.TOOL_USE][lcs.TOOL_USE_ID],
                            lcs.CONTENT: [{lcs.JSON: {lcs.RESULT: "Error raised due to invalid input"}}]
                        }})
                        self.chat_history.append(helper.append_chat_history(role=ss.USER, is_text=False, prompt=tool_result))
                        done_tool_call=True
                        break
                    self.chat_history.append(helper.append_chat_history(role=ss.USER, is_text=False, prompt=tool_result))
                
                    response = self.bedrock_obj.converse(messages=self.chat_history)
                    self.chat_history.append(helper.append_chat_history(is_text=False, prompt=response))
                        
                    
                    for content in response:
                        if 'text' in content:
                            reply = json.dumps({"reply": content['text']}).encode("utf-8")
        
        
            if done_tool_call: 
                break 
        return reply
    