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
    #st.session_state.sess = session.Session()
    #st.session_state.conn = st.session_state.sess.set_connection('rick','mejzyg-pafpov-9noXmi','TQNXPFG.BG28519')
    st.session_state.cur = None #conn.cursor()
    st.session_state[ss.TOOLS] = LLMTools(cur=st.session_state.cur)
    st.session_state.bedrock_obj = Bedrock()
    st.session_state[ss.CHAT_HISTORY].append({
        ss.ROLE:ss.USER,
        ss.CONTENT:[{
            ss.TEXT: lcs.SYSTEM_PROMPT_USER
        }]
    })
    st.session_state[ss.CHAT_HISTORY].append({
        ss.ROLE:ss.ASSISTANT,
        ss.CONTENT:[{
            ss.TEXT: lcs.SYSTEM_PROMPT_USER
        }]
    })
    st.session_state[ss.INITIALIZED] = True

if st.session_state[ss.INITIALIZED]:
    if prompt := st.chat_input("What's on your mind?"):
        with st.chat_message(ss.USER):
            st.markdown(prompt)
        st.session_state[ss.CHAT_HISTORY].append({
            ss.ROLE:ss.USER,
            ss.CONTENT:[{
                ss.TEXT:prompt
            }]
        })
        st.session_state[ss.MESSAGES].append({
            ss.ROLE:ss.USER,
            ss.CONTENT:prompt
        })
        with st.chat_message(ss.ASSISTANT):
            response = st.write_stream(helper.response_generator([ss.SHOVELING]))
        response = st.session_state.bedrock_obj.converse(messages=st.session_state[ss.CHAT_HISTORY])
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
                    tool_result_message = {
                        ss.ROLE:ss.USER,
                        ss.CONTENT:tool_result
                    }
                    st.session_state[ss.CHAT_HISTORY].append(tool_result_message)
                response = st.session_state.bedrock_obj.converse(messages=st.session_state[ss.CHAT_HISTORY])

                for content in response:
                    if ss.TEXT in content:
                        st.session_state[ss.MESSAGES].append({
                            ss.ROLE:ss.ASSISTANT,
                            ss.CONTENT:content[ss.TEXT]
                        })
                        with st.chat_message(ss.ASSISTANT):
                            st.markdown(content[ss.TEXT])
            if dont_tool_call: break
            
        
        #data_dict = readconf.main('schema')
        #try:
        #    qry = schema.main(**data_dict)
        #    cur.execute(qry)
        #except AttributeValidationError as e:
            ## DO NOT REMOVE THIS
            ## following prints for debugging the path
            #print(f"Raised module: {type(e).__module__}")
            #print(f"Caught module: {AttributeValidationError.__module__}")
            print(e)
    

        
