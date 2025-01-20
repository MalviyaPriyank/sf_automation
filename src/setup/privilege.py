import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../../vars/global'))
from global_vars import Priveleges as gv



class Object:
    def __set__():


class PrivilegeAttr:
    def __setattr__(self, name, value):
        if name in gv._allowed_object_type:
            if name == 'USER':
                self._privileges_list = gv._user_privileges
            elif name == 'ROLE':
                self._privileges_list = gv._role_privileges
            elif name == 'VIRTUAL WAREHOUSE':
                self._privileges_list = gv._virtual_warehouse_privileges
            elif name == 'DATABASE':
                self._privileges_list = gv._database_privileges
            elif name == 'SCHEMA':
                self._privileges_list = gv._schema_privileges
            elif name == 'TABLE':
                self._privileges_list = gv._table_privileges
            elif name == 'FILE FORMAT':
                self._privileges_list = gv._file_format_privileges
            elif name == 'PIPE':
                self._privileges_list = gv._pipe_privileges
            elif name == 'TASK':
                self._privileges_list = gv._task_privileges

    def __getattr__(self, name):
        return self._privileges_list

    def __delattr__(self, name):
        del self._privileges_list
        

class Privilege:
    def __init__(self,session,obj_type,privilege_type,role):
        attr = PrivilegeAttr(obj_type)
        self.obj_type = obj_type
        self.privilege_type = privilege_type
        self.role = role

    def grant_role_to_role(self,role1,role2):
        qry = f"GRANT ROLE {role1} to ROLE {role2}"
        return qry
    
    def validate_privilege_type(self):
        if self.privilege_type not in self.attr._privileges_list:
            raise ValueError


    def grant_privilege(self):
        qry = f"GRANT {self.privilege_type} ON {self.obj_type} TO ROLE"
        


    