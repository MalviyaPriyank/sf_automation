import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from setup import privilege
from .baseobj import BaseObject 
from dep import deploy
from snowflake.snowpark.functions import col
from src.vars.obj.openflow.gvopenflow import OpenFlowTag as tags
from src.usr.user import ChatHistory

class OpenFlowAdminRole:
    def __get__(self,instance,owner):
        return instance._open_flow_admin_role
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vo.role_exist(session=instance.parent.session,
                      role_name=value)
        instance._open_flow_admin_role=value

    def __del__(self,instance):
        del instance._open_flow_admin_role

class OpenFlowUserRole:
    def __get__(self,instance,owner):
        return instance._open_flow_user_role
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vo.role_exist(session=instance.parent.session,
                      role_name=value)
        instance._open_flow_user_role=value

    def __del__(self,instance):
        del instance._open_flow_user_role

class OpenFlowUser:
    def __get__(self,instance,owner):
        return instance._open_flow_user
    
    def __set__(self,instance,value):
        vo.user_exist(session=instance.parent.session,user_name=value)
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        instance._open_flow_user=value

    def __del__(self,instance):
        del instance._open_flow_user

class EventTableDatabase:
    def __get__(self,instance,owner):
        return instance._event_table_database
    
    def __set__(self,instance,value):
        vo.database_exist(session=instance.parent.session,
                          database_name=value)
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        instance._event_table_database=value

    def __del__(self,instance):
        del instance._event_table_database

class EventTableSchema:
    def __get__(self,instance,owner):
        return instance._event_table_schema
    
    def __set__(self,instance,value):
        vo.schema_exist(session=instance.parent.session,
                        database_name=instance._event_table_database,
                        schema_name=value)
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        instance._event_table_schema=value

    def __del__(self,instance):
        del instance._event_table_schema

class OpenFlowRunTimeRole:
    def __get__(self,instance,owner):
        return instance._open_flow_run_time_role
    
    def __set__(self,instance,value):
        instance._open_flow_run_time_role=value

    def __del__(self,instance):
        del instance._open_flow_run_time_role

class OpenFlowWarehouse:
    def __get__(self,instance,owner):
        return instance._open_flow_warehouse
    
    def __set__(self,instance,value):
        vo.warehouse_exist(session=instance.parent.session,
                           warehouse_name=value)
        instance._open_flow_warehouse=value

    def __del__(self,instance):
        del instance._open_flow_warehouse
 
class NetworkRuleName:
    def __get__(self,instance,owner):
        return instance._network_rule_name
    
    def __set__(self,instance,value):
        instance._network_rule_name=value

    def __del__(self,instance):
        del instance._network_rule_name 

class Host:
    def __get__(self,instance,owner):
        return instance._host
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        instance._host=value

    def __del__(self,instance):
        del instance._host 

class Port:
    def __get__(self,instance,owner):
        return instance._port
    
    def __set__(self,instance,value):
        instance._port=value

    def __del__(self,instance):
        del instance._port 

class OpenFlowSchema:
    def __get__(self,instance,owner):
        return instance._open_flow_schema
    
    def __set__(self,instance,value):
        instance._open_flow_schema=value

    def __del__(self,instance):
        del instance._open_flow_schema 

class OpenFlowDatabase:
    def __get__(self,instance,owner):
        return instance._open_flow_database
    
    def __set__(self,instance,value):
        instance._open_flow_database=value

    def __del__(self,instance):
        del instance._open_flow_database 

class OpenFlowImage:
    def __get__(self,instance,owner):
        return instance._open_flow_image
    
    def __set__(self,instance,value):
        instance._open_flow_image=value

    def __del__(self,instance):
        del instance._open_flow_image 

class OpenFlowExternalAccessIntegrationName:
    def __get__(self,instance,owner):
        return instance._open_flow_external_access_integration_name
    
    def __set__(self,instance,value):
        instance._open_flow_external_access_integration_name=value

    def __del__(self,instance):
        del instance._open_flow_external_access_integration_name 

class OpenFlowAttrs:
    def __init__(self,parent):
        self.parent=parent
    open_flow_admin_role=OpenFlowAdminRole()
    open_flow_user_role=OpenFlowUserRole()
    open_flow_user=OpenFlowUser()
    open_flow_database=OpenFlowDatabase()
    open_flow_schema=OpenFlowSchema()
    open_flow_image=OpenFlowImage()
    event_table_database=EventTableDatabase()
    event_table_schema=EventTableSchema()
    open_flow_runtime_role=OpenFlowRunTimeRole()
    open_flow_warehouse=OpenFlowWarehouse()
    network_rule_name=NetworkRuleName()
    open_flow_external_access_integration_name=OpenFlowExternalAccessIntegrationName()
    host=Host()
    port=Port()

