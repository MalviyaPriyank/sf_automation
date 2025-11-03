import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../processing'))

import logging
logger = logging.getLogger('Database logs')
from vars.gvobject import Config as cfg , Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from vars.obj.imagerepository.gvimagerepository import ImageRepositoryTag as tags
from dep import deploy
from setup import privilege 
from .baseobj import BaseObject 


class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)

    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            if ( vv.starts_with_alphabet(name,instance.parent.__class__.__name__,self.__class__.__name__) 
                and not vv.has_space(name,instance.parent.__class__.__name__,self.__class__.__name__)
                and not vv.has_special_characters_except_underscore(name,instance.parent.__class__.__name__,self.__class__.__name__)
                ):
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
                vv.required_attribute_check(old_name,instance.parent.__class__.__name__,self.__class__.__name__)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to


class Encryption:
    def __get__(self, instance, owner):
        return instance._encryption
    
    def __set__(self, instance, value):
        instance._encryption = value

    def __delete__(self, instance):
        del instance._encryption

class ImageRepositoryAttrs:
    name = Name()
    encryption=Encryption()


class ImageRepository(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = ImageRepositoryAttrs()
        self.session = session
        self.user_id = user_id
        self.logger = logger.getChild(self.__class__.__name__)

    # setter methods
    def set_name(self, val): self.attr.name = val
    def set_encryption(self,val): self.attr.encryption=val

    def set_object_properties_flag(self):
        self.flag_dic = {}
        def set_flag(tag, attrname):
            self.flag_dic[tag] = 1 if getattr(self.attr, attrname, None) is not None else 0

        set_flag(tags.NAME, "name")
        set_flag(tags.COMMENT, "comment")
        set_flag(tags.ENCRYPTION, "encryption")

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_qry(self):
        self.qry = f"CREATE OR REPLACE IMAGE REPOSITORY {self.attr.name[0]} "

    def add_properties_to_query(self):
        if tags.ENCRYPTION in self.property_lst:
            self.qry += f"ENCRYPTION = (TYPE={self.attr.encryption}) "

    def alter_object(self):
        for prop in self.property_lst:
            self.qry = f"ALTER COMPUTE POOL {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER COMPUTE POOL {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming compute pool {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_computepool_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        obj_inst=ImageRepository(session=session,
                         user_id=user_id,
                         logger=logger)
        
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()

