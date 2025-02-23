import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.gvobject import Stream as gv,Config as cfg, Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy
from validation.validateobject import ValidateObject as vo
from setup import privilege


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

    def __del__(self,instance):
        del instance._schema

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if ( vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__) 
            and not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
            and not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__)
            ):
                instance._name = value

    def __delete__(self,instance):
        del instance._name

class TableName:
    def __get__(self,instance,owner):
        return instance._table_name
    
    def __set__(self,instance,value):
        instance._table_name = value
    
    def __delete__(self,instance):
        del instance._table_name

class Tag:
    def __get__(self,instance,owner):
        return instance._tag
    
    def __set__(self,instance,value):
        instance._tag = value
    
    def __delete__(self,instance):
        del instance._tag

class At:
    def __get__(self,instance,owner):
        return instance._at
    
    def __set__(self,instance,value):
        instance._at = value
    
    def __delete__(self,instance):
        del instance._at

class AppendOnly:
    def __get__(self,instance,owner):
        return instance._append_only
    
    def __set__(self,instance,value):
        instance._append_only = value
    
    def __delete__(self,instance):
        del instance._append_only

class InsertOnly:
    def __get__(self,instance,owner):
        return instance._insert_only
    
    def __set__(self,instance,value):
        instance._insert_only = value

    def __delete__(self,instance):
        del instance._insert_only

class ShowInitialRows:
    def __get__(self,instance,owner):
        return instance._show_initial_rows
    
    def __set__(self,instance,value):
        instance._show_initial_rows = value

    def __delete__(self,instance):
        del instance._show_initial_rows

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = value

    def __delete__(self,instance):
        del instance._comment


class StreamAttrs:
    def __init__(self,parent):
        self.parent = parent

    database=Database()
    schema=Schema()   
    name=Name()
    table_name=TableName()
    tag=Tag()
    at=At()
    append_only=AppendOnly()
    insert_only=InsertOnly()
    show_initial_rows=ShowInitialRows()
    comment=Comment()

class Stream:
    def __init__(self,session,user_id,logger):
        self.session = session
        self.user_id = user_id
        self.qry = ""
        self.logger = logger
        self.attr = StreamAttrs(self)


    def set_database(self, value):
        self.attr.database = value

    def set_schema(self, value):
        self.attr.schema = value

    def set_name(self, value):
        self.attr.name = value

    def set_table_name(self, value):
        self.attr.table_name = value

    def set_tag(self, value):
        self.attr.tag = value

    def set_at(self, value):
        self.attr.at = value

    def set_append_only(self, value):
        self.attr.append_only = value

    def set_insert_only(self, value):
        self.attr.insert_only = value

    def set_show_initial_rows(self, value):
        self.attr.show_initial_rows = value

    def set_comment(self, value):
        self.attr.comment = value

    def set_qualified_name(self):
        self.qualified_name = f"{self.attr.database}.{self.attr.schema}.{self.attr.name}"


    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv._tag_tag,"_tag")
        set_flag(gv._at_tag,"_at")
        set_flag(gv._append_only_tag,"_append_only")
        set_flag(gv._insert_only_tag,"_insert_only")
        set_flag(gv._show_initial_rows_tag,"_show_initial_rows")
        set_flag(gv._comment_tag,"_comment")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"CREATE STREAM {self.attr.database}.{self.attr.schema}.{self.attr.name} ON TABLE {self.attr.database}.{self.attr.schema}.{self.attr.table_name}"

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gv._tag_tag:
                    self.qry = f" {self.qry} {gv._tag_tag} = {self.attr.tag} "
                if prop == gv._at_tag:
                    self.qry = f" {self.qry} {gv._at_tag} = {self.attr.at} "
                if prop == gv._append_only_tag:
                    self.qry = f" {self.qry} {gv._append_only_tag} = {self.attr.append_only} "
                if prop == gv._insert_only_tag:
                    self.qry = f" {self.qry} {gv._insert_only_tag} = {self.attr.insert_only} "
                if prop == gv._show_initial_rows_tag:
                    self.qry = f" {self.qry} {gv._show_initial_rows_tag} = {self.attr.show_initial_rows} "
                if prop == gv._comment_tag:
                    self.qry = f" {self.qry} {gv._comment_tag} = {self.attr.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()

    def create_stream(self):
        self.session.sql(self.qry).collect()

    def create_deployment_entry(self):
        deploy_inst = Deploy(self.session)
        self.logger.info(f"Tracking for deployment schema object : {self.attr.name}")
        deploy_inst.insert_into_deployment_script_table(obj_qry=self.qry, user_id=self.user_id)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database(self.attr.database)
        deploy_inst.set_object_schema(self.attr.schema)
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()

    def grant_default_privileges(self):
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges[self.__class__.__name__.upper()]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = self.__class__.__name__.upper(),object_identifier=self.qualified_name,role = role)


    def create_object(self,*largs,**kwargs):

        self.set_database(kwargs[gv._database_tag])
        self.set_schema(kwargs[gv._schema_tag])
        self.set_name(kwargs[gv._name_tag])
        self.set_table_name(gv._table_name_tag)
        self.set_tag(kwargs[gv._tag_tag])
        self.set_at(kwargs[gv._at_tag])
        self.set_append_only(kwargs[gv._append_only_tag])
        self.set_insert_only(kwargs[gv._insert_only_tag])
        self.set_show_initial_rows(kwargs[gv._show_initial_rows_tag])
        self.set_comment(kwargs[gv._comment_tag])
        self.set_qualified_name()
        self.prepare_query()
        self.create_stream()
        self.logger.info(f"creating stream {self.attr.name}")
        self.grant_default_privileges()
        if len(largs) == 0:
            self.create_deployment_entry()
