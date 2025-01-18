import os
import sys
import time
import logging
import streamlit as st

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../conf'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../utils'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../model'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../schema'))


from src.obj import connection,schema,account,database,share,internalstage,externalstage,role,fileformat,resourcemonitor,user,warehouse,session
from conf import readconf
from utils import helper
from model.tools import LLMTools
from model.bedrock import Bedrock
from schema import streamlit_schema as ss
from schema import llm_chat_schema as lcs
from valueexception import (
    AttributeValidationError,
    InvalidPassword
)

logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger('snowchain_logs').setLevel(logging.INFO)
logger = logging.getLogger('snowchain_logs')

st.title('Snowchain - Test Env')
#tools = LLMTools()

if ss.MESSAGES not in st.session_state:
    st.session_state[ss.MESSAGES] = []

if ss.CHAT_HISTORY not in st.session_state:
    st.session_state[ss.CHAT_HISTORY] = []

if ss.INITIALIZED not in st.session_state:
    st.session_state[ss.INITIALIZED] = False

with st.chat_message(ss.ASSISTANT):
    st.write("How may I assist you today?")

if not st.session_state[ss.INITIALIZED]:
    session_inst = session.Session()
    session_inst.set_user('rick')
    session_inst.set_password('mejzyg-pafpov-9noXmi')
    session_inst.set_account('TQNXPFG-BG28519')
    st.session_state.session = session_inst.get_session()
    st.session_state[ss.TOOLS] = LLMTools(sf_session=st.session_state.session, logger=logger)
    st.session_state.bedrock_obj = Bedrock()
    st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, prompt=lcs.SYSTEM_PROMPT_USER))
    st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(prompt=lcs.SYSTEM_PROMPT_ASST))
    st.session_state[ss.INITIALIZED] = True

if st.session_state[ss.INITIALIZED]:
    
    logger.info('session started')
            
    if prompt := st.chat_input("What's on your mind?"):
        with st.chat_message(ss.USER):
            st.markdown(prompt)
        st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, prompt=prompt))
        st.session_state[ss.MESSAGES].append(helper.msg_template(role=ss.USER, prompt=prompt))                                         

        with st.chat_message(ss.ASSISTANT):
            response = st.write_stream(helper.response_generator([ss.SHOVELING]))
        response = st.session_state.bedrock_obj.converse(messages=st.session_state[ss.CHAT_HISTORY])
        st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(is_text=False, prompt=response))
        logger.info('response')
        logger.info(response)

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
                    print(content)
                    tool_result = st.session_state[ss.TOOLS].tool_call(content, tool_result)
                    st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, is_text=False, prompt=tool_result))
                    
                    response = st.session_state.bedrock_obj.converse(messages=st.session_state[ss.CHAT_HISTORY])
                    st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(is_text=False, prompt=response))
                    for content in response:
                        if ss.TEXT in content:
                            st.session_state[ss.MESSAGES].append(helper.msg_template(role=ss.ASSISTANT, prompt=content[ss.TEXT]))
                            
                            with st.chat_message(ss.ASSISTANT):
                                st.markdown(content[ss.TEXT])

            if done_tool_call: break