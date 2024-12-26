import os
import sys
import streamlit as st

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../conf'))

from src import math_tools
from src.obj import account
from conf import readconf



st.title('Snowchain - Test Env')

with st.chat_message("assistant"):
    st.write("Please type two numbers separated by space, for addition")

if prompt := st.chat_input("How can I assist you today?"):
    with st.chat_message("user"):
        st.markdown(prompt)
        #num1, num2 = prompt.split(' ')
        #st.markdown(math_tools.addition(num1, num2))
        data_dict = readconf.main('account')
        print(data_dict)
        print(type(data_dict))
        account.main(**data_dict)