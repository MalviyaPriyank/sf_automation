import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))


from vars.gvobject import Stream as gv,Config as cfg, Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy
from validation.validateobject import ValidateObject as vo
from setup import privilege
from .baseobj import BaseObject 
from vars.obj.stream.gvstream import StreamTag as tags
from exception.operationexception import PropertyNotSupported

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

class ObjectType:
    def __get__(self,instance,owner):
        return instance._object_type
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__) 
        vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.OBJECT_TYPE),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        instance._object_type = value
    
    def __delete__(self,instance):
        del instance._object_type

class Name:   
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)
    
    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_object(session=instance.parent.session,
                             object_type=instance.parent.__class__.__name__,
                             object_name=value)
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
                raise PropertyNotSupported(object_type=instance.parent.__class__.__name__,
                                           property_name=instance.__class__.__name__)


    def __del__(self,instance):
        del instance._name
        del instance._rename_to


class TableName:
    def __get__(self,instance,owner):
        return instance._table_name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        if instance._object_type != 'STAGE':
            vo.table_exist(session=instance.parent.session,database_name=instance._database,schema_name=instance._schema,table_name=value)
        elif instance._object_type=='STAGE':
            vo.stage_exist(session=instance.parent.session,database_name=instance._database,schema_name=instance._schema,stage_name=value)
        instance._table_name = value
    
    def __delete__(self,instance):
        del instance._table_name


class At:
    def __get__(self,instance,owner):
        return instance._at
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._at=value
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._at = value
    
    def __delete__(self,instance):
        del instance._at

class Before:
    def __get__(self,instance,owner):
        return instance._before
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._before=value
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._before = value
    
    def __delete__(self,instance):
        del instance._before

class Timestamp:
    def __get__(self,instance,owner):
        return instance._timestamp
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._timestamp=value
        else:
            vv.is_valid_timestamp(object_name=instance.parent.__class__.__name__,attribute_name=self.__class__.__name__,value=value)
            instance._timestamp = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._timestamp

class Offset:
    def __get__(self,instance,owner):
        return instance._offset
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._offset=value
        else:
            vv.is_positive_number(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._offset = 60*value
    
    def __delete__(self,instance):
        del instance._timestamp

class AppendOnly:
    def __get__(self,instance,owner):
        return instance._append_only
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._append_only=value
        else:
            if (instance._object_type=="TABLE" 
                or instance._object_type=="VIEW"):
                vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                instance._append_only = value
            else:
                vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f"for streams not on STANDARD TABLEs or VIEWs")
    
    def __delete__(self,instance):
        del instance._append_only

class InsertOnly:
    def __get__(self,instance,owner):
        return instance._insert_only
    
    def __set__(self,instance,value):
        if instance._object_type=="EXTERNAL TABLE":
            vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,*['if stream is created on EXTERNAL TABLE'])
            instance._insert_only=value
        elif value=="NONE":
            instance._insert_only=value
        else:
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f"for streams that are not on EXTERNAL TABLEs")

    def __delete__(self,instance):
        del instance._insert_only

class ShowInitialRows:
    def __get__(self,instance,owner):
        return instance._show_initial_rows
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._show_initial_rows=value
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._show_initial_rows = value

    def __delete__(self,instance):
        del instance._show_initial_rows

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._comment = value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._comment=f"'{value}'"

    def __delete__(self,instance):
        del instance._comment


class StreamAttrs:
    def __init__(self,parent):
        self.parent = parent

    database=Database()
    schema=Schema()   
    name=Name()
    object_type=ObjectType()
    table_name=TableName()
    at=At()
    offset=Offset()
    before=Before()
    timestamp=Timestamp()
    append_only=AppendOnly()
    insert_only=InsertOnly()
    show_initial_rows=ShowInitialRows()
    comment=Comment()

