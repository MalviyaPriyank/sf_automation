import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../processing'))



from vars.gvobject import Database as gv, Config as cfg , Privilege as gv_priv
from vars.obj.database.gvdatabase import Database as gv_db
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from dep import deploy
from setup import privilege 


class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.is_new_database(session=instance.parent.session, database_name=value)
        if ( vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__) 
            and not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
            and not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__)
            ):
            instance._name = value


    def __delete__(self,instance):
        del instance._name


class DatabaseAttrs:
    def __init__(self,parent):
        self.parent = parent
    name = Name()

class Database:
    def __init__(self,session,user_id,logger):
        self.session = session
        self.user_id = user_id
        self.logger = logger
        self.baseattr = DatabaseAttrs(self)

    def set_name(self, value):
        self.baseattr.name = value

    def set_query(self,value):
        self.qry=value

    def create_database(self):
        self.session.sql(self.qry).collect()
            

