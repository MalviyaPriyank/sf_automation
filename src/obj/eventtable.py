import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../processing'))



from vars.gvobject import Config as cfg , Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from vars.obj.eventtable.gveventtable import EventTableTag as tags
from dep import deploy
from setup import privilege 
from .baseobj import BaseObject 

from src.usr.user import ChatHistory

class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)
    
    def __set__(self,instance,value):
        db_name=instance.parent.attr.database
        schema_name=instance.parent.attr.schema

        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            if schema_name == "NONE":
                vo.is_new_object(session=instance.parent.session,
                                object_type=instance.parent.object_type,
                                object_name=name,
                                DATABASE=db_name)
            elif schema_name !="NONE":
                vo.is_new_object(
                    session=instance.parent.session,
                    object_type=instance.parent.object_type,
                    object_name=name,
                    DATABASE=db_name,
                    SCHEMA=schema_name
                    )
            if ( vv.starts_with_alphabet(name,instance.parent.__class__.__name__,self.__class__.__name__) 
                and not vv.has_space(name,instance.parent.__class__.__name__,self.__class__.__name__)
                and not vv.has_special_characters_except_underscore(name,instance.parent.__class__.__name__,self.__class__.__name__)
                ):
                instance._name = name
                instance._rename_to="NONE"
        else:
            instance.parent.logger.info(f" for rename operation")
            old_name=value["NAME"]
            new_name=value["RENAME_TO"]
            instance.parent.logger.info(f" changing name from {old_name} to {new_name}")
            if new_name != "NONE":
                vv.required_attribute_check(old_name,instance.parent.__class__.__name__,self.__class__.__name__)
                if schema_name =="NONE":
                    vo.object_exist(
                        session=instance.parent.session,
                        object_type=instance.parent.object_type,
                        object_name=old_name,
                        DATABASE=db_name
                    )
                    vo.is_new_object(
                        session=instance.parent.session,
                        object_type=instance.parent.object_type,
                        object_name=new_name,
                        DATABASE=db_name,
                    )
                elif schema_name != "NONE":
                    vo.object_exist(
                        session=instance.parent.session,
                        object_type=instance.parent.object_type,
                        object_name=old_name,
                        DATABASE=db_name,
                        SCHEMA=schema_name
                    )
                    vo.is_new_object(
                        session=instance.parent.session,
                        object_type=instance.parent.object_type,
                        object_name=new_name,
                        DATABASE=db_name,
                        SCHEMA=schema_name
                    )
                    
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name="NONE"
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name