class Stream(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session, user_id, logger)
        self.attr = StreamAttrs(self)


    def set_database(self, value):
        self.attr.database = value

    def set_schema(self, value):
        self.attr.schema = value

    def set_name(self, value):
        self.attr.name = value

    def set_object_type(self, value):
        self.attr.object_type = value

    def set_table_name(self, value):
        self.attr.table_name = value

    def set_at(self, value):
        self.attr.at = value

    def set_before(self, value):
        self.attr.before = value

    def set_timestamp(self, value):
        self.attr.timestamp = value

    def set_offset(self, value):
        self.attr.offset = value

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

        set_flag(tags.AT,"_at")
        set_flag(tags.BEFORE,"_before")
        set_flag(tags.TIMESTAMP,"_timestamp")
        set_flag(tags.OFFSET,"_offset")
        set_flag(tags.APPEND_ONLY,"_append_only")
        set_flag(tags.INSERT_ONLY,"_insert_only")
        set_flag(tags.SHOW_INITIAL_ROWS,"_show_initial_rows")
        set_flag(tags.COMMENT,"_comment")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def alter_object(self):
        for prop in self.property_lst:
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()

    def set_create_qry(self):
        if self.attr.object_type.upper()=="TABLE":
            self.qry = f"CREATE STREAM {self.attr.database}.{self.attr.schema}.{self.attr.name} ON TABLE {self.attr.database}.{self.attr.schema}.{self.attr.table_name}"
        elif self.attr.object_type.upper()=="EXTERNAL TABLE":
            self.qry = f"CREATE STREAM {self.attr.database}.{self.attr.schema}.{self.attr.name} ON EXTERNAL TABLE {self.attr.database}.{self.attr.schema}.{self.attr.table_name}"
        elif self.attr.object_type.upper()=="STAGE":
            self.qry = f"CREATE STREAM {self.attr.database}.{self.attr.schema}.{self.attr.name} ON STAGE {self.attr.database}.{self.attr.schema}.{self.attr.table_name}"
        elif self.attr.object_type.upper()=="VIEW":
            self.qry = f"CREATE STREAM {self.attr.database}.{self.attr.schema}.{self.attr.name} ON VIEW {self.attr.database}.{self.attr.schema}.{self.attr.table_name}"


    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if tags.AT in self.property_lst:
                    self.qry = f" {self.qry} {tags.AT} ("
                    if tags.TIMESTAMP in self.property_lst:
                        self.qry=f" {tags.TIMESTAMP} => {self.attr.timestamp}) "
                    elif tags.OFFSET in self.property_lst:
                        self.qry=f" {tags.OFFSET} => {self.attr.offset}) "
                elif tags.BEFORE in self.property_lst:
                    self.qry = f" {self.qry} {tags.BEFORE} ("
                    if tags.TIMESTAMP in self.property_lst:
                        self.qry=f" {tags.TIMESTAMP} => {self.attr.timestamp}) "
                    elif tags.OFFSET in self.property_lst:
                        self.qry=f" {tags.OFFSET} => {self.attr.offset} "
                if prop == tags.APPEND_ONLY:
                    self.qry = f" {self.qry} {tags.APPEND_ONLY} = {self.attr.append_only} "
                if prop == tags.INSERT_ONLY:
                    self.qry = f" {self.qry} {tags.INSERT_ONLY} = {self.attr.insert_only} "
                if prop == tags.SHOW_INITIAL_ROWS:
                    self.qry = f" {self.qry} {tags.SHOW_INITIAL_ROWS} = {self.attr.show_initial_rows} "
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create=="TRUE":
            self.set_create_qry()
            self.add_properties_to_query()
        elif self.is_create=="FALSE":
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()

    def create_stream(self):
        self.execute_final_query()

    def create_object(self,*largs,**kwargs):
        self.logger.info(f"Operating on {self.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        self.logger.info(f'dictionary passed {kwargs}')
        self.is_create=kwargs[tags.IS_CREATE]

        self.set_database(kwargs[tags.DATABASE])
        self.set_schema(kwargs[tags.SCHEMA])
        self.set_name(kwargs[tags.NAME])
        self.set_table_name(kwargs[tags.TABLE_NAME])
        self.set_at(kwargs[tags.AT])
        self.set_append_only(kwargs[tags.APPEND_ONLY])
        self.set_insert_only(kwargs[tags.INSERT_ONLY])
        self.set_show_initial_rows(kwargs[tags.SHOW_INITIAL_ROWS])
        self.set_comment(kwargs[tags.COMMENT])
        self.set_qualified_name()
        self.prepare_query()
        self.create_stream()
        self.logger.info(f"creating stream {self.attr.name}")
        if len(largs) == 0:
            self.logger.info('create deployment entry')
            self.create_deployment_entry(object_name=self.attr.name[0],
                                         object_type=self.__class__.__name__,
                                         object_database=self.attr.database,
                                         object_schema=self.attr.schema)

            self.logger.info('writing file to git')
            self.write_file_to_git(object_name=self.attr.name[0],
                                   object_type=self.__class__.__name__,
                                   object_database=self.attr.database,
                                   object_schema=self.attr.schema)


class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        obj_inst=DatabaseRole(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info("set database")
        if tags.DATABASE in kwargs.keys():
            obj_inst.set_database(kwargs[tags.DATABASE])
        else:
            obj_inst.set_database(kwargs[tags.DATABASE])

        logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name(kwargs[tags.NAME])

        logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment(kwargs[tags.COMMENT])


        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
