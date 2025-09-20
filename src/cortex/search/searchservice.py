
import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

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

class CortexSearchAttrs:
    service_name=ServiceName()
    service_attributes=ServiceAttributes()
    service_warehouse=ServiceWarehouse()
    service_target_lag=ServiceTargetLag()
    service_embedding_model=ServiceEmbeddingModel()
    service_initialize=ServiceInitialize()
    service_commnet=ServiceComment()
    service_query=ServiceQuery()

class CortexSearch:
    def __init__(self,session):
        self.attr=CortexSearchAttrs()
        self.session=session

    def set_service_name(self,val=None):
        self.attr.service_name=val

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

    def set_service_commnet(self,val=None):
        self.attr.service_commnet=val

    def set_service_query(self,val=None):
        self.attr.service_query=val

    def create_object(self,*largs,**kwargs):
        self.logger.info(f'dictionary passed {kwargs}')

        if len(largs) != 0:
            self.logger.info(' list args passed')
            self.qry = f"CREATE OR REPLACE DATABASE {kwargs[tags.NAME]}"
            self.logger.info('calling create database')
            self.create_database()
            self.logger.info('granting default privileges')
            self.grant_default_privileges(*['initial'])
        else:
            self.logger.info('set name')
            self.set_name(kwargs[tags.NAME])

            self.logger.info('set DATA_RETENTION_TIME_IN_DAYS')
            self.set_data_retention_time_in_days(kwargs[tags.DATA_RETENTION_TIME_IN_DAYS])

            self.logger.info('set MAX_DATA_EXTENSION_TIME_IN_DAYS')
            self.set_max_data_extension_time_in_days(kwargs[tags.MAX_DATA_EXTENSION_TIME_IN_DAYS])

            self.logger.info('set EXTERNAL_VOLUME')
            self.set_external_volume(kwargs[tags.EXTERNAL_VOLUME])

            self.logger.info('set CATALOG')
            self.set_catalog(kwargs[tags.CATALOG])

            self.logger.info('set REPLACE_INVALID_CHARACTERS')
            self.set_replace_invalid_characters(kwargs[tags.REPLACE_INVALID_CHARACTERS])

            self.logger.info('set DEFAULT_DDL_COLLATION')
            self.set_default_ddl_collation(kwargs[tags.DEFAULT_DDL_COLLATION])

            self.logger.info('set LOG_LEVEL')
            self.set_log_level(kwargs[tags.LOG_LEVEL])

            self.logger.info('set TRACE_LEVEL')
            self.set_trace_level(kwargs[tags.TRACE_LEVEL])

            self.logger.info('set STORAGE_SERIALIZATION_POLICY')
            self.set_storage_serialization_policy(kwargs[tags.STORAGE_SERIALIZATION_POLICY])

            self.logger.info('set COMMENT')
            self.set_comment(kwargs[tags.COMMENT])

            self.logger.info('preapare query')
            self.prepare_query()

            self.logger.info('execute query')
            self.create_database()

            self.logger.info('grant default priv')
            self.grant_default_privileges()
            
            self.logger.info('create deployment entry')
            self.create_deployment_entry(object_name=self.attr.name,object_type=self.__class__.__name__,object_database='NA',object_schema='NA')

            self.logger.info('writing file to git')
            self.write_file_to_git(object_name=self.attr.name,object_type=self.__class__.__name__,object_database='NA',object_schema='NA')
