import os
import sys
import json
import time
import logging
import pandas as pd
import streamlit as st

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../conf'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../schema'))
from src.obj import session

#from src.obj import connection,account,database,share,internalstage,externalstage,role,fileformat,resourcemonitor,user,warehouse,session
from conf import readconf
from src.utils import helper
from src.model.tools import LLMTools
from src.model.bedrock import Bedrock
from schema import streamlit_schema as ss
from schema import llm_chat_schema as lcs
from snowchainexception import (
    SnowchainException
)




logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger('snowchain_logs').setLevel(logging.INFO)
logger = logging.getLogger('snowchain_logs')

st.title('Snowchain')
#tools = LLMTools()


if ss.CHAT_DISABLED not in st.session_state:
    st.session_state[ss.CHAT_DISABLED] = False

if ss.MESSAGES not in st.session_state:
    st.session_state[ss.MESSAGES] = []
    with st.chat_message(ss.ASSISTANT):
        st.write("Hi this is Frosty, your AI Assistant for Snowflake. How may I assist you today?")
else:
    for message in st.session_state[ss.MESSAGES]:
        with st.chat_message(message[ss.ROLE]):
            st.markdown(message[ss.CONTENT])

if ss.CHAT_HISTORY not in st.session_state:
    st.session_state[ss.CHAT_HISTORY] = []
    for message in lcs.SYSTEM_PROMPTS:
        st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=message, prompt=lcs.SYSTEM_PROMPTS[message]))

if ss.INITIALIZED not in st.session_state:
    st.session_state[ss.INITIALIZED] = False

def disable_chat():
    st.session_state[ss.CHAT_DISABLED] = True

if not st.session_state[ss.INITIALIZED]:
    session_inst = session.Session()
    session_inst.set_user('RAJU')
    session_inst.set_password('Hellosnowflake@123')
    session_inst.set_account('CHBQBTW-RC94301')
    st.session_state.session = session_inst.get_session()
    root = session_inst.get_root_object()
    st.session_state.bedrock_obj = Bedrock()
    retrieval_workflow = st.session_state.bedrock_obj.get_retriever_obj()
    st.session_state[ss.TOOLS] = LLMTools(sf_session=st.session_state.session,retrieval_workflow = retrieval_workflow,root = root, logger=logger)
    #st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, prompt=lcs.SYSTEM_PROMPT_USER))
    #st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(prompt=lcs.SYSTEM_PROMPT_ASST))
    st.session_state[ss.INITIALIZED] = True

if st.session_state[ss.INITIALIZED]:
    logger.info('session started')
            
    if prompt := st.chat_input("What's on your mind?", disabled=st.session_state[ss.CHAT_DISABLED], on_submit=disable_chat):
        
        with st.chat_message(ss.USER):
            st.markdown(prompt)
        st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, prompt=prompt))
        st.session_state[ss.MESSAGES].append(helper.msg_template(role=ss.USER, prompt=prompt))                                         

        with st.chat_message(ss.ASSISTANT):
            st.write_stream(helper.response_generator([ss.SHOVELING]))
        
        try: 
            response = st.session_state.bedrock_obj.converse(messages=st.session_state[ss.CHAT_HISTORY])
            st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(is_text=False, prompt=response))
            logger.info(f'response: {response}')

            for content in response:
                if ss.TEXT in content:
                    st.session_state[ss.MESSAGES].append({
                        ss.ROLE:ss.ASSISTANT,
                        ss.CONTENT:content[ss.TEXT]
                    })
                    with st.chat_message(ss.ASSISTANT):
                        st.markdown(content[ss.TEXT])
                
    
            while len(response)>0:
                tool_result = []
                done_tool_call = False
                for content in response:
                    if (ss.TEXT in content) and (len(response)==1): 
                        done_tool_call = True
                        break
                    if lcs.TOOL_USE in content:
                        stage = Stage()
                        if content[lcs.TOOL_USE][lcs.NAME] == 'create_single_table_object':
                             csv_upload = st.file_uploader(
                                 'Please upload data dictionary for tables',
                                 accept_multiple_files=True,
                                 type='csv'
                             )
                             if csv_upload is not None:
                                 for file in csv_upload:
                                     pd.to_csv(f'tmp/{uploaded_file.name}')
     
                        try:
                            tool_result = st.session_state[ss.TOOLS].tool_call(content, tool_result)
                        except SnowchainException as e:
                            logger.info('attr-error')
                            st.session_state[ss.MESSAGES].append(helper.msg_template(role=ss.ASSISTANT, prompt=e))
                            with st.chat_message(ss.ASSISTANT):
                                st.markdown(e)
                            tool_result.append({lcs.TOOL_RESULT:{
                                lcs.TOOL_USE_ID: content[lcs.TOOL_USE][lcs.TOOL_USE_ID],
                                lcs.CONTENT: [{lcs.JSON: {lcs.RESULT: "Error raised due to invalid input"}}]
                            }})
                            st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, is_text=False, prompt=tool_result))
                            done_tool_call=True
                            break
                        st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, is_text=False, prompt=tool_result))
                    
                        response = st.session_state.bedrock_obj.converse(messages=st.session_state[ss.CHAT_HISTORY])
                        st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(is_text=False, prompt=response))
                        for content in response:
                            if ss.TEXT in content:
                                st.session_state[ss.MESSAGES].append(helper.msg_template(role=ss.ASSISTANT, prompt=content[ss.TEXT]))
                                
                                with st.chat_message(ss.ASSISTANT):
                                    st.markdown(content[ss.TEXT])
    
    
                if done_tool_call: 
                    break 

            st.session_state[ss.CHAT_DISABLED] = False
            st.rerun()
            
        except Exception as e:
            logger.info('app-error')
            logger.info(e)
            if st.session_state[ss.CHAT_HISTORY][-1][ss.ROLE]!=ss.ASSISTANT:
                st.session_state[ss.CHAT_HISTORY].append(helper.msg_template(role=ss.ASSISTANT, prompt=str(e)))
            with st.chat_message(ss.ASSISTANT):
                st.markdown('Looks like I dont have the tools to help with this request right now. Apologies :(')
            st.session_state[ss.CHAT_DISABLED] = False
            st.rerun()