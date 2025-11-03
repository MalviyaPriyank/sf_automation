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

class OpenFlowAdminRole:
    def __get__(self,instance,owner):
        return instance._open_flow_admin_role
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
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
        vo.database_exist(session=instance.parent.session,
                          database_name=value)
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




