
import sys
import os 
import logging

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.gvobject import Config as cfg
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy
from src.obj.baseobj import BaseObject 
from vars.obj.role.gvrole import RoleTag as tags
from src.usr.user import ChatHistory

class Name:   
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            instance._name = name
            instance._rename_to="NONE"
        else:
            instance.parent.logger.info(f" for alter operation")
            old_name=value["NAME"]
            instance.parent.logger.info(f"old name {old_name}")
            new_name=value.get("RENAME_TO","NONE")
            instance.parent.logger.info(f"new name {new_name}")
            if new_name!="NONE":
                instance.parent.logger.info(f" changing name from {old_name} to {new_name}")
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"


    def __del__(self,instance):
        del instance._name
        del instance._rename_to



class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
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
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger, database_required=False, schema_required=False)
        self.attr = RoleAttrs(self)

    def set_name(self,val):
        self.attr.name = val

    def set_comment(self,val):
        self.attr.comment = val


    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.COMMENT,"_comment")

    def alter_object(self):        
        for prop in self.property_lst:
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming {self.__class__.__name__.upper()} {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_qry(self):
        self.qry = f"CREATE ROLE {self.attr.name[0]} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == 'TRUE':
            self.set_create_qry()
            self.add_properties_to_query()
        elif self.is_create=='FALSE':
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()
        
    def create_role(self):
        self.execute_final_query()

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=Role(session=session,
                         user_id=user_id,
                         logger=logger)
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.set_base_attributes(kwargs=kwargs)
        
        logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')


        logger.info('prepare query')
        obj_inst.prepare_query()

        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                        object_identifier=obj_inst.attr.name[0],
                                        qry=obj_inst.qry)

    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()