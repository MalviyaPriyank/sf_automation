from abc import ABC,abstractmethod
from src.usr.user import User
from src.model.bedrock import Bedrock
from src.model.tools_new import LLMTools
import json

class AgentABC(ABC):
    def __init__(self,agent_name,database_name):
        self.agent_name=agent_name
        self.database_name=database_name

    @abstractmethod
    def __init_user(self):
        '''
        This method should instantiate the user object.


        '''
        pass

    @abstractmethod
    def __init_chat_history(self):
        '''
        This method should instantiate the chat history which would be maintained per user.
        '''
        pass

    @abstractmethod
    def __init_tools(self):
        '''
        This method should check for the agent name / database name and determine which tools are required by the agent and instantitate the tools.
        '''
        pass

    @abstractmethod
    def __init_tool_call_counter(self):
        '''
        This method initialize the tool call counter to keep track of total tool calls made per call.
        '''
        pass

    @abstractmethod
    def __increment_tool_call_counter(self):
        '''
        This method increment tool call counter by 1 each time a new tool is called.
        '''
        pass

    @abstractmethod
    def __init_tool_call_list(self):
        '''
        This method instantiate a list to hold the tool names called per call.
        '''
        pass

    @abstractmethod 
    def __append_tool_to_list(self):
        '''
        This method to append the name of tool called, each time a new tool is called by the agent.
        '''
        pass

    @abstractmethod
    def add_user_message_to_chat_history(self):
        pass

    @abstractmethod
    def add_assistant_message_to_chat_history(self):
        pass



class GyrusAgent(AgentABC):
    def __init__(self, agent_name, database_name):
        super().__init__(agent_name, database_name)

    def __init_user(self,user_name):
        self.user=User(user_name=user_name)
        
            
    def __init_chat_history(self,prompt):
        #list for now, will replace with other efficient DS
        self.chat_history=[]
        self.chat_history.append({'role':'user',
                            'content':[{'text':[prompt]}]})

    def __init_tools(self,logger,session_state,root):
        #session state , logger, root and Bedrock to be removed from this
        if self.agent_name=='FROSTY':
            self.tools=LLMTools(logger=logger,
                            sf_session=session_state,
                            root=root,
                            bedrock_obj=Bedrock(),
                            )

    def __init_tool_call_counter(self):
        self.tool_call_count=0

    def __increment_tool_call_counter(self):
        self.tool_call_count+=1

    def __init_tool_call_list(self):
        self.tool_call_list=[]

    def __append_tool_to_list(self,tool_name):
        self.tool_call_list.append(tool_name)
        

    def add_user_message_to_chat_history(self,prompt):
        self.chat_history.append({'role':'user',
                                  'content':prompt})
        
    def add_assistant_message_to_chat_history(self,prompt):
            self.chat_history.append({'role': 'assistant',
                                        'content': prompt})
            
    def converse(self):
        bedrock_obj=Bedrock()
        response = bedrock_obj.converse(messages=self.chat_history)
        self.add_assistant_message_to_chat_history(response)

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
                    break
                if 'toolUse' in content:
                    try:
                        #parse the content and store tool call counter and tool names in instance variable
                        tool_result = self.tools.tool_call(content, tool_result)                            
                    except SnowchainException as e:
                        self.logger.info('attr-error')
                        tool_result.append({'toolResult':{
                            'toolUseId': content['toolUse']['toolUseId'],
                            'content': [{'json': {'result': "Error raised due to invalid input"}}]
                        }})
                        self.add_user_message_to_chat_history(prompt=tool_result)
                        done_tool_call=True
                        break
                    self.add_user_message_to_chat_history(prompt=tool_result)
                
                    response = bedrock_obj.converse(messages=self.chat_history)
                    self.add_assistant_message_to_chat_history(prompt=response)
                        
                    
                    for content in response:
                        if 'text' in content:
                            reply = json.dumps({"reply": content['text']}).encode("utf-8")
        
        
            if done_tool_call: 
                break 
        return reply
    