class ClusterBy:
    def __get__(self,instance,owner):
        return instance._cluster_by
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._cluster_by = value
        else:   
            vv.is_allowed_value(
                value=value,
                allowed_list=tags.allowed_value_list().get(tags.CLUSTER_BY),
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._cluster_by = value

    def __delete__(self,instance):
        del instance._cluster_by


class DataRetentionTimeInDays:
    def __get__(self,instance,owner):
        return instance._data_retention_time_in_days
    
    def __set__(self,instance,value):
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
        if value == "NONE":
            instance._max_data_extension_time_in_days = value
        else:
            vv.is_positive_number(value,instance.parent.__class__.__name__,self.__class__.__name__)
            vv.is_between(value,tags.min_allowed_value().get(tags.MAX_DATA_EXTENSION_TIME_IN_DAYS),tags.max_allowed_value().get(tags.MAX_DATA_EXTENSION_TIME_IN_DAYS),instance.parent.__class__.__name__,self.__class__.__name__)    
            instance._max_data_extension_time_in_days = value

    def __delete__(self,instance):
        del instance._max_data_extension_time_in_days

class ChangeTracking:
    def __get__(self,instance,owner):
        return instance._change_tracking
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._change_tracking = value
        else:
            vv.is_bool(
                value=value,
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._change_tracking=value

    def __delete__(self,instance):
        del instance._change_tracking

class DefaultDDLCollation:
    def __get__(self,instance,owner):
        return instance._default_ddl_collation
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._default_ddl_collation = value
        else:
            vv.is_allowed_value(
                value=value,
                allowed_list=tags.allowed_value_list().get(tags.DEFAULT_DDL_COLLATION),
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._default_ddl_collation=value

    def __delete__(self,instance):
        del instance._default_ddl_collation

class EventTableAttrs:
    def __init__(self,parent):
        self.parent = parent

    name = Name()
    cluster_by=ClusterBy()
    data_retention_time_in_days = DataRetentionTimeInDays()
    max_data_extension_time_in_days = MaxDataExtensionTimeInDays()
    change_tracking=ChangeTracking()
    default_ddl_collation=DefaultDDLCollation()

class EventTable(BaseObject):
    def __init__(self,session,user_id,logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger,database_required=True,schema_required=True)
        self.attr = EventTableAttrs(self)
        self.object_type=self.__class__.__name__

    def set_name(self, value):
        self.attr.name = value

    def set_cluster_by(self,value):
        self.attr.cluster_by=value

    def set_data_retention_time_in_days(self, value):
        self.attr.data_retention_time_in_days = value

    def set_max_data_extension_time_in_days(self, value):
        self.attr.max_data_extension_time_in_days = value

    def set_change_tracking(self, value):
        self.attr.change_tracking = value

    def set_default_ddl_collation(self,value):
        self.attr.default_ddl_collation=value

    def set_comment(self, value):
        self.attr.comment=value

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.CLUSTER_BY,"_cluster_by")       
        set_flag(tags.DATA_RETENTION_TIME_IN_DAYS,"_data_retention_time_in_days")
        set_flag(tags.MAX_DATA_EXTENSION_TIME_IN_DAYS,"_max_data_extension_time_in_days")
        set_flag(tags.CHANGE_TRACKING,"_change_tracking")
        set_flag(tags.DEFAULT_DDL_COLLATION,"_default_ddl_collation")
        set_flag(tags.COMMENT,"comment")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_qry(self):
        self.session.sql(f"USE DATABASE {self.attr.database}").collect()
        if self.attr.schema=="NONE":
            self.qry = f"CREATE OR REPLACE EVENT TABLE  {self.attr.name[0]} "
        elif self.attr.schema!="NONE":
            self.qry = f"CREATE OR REPLACE EVENT TABLE  {self.attr.schema}.{self.attr.name[0]} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:                
                if prop == tags.CLUSTER_BY:
                    self.qry = f" {self.qry} {tags.CLUSTER_BY} = ({self.attr.cluster_by}) "
                if prop == tags.DATA_RETENTION_TIME_IN_DAYS:
                    self.qry = f" {self.qry} {tags.DATA_RETENTION_TIME_IN_DAYS} = {self.attr.data_retention_time_in_days} "
                if prop == tags.MAX_DATA_EXTENSION_TIME_IN_DAYS:
                    self.qry = f" {self.qry} {tags.MAX_DATA_EXTENSION_TIME_IN_DAYS} = {self.attr.max_data_extension_time_in_days} "
                if prop == tags.CHANGE_TRACKING:
                    self.qry = f" {self.qry} {tags.CHANGE_TRACKING} = {self.attr.change_tracking} "
                if prop == tags.DEFAULT_DDL_COLLATION:
                    self.qry = f" {self.qry} {tags.DEFAULT_DDL_COLLATION} = '{self.attr.default_ddl_collation}' "
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "

    def alter_object(self):        
        for prop in self.property_lst:
            if prop == tags.CLUSTER_BY:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.CLUSTER_BY} = ({self.attr.cluster_by})"
                self.execute_final_query()
            if prop == tags.DATA_RETENTION_TIME_IN_DAYS:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.DATA_RETENTION_TIME_IN_DAYS} = {self.attr.data_retention_time_in_days}"
                self.execute_final_query()
            if prop == tags.MAX_DATA_EXTENSION_TIME_IN_DAYS:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.MAX_DATA_EXTENSION_TIME_IN_DAYS} = {self.attr.max_data_extension_time_in_days}"
                self.execute_final_query()
            if prop == tags.CHANGE_TRACKING:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.CHANGE_TRACKING} = {self.attr.change_tracking}"
                self.execute_final_query()
            if prop == tags.DEFAULT_DDL_COLLATION:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.DEFAULT_DDL_COLLATION} = {self.attr.default_ddl_collation}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER {self.__class__.__name__}.upper() {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming database {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()
        
    
    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == 'TRUE':
            self.set_create_qry()
            self.add_properties_to_query()
        elif self.is_create=='FALSE':
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()


class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=EventTable(session=session,
                         user_id=user_id,
                         logger=logger)
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')

        obj_inst.set_base_attributes(kwargs=kwargs)

        obj_inst.logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        obj_inst.logger.info("set cluster by")
        if tags.CLUSTER_BY in kwargs.keys():
            obj_inst.set_cluster_by(kwargs[tags.CLUSTER_BY])
        else:
            obj_inst.set_cluster_by('NONE')

        obj_inst.logger.info("set data_retention_time_in_days")
        if tags.DATA_RETENTION_TIME_IN_DAYS in kwargs.keys():
            obj_inst.set_data_retention_time_in_days(kwargs[tags.DATA_RETENTION_TIME_IN_DAYS])
        else:
            obj_inst.set_data_retention_time_in_days('NONE')

        obj_inst.logger.info("set max_data_extension_time_in_days")
        if tags.MAX_DATA_EXTENSION_TIME_IN_DAYS in kwargs.keys():
            obj_inst.set_max_data_extension_time_in_days(kwargs[tags.MAX_DATA_EXTENSION_TIME_IN_DAYS])
        else:
            obj_inst.set_max_data_extension_time_in_days('NONE')

        obj_inst.logger.info("set change tracking")
        if tags.CHANGE_TRACKING in kwargs.keys():
            obj_inst.set_change_tracking(kwargs[tags.CHANGE_TRACKING])
        else:
            obj_inst.set_change_tracking('NONE')

        obj_inst.logger.info("set default_ddl_collation")
        if tags.DEFAULT_DDL_COLLATION in kwargs.keys():
            obj_inst.set_default_ddl_collation(kwargs[tags.DEFAULT_DDL_COLLATION])
        else:
            obj_inst.set_default_ddl_collation('NONE')

        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        obj_inst.print_query()
        
        obj_inst.logger.info('execute query')
        obj_inst.execute_final_query()

        obj_inst.logger.info('create deployment entry')
        if obj_inst.attr.schema=="NONE":
            obj_inst.create_deployment_entry(
                object_name=obj_inst.attr.name[0],
                object_type=obj_inst.object_type,
                object_database=obj_inst.attr.database,
                object_schema='NA'
            )
        else:
            obj_inst.create_deployment_entry(
                object_name=obj_inst.attr.name[0],
                object_type=obj_inst.object_type,
                object_database=obj_inst.attr.database,
                object_schema=obj_inst.attr.schema
            )

        obj_inst.logger.info("Write to git")
        if obj_inst.attr.schema=="NONE":
            obj_inst.write_file_to_git(
                object_name=obj_inst.attr.name[0],
                object_type=obj_inst.object_type,
                object_database=obj_inst.attr.database,
                object_schema='NA'
            )
        else:
            obj_inst.write_file_to_git(
                object_name=obj_inst.attr.name[0],
                object_type=obj_inst.object_type,
                object_database=obj_inst.attr.database,
                object_schema=obj_inst.attr.schema
            )    

        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                        object_identifier=obj_inst.attr.name[0],
                                        qry=obj_inst.qry)


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()

