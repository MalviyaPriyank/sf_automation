
from accountglobalvars import *

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
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

class SchemaAttrs:
    name = Name()
    name_tag = NameTag()

    comment = Comment()
    comment_tag = CommentTag()


class Schema:
    def __init__(self,session):
        self.attr = SchemaAttrs()
        self.session = session
        self.qry = ""

    def set_name(self,name):
        self.attr.name = name

    def set_name_tag(self,name_tag):
        self.attr.name_tag = name_tag

    def set_comment(self,comment):
        self.attr.comment = comment

    def set_comment_tag(self,comment_tag):
        self.attr.comment_tag = comment_tag


    def set_object_properties_flag(self):
        self.flag_dic = {}

        if self.attr.name is not None:
            self.flag_dic[SCHT._name_tag] = 1
        else:
            self.flag_dic[SCHT._name_tag] = 0

        if self.attr.comment is not None:
            self.flag_dic[SCHT._comment_tag] = 1
        else:
            self.flag_dic[SCHT._comment_tag] = 0

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"CREATE DATABASE  {self.attr.name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == SCHT._comment_tag:
                    self.qry = f" {self.qry} {self.attr.comment_tag} = {self.attr.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()


def main(session,**kwargs):
    schema = Schema()
    schema_tags = SCHT()

    schema.set_name(kwargs[schema_tags._name_tag])
    schema.set_name_tag(schema_tags._name_tag)

    schema.set_comment(kwargs[schema_tags._comment_tag])
    schema.set_comment_tag(schema_tags._comment_tag)

    schema.prepare_query()

    return schema.qry
