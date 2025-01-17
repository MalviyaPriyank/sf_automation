import time
path_global_var = 'sf_automation/vars/global'
path_validation_func = 'sf_automation/src/validation'

def get_global_var_path():
    return path_global_var

def get_validation_func_path():
    return path_validation_func

def response_generator(responses):
    response = responses[-1]
    for word in response.split():
        yield word + " "
        time.sleep(0.05)