import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../processing'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../table'))

from vars.gvobject import Config as cfg,Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from processing.stage import Stage
from dep.deploy import Deploy
from setup import privilege
from base import BaseTable


class Type:
    def __get__(self,instance,owner):
        return instance._type
    
    def __set__(self,instance,value):
        instance._column_type_list = value

    def __delete__(self,instance):
        del instance._column_type_list


class TempTable(BaseTable):
    def __init__(self, session, root, user_id, logger):
        super().__init__(session, root, user_id, logger)

