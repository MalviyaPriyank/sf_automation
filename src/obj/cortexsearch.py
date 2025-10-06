import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from .baseobj import BaseObject
from vars.obj.cortexsearch.gvcortexsearch import CortexSearchTag as tags

class ServiceName:
    # validate : task
    def __get__(self,instance,owner):
        return instance._name

    def __set__(self,instance,value):
        instance._name = value

    def __delete__(self,instance):
        del instance._name

class ServiceAttributes:
    def __get__(self,instance,owner):
        return instance._service_attributes
    
    def __set__(self,instance,value):
        instance._service_attributes = value


    def __delete__(self,instance):
        del instance._service_attributes


class ServiceWarehouse:
    def __get__(self,instance,owner):
        return instance._warehouse
    
    def __set__(self,instance,value):
        instance._warehouse = value


    def __delete__(self,instance):
        del instance._warehouse

class ServiceTargetLag:
    def __get__(self,instance,owner):
        return instance._target_lag
    
    def __set__(self,instance,value):
        instance._target_lag = f"'{value}'"


    def __delete__(self,instance):
        del instance._target_lag

class ServiceEmbeddingModel:
    def __get__(self,instance,owner):
        return instance._embedding_model
    
    def __set__(self,instance,value):
        instance._embedding_model = f"'{value}'"


    def __delete__(self,instance):
        del instance._embedding_model

class ServiceInitialize:
    def __get__(self,instance,owner):
        return instance._initialize
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._initialize='ON_CREATE'
        else:
            instance._initialize = value


    def __delete__(self,instance):
        del instance._initialize

class ServiceQuery:
    def __get__(self,instance,owner):
        return instance._query
    
    def __set__(self,instance,value):
        instance._query = value


    def __delete__(self,instance):
        del instance._query

class ServiceOn:
    def __get__(self,instance,owner):
        return instance._on
    
    def __set__(self,instance,value):
        instance._on = value


    def __delete__(self,instance):
        del instance._on

class CortexSearchAttrs:
    name=ServiceName()
    on=ServiceOn()
    service_attributes=ServiceAttributes()
    warehouse=ServiceWarehouse()
    target_lag=ServiceTargetLag()
    embedding_model=ServiceEmbeddingModel()
    initialize=ServiceInitialize()
    query=ServiceQuery()

class CortexSearch(BaseObject):
    def __init__(self,session,user_id,logger):
        self.attr=CortexSearchAttrs()
        self.session=session
        self.logger=logger
        self.user_id=user_id

    def set_name(self,val=None):
        self.attr.name=val

    def set_on(self,val=None):
        self.attr.on=val

    def set_service_attributes(self,val=None):
        self.attr.service_attributes=val

    def set_warehouse(self,val=None):
        self.attr.warehouse=val

    def set_target_lag(self,val=None):
        self.attr.target_lag=val

    def set_embedding_model(self,val=None):
        self.attr.embedding_model=val

    def set_initialize(self,val=None):
        self.attr.initialize=val


    def set_query(self,val=None):
        self.attr.query=val

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.ON,"on")
        set_flag(tags.ATTRIBUTES,"service_attributes")
        set_flag(tags.WAREHOUSE,"warehouse")
        set_flag(tags.TARGET_LAG,"target_lag")
        set_flag(tags.EMBEDDING_MODEL,"embedding_model")
        set_flag(tags.INITIALIZE,"initialize")
        set_flag(tags.QUERY,"query")

    def alter_object(self):        
        for prop in self.property_lst:
            if prop == tags.ON:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.ON} = {self.attr.on}"
                self.execute_final_query()
            if prop == tags.ATTRIBUTES:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.ATTRIBUTES} = {self.attr.service_attributes}"
                self.execute_final_query()
            if prop == tags.WAREHOUSE:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.WAREHOUSE} = {self.attr.warehouse}"
                self.execute_final_query()
            if prop == tags.TARGET_LAG:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.TARGET_LAG} = {self.attr.target_lag}"
                self.execute_final_query()
            if prop == tags.EMBEDDING_MODEL:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.EMBEDDING_MODEL} = {self.attr.embedding_model}"
                self.execute_final_query()
            if prop == tags.INITIALIZE:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.INITIALIZE} = {self.attr.initialize}"
                self.execute_final_query()
            if prop == tags.QUERY:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.QUERY} = {self.attr.query}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER {self.__class__.__name__.upper()} {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming database {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.ON:
                    self.qry = f" {self.qry} {tags.ON}  {self.attr.on} "
                if prop == tags.ATTRIBUTES:
                    self.qry = f" {self.qry} {tags.ATTRIBUTES}  {self.attr.service_attributes} "
                if prop == tags.WAREHOUSE:
                    self.qry = f" {self.qry} {tags.WAREHOUSE} = {self.attr.warehouse} "
                if prop == tags.TARGET_LAG:
                    self.qry = f" {self.qry} {tags.TARGET_LAG} = {self.attr.target_lag} "
                if prop == tags.EMBEDDING_MODEL:
                    self.qry = f" {self.qry} {tags.EMBEDDING_MODEL} = {self.attr.embedding_model} "
                if prop == tags.INITIALIZE:
                    self.qry = f" {self.qry} {tags.INITIALIZE} = {self.attr.initialize} "
                if prop == tags.QUERY:
                    self.qry = f" {self.qry} AS ({self.attr.query} )"

    def set_create_cortex_search_qry(self):
        self.qry = f"CREATE CORTEX SEARCH SERVICE CRM_DEV_DB.SALES.{self.attr.name[0]} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == 'TRUE':
            self.set_create_cortex_search_qry()
            self.add_properties_to_query()
        elif self.is_create=='FALSE':
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()

    def create_search_service(self):
        self.execute_final_query()

    def create_object(self,*largs,**kwargs):
        self.logger.info(f"Operating on {self.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        self.logger.info(f'dictionary passed {kwargs}')
        self.is_create=kwargs[tags.IS_CREATE]

        self.set_name(kwargs[tags.NAME])

        self.set_on(kwargs[tags.ON])
        self.logger.info('set ATTRIBUTES')
        self.set_service_attributes(kwargs[tags.ATTRIBUTES])

        self.logger.info('set WAREHOUSE')
        self.set_warehouse(kwargs[tags.WAREHOUSE])

        self.logger.info('set TARGET_LAG')
        self.set_target_lag(kwargs[tags.TARGET_LAG])

        self.logger.info('set EMBEDDING_MODEL')
        self.set_embedding_model(kwargs[tags.EMBEDDING_MODEL])

        self.logger.info('set INITIALIZE')
        self.set_initialize(kwargs[tags.INITIALIZE])

        self.logger.info('set QUERY')
        self.set_query(kwargs[tags.QUERY])

        self.logger.info('preapare query')
        self.prepare_query()

        self.logger.info('execute query')
        self.create_search_service()