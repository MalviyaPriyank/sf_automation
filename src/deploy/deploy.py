
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))

from vars.global_vars import Config as cfg


class ObjectType:
    def __get__(self,instance,owner):
        return instance._object_type
    
    def __set__(self,instance,value):
        instance._object_type = value

    def __delete__(self,instance):
        del instance._object_type

class ObjectDatabase:
    def __get__(self,instance,owner):
        return instance._object_database
    
    def __set__(self,instance,value):
        instance._object_database = value

    def __delete__(self,instance):
        del instance._object_database

class ObjectSchema:
    def __get__(self,instance,owner):
        return instance._object_schema
    
    def __set__(self,instance,value):
        instance._object_schema = value

    def __delete__(self,instance):
        del instance._object_schema

class ObjectName:
    def __get__(self,instance,owner):
        return instance._object_name
    
    def __set__(self,instance,value):
        instance._object_name = value

    def __delete__(self,instance):
        del instance._object_name

class ModifiedBy:
    def __get__(self,instance,owner):
        return instance._modified_by
    
    def __set__(self,instance,value):
        instance._modified_by = value

    def __delete__(self,instance):
        del instance._modified_by

class DeploymentStatus:
    def __get__(self,instance,owner):
        return instance._deployment_status
    
    def __set__(self,instance,value):
        instance._deployment_status = value

    def __delete__(self,instance):
        del instance._deployment_status


class DeploymentID:
    def __get__(self,instance,owner):
        return instance._deployment_id
    
    def __set__(self,instance,value):
        instance._deployment_id = value

    def __delete__(self,instance):
        del instance._deployment_id

class DeployAttr:
    object_type = ObjectType()
    object_database = ObjectDatabase()
    object_schema = ObjectSchema()
    object_name = ObjectName()
    modified_by = ModifiedBy()
    deployment_status = DeploymentStatus()
    deployment_id = DeploymentID()

class Deploy:
    def __init__(self,session):
        self.attr = DeployAttr()
        self.session = session

    def set_object_type(self,value):
        self.attr.object_type = value

    def set_object_database(self,value):
        self.attr.object_database = value

    def set_object_schema(self,value):
        self.attr.object_schema = value

    def set_object_name(self,value):
        self.attr.object_name = value

    def set_modified_by(self,value):
        self.attr.modified_by = value

    def set_deployment_status(self,value):
        self.attr.deployment_status = value

    def set_deployment_id(self,value):
        self.attr.deployment_id = value

    def create_deploy_control_table(self):
        qry = f"CREATE TABLE {cfg._config_database}.{cfg._config_schema}.{cfg._deployment_control_table} ("
        for i in range(0,len(cfg._deployment_control_table_column_list)):
            if i != len(cfg._deployment_control_table_column_list) - 1:
                qry = qry + cfg._deployment_control_table_column_list[i] + " " + cfg._deployment_control_table_column_data_type_dict[cfg._deployment_control_table_column_list[i]] + ","
            elif i == len(cfg._deployment_control_table_column_list) - 1:
                qry = qry + cfg._deployment_control_table_column_list[i] + " " + cfg._deployment_control_table_column_data_type_dict[cfg._deployment_control_table_column_list[i]] + ")"
        self.session.sql(qry).collect() 

    def create_deploy_history_table(self):
        qry = f"CREATE TABLE {cfg._config_database}.{cfg._config_schema}.{cfg._deployment_history_table} ("
        for i in range(0,len(cfg._deployment_history_table_column_list)):
            if i != len(cfg._deployment_history_table_column_list) - 1:
                qry = qry + cfg._deployment_history_table_column_list[i] + " " + cfg._deployment_history_table_column_data_type_dict[cfg._deployment_history_table_column_list[i]] + ","
            elif i == len(cfg._deployment_history_table_column_list) - 1:
                qry = qry + cfg._deployment_history_table_column_list[i] + " " + cfg._deployment_history_table_column_data_type_dict[cfg._deployment_history_table_column_list[i]] + ")"
        self.session.sql(qry).collect() 

    def create_deploy_log_table(self):
        qry = f"CREATE TABLE {cfg._config_database}.{cfg._config_schema}.{cfg._deployment_log_table} ("
        for i in range(0,len(cfg._deployment_log_table_column_list)):
            if i != len(cfg._deployment_log_table_column_list) - 1:
                qry = qry + cfg._deployment_log_table_column_list[i] + " " + cfg._deployment_log_table_column_data_type_dict[cfg._deployment_log_table_column_list[i]] + ","
            elif i == len(cfg._deployment_log_table_column_list) - 1:
                qry = qry + cfg._deployment_log_table_column_list[i] + " " + cfg._deployment_log_table_column_data_type_dict[cfg._deployment_log_table_column_list[i]] + ")"
        self.session.sql(qry).collect()  

    def insert_into_deploy_control_table(self):
        qry = f"""
            INSERT INTO {cfg._config_database}.{cfg._config_schema}.{cfg._deployment_control_table} 
             VALUES 
             (
             '{self.attr.object_type}',
             '{self.attr.object_database}',
             '{self.attr.object_schema}',
             '{self.attr.object_name}',
             '{self.attr.modified_by}',
             '{self.attr.deployment_status}',
             '{self.attr.deployment_id}'
             )
        """     
        self.session.sql(qry).collect() 

    def move_records_to_deployment_history_table(self,env):





        
