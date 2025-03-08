
import sys
import os 
import logging

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.gvobject import Role as gv,Config as cfg
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy


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

class Role:
    def __init__(self,session,user_id,logger):
        self.attr = RoleAttrs(self)
        self.session = session
        self.user_id = user_id
        self.qry = ""
        self.logger = logger

    def set_name(self,val):
        self.attr.name = val

    def set_comment(self,val):
        self.attr.comment = val


    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv._name_tag,"_name")
        set_flag(gv._comment_tag,"_comment")

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
                if prop == gv._comment_tag:
                    self.qry = f" {self.qry} {gv._comment_tag} = {self.attr.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()
        
    def create_role(self):
        self.attr.session.sql(self.qry).collect()

    def create_object(self,*pargs,**kwargs): 
        self.set_name(kwargs[gv._name_tag])
        self.set_comment(kwargs[gv._comment_tag])
        self.prepare_query()
        self.logger.info(f"creating role {self.attr.name}")
        self.create_role()
        if len(pargs) == 0:
            self.create_deployment_entry()

    def create_deployment_entry(self):
        deploy_inst = Deploy(self.attr.session)
        self.logger.info(f"Tracking for deployment internal stage object : {self.attr.name}")
        deploy_inst.insert_into_deployment_script_table(qry=self.qry, user_id=self.user_id)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database('NA')
        deploy_inst.set_object_schema('NA')
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()
