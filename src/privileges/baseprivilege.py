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

class ObjectIdentifier:
    def __get__(self,instance,owner):
        return instance._object_identifier
    
    def __set__(self,instance,value):
        instance._object_identifier = value

    def __delete__(self,instance):
        del instance._object_identifier


class AbsGVPrivilegeAttr:
    object_type = ObjectType()
    object_identifier=ObjectIdentifier()

class AbsGVPrivilege(ABC):
    def __init__(self,session,logger):
        self.attr = AbsGVPrivilegeAttr()
        self.session=session
        self.logger=logger

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
    def __init__(self,session,logger):
        super().__init__(session=session,logger=logger)

    def set_object_type(self,val):
        self.attr.object_type=val
    
    def set_object_identifier(self,val):
        self.attr.object_identifier=val

    def grant_privilege_on_object_to_role(self,privlege_type,role) -> str: 
        self.logger.info(f"inside to grant {privlege_type} privilege to role {role}")     
        qry = f"GRANT {privlege_type} ON {self.attr.object_type} {self.attr.object_identifier} TO ROLE {role}"
        self.session.sql(qry).collect()
        self.logger.info("privilege granted")
        return qry
    
    @classmethod
    def grant_role_to_role(cls,role1,role2):
        qry = f"GRANT ROLE {role1} to ROLE {role2}"
        return qry

    def get_allowed_privileges(self) -> list:
        return priv._allowed_privileges[self.attr.object_type]
    

        