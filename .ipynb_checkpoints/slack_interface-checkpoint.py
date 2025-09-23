import os
import sys
import json
import time
import logging
import requests
import pandas as pd
from pathlib import Path
import traceback

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

chat_history = []

def get_new_files_since(start_time, folder='analysis'):
    new_files = []
    for file in Path(folder).glob('*'):
        if file.is_file() and file.stat().st_mtime > start_time:
            new_files.append(str(file))
    return new_files

def run(body, say):
    try:
        session_inst = session.Session()

        session_inst.set_user('pehlaadmi')
        session_inst.set_password('Hellopehlaadmi@24')
        session_inst.set_account('kzekzkb-pm40264')

        logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        logging.getLogger('snowchain_logs').setLevel(logging.INFO)
        logger = logging.getLogger('snowchain_logs')
        
        logger.info('session started')

        session_state = session_inst.get_session()
        root = session_inst.get_root_object()
        bedrock_obj = Bedrock()
        retrieval_workflow = bedrock_obj.get_retriever_obj()
        tools = LLMTools(sf_session=session_state,retrieval_workflow = retrieval_workflow,root = root, logger=logger, bedrock_obj=bedrock_obj)
        logger.info("************** TOOL LIST **********************")
        logger.info(tools)
        logger.info("************** TOOL LIST **********************")
        # say('Logged in to snowflake')
        # print(body)
        prompt = body['event']['text']
        file_upload_prompt = 'Files for tables are already provided. You need not ask user for table names or any other details'
        if 'files' in body['event']:
            for file_info in body['event']['files']:
                file_id = file_info['id']
                file_name = file_info['name']
                file_url = file_info['url_private_download']

                print(f'Detected file upload: {file_name} ID: {file_id}')

                try:
                    headers = {'Authorization':f'Bearer xoxb-9208561529233-9197498838290-zf4Agy7eak9f3rF6bIDLJBbD'}
                    doc_response = requests.get(file_url, headers=headers)
                    doc_response.raise_for_status()
                    os.makedirs('tmp', exist_ok=True)
                    filepath = f'tmp/{file_name}'
                    with open(filepath, 'wb') as f:
                        f.write(doc_response.content)
                    print(f'File {file_name} downloaded successfully')
                    prompt += file_upload_prompt
                except requests.exceptions.RequestException as e:
                    print(f'Error downloading file {filename}: {e}')
                except Exception as e:
                    print(f'Error processing file {filename}: {e}')
        
        prompt = body['event']['text']
        chat_history.append(helper.append_chat_history(role=ss.USER, prompt=prompt))                                        
        logger.info(chat_history)
        response = bedrock_obj.converse(messages=chat_history)
        chat_history.append(helper.append_chat_history(is_text=False, prompt=response))
        logger.info(f'response: {response}')
        
        for content in response:
            if ss.TEXT in content:
                say(content[ss.TEXT])
        
        tool_start_time = time.time()
        while len(response)>0:
            tool_result = []
            done_tool_call = False
            for content in response:
                if (ss.TEXT in content) and (len(response)==1): 
                    done_tool_call = True
                    break
                if lcs.TOOL_USE in content:
                    try:
                        tool_result = tools.tool_call(content, tool_result)
                    except SnowchainException as e:
                        logger.info('attr-error')
                        say(str(e))
                        tool_result.append({lcs.TOOL_RESULT:{
                            lcs.TOOL_USE_ID: content[lcs.TOOL_USE][lcs.TOOL_USE_ID],
                            lcs.CONTENT: [{lcs.JSON: {lcs.RESULT: "Error raised due to invalid input"}}]
                        }})
                        chat_history.append(helper.append_chat_history(role=ss.USER, is_text=False, prompt=tool_result))
                        done_tool_call=True
                        break
                    chat_history.append(helper.append_chat_history(role=ss.USER, is_text=False, prompt=tool_result))
                
                    response = bedrock_obj.converse(messages=chat_history)
                    chat_history.append(helper.append_chat_history(is_text=False, prompt=response))
                        
                    
                    for content in response:
                        if ss.TEXT in content:
                            say(content[ss.TEXT])
        
        
            if done_tool_call: 
                break 

        new_files = get_new_files_since(tool_start_time)
        for file_path in new_files:
            app.client.files_upload_v2(
                channel=body['event']['channel'],
                file=file_path,
                title=os.path.basename(file_path)
            )   
    except Exception as e:
        logger.info(f"{traceback.print_exc()}")
        logger.info(e)
        say('There was an issue processing your request, Apologies :(')

@app.event("message")
def handle_message_events(body, say):
    # print(body)
    #say(f"Hey there <@{body['event']['user']}>!")
    run(body, say)

@app.event("app_mention")
def message_hello(body, say):
    # say() sends a message to the channel where the event was triggered
    #say(f"Hey there <@{body['event']['user']}>!")
    run(body, say)

SocketModeHandler(app, "xapp-1-A095SRHCLJZ-9196877250133-bbac21ac7e626fedc0734a6dc3bf027c79eed9b43d1ef70fc3c392cbadde797d").start()