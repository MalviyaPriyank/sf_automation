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

import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token="xoxb-9208561529233-9197498838290-zf4Agy7eak9f3rF6bIDLJBbD")


@app.event("message")
def handle_message_events(body, say):
    print(body)
    #say(f"Hey there <@{body['event']['user']}>!")
    run()

@app.event("app_mention")
def message_hello(body, say):
    # say() sends a message to the channel where the event was triggered
    #say(f"Hey there <@{body['event']['user']}>!")
    run()

SocketModeHandler(app, "xapp-1-A095SRHCLJZ-9196877250133-bbac21ac7e626fedc0734a6dc3bf027c79eed9b43d1ef70fc3c392cbadde797d").start()


def run(body, say):
    session_inst = session.Session()

    session_inst.set_user('pehlaadmi')
    session_inst.set_password('Hellopehlaadmi@24')
    session_inst.set_account('QYMNFNW-FDB17384')

    session_state = session_inst.get_session()
    root = session_inst.get_root_object()
    bedrock_obj = Bedrock()
    retrieval_workflow = session_state.bedrock_obj.get_retriever_obj()
    tools = LLMTools(sf_session=session_state.session,retrieval_workflow = retrieval_workflow,root = root, logger=logger)
    say('Logged in to snowflake')

'''
@app.event("message")
def handle_message_events(body, logger):
    say(f"Hey there <@{body['event']['user']}>!")



logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger('snowchain_logs').setLevel(logging.INFO)
logger = logging.getLogger('snowchain_logs')

st.title('Snowchain')
#tools = LLMTools()

if 'count' not in st.session_state:
    st.session_state['count'] = 0

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

if 'create_table' not in st.session_state:
    st.session_state['create_table'] = False

if 'database' not in st.session_state:
    st.session_state['database'] = None
    
if 'schema' not in st.session_state:
    st.session_state['schema'] = None

if 'tool_id' not in st.session_state:
    st.session_state['tool_id'] = None

def disable_chat():
    st.session_state[ss.CHAT_DISABLED] = True

if st.session_state['create_table']:
     csv_upload = st.file_uploader(
         'Please upload data dictionary for tables',
         accept_multiple_files=True,
         type='csv',
         key=f'fileuploader'
     )
     if csv_upload is not None:
         if not os.path.isdir('tmp'): os.mkdir('tmp')
         logger.info('here2')
         filelist = []
         for file in csv_upload:
             df = pd.read_csv(file)
             df.to_csv(f'tmp/{file.name}')
             filelist.append(file.name)
         if len(filelist)==len(csv_upload):
             logger.info(os.listdir('tmp/'))
             logger.info(filelist)
             _, upload_complete = st.session_state[ss.TOOLS].create_single_table_object(database=st.session_state['database'], 
                                                               schema=st.session_state['schema'],
                                                               filelist=filelist)
             
             if upload_complete:
                 logger.info('upload complete')
                 tool_result = []
                 tool_result.append({lcs.TOOL_RESULT:{
                                lcs.TOOL_USE_ID: st.session_state['tool_id'],
                                lcs.CONTENT: [{lcs.JSON: {lcs.RESULT: f"Tables created = {filelist}"}}]
                            }})
                 st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, is_text=False, prompt=tool_result))
                 st.session_state[ss.MESSAGES].append(helper.msg_template(role=ss.USER, prompt='Tables created successfully'))
                 st.session_state[ss.CHAT_DISABLED] = False
                 st.session_state['tool_id'] = None
                 st.session_state['create_table'] = False
                 st.rerun()
                 


if not st.session_state[ss.INITIALIZED]:
    session_inst = session.Session()

    session_inst.set_user('jjkennedy')
    session_inst.set_password('JJ_get_rich_12345')
    session_inst.set_account('QYMNFNW-FDB17384')

    st.session_state.session = session_inst.get_session()
    root = session_inst.get_root_object()
    st.session_state.bedrock_obj = Bedrock()
    retrieval_workflow = st.session_state.bedrock_obj.get_retriever_obj()
    st.session_state[ss.TOOLS] = LLMTools(sf_session=st.session_state.session,retrieval_workflow = retrieval_workflow,root = root, logger=logger)
    #st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, prompt=lcs.SYSTEM_PROMPT_USER))
    #st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(prompt=lcs.SYSTEM_PROMPT_ASST))
    st.session_state[ss.INITIALIZED] = True

if (st.session_state[ss.INITIALIZED]) and (st.session_state['create_table']==False):
    logger.info('session started')
            
    if prompt := st.chat_input("What's on your mind?", disabled=st.session_state[ss.CHAT_DISABLED], on_submit=disable_chat):
        
        with st.chat_message(ss.USER):
            st.markdown(prompt)
        st.session_state[ss.CHAT_HISTORY].append(helper.append_chat_history(role=ss.USER, prompt=prompt))
        st.session_state[ss.MESSAGES].append(helper.msg_template(role=ss.USER, prompt=prompt))                                         

        with st.chat_message(ss.ASSISTANT):
            st.write_stream(helper.response_generator([ss.SHOVELING]))
        
        #try: 
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
                    if content[lcs.TOOL_USE][lcs.NAME] == 'create_single_table_object':
                        print('here')
                        st.session_state['database'] = content[lcs.TOOL_USE]['input']['database']
                        st.session_state['schema'] = content[lcs.TOOL_USE]['input']['schema']
                        response = None
                        st.session_state['tool_id'] = content[lcs.TOOL_USE][lcs.TOOL_USE_ID]
                        st.session_state['create_table'] = True
                        done_tool_call = True
                        break
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
'''
'''
        except Exception as e:
            logger.info('app-error')
            logger.info(e)
            if st.session_state[ss.CHAT_HISTORY][-1][ss.ROLE]!=ss.ASSISTANT:
                st.session_state[ss.CHAT_HISTORY].append(helper.msg_template(role=ss.ASSISTANT, prompt=str(e)))
            with st.chat_message(ss.ASSISTANT):
                st.markdown('Looks like I dont have the tools to help with this request right now. Apologies :(')
            st.session_state[ss.CHAT_DISABLED] = False
            st.rerun()
'''