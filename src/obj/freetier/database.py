import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../processing'))


from validation.validatevalue import ValidateValue as vv
from vars.obj.database.gvdatabase import DatabaseTag as tags
from src.obj.baseobj import BaseObject 
from src.usr.user import ChatHistory


class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)

    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
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
                #vo.database_exist(session=instance.parent.session,database_name=old_name)
                #vo.is_new_database(session=instance.parent.session,database_name=new_name)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to

class DataRetentionTimeInDays:
    def __get__(self,instance,owner):
        return instance._data_retention_time_in_days
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value == "NONE":
            instance._data_retention_time_in_days = value
        else:
            vv.is_positive_number(value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_between(value,tags.min_allowed_value().get(tags.DATA_RETENTION_TIME_IN_DAYS),tags.max_allowed_value().get(tags.DATA_RETENTION_TIME_IN_DAYS),instance.parent.__class__.__name__,self.__class__.__name__)
            instance._data_retention_time_in_days = value

    
    def __delete__(self,instance):
        del instance._data_retention_time_in_days

class MaxDataExtensionTimeInDays:
    def __get__(self,instance,owner):
        return instance._max_data_extension_time_in_days
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value == "NONE":
            instance._max_data_extension_time_in_days = value
        else:
            vv.is_positive_number(value,instance.parent.__class__.__name__,self.__class__.__name__)
            vv.is_between(value,tags.min_allowed_value().get(tags.MAX_DATA_EXTENSION_TIME_IN_DAYS),tags.max_allowed_value().get(tags.MAX_DATA_EXTENSION_TIME_IN_DAYS),instance.parent.__class__.__name__,self.__class__.__name__)    
            instance._max_data_extension_time_in_days = value

    def __delete__(self,instance):
        del instance._max_data_extension_time_in_days


class ExternalVolume:
    def __get__(self,instance,owner):
        return instance._external_volume
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._external_volume = value
        else:
            #vo.is_valid_external_volume(session=instance.parent.session,external_volume_identifier=value,object_type=self.__class__.__name__)
            instance._external_volume=value

    def __delete__(self,instance):
        del instance._external_volume

class Catalog:
    def __get__(self,instance,owner):
        return instance._catalog
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._catalog=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            #vo.is_valid_catalog(session=instance.parent.session,catalog_identifier=value,object_type=self.__class__.__name__)
            instance._catalog=value

    def __delete__(self,instance):
        del instance._catalog


class ReplaceInvalidCharacters:
    def __get__(self,instance,owner):
        return instance._replace_invalid_characters
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value == "NONE":
            instance._replace_invalid_characters = value
        elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._replace_invalid_characters = value

    def __delete__(self,instance):
        del instance._replace_invalid_characters


class DefaultDdlCollation:
    def __get__(self,instance,owner):
        return instance._default_ddl_collation
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._default_ddl_collation=value
        else:
            vv.is_valid_collation_specifier(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,valid_specifiers=tags.allowed_value_list().get(tags.DEFAULT_DDL_COLLATION))
            instance._default_ddl_collation = f"'{value}'"

    def __delete__(self,instance):
        del instance._default_ddl_collation


class LogLevel:
    def __get__(self,instance,owner):
        return instance._log_level
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._log_level=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.LOG_LEVEL),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._log_level = f"'{value}'"

    def __delete__(self,instance):
        del instance._log_level

class TraceLevel:
    def __get__(self,instance,owner):
        return instance._trace_level
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._trace_level=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.TRACE_LEVEL),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._trace_level = f"'{value}'"

    def __delete__(self,instance):
        del instance._trace_level

class StorageSerializationPolicy:
    def __get__(self,instance,owner):
        return instance._storage_serialization_policy
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value == "NONE":
            instance._storage_serialization_policy = value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.STORAGE_SERIALIZATION_POLICY),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._storage_serialization_policy = value

    def __delete__(self,instance):
        del instance._storage_serialization_policy

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value == 'NONE':
            instance._comment = value
        else:
            instance._comment = f"'{value}'"
    
    def __delete__(self,instance):
        del instance._comment

class DatabaseAttrs:
    def __init__(self,parent):
        self.parent = parent

    name = Name()

    data_retention_time_in_days = DataRetentionTimeInDays()

    max_data_extension_time_in_days = MaxDataExtensionTimeInDays()

    external_volume = ExternalVolume()

    catalog = Catalog()

    replace_invalid_characters = ReplaceInvalidCharacters()

    default_ddl_collation = DefaultDdlCollation()

    log_level=LogLevel()
    trace_level=TraceLevel()

    storage_serialization_policy = StorageSerializationPolicy()

    comment = Comment()


