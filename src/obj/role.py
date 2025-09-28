
import sys
import os 
import logging

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.gvobject import Config as cfg
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy
from .baseobj import BaseObject 
from vars.obj.role.gvrole import RoleTag as tags

class Name:
    def __get__(self,instance,owner):
        return instance._name

    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._name = value

    def __delete__(self,instance):
        del instance._name


class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._comment

class RoleAttrs:
    def __init__(self,parent):
        self.parent = parent

    name = Name()
    comment = Comment()

class Role(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session, user_id, logger)
        self.attr = RoleAttrs(self)

    def set_name(self,val):
        self.attr.name = val

    def set_comment(self,val):
        self.attr.comment = val


    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.NAME,"_name")
        set_flag(tags.COMMENT,"_comment")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"CREATE ROLE {self.attr.name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()
        
    def create_role(self):
        self.execute_final_query()

    def create_object(self,*pargs,**kwargs): 
        self.set_name(kwargs[tags.NAME])
        self.set_comment(kwargs[tags.COMMENT])
        self.prepare_query()
        self.logger.info(f"creating role {self.attr.name}")
        self.create_role()
        if len(pargs) == 0:
            self.create_deployment_entry(object_name=self.attr.name,object_type=self.__class__.__name__,object_database='NA',object_schema='NA')
            self.write_file_to_git(object_name=self.attr.name,object_type=self.__class__.__name__,object_database='NA',object_schema='NA')


    @classmethod
    def grant_role_to_user(self,role,user):
        self.qry=f" GRANT ROLE {role} TO USER {user}"
        self.execute_final_query()
        self.create_deployment_entry(object_name='ROLE_GRANT',object_type=self.__class__.__name__,object_database='NA',object_schema='NA')
        self.write_file_to_git(object_name='ROLE_GRANT',object_type=self.__class__.__name__,object_database='NA',object_schema='NA')
    
    @classmethod
    def grant_role_to_role(self,parent_role,child_role):
        self.qry=f" GRANT ROLE {parent_role} TO ROLE {child_role}"
        self.execute_final_query()
        self.create_deployment_entry(object_name='ROLE_GRANT',object_type=self.__class__.__name__,object_database='NA',object_schema='NA')
        self.write_file_to_git(object_name='ROLE_GRANT',object_type=self.__class__.__name__,object_database='NA',object_schema='NA')
