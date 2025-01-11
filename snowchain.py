import os
import sys
import time
import streamlit as st

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../conf'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../model'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../schema'))

from src import math_tools
from src.obj import connection,schema,account,database,share,internalstage,externalstage,role,fileformat,resourcemonitor,user,warehouse,session
from src.exception.valueexception import AttributeValidationError,MustNotHaveSpecialCharacters
from conf import readconf
#from model.tools import LLMTools
from schema import streamlit_schema as ss
from schema import llm_chat_schema as lcs



st.title('Snowchain - Test Env')
#tools = LLMTools()

if ss.MESSAGES not in st.session_state:
    st.session_state[ss.MESSAGES] = []

if ss.CHAT_HISTORY not in st.session_state:
    st.session_state[ss.CHAT_HISTORY] = []

with st.chat_message(ss.ASSISTANT):
    st.write("Please type two numbers separated by space, for addition")

if prompt := st.chat_input("How can I assist you today?"):
    with st.chat_message(ss.USER):
        st.markdown(prompt)
        #st.session_state[ss.CHAT_HISTORY].append({
        #    ss.ROLE:ss.USER,
        #    ss.CONTENT:[{
        #        ss.TEXT:prompt
        #    }]
        #})
        #st.session_state[ss.MESSAGES].append({
        #    ss.ROLE:ss.USER,
        #    ss.CONTENT:prompt
        #})
        #response = bedrock_obj.converse(messages=st.session_state[ss.CHAT_HISTORY])
        #output_message = response[ss.OUTPUT][ss.MESSAGE]
        #new_content = output_message[ss.CONTENT]
        #st.session_state[ss.CHAT_HISTORY].append({
        #    ss.ROLE:ss.ASSISTANT,
        #    ss.CONTENT:new_content
        #})
        #for content in output_messages[ss.CONTENT]:
        #    if ss.TEXT in content:
        #        st.session_state[ss.MESSAGES].append({
        #            ss.ROLE:ss.ASSISTANT,
        #            ss.CONTENT:content[ss.TEXT]
        #        })
        #        with st.chat_message(ss.ASSISTANT):
        #            st.markdown(content[ss.TEXT])

        #while len(new_content)>0:
        #    tool_result = []
        #    for content in output_messages[ss.CONTENT]:
        #        if (ss.TEXT in content) and (len(new_content)==1): break
        #        if lcs.TOOL_USE in content:
        #            tool_result = tools.create_sf_object(tool_result)
        #            tool_result_message = {
        #                ss.ROLE:ss.USER,
        #                ss.CONTENT:tool_result
        #            }
        #        st.session_state[ss.CHAT_HISTORY].append(tool_result_message)
        #        response = bedrock_obj.converse(messages=st.session_state[ss.CHAT_HISTORY])
        #        output_message = response[ss.OUTPUT][ss.MESSAGE]
        #        new_content = output_message[ss.CONTENT]
        #        st.session_state[ss.CHAT_HISTORY].append({
        #            ss.ROLE:ss.ASSISTANT,
        #            ss.CONTENT:new_content
        #        })

        #        for content in output_message[ss.CONTENT]:
        #            if ss.TEXT in content:
        #            st.session_state[ss.MESSAGES].append({
        #                ss.ROLE:ss.ASSISTANT,
        #                ss.CONTENT:content[ss.TEXT]
        #            })
        #            with st.chat_message(ss.ASSISTANT):
        #                st.markdown(content[ss.TEXT])
        
        #conn = session.main()
        data_dict = readconf.main('account')
        try:
            qry = account.main(**data_dict)
        except Exception as e:
            print(e)
        