class Database(BaseObject):
    def __init__(self,session,user_id,logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger, database_required=False, schema_required=False)
        self.attr = DatabaseAttrs(self)

    def set_name(self, value):
        self.attr.name = value

    def set_data_retention_time_in_days(self, value):
        self.attr.data_retention_time_in_days = value

    def set_max_data_extension_time_in_days(self, value):
        self.attr.max_data_extension_time_in_days = value

    def set_external_volume(self, value):
        self.attr.external_volume = value


    def set_catalog(self, value):
        self.attr.catalog = value

    def set_replace_invalid_characters(self, value):
        self.attr.replace_invalid_characters = value

    def set_default_ddl_collation(self, value):
        self.attr.default_ddl_collation = value

    def set_log_level(self, value):
        self.attr.log_level = value

    def set_trace_level(self, value):
        self.attr.trace_level = value

    def set_storage_serialization_policy(self, value):
        self.attr.storage_serialization_policy = value

    def set_comment(self, value):
        self.attr.comment = value


    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.DATA_RETENTION_TIME_IN_DAYS,"_data_retention_time_in_days")
        set_flag(tags.MAX_DATA_EXTENSION_TIME_IN_DAYS,"_max_data_extension_time_in_days")
        set_flag(tags.EXTERNAL_VOLUME,"_external_volume")
        set_flag(tags.CATALOG,"_catalog")
        set_flag(tags.REPLACE_INVALID_CHARACTERS,"_replace_invalid_characters")
        set_flag(tags.DEFAULT_DDL_COLLATION,"_default_ddl_collation")
        set_flag(tags.LOG_LEVEL,"_log_level")
        set_flag(tags.TRACE_LEVEL,"_trace_level")
        set_flag(tags.STORAGE_SERIALIZATION_POLICY,"_storage_serialization_policy")
        set_flag(tags.COMMENT,"_comment")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"""
        CREATE OR REPLACE DATABASE  
        {self.attr.name[0]} 
        """

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.DATA_RETENTION_TIME_IN_DAYS:
                    self.qry = f" {self.qry} {tags.DATA_RETENTION_TIME_IN_DAYS} = {self.attr.data_retention_time_in_days} \n"
                if prop == tags.MAX_DATA_EXTENSION_TIME_IN_DAYS:
                    self.qry = f" {self.qry} {tags.MAX_DATA_EXTENSION_TIME_IN_DAYS} = {self.attr.max_data_extension_time_in_days} \n"
                if prop == tags.EXTERNAL_VOLUME:
                    self.qry = f" {self.qry} {tags.EXTERNAL_VOLUME} = {self.attr.external_volume} \n"
                if prop == tags.CATALOG:
                    self.qry = f" {self.qry} {tags.CATALOG} = {self.attr.catalog} \n"
                if prop == tags.REPLACE_INVALID_CHARACTERS:
                    self.qry = f" {self.qry} {tags.REPLACE_INVALID_CHARACTERS} = {self.attr.replace_invalid_characters} \n"
                if prop == tags.DEFAULT_DDL_COLLATION:
                    self.qry = f" {self.qry} {tags.DEFAULT_DDL_COLLATION} = {self.attr.default_ddl_collation} \n"
                if prop == tags.LOG_LEVEL:
                    self.qry = f" {self.qry} {tags.LOG_LEVEL} = {self.attr.log_level} \n"
                if prop == tags.TRACE_LEVEL:
                    self.qry = f" {self.qry} {tags.TRACE_LEVEL} = {self.attr.trace_level} \n"
                if prop == tags.STORAGE_SERIALIZATION_POLICY:
                    self.qry = f" {self.qry} {tags.STORAGE_SERIALIZATION_POLICY} = {self.attr.storage_serialization_policy} \n"
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "

    def alter_object(self):        
        for prop in self.property_lst:
            if prop == tags.DATA_RETENTION_TIME_IN_DAYS:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} SET {tags.DATA_RETENTION_TIME_IN_DAYS} = {self.attr.data_retention_time_in_days}"
                self.execute_final_query()
            if prop == tags.MAX_DATA_EXTENSION_TIME_IN_DAYS:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} SET {tags.MAX_DATA_EXTENSION_TIME_IN_DAYS} = {self.attr.max_data_extension_time_in_days}"
                self.execute_final_query()
            if prop == tags.EXTERNAL_VOLUME:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} SET {tags.EXTERNAL_VOLUME} = {self.attr.external_volume}"
                self.execute_final_query()
            if prop == tags.CATALOG:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} SET {tags.CATALOG} = {self.attr.catalog}"
                self.execute_final_query()
            if prop == tags.REPLACE_INVALID_CHARACTERS:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} SET {tags.REPLACE_INVALID_CHARACTERS} = {self.attr.replace_invalid_characters}"
                self.execute_final_query()
            if prop == tags.DEFAULT_DDL_COLLATION:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} SET {tags.DEFAULT_DDL_COLLATION} = {self.attr.default_ddl_collation}"
                self.execute_final_query()
            if prop == tags.LOG_LEVEL:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} SET {tags.LOG_LEVEL} = {self.attr.log_level}"
                self.execute_final_query()
            if prop == tags.TRACE_LEVEL:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} SET {tags.TRACE_LEVEL} = {self.attr.trace_level}"
                self.execute_final_query()
            if prop == tags.STORAGE_SERIALIZATION_POLICY:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} SET {tags.STORAGE_SERIALIZATION_POLICY} = {self.attr.storage_serialization_policy}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming {self.__class__.__name__.upper()} {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()
        
    
    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == 'TRUE':
            self.set_create_account_qry()
            self.add_properties_to_query()
        elif self.is_create=='FALSE':
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()

    def create_database(self):
        self.execute_final_query()

    
class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        db_inst=Database(session=session,
                         user_id=user_id,
                         logger=logger)
        
        db_inst.logger.info(f"Operating on {db_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        db_inst.logger.info(f'dictionary passed {kwargs}')
        db_inst.set_base_attributes(kwargs=kwargs)


        if len(largs) != 0:
            db_inst.logger.info(' list args passed')
            db_inst.qry = f"CREATE OR REPLACE DATABASE {kwargs[tags.NAME]}"
            db_inst.logger.info('calling create database')
            db_inst.create_database()
            db_inst.logger.info('granting default privileges')
            #self.grant_default_privileges(*['initial'])
        else:
            db_inst.logger.info('set name')
            db_inst.set_name(kwargs[tags.NAME])

            db_inst.logger.info('set DATA_RETENTION_TIME_IN_DAYS')
            if tags.DATA_RETENTION_TIME_IN_DAYS in  kwargs.keys(): 
                db_inst.set_data_retention_time_in_days(kwargs[tags.DATA_RETENTION_TIME_IN_DAYS])
            else:
                db_inst.set_data_retention_time_in_days("NONE")

            db_inst.logger.info('set MAX_DATA_EXTENSION_TIME_IN_DAYS')
            if tags.MAX_DATA_EXTENSION_TIME_IN_DAYS in kwargs.keys():
                db_inst.set_max_data_extension_time_in_days(kwargs[tags.MAX_DATA_EXTENSION_TIME_IN_DAYS])
            else:
                db_inst.set_max_data_extension_time_in_days("NONE")

            db_inst.logger.info('set EXTERNAL_VOLUME')
            if tags.EXTERNAL_VOLUME in kwargs.keys():
                db_inst.set_external_volume(kwargs[tags.EXTERNAL_VOLUME])
            else:
                db_inst.set_external_volume("NONE")

            db_inst.logger.info('set CATALOG')
            if tags.CATALOG in kwargs.keys():
                db_inst.set_catalog(kwargs[tags.CATALOG])
            else:
                db_inst.set_catalog("NONE")

            db_inst.logger.info('set REPLACE_INVALID_CHARACTERS')
            if tags.REPLACE_INVALID_CHARACTERS in kwargs.keys():
                db_inst.set_replace_invalid_characters(kwargs[tags.REPLACE_INVALID_CHARACTERS])
            else:
                db_inst.set_replace_invalid_characters("NONE")

            db_inst.logger.info('set DEFAULT_DDL_COLLATION')
            if tags.DEFAULT_DDL_COLLATION in kwargs.keys():
                db_inst.set_default_ddl_collation(kwargs[tags.DEFAULT_DDL_COLLATION])
            else:
                db_inst.set_default_ddl_collation("NONE")

            db_inst.logger.info('set LOG_LEVEL')
            if tags.LOG_LEVEL in kwargs.keys():
                db_inst.set_log_level(kwargs[tags.LOG_LEVEL])
            else:
                db_inst.set_log_level("NONE")

            db_inst.logger.info('set TRACE_LEVEL')
            if tags.TRACE_LEVEL in kwargs.keys():
                db_inst.set_trace_level(kwargs[tags.TRACE_LEVEL])
            else:
                db_inst.set_trace_level("NONE")

            db_inst.logger.info('set STORAGE_SERIALIZATION_POLICY')
            if tags.STORAGE_SERIALIZATION_POLICY in kwargs.keys():
                db_inst.set_storage_serialization_policy(kwargs[tags.STORAGE_SERIALIZATION_POLICY])
            else:
                db_inst.set_storage_serialization_policy("NONE")

            db_inst.logger.info('set COMMENT')
            if tags.COMMENT in kwargs.keys():
                db_inst.set_comment(kwargs[tags.COMMENT])
            else:
                db_inst.set_comment("NONE")

            db_inst.logger.info('preapare query')
            db_inst.prepare_query()

            if kwargs[tags.IS_CREATE] == "TRUE":
                db_inst.logger.info('execute query')
                #db_inst.create_database()

                db_inst.logger.info('grant default priv')
                #self.grant_default_privileges()

                user_chat_inst.add_to_chat_history(object_type=db_inst.__class__.__name__,
                                                object_identifier=db_inst.attr.name[0],
                                                qry=db_inst.qry)

    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()