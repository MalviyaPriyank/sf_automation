#!/usr/bin/env python3
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

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
from src.obj import session as snowflake_session

from conf import readconf
from src.utils import helper
from src.usr.user import User,ChatHistory,Session
from src.model.tools_new import LLMTools
from src.model.bedrock import Bedrock
from agent import DataAgent 
from schema import streamlit_schema as ss
from schema import llm_chat_schema as lcs
from snowchainexception import (
    SnowchainException
)

import os
chat_history = []

class EchoHandler(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_POST(self):
        if self.path != "/echo":
            self.send_error(404, "Not Found")
            return

        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length)
        data = json.loads(raw.decode("utf-8")) if raw else {}
        message = (data.get("message") or "").strip()

        # add frosty logic - start
        try:
            global chat_history
            session_inst = snowflake_session.Session()
    
            session_inst.set_user('frosty')
            session_inst.set_password('Hellopehlaadmi@24')
            session_inst.set_account('kzekzkb-pm40264')
    
            logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            logging.getLogger(__name__).setLevel(logging.INFO)
            logger = logging.getLogger(__name__)
            
            logger.info('session started')
    
            session_state = session_inst.get_session()
            root = session_inst.get_root_object()
            prompt = message
            agent=DataAgent(session_state=session_state,
                            user_name='frosty',
                            logger=logger,
                            root=root,
                            prompt=prompt)
            '''
            user=User(user_name='frosty')
            user_session=Session()
            user_session.register_session(user,session_state)
            bedrock_obj = Bedrock()
            tools = LLMTools(sf_session=session_state,
                             root = root, 
                             logger=logger, 
                             bedrock_obj=bedrock_obj,
                             user_chat_inst=chat_inst)
            '''
            agent.initialize_chat_history(prompt=prompt)
            reply=agent.converse()
            #chat_inst.add_prompt(prompt=prompt)
            #chat_history.append(helper.append_chat_history(role=ss.USER, prompt=prompt))                                        
            #response = bedrock_obj.converse(messages=chat_history)
            #chat_history.append(helper.append_chat_history(is_text=False, prompt=response))
            #logger.info(f'response: {response}')
            '''
            for content in response:
                if ss.TEXT in content:
                    reply = json.dumps({"reply": content[ss.TEXT]}).encode("utf-8")
            
            tool_start_time = time.time()
            while len(response)>0:
                logger.info(chat_history)
                tool_result = []
                done_tool_call = False
                for content in response:
                    if (ss.TEXT in content) and (len(response)==1): 
                        done_tool_call = True
                        if tools.query_count !=0:
                            chat_inst.store_chat_history(snowflake_session=session_state)
                        break
                    if lcs.TOOL_USE in content:
                        try:
                            tool_result = tools.tool_call(content, tool_result)                            
                        except SnowchainException as e:
                            logger.info('attr-error')
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
                                reply = json.dumps({"reply": content[ss.TEXT]}).encode("utf-8")
            
            
                if done_tool_call: 
                    break 
            '''
        except Exception as e:
            print(f"{traceback.print_exc()}")
            print(e)
            chat_history=[]
            reply = json.dumps({"reply": 'There was an issue processing your request, I have raised a ticket with details. Someone will reach out to you shortly.'}).encode("utf-8")
            chat_history = []

        # Add frosty logic - end
        
        #reply = json.dumps({"reply": message}).encode("utf-8")
        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(reply)))
        self.end_headers()
        self.wfile.write(reply)

if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 80), EchoHandler)
    print("Backend running at http://0.0.0.0:80")
    server.serve_forever()
