
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
from .baseobj import BaseObject 
from vars.obj.storedprocedure.gvstoredprocedure import StoredProcedureTag as tags


class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.database_exist(session=instance.parent.session, database_name=value)
        instance._database = value
    
    def __delete__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.schema_exist(session=instance.parent.session, database_name=instance._database, schema_name=value)
        instance._schema = value
    
    def __delete__(self,instance):
        del instance._schema

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._name = value
        else:
            instance._name = value
    
    def __delete__(self,instance):
        del instance._name

class Logic:
    def __get__(self,instance,owner):
        return instance._logic
    
    def __set__(self,instance,value):
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
        if value == 'NONE':
            instance._packages = value
        else:
            instance._packages = value
    
    def __delete__(self,instance):
        del instance._packages

class Handler:
    def __get__(self,instance,owner):
        return instance._handler
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._handler = value
        else:
            instance._handler = value
    
    def __delete__(self,instance):
        del instance._handler

class ReturnType:
    def __get__(self,instance,owner):
        return instance._return_type
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._return_type = value
        else:
            instance._return_type = value
    
    def __delete__(self,instance):
        del instance._return_type

class StoredProcedureAttrs:
    def __init__(self,parent):
        self.parent=parent

    database=Database()
    schema=Schema()
    name=Name()
    logic=Logic()
    return_type=ReturnType()
    language=Language()
    handler=Handler()
    packages=Packages()

class StoredProcedure(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session, user_id, logger)
        self.attr=StoredProcedureAttrs(self)

    def set_database(self,value):
        self.attr.database=value

    def set_schema(self,value):
        self.attr.schema=value

    def set_name(self,value):
        self.attr.name=value

    def set_return_type(self,value):
        self.attr.return_type=value

    def set_language(self,value):
        self.attr.language=value

    def set_handler(self,value):
        self.attr.handler=value

    def set_packages(self,value):
        self.attr.packages=value

    def set_logic(self,value):
        self.attr.logic=value

    def set_qualified_name(self):
        self.qualified_name=f"{self.attr.database}.{self.attr.schema}.{self.attr.name}"

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.RETURNS,"_return_type")
        set_flag(tags.LANGUAGE,"_language")
        set_flag(tags.HANDLER,"_handler")
        set_flag(tags.PACKAGES,"_packages")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_stored_procedure_qry(self):
        self.qry = f"CREATE PROCEDURE {self.attr.database}.{self.attr.schema}.{self.attr.name} "
    
    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.RETURNS:
                    self.qry = f" {self.qry} {tags.RETURNS} = {self.attr.return_type} "
                if prop == tags.LANGUAGE:
                    self.qry = f" {self.qry} {tags.LANGUAGE} = {self.attr.language} "
                if prop == tags.HANDLER:
                    self.qry = f" {self.qry} {tags.HANDLER} = {self.attr.handler} "
                if prop == tags.PACKAGES:
                    self.qry = f" {self.qry} {tags.PACKAGES} = {self.attr.packages} "

        self.qry= self.qry + " AS $$ " + self.attr.logic + " $$;"

    def create_stored_procedure(self):
        self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_stored_procedure_qry()
        self.add_properties_to_query()

    def create_deployment_entry(self):
        deploy_inst = Deploy(self.session)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database(self.attr.database)
        deploy_inst.set_object_schema(self.attr.schema)
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()

    def create_object(self,*largs,**kwargs):
        self.set_database(kwargs[tags.DATABASE])
        self.set_schema(kwargs[tags.SCHEMA])
        self.set_name(kwargs[tags.NAME])
        self.set_logic(kwargs[tags.LOGIC])
        self.set_return_type(kwargs[tags.RETURNS])
        self.set_language(kwargs[tags.LANGUAGE])
        self.set_handler(kwargs[tags.HANDLER])
        self.set_qualified_name()
        self.prepare_query()
        self.logger.info(f"creating store procedure : {self.attr.name}")
        self.create_stored_procedure()
        self.create_deployment_entry()