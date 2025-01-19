import os
import sys
import glob
import json
import time
path_global_var = 'sf_automation/vars/global'
path_validation_func = 'sf_automation/src/validation'

sys.path.append(os.path.join(os.path.dirname(__file__),'../../schema'))
from schema import streamlit_schema as ss

def get_global_var_path():
    return path_global_var

def get_validation_func_path():
    return path_validation_func

def response_generator(responses):
    response = responses[-1]
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

def append_chat_history(prompt,
                        is_text=True,
                        role=ss.ASSISTANT):
    if is_text: prompt=[{ss.TEXT: prompt}]
    return {ss.ROLE: role,
            ss.CONTENT: prompt}

def msg_template(prompt,
                 role=ss.USER):
    return {ss.ROLE: role,
            ss.CONTENT: prompt}

def get_obj_names():
    obj_list = []
    for file in glob.glob("../obj/*"):
        if file.endswith('.py'):
            obj_list.append(file.split('/')[-1].replace('.py',''))
    return obj_list

def obj_json_template(filepath):
    with open(filepath, "r") as file:
        data = json.load(file)
    return data