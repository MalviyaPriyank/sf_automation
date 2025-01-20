import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
from global_vars import Privilege as gv
from privilegeexception import InvalidObject



class Object:
    def __get__(self,instance,owner):
        return instance._object
    
    def __set__(self,instance,value):
        if value not in gv._allowed_object_type:
            raise InvalidObject(value)
        else:
            instance._object = value

    def __delete__(self,instance):
        del instance._object

class PrivilegeAttr:
    object = Object()

class Privilege:
    def __init__(self,session):
        self.attr = PrivilegeAttr()
        self.session = session

    def set_object(self,value):
        self.attr.object = value

    @classmethod
    def grant_role_to_role(self,role1,role2):
        qry = f"GRANT ROLE {role1} to ROLE {role2}"
        self.session.sql(qry).collect()

    def grant_privilege
        

 
    