class OpenFlow:
    def __init__(self,session,logger):
        self.attr=OpenFlowAttrs(self)
        self.session=session
        self.logger=logger.getChild(self.__class__.__name__)

    def set_open_flow_admin_role(self,val):
        self.attr.open_flow_admin_role=val

    def set_open_flow_user_role(self,val):
        self.attr.open_flow_user_role=val

    def set_open_flow_user(self,val):
        self.attr.open_flow_user=val

    def execute_sql(self,qry):
        self.session.sql(qry).collect()

    def get_list_of_open_flow_data_plane(self):
        df=self.session.sql("SHOW OPENFLOW DATA PLANE INTEGRATIONS")
        df=df.select(col("*")).collect()
        df=self.session.create_dataframe(df)
        df=df.select(col("name")).collect()
        name_lst = [name for row in df for name in row]
        return name_lst


    def configure_event_table(self):
        self.execute_sql(f"GRANT USAGE ON DATABASE {self.attr.event_table_database} TO ROLE {self.attr.open_flow_admin_role}")
        self.execute_sql(f"GRANT USAGE ON SCHEMA  TO ROLE {self.attr.open_flow_admin_role}")
        self.execute_sql(f"GRANT CREATE EVENT TABLE ON SCHEMA {self.attr.event_table_database}.{self.attr.event_table_schema} TO ROLE {self.attr.open_flow_admin_role}")
        self.execute_sql(f"USE ROLE {self.attr.open_flow_admin_role}")
        self.execute_sql(f"CREATE EVENT TABLE IF NOT EXISTS {self.attr.event_table_database}.{self.attr.event_table_schema}.EVENTS")
        self.execute_sql(f"USE ROLE ACCOUNTADMIN")
        self.logger.info("getting data flow planes")
        data_plane_lst=self.get_list_of_open_flow_data_plane()
        self.logger.info(f"creating event table for {data_plane_lst}")
        for planes in data_plane_lst:
            self.execute_sql(f"ALTER OPENFLOW DATA PLANE INTEGRATION {planes} SET EVENT_TABLE = {self.attr.open_flow_database}.{self.attr.open_flow_schema}.EVENTS")
        
    def configure_runtime_role(self):
        self.execute_sql(f"USE ROLE {self.attr.open_flow_admin_role}")
        self.execute_sql(f"CREATE ROLE IF NOT EXISTS {self.attr.open_flow_runtime_role}")
        self.execute_sql(f"GRANT ROLE {self.attr.open_flow_runtime_role} TO ROLE {self.attr.open_flow_admin_role}")
        self.execute_sql(f"GRANT USAGE, OPERATE ON WAREHOUSE {self.attr.open_flow_warehouse} TO ROLE {self.attr.open_flow_runtime_role}")
        self.execute_sql(f"GRANT USAGE ON DATABASE {self.attr.open_flow_database} TO ROLE {self.attr.open_flow_runtime_role}")
        self.execute_sql(f"GRANT USAGE ON SCHEMA {self.attr.open_flow_schema} TO ROLE {self.attr.open_flow_runtime_role}")


    def setup_admin_role(self):
        self.logger.info("Creating admin role")
        self.execute_sql(f"CREATE ROLE IF NOT EXISTS {self.attr.open_flow_admin_role}")
        self.execute_sql(f"GRANT CREATE ROLE ON ACCOUNT TO ROLE {self.attr.open_flow_admin_role}")
        self.execute_sql(f"GRANT CREATE OPENFLOW DATA PLANE INTEGRATION ON ACCOUNT TO ROLE {self.attr.open_flow_admin_role}")
        self.execute_sql(f"GRANT CREATE OPENFLOW RUNTIME INTEGRATION ON ACCOUNT TO ROLE {self.attr.open_flow_admin_role}")
        self.execute_sql(f"GRANT CREATE COMPUTE POOL ON ACCOUNT TO ROLE {self.attr.open_flow_admin_role}")
        self.logger.info("admin role created and grants executed")

    def configure_user_for_admin_role(self):
        self.logger.info(f"Configuring open flow for user :{self.attr.open_flow_user}")
        self.execute_sql(f"GRANT ROLE {self.attr.open_flow_admin_role} TO USER {self.attr.open_flow_user}")
        self.execute_sql(f"ALTER USER {self.attr.open_flow_user} SET DEFAULT_ROLE = {self.attr.open_flow_admin_role}")
        self.execute_sql(f"ALTER USER {self.attr.open_flow_user} SET DEFAULT_SECONDARY_ROLES = ('ALL')")
        self.logger.info(f"{self.attr.open_flow_user} user configured for open flow")

    def create_database_schema_and_stage(self):
        self.logger.info(f"creating dataabase schema and image")
        self.execute_sql(f"CREATE DATABASE IF NOT EXISTS {self.attr.open_flow_database}")
        self.execute_sql(f"CREATE SCHEMA IF NOT EXISTS {self.attr.open_flow_database}.{self.attr.open_flow_schema}")
        self.execute_sql(f"CREATE IMAGE REPOSITORY IF NOT EXISTS {self.attr.open_flow_database}.{self.attr.open_flow_schema}.{self.attr.open_flow_image}")
        self.logger.info("Database schema and image created, granting privileges")
        self.execute_sql(f"GRANT USAGE ON DATABASE {self.attr.open_flow_database} TO ROLE PUBLIC")
        self.execute_sql(f"GRANT USAGE ON SCHEMA {self.attr.open_flow_schema} TO ROLE PUBLIC")
        self.execute_sql(f"GRANT READ ON IMAGE REPOSITORY {self.attr.open_flow_database}.{self.attr.open_flow_schema}.{self.attr.open_flow_image} TO ROLE PUBLIC")
        self.logger.info("Privileges granted, enabling the bundle")
        self.execute_sql(f"call SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE('2025_06')")


    def configure_core_snowflake(self):
        self.setup_admin_role()
        self.configure_user_for_admin_role()
        self.create_database_schema_and_stage()

        #create deployment
        self.configure_event_table()

        #craete runtime role
        self.configure_runtime_role()

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=OpenFlow(session=session,
                         user_id=user_id,
                         logger=logger)
        
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]


        if len(largs) != 0:
            obj_inst.logger.info(' list args passed')
            obj_inst.qry = f"CREATE OR REPLACE DATABASE {kwargs[tags.NAME]}"
            obj_inst.logger.info('calling create database')
            obj_inst.create_database()
            obj_inst.logger.info('granting default privileges')
            #self.grant_default_privileges(*['initial'])
        else:
            obj_inst.logger.info('set name')
            obj_inst.set_name(kwargs[tags.NAME])

            obj_inst.logger.info('set DATA_RETENTION_TIME_IN_DAYS')
            if tags.DATA_RETENTION_TIME_IN_DAYS in  kwargs.keys(): 
                obj_inst.set_data_retention_time_in_days(kwargs[tags.DATA_RETENTION_TIME_IN_DAYS])
            else:
                obj_inst.set_data_retention_time_in_days("NONE")

            obj_inst.logger.info('set MAX_DATA_EXTENSION_TIME_IN_DAYS')
            if tags.MAX_DATA_EXTENSION_TIME_IN_DAYS in kwargs.keys():
                obj_inst.set_max_data_extension_time_in_days(kwargs[tags.MAX_DATA_EXTENSION_TIME_IN_DAYS])
            else:
                obj_inst.set_max_data_extension_time_in_days("NONE")

            obj_inst.logger.info('set EXTERNAL_VOLUME')
            if tags.EXTERNAL_VOLUME in kwargs.keys():
                obj_inst.set_external_volume(kwargs[tags.EXTERNAL_VOLUME])
            else:
                obj_inst.set_external_volume("NONE")

            obj_inst.logger.info('set CATALOG')
            if tags.CATALOG in kwargs.keys():
                obj_inst.set_catalog(kwargs[tags.CATALOG])
            else:
                obj_inst.set_catalog("NONE")

            obj_inst.logger.info('set REPLACE_INVALID_CHARACTERS')
            if tags.REPLACE_INVALID_CHARACTERS in kwargs.keys():
                obj_inst.set_replace_invalid_characters(kwargs[tags.REPLACE_INVALID_CHARACTERS])
            else:
                obj_inst.set_replace_invalid_characters("NONE")

            obj_inst.logger.info('set DEFAULT_DDL_COLLATION')
            if tags.DEFAULT_DDL_COLLATION in kwargs.keys():
                obj_inst.set_default_ddl_collation(kwargs[tags.DEFAULT_DDL_COLLATION])
            else:
                obj_inst.set_default_ddl_collation("NONE")

            obj_inst.logger.info('set LOG_LEVEL')
            if tags.LOG_LEVEL in kwargs.keys():
                obj_inst.set_log_level(kwargs[tags.LOG_LEVEL])
            else:
                obj_inst.set_log_level("NONE")

            obj_inst.logger.info('set TRACE_LEVEL')
            if tags.TRACE_LEVEL in kwargs.keys():
                obj_inst.set_trace_level(kwargs[tags.TRACE_LEVEL])
            else:
                obj_inst.set_trace_level("NONE")

            obj_inst.logger.info('set STORAGE_SERIALIZATION_POLICY')
            if tags.STORAGE_SERIALIZATION_POLICY in kwargs.keys():
                obj_inst.set_storage_serialization_policy(kwargs[tags.STORAGE_SERIALIZATION_POLICY])
            else:
                obj_inst.set_storage_serialization_policy("NONE")

            obj_inst.logger.info('set COMMENT')
            if tags.COMMENT in kwargs.keys():
                obj_inst.set_comment(kwargs[tags.COMMENT])
            else:
                obj_inst.set_comment("NONE")

            obj_inst.logger.info('preapare query')
            obj_inst.prepare_query()

            if kwargs[tags.IS_CREATE] == "TRUE":
                obj_inst.logger.info('execute query')
                obj_inst.create_database()

                obj_inst.logger.info('grant default priv')
                #self.grant_default_privileges()
                
                obj_inst.logger.info('create deployment entry')
                obj_inst.create_deployment_entry(object_name=obj_inst.attr.name[0],object_type=obj_inst.__class__.__name__,object_database='NA',object_schema='NA')

                obj_inst.logger.info('writing file to git')
                obj_inst.write_file_to_git(object_name=obj_inst.attr.name[0],object_type=obj_inst.__class__.__name__,object_database='NA',object_schema='NA')

                user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                                object_identifier=obj_inst.attr.name[0],
                                                qry=obj_inst.qry)

    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()







