import os
import sys
import streamlit as st

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))

from src import math_tools
from src.obj import account



st.title('Snowchain - Test Env')

with st.chat_message("assistant"):
    st.write("Please type two numbers separated by space, for addition")

if prompt := st.chat_input("How can I assist you today?"):
    with st.chat_message("user"):
        st.markdown(prompt)
        #num1, num2 = prompt.split(' ')
        #st.markdown(math_tools.addition(num1, num2))
        account.main(session='test_session')