

import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))

from vars.gvobject import Share as gv
from validation.validatevalue import ValidateValue as vv


class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if not vv.starts_with_alphabet(value):
            raise ValueError
        elif not vv.is_enclosed_in_double_quotes(value):
            if vv.has_space(value):
                raise ValueError
            if vv.has_special_characters(value):
                raise ValueError
            else:
                instance._name = value

    def __delete__(self,instance):
        del instance._name

class NameTag:
    def __get__(self,instance,owner):
        return instance._name_tag
    
    def __set__(self,instance,value):
        instance._name_tag = value
    
    def __delete__(self,instance):
        del instance._name_tag

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = value
    
    def __delete__(self,instance):
        del instance._comment

class CommentTag:
    def __get__(self,instance,owner):
        return instance._comment_tag
    
    def __set__(self,instance,value):
        instance._comment_tag = value
    
    def __delete__(self,instance):
        del instance._comment_tag

class ShareAttrs:
    def __init__(self,parent):
        self.parent = parent

    name = Name()
    name_tag = NameTag()

    comment = Comment()
    comment_tag = CommentTag()


class Share:
    def __init__(self):
        self.attr = ShareAttrs(self)
        self.session = 'session'
        self.qry = ""

    def set_name(self,val):
        self.attr.name = val

    def set_name_tag(self,val):
        self.attr.name_tag = val

    def set_comment(self,val):
        self.attr.comment = val

    def set_comment_tag(self,val):
        self.attr.comment_tag = val

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
        self.qry = f"CREATE SHARE  {self.attr.name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gv._comment_tag:
                    self.qry = f" {self.qry} {self.attr.comment_tag} = {self.attr.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()
    
    def create_share(self):
        self.session.sql(self.qry)

    def create_object(session,**kwargs):
        share = Share(session)

        share.set_name(kwargs[gv._name_tag])
        share.set_name_tag(gv._name_tag)

        share.set_comment(kwargs[gv._comment_tag])
        share.set_comment_tag(gv._comment_tag)

        share.prepare_query()
        share.create_share()