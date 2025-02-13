import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../setup'))




from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from vars.gvstreamlit import Streamlit as gvslit
from setup.privilege import Privilege as priv


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
        vo.database_exist(session=instance.parent.session, database_name=value)
        instance._schema = value

    def __delete__(self,instance):
        del instance._schema

class Warehouse:
    def __get__(self,instance,owner):
        return instance._warehouse
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.warehouse_exist(session=instance.parent.session, warehouse_name=value)
        instance._warehouse = value

    def __delete__(self,instance):
        del instance._warehouse

class Role:
    def __get__(self,instance,owner):
        return instance._role
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.role_exist(session=instance.parent.session, role_name=value)
        instance._role = value

    def __delete__(self,instance):
        del instance._role


class StreamlitAttrs:

    def __init__(self,parent):
        self.parent=parent

    database = Database()
    schema = Schema()
    warehouse = Warehouse()
    role = Role()


class Streamlit:
    def __init__(self,session):
        self.session=session
        self.attr=StreamlitAttrs(self)

    def set_database(self,value):
        self.attr.database = value

    def set_schema(self,value):
        self.attr.schema = value

    def set_warehouse(self,value):
        self.attr.warehouse = value

    def set_role(self,value):
        self.attr.role = value
    
    def grant_privileges(self):
        priv_inst=priv(session=self.session)
        for object,privilege in gvslit._required_privileges_dict.items():
            if object == 'SCHEMA':
                priv_inst.grant_privilege_on_object_to_role(privilege_type=privilege,object_type=object,object_identifier=f"{self.attr.database}.{self.attr.schema}",role=self.attr.role)
            if object == 'DATABASE':
                priv_inst.grant_privilege_on_object_to_role(privilege_type=privilege,object_type=object,object_identifier=f"{self.attr.database}",role=self.attr.role)
            if object == 'WAREHOUSE':
                priv_inst.grant_privilege_on_object_to_role(privilege_type=privilege,object_type=object,object_identifier=f"{self.attr.warehouse}",role=self.attr.role)

    def grant_privileges_for_streamlit(self,**kwargs):
        self.set_database(kwargs[gvslit._database_tag])
        self.set_schema(kwargs[gvslit._schema_tag])
        self.set_role(kwargs[gvslit._role_tag])
        self.set_warehouse(kwargs[gvslit._role_tag])
        self.grant_privileges()

