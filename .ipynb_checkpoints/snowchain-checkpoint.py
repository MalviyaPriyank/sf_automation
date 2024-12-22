import streamlit as st
from src.tools import math_tools


st.title('Snowchain - Test Env')

with st.chat_message("assistant"):
    st.write("Please type two numbers separated by space, for addition")

if prompt := st.chat_input("How can I assist you today?"):
    with st.chat_message("user"):
        st.markdown(prompt)
        num1, num2 = prompt.split(' ')
        st.markdown(math_tools.addition(num1, num2))