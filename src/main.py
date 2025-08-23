from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
import os
import sys
from langgraph.checkpoint.memory import InMemorySaver
import getpass
import os
from langchain.chat_models import init_chat_model
from langgraph.func import entrypoint

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, repo_root)
from langgraph.graph import StateGraph, START, END

from model.tool import get_dependencies
from model.tool import tool_mappings
from model.prompts import PromptObjectDependency
from model.agents import *
from model.state import GraphState,AgentDependencyOutputState

os.environ["OPENAI_API_KEY"] = "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"
llm = ChatOpenAI(model="gpt-4o",api_key = os.environ["OPENAI_API_KEY"])
checkpointer = InMemorySaver()
from langchain_core.messages import ToolMessage
import json
@entrypoint()
def find_object_dependency(user_question):
    conversation_history = []
    """A workflow"""
    agent_inst = AgentObjectDependency(model=llm)
    object_dependency_agent = agent_inst.get_react_agent()
    conversation_history.append(HumanMessage(content=user_question))
    for stream_mode,chunk in object_dependency_agent.stream(
    {"messages": [{"role":"user","content":user_question}]},
    stream_mode=["updates", "messages", "custom"]
    ):
        if 'agent' in chunk:
            conversation_history.append(AIMessage(content = chunk['agent']['messages'][0].content))
    
        
from langgraph.func import entrypoint

if __name__ == '__main__':
    find_object_dependency.invoke("I want to create a Table")
        
# {'graph_output': 'My name is Lance'}
'''   
tools = [get_dependencies]
prmpt = PromptObjectDependency()
prmpt.initialize_prompt()
formatted_prompt = prmpt.get_prompt("I want to create a table")
llm = init_chat_model("gpt-4o-mini", model_provider="openai")
llm_with_tools = llm.bind_tools(tools)
ai_msg = llm_with_tools.invoke(formatted_prompt)
for tool_call in ai_msg.tool_calls:
    selected_tool = tool_mappings[tool_call["name"].lower()]
    tool_msg = selected_tool.invoke(tool_call)
print(tool_msg.content)
'''

