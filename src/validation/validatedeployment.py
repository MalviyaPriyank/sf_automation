import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
from exception.deploymentexception import (
    NoScriptsForObjectForDeployment,
    NoScriptsForDeployment
)

class ValidateDeployment:
    def __init__(self):
        pass
    
    @staticmethod
    def scripts_exist(lst,deployment_status,src_db,**kwargs):
        if len(lst):
            return True
        else:
            if 'OBJECT' in kwargs.keys():
                raise NoScriptsForObjectForDeployment(src_db,deployment_status,kwargs['OBJECT'])
            else:
                raise NoScriptsForDeployment(src_db,deployment_status)
