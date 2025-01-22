import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
from global_vars import Privilege as gv_priv
from privilegeexception import InvalidObject,InvalidPrivilege



class Object:
    def __get__(self,instance,owner):
        return instance._object
    
    def __set__(self,instance,value):
        if value not in gv_priv._allowed_object_type:
            raise InvalidObject(value)
        else:
            instance._object = value

    def __delete__(self,instance):
        del instance._object

class PrivlegeType:
    def __get__(self,instance,owner):
        return instance._privilege_type
    
    def __set__(self,instance,value):
        if value not in gv_priv._allowed_privileges[instance._object]:
            raise InvalidPrivilege(value,instance._object)
        else:
            instance._privilege_type = value

    def __delete__(self,instance):
        del instance._privilege_type

class Role:
    def __get__(self,instance,owner):
        return instance._role
    
    def __set__(self,instance,value):
        instance._role = value

    def __delete__(self,instance):
        del instance._role

class PrivilegeAttr:
    object_type = Object()
    privilege_type = PrivlegeType()
    role = Role()

class Privilege:
    def __init__(self,session):
        self.attr = PrivilegeAttr()
        self.session = session

    def set_object_type(self,value):
        self.attr.object_type = value

    def set_privilege_type(self,value):
        self.attr.privilege_type= value

    def set_role(self,value):
        self.attr.role = value

    def grant_role_to_role(self,role1,role2):
        qry = f"GRANT ROLE {role1} to ROLE {role2}"
        self.session.sql(qry).collect()


    def grant_privilege_on_object_to_role(self,privilege_type,object_type,object_identifier,role):
        self.set_object_type(object_type)
        self.set_privilege_type(privilege_type)
        self.set_role(role)
        qry = f"GRANT {self.attr.privilege_type} ON {self.attr.object_type} {object_identifier} TO ROLE {self.attr.role}"
        self.session.sql(qry).collect()

        

 
    