
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))

from vars.gvobject import Config as cfg

_dev_env = 'DEV'
_test_env = 'TEST'

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
    def __init__(self,session,logger):
        self.attr = DeployAttr()
        self.session = session
        self.logger = logger

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

    def create_entry(self,deploy_obj):
        self.set_object_type(deploy_obj.__class__.__name__)
        self.set_object_database(deploy_obj.attr.database)
        self.set_object_schema(deploy_obj.attr.schema)
        self.set_object_name(deploy_obj.attr.name)
        self.set_modified_by(deploy_obj.user_id)
        self.set_deployment_status(cfg._deployment_status_in_development)
        self.set_deployment_id('NA')
        self.insert_into_deploy_control_table()

    def get_ddl(self):
        if self.attr.object_type.upper() == 'DATABASE':
            ddl_qry = f""" select get_ddl('{self.attr.object_type}.upper()','{self.attr.object_name}')"""
        elif self.attr.object_type.upper() == 'SCHEMA':
            ddl_qry = f""" select get_ddl('{self.attr.object_type}.upper()','{self.attr.object_database}.{self.attr.object_name}')"""
        elif self.attr.object_type.upper() == 'WAREHOUSE':
            ddl_qry = f""" select get_ddl('{self.attr.object_type}.upper()','{self.attr.object_name}')"""
        else:
            ddl_qry = f""" select get_ddl('{self.attr.object_type}.upper()','{self.attr.object_database}.{self.attr.object_schema}.{self.attr.object_name}')"""
        
        self.session.sql(ddl_qry)

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

    def create_deploy_reference_table(self):
        qry = f"CREATE TABLE {cfg._config_database}.{cfg._config_schema}.{cfg._deployment_reference_table} ("
        for i in range(0,len(cfg._deployment_reference_table_column_list)):
            if i != len(cfg._deployment_reference_table_column_list) - 1:
                qry = qry + cfg._deployment_reference_table_column_list[i] + " " + cfg._deployment_reference_table_column_data_type_dict[cfg._deployment_reference_table_column_list[i]] + ","
            elif i == len(cfg._deployment_reference_table_column_list) - 1:
                qry = qry + cfg._deployment_reference_table_column_list[i] + " " + cfg._deployment_reference_table_column_data_type_dict[cfg._deployment_reference_table_column_list[i]] + ")"
        self.session.sql(qry).collect()  

    def create_deploy_scripts_table(self):
        qry = f"CREATE TABLE {cfg._config_database}.{cfg._config_schema}.{cfg._deployment_scripts_table} ("
        for i in range(0,len(cfg._deployment_scripts_table_column_list)):
            if i != len(cfg._deployment_scripts_table_column_list) - 1:
                qry = qry + cfg._deployment_scripts_table_column_list[i] + " " + cfg._deployment_scripts_table_column_data_type_dict[cfg._deployment_scripts_table_column_list[i]] + ","
            elif i == len(cfg._deployment_scripts_table_column_list) - 1:
                qry = qry + cfg._deployment_scripts_table_column_list[i] + " " + cfg._deployment_scripts_table_column_data_type_dict[cfg._deployment_scripts_table_column_list[i]] + ")"
        self.session.sql(qry).collect() 

    def insert_into_deploy_control_table(self):
        qry = f"""
            INSERT INTO 
            {cfg._config_database}.{cfg._config_schema}.{cfg._deployment_control_table} 
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

    @staticmethod
    def remove_escape_character_from_query(qry):
        qry=qry.replace("''","'")
        return qry
    
    @staticmethod
    def escape_single_quotes_from_sql_query(qry):
        qry=qry.replace("'","''")
        return qry    
    
    def insert_into_deployment_script_table(self,obj_qry,user_id):
        obj_qry = self.escape_single_quotes_from_sql_query(obj_qry)
        qry = f"""
            INSERT INTO 
            {cfg._config_database}.{cfg._config_schema}.{cfg._deployment_scripts_table}
            VALUES
            (
                '{obj_qry}',
                '{user_id}'
            )
            """
        self.session.sql(qry).collect()

    def get_db_name_of_environment(self,environment_name):
        get_database_name_qry = f"""
                                SELECT {cfg._deployment_reference_table_column_list[1]} 
                                FROM 
                                {cfg._config_database}.{cfg._config_schema}.{cfg._deployment_reference_table}
                                WHERE 
                                {cfg._deployment_reference_table_column_list[0]} = '{environment_name}'
                                """
        db_name = self.session.sql(get_database_name_qry).collect()
        return db_name[0][0]
    
    def get_scripts_to_deploy(self):
        qry = f"""
        SELECT 
            {cfg._deployment_scripts_table_column_list[0]} 
        FROM 
            {cfg._config_database}.{cfg._config_schema}.{cfg._deployment_scripts_table}
        """
        qry = self.remove_escape_character_from_query(qry=qry)
        res = self.session.sql(qry).collect()
        qry_lst = []
        for inner_qry in res:
            for qry in inner_qry:
                qry_lst.append(qry)
        clean_table = f"""
        DELETE FROM 
        {cfg._config_database}.{cfg._config_schema}.{cfg._deployment_scripts_table}
        """
        self.session.sql(clean_table).collect()
        return qry_lst
    
    def deploy_from_dev_to_test(self):
        dev_db = self.get_db_name_of_environment(_dev_env)
        test_db = self.get_db_name_of_environment(_test_env)
        self.logger.info("before getting scripts to deploy")
        sql_lst = self.get_scripts_to_deploy()
        self.logger.info(f"after getting scripts: {sql_lst}")
        for qry in sql_lst:
            qry = qry.replace(dev_db,test_db)
            self.session.sql(qry).collect()