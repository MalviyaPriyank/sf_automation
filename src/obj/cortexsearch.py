import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from .baseobj import BaseObject
from vars.obj.cortexsearch.gvcortexsearch import CortexSearchTag as tags

class ServiceName:
    def __get__(self,instance,owner):
        return instance.__service_name
    
    def __set__(self,instance,value):
        instance.__service_name = value


    def __delete__(self,instance):
        del instance.__service_name

class ServiceAttributes:
    def __get__(self,instance,owner):
        return instance.__service_attributes
    
    def __set__(self,instance,value):
        instance.__service_attributes = value


    def __delete__(self,instance):
        del instance.__service_attributes


class ServiceWarehouse:
    def __get__(self,instance,owner):
        return instance.__service_warehouse
    
    def __set__(self,instance,value):
        instance.__service_warehouse = value


    def __delete__(self,instance):
        del instance.__service_warehouse

class ServiceTargetLag:
    def __get__(self,instance,owner):
        return instance.__service_target_lag
    
    def __set__(self,instance,value):
        instance.__service_target_lag = value


    def __delete__(self,instance):
        del instance.__service_target_lag

class ServiceEmbeddingModel:
    def __get__(self,instance,owner):
        return instance.__service_embedding_model
    
    def __set__(self,instance,value):
        instance.__service_embedding_model = value


    def __delete__(self,instance):
        del instance.__service_embedding_model

class ServiceInitialize:
    def __get__(self,instance,owner):
        return instance.__service_initialize
    
    def __set__(self,instance,value):
        instance.__service_initialize = value


    def __delete__(self,instance):
        del instance.__service_initialize

class ServiceComment:
    def __get__(self,instance,owner):
        return instance.__service_comment
    
    def __set__(self,instance,value):
        instance.__service_comment = value


    def __delete__(self,instance):
        del instance.__service_comment

class ServiceQuery:
    def __get__(self,instance,owner):
        return instance.__service_query
    
    def __set__(self,instance,value):
        instance.__service_query = value


    def __delete__(self,instance):
        del instance.__service_query

class ServiceOn:
    def __get__(self,instance,owner):
        return instance.__service_on
    
    def __set__(self,instance,value):
        instance.__service_on = value


    def __delete__(self,instance):
        del instance.__service_on

class CortexSearchAttrs:
    service_name=ServiceName()
    service_on=ServiceOn()
    service_attributes=ServiceAttributes()
    service_warehouse=ServiceWarehouse()
    service_target_lag=ServiceTargetLag()
    service_embedding_model=ServiceEmbeddingModel()
    service_initialize=ServiceInitialize()
    service_comment=ServiceComment()
    service_query=ServiceQuery()

class CortexSearch(BaseObject):
    def __init__(self,session,logger):
        self.attr=CortexSearchAttrs()
        self.session=session
        self.logger=logger

    def set_service_name(self,val=None):
        self.attr.service_name=val

    def set_service_on(self,val=None):
        self.attr.service_on=val

    def set_service_attributes(self,val=None):
        self.attr.service_attributes=val

    def set_service_warehouse(self,val=None):
        self.attr.service_warehouse=val

    def set_service_target_lag(self,val=None):
        self.attr.service_target_lag=val

    def set_service_embedding_model(self,val=None):
        self.attr.service_embedding_model=val

    def set_service_initialize(self,val=None):
        self.attr.service_initialize=val

    def set_service_comment(self,val=None):
        self.attr.service_comment=val

    def set_service_query(self,val=None):
        self.attr.service_query=val

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.NAME,"__service_name")
        set_flag(tags.ON,"__service_on")
        set_flag(tags.ATTRIBUTES,"__service_attributes")
        set_flag(tags.WAREHOUSE,"__service_warehouse")
        set_flag(tags.TARGET_LAG,"__service_target_lag")
        set_flag(tags.EMBEDDING_MODEL,"__service_embedding_model")
        set_flag(tags.INITIALIZE,"__service_initialize")
        set_flag(tags.COMMENT,"_comment")
        set_flag(tags.QUERY,"__service_query")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.ON:
                    self.qry = f" {self.qry} {tags.ON} = {self.attr.service_on} "
                if prop == tags.ATTRIBUTES:
                    self.qry = f" {self.qry} {tags.ATTRIBUTES} = {self.attr.service_attributes} "
                if prop == tags.WAREHOUSE:
                    self.qry = f" {self.qry} {tags.WAREHOUSE} = {self.attr.service_warehouse} "
                if prop == tags.TARGET_LAG:
                    self.qry = f" {self.qry} {tags.TARGET_LAG} = {self.attr.service_target_lag} "
                if prop == tags.EMBEDDING_MODEL:
                    self.qry = f" {self.qry} {tags.EMBEDDING_MODEL} = {self.attr.service_embedding_model} "
                if prop == tags.INITIALIZE:
                    self.qry = f" {self.qry} {tags.INITIALIZE} = {self.attr.service_initialize} "
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.service_comment} "
                if prop == tags.QUERY:
                    self.qry = f" {self.qry} AS {self.attr.service_query} "

    def set_create_cortex_search_qry(self):
        self.qry = f"CREATE CORTEX SEARCH SERVICE  {self.attr.service_name} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_cortex_search_qry()
        self.add_properties_to_query()

    def create_search_service(self):
        self.execute_final_query()

    def create_object(self,*largs,**kwargs):
        self.logger.info(f'dictionary passed {kwargs}')
        self.logger.info('set name')
        self.set_service_name(kwargs[tags.NAME])

        self.logger.info('set ATTRIBUTES')
        self.set_service_attributes(kwargs[tags.ATTRIBUTES])

        self.logger.info('set WAREHOUSE')
        self.set_service_warehouse(kwargs[tags.WAREHOUSE])

        self.logger.info('set TARGET_LAG')
        self.set_service_target_lag(kwargs[tags.TARGET_LAG])

        self.logger.info('set EMBEDDING_MODEL')
        self.set_service_embedding_model(kwargs[tags.EMBEDDING_MODEL])

        self.logger.info('set INITIALIZE')
        self.set_service_initialize(kwargs[tags.INITIALIZE])

        self.logger.info('set COMMENT')
        self.set_service_commnet(kwargs[tags.COMMENT])

        self.logger.info('set QUERY')
        self.set_service_query(kwargs[tags.QUERY])

        self.logger.info('preapare query')
        self.prepare_query()

        self.logger.info('execute query')
        self.create_search_service()
        
        self.logger.info('create deployment entry')
        self.create_deployment_entry(object_name=self.attr.service_name,object_type=self.__class__.__name__,object_database='NA',object_schema='NA')

        self.logger.info('writing file to git')
        self.write_file_to_git(object_name=self.attr.service_name,object_type=self.__class__.__name__,object_database='NA',object_schema='NA')
