import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))

from vars.gvobject import Privilege as priv
from exception.privilegeexception import InvalidObject,InvalidPrivilege
from abc import ABC,abstractmethod

class ObjectType:
    def __get__(self,instance,owner):
        return instance._object_type
    
    def __set__(self,instance,value):
        if value not in priv._allowed_object_type:
            raise InvalidObject(value)
        instance._object_type = value

    def __delete__(self,instance):
        del instance._object_type


class AbsGVPrivilegeAttr:
    object_type = ObjectType()

class AbsGVPrivilege(ABC):
    def __init__(self):
        self.attr = AbsGVPrivilegeAttr()

    @abstractmethod
    def set_object_type():
        """
        method to set the type of object
        """
        pass  
        
    @abstractmethod
    def get_allowed_privileges():
        """
        method to retrieve the allowed privielges for the object type
        """
        pass

    @classmethod
    @abstractmethod
    def grant_privilege_on_object_to_role():
        """
        method to grant privilege on object to role
        """
        pass

    @abstractmethod
    @classmethod
    def grant_role_to_role():
        """
        method to grant privilege on object to role
        """
        pass


class BasePrivilege(AbsGVPrivilege):
    def __init__(self):
        super().__init__()

    def set_object_type(self,val):
        self.attr.object_type=val

    @classmethod
    def grant_privilege_on_object_to_role(cls,privlege_type,object_type,object_identifier,role) -> str: 
        qry = f"GRANT {privlege_type} ON {object_type} {object_identifier} TO ROLE {role}"
        return qry
    
    @classmethod
    def grant_role_to_role(cls,role1,role2):
        qry = f"GRANT ROLE {role1} to ROLE {role2}"
        return qry

    def get_allowed_privileges(self) -> list:
        return priv._allowed_privileges[self.attr.object_type]
    

        