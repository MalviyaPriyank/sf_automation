import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from .baseobj import BaseObject
from vars.obj.cortexsearch.gvcortexsearch import CortexSearchTag as tags
from src.usr.user import ChatHistory
from src.validation.validateobject import ValidateObject as vo
from src.validation.validatevalue import ValidateValue as vv


class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)

    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_object(session=instance.parent.session,object_type=instance.parent.__class__.__name__,object_name=name)
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
                vo.object_exist(session=instance.parent.session,object_type=instance.parent.__class__.__name__,object_name=old_name)
                vo.is_new_object(session=instance.parent.session,object_type=instance.parent.__class__.__name__,object_name=name)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to


class BaseTable:
    def __get__(self,instance,owner):
        return instance._base_table
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vo.table_exist(session=instance.parent.session,
                       database_name=instance.parent.attr.database,
                       schema_name=instance.parent.attr.schema,
                       table_name=value)
        instance._base_table = value


    def __delete__(self,instance):
        del instance._base_table

class On:
    def __get__(self,instance,owner):
        return instance._on
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vo.column_exist(session=instance.parent.session,
                        database=instance.parent.attr.database,
                        schema=instance.parent.attr.schema,
                        table=instance._base_table,
                        column=value)
        instance._on = value


    def __delete__(self,instance):
        del instance._on

class Attributes:
    def __get__(self,instance,owner):
        return instance._attributes
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        instance._attributes=""
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vv.is_list(value=value,
                   object_type=instance.parent.__class__.__name__,
                   attr_name=self.__class__.__name__)
        for i in range(0,len(value)):
            vo.column_exist(session=instance.parent.session,
                            database=instance.parent.attr.database,
                            schema=instance.parent.attr.schema,
                            table=instance._base_table,
                            column=value[i])
            if i != len(value)-1:
                instance._attributes=instance._attributes + str(value[i]) +","
            elif i==len(value)-1:
                instance._attributes=instance._attributes + str(value[i])
        instance.parent.logger.info(f" attributes : {instance._attributes}" )


    def __delete__(self,instance):
        del instance._attributes


class Warehouse:
    def __get__(self,instance,owner):
        return instance._warehouse
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vo.warehouse_exist(session=instance.parent.session,
                           warehouse_name=value)
        instance._warehouse = value


    def __delete__(self,instance):
        del instance._warehouse

class TargetLagUnit:
    def __get__(self,instance,owner):
        return instance._target_lag_unit
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vv.is_string(value=value,
                     object_type=instance.parent.__class__.__name__,
                     attr_name=self.__class__.__name__)
        instance._target_lag_unit = value

    def __delete__(self,instance):
        del instance._target_lag_unit

class TargetLag:
    def __get__(self,instance,owner):
        return instance._target_lag

    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vv.is_positive_number(value=value,
                              object_type=instance.parent.__class__.__name__,
                              attr_name=self.__class__.__name__)
        instance._target_lag = value

    def __delete__(self,instance):
        del instance._target_lag

class EmbeddingModel:
    def __get__(self,instance,owner):
        return instance._embedding_model
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value=="NONE":
            instance._embedding_model=value
        else:
            vv.is_allowed_value(value=value,
                                allowed_list=tags.allowed_value_list().get(tags.EMBEDDING_MODEL),
                                object_type=instance.parent.__class__.__name__,
                                attr_name=self.__class__.__name__)
            instance._embedding_model = value

    def __delete__(self,instance):
        del instance._embedding_model

class Initialize:
    def __get__(self,instance,owner):
        return instance._initialize
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if value == 'NONE':
            instance._initialize='NONE'
        else:
            vv.is_allowed_value(value=value,
                                allowed_list=tags.allowed_value_list().get(tags.INITIALIZE),
                                object_type=instance.parent.__class__.__name__,
                                attr_name=self.__class__.__name__)
            instance._initialize = value


    def __delete__(self,instance):
        del instance._initialize

class ServiceQuery:
    def __get__(self,instance,owner):
        return instance._service_query
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        instance._service_query = value

    def __delete__(self,instance):
        del instance._service_query

class CortexSearchAttrs:
    def __init__(self,parent):
        self.parent=parent
    name=Name()
    on=On()
    attributes=Attributes()
    warehouse=Warehouse()
    target_lag=TargetLag()
    embedding_model=EmbeddingModel()
    initialize=Initialize()
    service_query=ServiceQuery()
    target_lag_unit=TargetLagUnit()
    base_table=BaseTable()

