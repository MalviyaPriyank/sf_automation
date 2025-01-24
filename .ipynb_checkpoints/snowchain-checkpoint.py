import os
import sys
import json
import time
import logging
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
    st.session_state[ss.MESSAGES] = [helper.msg_template(role=ss.ASSISTANT, prompt="Hi, this is Frosty, here to help you with Snowflake!")]

if ss.CHAT_HISTORY not in st.session_state:
    st.session_state[ss.CHAT_HISTORY] = []

if ss.INITIALIZED not in st.session_state:
    st.session_state[ss.INITIALIZED] = False

if ss.MESSAGES in st.session_state:
    for message in st.session_state[ss.MESSAGES]:
        with st.chat_message(message[ss.ROLE]):
            st.write(message[ss.CONTENT])

if lcs.CREATE_SF_OBJ not in st.session_state:
    st.session_state[lcs.CREATE_SF_OBJ] = False


#if 'json_upload' not in st.session_state:
#    st.session_state['json_upload'] = True

#if 'json_download' not in st.session_state:
#    st.session_state['json_download'] = True

#if 'content' not in st.session_state:
#    st.session_state['content'] = None

#if 'cnt' not in st.session_state:
#    st.session_state['cnt'] = 0

#if 'obj_name' not in st.session_state:
#    st.session_state['obj_name'] = None


if lcs.RETRIEVAL_WORKFLOW not in st.session_state:
    bedrock_obj = Bedrock()
    st.session_state[lcs.RETRIEVAL_WORKFLOW] = bedrock_obj.get_retriever_obj()


#if st.session_state[lcs.CREATE_SF_OBJ]:
#    tool_result = []
#    json_upload = st.file_uploader(
#        lcs.JSON_UPLOAD_GREETING,
#        accept_multiple_files=False,
#        type=lcs.JSON,
#            key=f'{st.session_state["obj_name"]}_json_upload{st.session_state["cnt"]}'
#    )
#    if json_upload is not None:
#        logger.info('there')
#        with open(f'conf/template/{st.session_state["content"][lcs.TOOL_USE][lcs.INPUT][lcs.OBJ_NAME]}/user_upload.json', 'w') as f:
#            json.dump(json.load(json_upload), f)
#        tool_result = st.session_state[ss.TOOLS].tool_call(st.session_state['content'], tool_result)
#        st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, is_text=False, prompt=tool_result))
        
#        response = st.session_state.bedrock_obj.converse(messages=st.session_state[ss.CHAT_HISTORY])
#        st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(is_text=False, prompt=response))
#        for content in response:
#            if ss.TEXT in content:
#                st.session_state[ss.MESSAGES].append(helper.msg_template(role=ss.ASSISTANT, prompt=content[ss.TEXT]))
                
#                with st.chat_message(ss.ASSISTANT):
#                    st.markdown(content[ss.TEXT])
#                st.session_state[lcs.CREATE_SF_OBJ] = False


if not st.session_state[ss.INITIALIZED]:
    session_inst = session.Session()
    session_inst.set_user('rick')
    session_inst.set_password('mejzyg-pafpov-9noXmi')
    session_inst.set_account('TQNXPFG-BG28519')
    st.session_state.session = session_inst.get_session()
    st.session_state[ss.TOOLS] = LLMTools(sf_session=st.session_state.session, 
                                          retrieval_workflow=st.session_state[lcs.RETRIEVAL_WORKFLOW], 
                                          logger=logger)
    st.session_state.bedrock_obj = Bedrock()
    st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, prompt=lcs.SYSTEM_PROMPT_USER))
    #for key in lcs.OBJ_PROMPTS:
    #    st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(prompt=lcs.OBJ_PROMPTS[key]))
    #    st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, prompt=key))
    st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(prompt=lcs.SYSTEM_PROMPT_ASST))
    st.session_state[ss.INITIALIZED] = True


if st.session_state[ss.INITIALIZED]:
    
    logger.info('session started')
            
    if prompt := st.chat_input("How can I help?"):
        

        with st.chat_message(ss.USER):
            st.markdown(prompt)
        st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, prompt=prompt))
        st.session_state[ss.MESSAGES].append(helper.msg_template(role=ss.USER, prompt=prompt))                                         

        with st.chat_message(ss.ASSISTANT):
            response = st.write_stream(helper.response_generator([ss.SHOVELING]))
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

        download_button = st.empty()
        upload_button = st.empty()
        while len(response)>0:
            tool_result = []
            #st.session_state['cnt'] += 1
            done_tool_call = False
            for content in response:
                if (ss.TEXT in content) and (len(response)==1): 
                    done_tool_call = True
                    break
                if lcs.TOOL_USE in content:
                #    if content[lcs.TOOL_USE][lcs.NAME] == lcs.CREATE_SF_OBJ:
                        #st.session_state['content'] = content
                        
                        #st.session_state['obj_name'] = content[lcs.TOOL_USE][lcs.INPUT][lcs.OBJ_NAME]
                        #json_template = helper.obj_json_template(f'conf/template/{st.session_state["obj_name"]}/required.json')
                        #json_string = json.dumps(json_template, indent=4)
                        #if json_template:
                        #    if st.session_state['json_download']:
                        #        st.download_button(
                        #            label="Download JSON template",
                        #            data=json_string,
                        #            file_name=f"{st.session_state['obj_name']}_template.json",
                        #            mime="application/json",
                        #            key=f'{st.session_state["obj_name"]}_json_template{st.session_state["cnt"]}'
                        #        )
                        #    st.session_state['json_download'] = False
                        
                        
                        #st.session_state[lcs.CREATE_SF_OBJ] = True
                        
                    #else:
                    tool_result = st.session_state[ss.TOOLS].tool_call(content, tool_result)
                    st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, is_text=False, prompt=tool_result))
                    
                    response = st.session_state.bedrock_obj.converse(messages=st.session_state[ss.CHAT_HISTORY])
                    st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(is_text=False, prompt=response))
                    for content in response:
                        if ss.TEXT in content:
                            st.session_state[ss.MESSAGES].append(helper.msg_template(role=ss.ASSISTANT, prompt=content[ss.TEXT]))
                            
                            with st.chat_message(ss.ASSISTANT):
                                st.markdown(content[ss.TEXT])

            if done_tool_call: 
                #st.session_state['json_download']
                #st.session_state['json_upload']
                break