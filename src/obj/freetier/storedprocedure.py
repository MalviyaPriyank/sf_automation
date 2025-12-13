
import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../processing'))



from vars.gvobject import StoredProcedure as gv, Config as cfg , Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from dep.deploy import Deploy
from setup import privilege 
from src.obj.baseobj import BaseObject 
from vars.obj.storedprocedure.gvstoredprocedure import StoredProcedureTag as tags
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

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to


class Logic:
    def __get__(self,instance,owner):
        return instance._logic
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value == 'NONE':
            instance._logic = value
        else:
            instance._logic = value
    
    def __delete__(self,instance):
        del instance._logic

class Language:

    def __get__(self,instance,owner):
        return instance._language
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        object_type=instance.parent.__class__.__name__
        attr_name=self.__class__.__name__
        if value == 'NONE':
            instance._language = value
        else:
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.LANGUAGE),object_type=object_type,attr_name=attr_name)
            instance._language = value
    
    def __delete__(self,instance):
        del instance._language

class Packages:
    def __get__(self,instance,owner):
        return instance._packages
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        instance._packages = value
    
    def __delete__(self,instance):
        del instance._packages

class Handler:
    def __get__(self,instance,owner):
        return instance._handler
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        instance._handler = value
    
    def __delete__(self,instance):
        del instance._handler

class ReturnType:
    def __get__(self,instance,owner):
        return instance._return_type
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        instance._return_type = value
    
    def __delete__(self,instance):
        del instance._return_type

class StoredProcedureAttrs:
    def __init__(self,parent):
        self.parent=parent

    name=Name()
    logic=Logic()
    return_type=ReturnType()
    language=Language()

class StoredProcedure(BaseObject):
    def __init__(self, session, user_id, logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger,database_required=True,schema_required=True)
        self.attr=StoredProcedureAttrs(self)


    def set_name(self,value):
        self.attr.name=value

    def set_return_type(self,value):
        self.attr.return_type=value

    def set_language(self,value):
        self.attr.language=value

    def set_logic(self,value):
        self.attr.logic=value

    def set_qualified_name(self):
        self.qualified_name=f"{self.attr.database}.{self.attr.schema}.{self.attr.name}"

    def set_object_properties_flag(self):
        pass

    def check_properties_to_set(self): 
        pass

    def set_create_stored_procedure_qry(self):
        self.qry = f"""
        CREATE PROCEDURE 
        {self.attr.database}.{self.attr.schema}.{self.attr.name[0]}() 
        RETURNS {self.attr.return_type}
        LANGUAGE {self.attr.language}
        AS
        $$
            BEGIN
                {self.attr.logic};
            END;
        $$
        """
    
    def add_properties_to_query(self):
        pass

    def create_stored_procedure(self):
        self.execute_final_query()

    def prepare_query(self):
        #self.set_object_properties_flag()
        #self.check_properties_to_set()
        self.set_create_stored_procedure_qry()
        self.add_properties_to_query()


class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=StoredProcedure(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.set_base_attributes(kwargs=kwargs)

        
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')
        obj_inst.logger.info(f"set name {obj_inst.attr.name}")

        
        if tags.LOGIC in kwargs.keys():
            obj_inst.set_logic(kwargs[tags.LOGIC])
        else:
            obj_inst.set_logic('NONE')
        obj_inst.logger.info(f"set logic {obj_inst.attr.logic}")

        
        if tags.RETURNS in kwargs.keys():
            obj_inst.set_return_type(kwargs[tags.RETURNS])
        else:
            obj_inst.set_return_type('NONE')
        obj_inst.logger.info(f"set return_type {obj_inst.attr.return_type}")
        
        if tags.LANGUAGE in kwargs.keys():
            obj_inst.set_language(kwargs[tags.LANGUAGE])
        else:
            obj_inst.set_language('NONE')
        obj_inst.logger.info(f"set language {obj_inst.attr.language}")


        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        obj_inst.print_query()

        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                        object_identifier=obj_inst.attr.name[0],
                                        qry=obj_inst.qry)


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