class CortexSearch(BaseObject):
    def __init__(self,session,user_id,logger):
        self.logger=logger.getChild(self.__class__.__name__)
        super().__init__(session=session,user_id=user_id,logger=logger,database_required=True,schema_required=True)
        self.attr=CortexSearchAttrs(self)

        self.user_id=user_id

    def set_name(self,val):
        self.attr.name=val

    def set_on(self,val):
        self.attr.on=val

    def set_attributes(self,val):
        self.attr.attributes=val

    def set_warehouse(self,val):
        self.attr.warehouse=val

    def set_target_lag(self,val):
        self.attr.target_lag=val

    def set_embedding_model(self,val):
        self.attr.embedding_model=val

    def set_initialize(self,val):
        self.attr.initialize=val

    def set_target_lag_unit(self,val):
        self.attr.target_lag_unit=val

    def set_service_query(self,val):
        self.attr.service_query=val

    def set_base_table(self,val):
        self.attr.base_table=val

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.EMBEDDING_MODEL,"embedding_model")
        set_flag(tags.INITIALIZE,"initialize")
        set_flag(tags.COMMENT,"comment")
        set_flag(tags.SERVICE_QUERY,"service_query")
        

    def alter_object(self):     
        alter_object="CORTEX SEARCH SERVICE"   
        for prop in self.property_lst:
            if prop == tags.WAREHOUSE:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.WAREHOUSE} = {self.attr.warehouse}"
                self.execute_final_query()
            if prop == tags.TARGET_LAG:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.TARGET_LAG} = {self.attr.target_lag}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.COMMENT} = '{self.attr.comment}'"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            vo.operation_on_object_not_suppported(message=f"Cannot alter {tags.NAME} for Cortex Search Service")



    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.EMBEDDING_MODEL:
                    self.qry = f" {self.qry} {tags.EMBEDDING_MODEL} = {self.attr.embedding_model} \n"
                if prop == tags.INITIALIZE:
                    self.qry = f" {self.qry} {tags.INITIALIZE} = {self.attr.initialize} \n"
                if prop == tags.COMMENT:
                    self.qry = f"{self.qry} {tags.COMMENT} = '{self.attr.comment}' \n"
                if prop == tags.SERVICE_QUERY:
                    self.qry = f"{self.qry} AS ({self.attr.service_query})"

    def set_create_cortex_search_qry(self):
        self.qry = f"""CREATE CORTEX SEARCH SERVICE {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} 
        ON {self.attr.on} 
        {tags.ATTRIBUTES} {self.attr.attributes}
        {tags.WAREHOUSE} = {self.attr.warehouse}
        {tags.TARGET_LAG} = '{self.attr.target_lag} {self.attr.target_lag_unit}'
        """

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.logger.info("checking if create or alter")
        if self.is_create == 'TRUE':
            self.logger.info("inside create")
            self.logger.info("creating query")
            self.set_create_cortex_search_qry()
            self.add_properties_to_query()
        elif self.is_create=='FALSE':
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()


class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=CortexSearch(session=session,
                         user_id=user_id,
                         logger=logger)
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.set_base_attributes(kwargs=kwargs)

        obj_inst.logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.logger.info(f"{kwargs[tags.NAME]}")
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        obj_inst.logger.info("set base table")
        if tags.BASE_TABLE in kwargs.keys():
            obj_inst.logger.info(f"{kwargs[tags.BASE_TABLE]}")
            obj_inst.set_base_table(kwargs[tags.BASE_TABLE])
        else:
            obj_inst.set_base_table('NONE')

        obj_inst.logger.info("set on")
        if tags.ON in kwargs.keys():
            obj_inst.set_on(kwargs[tags.ON])
        else:
            obj_inst.set_on('NONE')

        obj_inst.logger.info("set ATTRIBUTES")
        if tags.ATTRIBUTES in kwargs.keys():
            obj_inst.set_attributes(kwargs[tags.ATTRIBUTES])
        else:
            obj_inst.set_attributes('NONE')

        obj_inst.logger.info("set WAREHOUSE")
        if tags.WAREHOUSE in kwargs.keys():
            obj_inst.set_warehouse(kwargs[tags.WAREHOUSE])
        else:
            obj_inst.set_warehouse('NONE')

        obj_inst.logger.info("set TARGET_LAG_UNIT")
        if tags.TARGET_LAG_UNIT in kwargs.keys():
            obj_inst.set_target_lag_unit(kwargs[tags.TARGET_LAG_UNIT])
        else:
            obj_inst.set_target_lag_unit('NONE')

        obj_inst.logger.info("set TARGET_LAG")
        if tags.TARGET_LAG in kwargs.keys():
            obj_inst.set_target_lag(kwargs[tags.TARGET_LAG])
        else:
            obj_inst.set_target_lag('NONE')

        obj_inst.logger.info("set EMBEDDING_MODEL")
        if tags.EMBEDDING_MODEL in kwargs.keys():
            obj_inst.set_embedding_model(kwargs[tags.EMBEDDING_MODEL])
        else:
            obj_inst.set_embedding_model('NONE')

        obj_inst.logger.info("set INITIALIZE")
        if tags.INITIALIZE in kwargs.keys():
            obj_inst.set_initialize(kwargs[tags.INITIALIZE])
        else:
            obj_inst.set_initialize('NONE') 

        obj_inst.logger.info("set QUERY")
        if tags.SERVICE_QUERY in kwargs.keys():
            obj_inst.set_service_query(kwargs[tags.SERVICE_QUERY])
        else:
            obj_inst.set_service_query('NONE') 

        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        obj_inst.print_query()

        obj_inst.logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry()
        
        obj_inst.write_file_to_git()

        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                           object_identifier=obj_inst.attr.name[0],
                                           qry=obj_inst.qry)

    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
