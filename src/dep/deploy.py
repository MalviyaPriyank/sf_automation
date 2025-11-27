
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))

from vars.gvobject import Config as cfg
import uuid
from datetime import datetime
from validation.validatedeployment import ValidateDeployment as vd

_dev_env = 'DEV'
_test_env = 'TEST'
_bronze_env='BRONZE'
_silver_env='SILVER'


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

class Query:
    def __get__(self,instance,owner):
        return instance._query
    
    def __set__(self,instance,value):
        instance._query = value

    def __delete__(self,instance):
        del instance._query

class DeployAttr:
    object_type = ObjectType()
    object_database = ObjectDatabase()
    object_schema = ObjectSchema()
    object_name = ObjectName()
    modified_by = ModifiedBy()
    deployment_status = DeploymentStatus()
    deployment_id = DeploymentID()
    query=Query()

class Deploy:
    def __init__(self,session,logger):
        self.attr = DeployAttr()
        self.session = session
        self.logger = logger
        self.deploy_id=str(uuid.uuid4())

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

    def set_query(self,value):
        self.attr.query=value

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
        current_time=datetime.now()
        qry = f"""
            INSERT INTO 
            {cfg._config_database}.{cfg._config_schema}.DEPLOYMENT_DTLS 
             VALUES 
             (
             '{self.deploy_id}',
             '{self.attr.object_type}',
             '{self.attr.object_database}',
             '{self.attr.object_schema}',
             '{self.attr.object_name}',
             '{self.attr.modified_by}',
             '{self.attr.deployment_status}',
             '{self.attr.query}',
             '{current_time}'
             )
        """     
        self.session.sql(qry).collect()

    @staticmethod
    def remove_escape_character_from_query(qry):
        qry=qry.replace("''","'")
        return qry

    def run_query(self,qry):
        self.session.sql(qry).collect()
    
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
    
    def __get_scripts_to_deploy(self,src_db,**kwargs):
        if 'OBJECT' in kwargs.keys():
            qry = f"""
            SELECT
                sql_text
                ,deploy_id
            FROM 
                {cfg._config_database}.{cfg._config_schema}.DEPLOYMENT_DTLS
            WHERE 
                object_name='{src_db}'
            AND
                deployment_status='{cfg._deployment_status_in_development}'
            UNION
            SELECT 
                sql_text
                ,deploy_id
            FROM 
                {cfg._config_database}.{cfg._config_schema}.DEPLOYMENT_DTLS
            WHERE
                object_database='{src_db}'
            AND
                object_type='{kwargs['OBJECT']}',
                deployment_status='{cfg._deployment_status_in_development}'
            ORDER BY ENTRY_TIMESTAMP
            """
        else:
            qry = f"""
            SELECT
                sql_text
                ,deploy_id
            FROM 
                {cfg._config_database}.{cfg._config_schema}.DEPLOYMENT_DTLS
            WHERE 
                object_name='{src_db}'
            AND
                deployment_status='{cfg._deployment_status_in_development}'
            UNION
            SELECT 
                sql_text
                ,deploy_id
            FROM 
                {cfg._config_database}.{cfg._config_schema}.DEPLOYMENT_DTLS
            WHERE
                object_database='{src_db}'
            AND
                deployment_status='{cfg._deployment_status_in_development}'
            """
        
        res = self.session.sql(qry).collect()
        qry_lst = []
        id_lst=[]
        for inner_qry in res:
            qry_lst.append(inner_qry[0])
            id_lst.append(inner_qry[1])
        return qry_lst,id_lst


    def __get_all_objects_ready_for_deployment(self,deployment_status):
        qry=f"""
        SELECT
        DISTINCT OBJECT_TYPE
        FROM 
        {cfg._config_database}.{cfg._config_schema}.DEPLOYMENT_DTLS
        WHERE
        DEPLOYMENT_STATUS = '{deployment_status}'
        """
        object_types=self.session.sql(qry).collect()
        return object_types
    
    def clean_deployment_table(self):
        clean_table = f"""
        DELETE FROM 
        {cfg._config_database}.{cfg._config_schema}.{cfg._deployment_scripts_table}
        """
        self.session.sql(clean_table).collect()

    def __update_record_deployment_dtls(self,id):
        self.logger.info(f"updating entry for {id}")
        qry=f"""
        UPDATE
            {cfg._config_database}.{cfg._config_schema}.DEPLOYMENT_DTLS
        SET
            deployment_status='{cfg._deployment_status_in_test}'
        WHERE 
            deploy_id='{id}' 
        """
        self.run_query(qry=qry)

    def deploy_from_dev_to_test(self,**kwargs):
        #dev_db = self.get_db_name_of_environment(_dev_env)
        #test_db = self.get_db_name_of_environment(_test_env)

        src_db=kwargs['SRC_DB']
        tgt_db=kwargs['TGT_DB']
        self.logger.info(f"deploying from {src_db} to {tgt_db}")
        if 'OBJECT_LST' in kwargs:
            self.logger.info(f" for objects : {kwargs['OBJECT_LST']}")
            object_lst=kwargs['OBJECT_LST']
        
        if len(object_lst):
            for obj in object_lst:
                self.logger.info(f" getting scripts for {obj}")
                sql_lst,id_lst = self.__get_scripts_to_deploy(src_db,**{'OBJECT':obj})
                vd.scripts_exist(
                    lst=sql_lst,
                    deployment_status=f'{cfg._deployment_status_in_development}',
                    src_db=src_db,
                    **{'OBJECT':obj}
                )
                for i in range(0,len(sql_lst)):
                    qry=sql_lst[i]
                    id=id_lst[i]
                    self.logger.info(f"deploying: {qry}")
                    self.logger.info(f"id  : {id}")
                    if src_db.upper() in qry.upper():
                        qry=qry.replace(src_db,tgt_db)
                        self.run_query(qry=qry)
                        self.__update_record_deployment_dtls(id=id)
                        self.logger.info(f" deployed : {id}")
                    else:
                        self.logger.info(f"{src_db.upper()} not found id {qry.upper()} ") 
                    self.logger.info(f"All scripts deployed successfully for {obj} ")
            self.logger.info("All objects deployed successfully")
        else:
            self.logger.info(f"deploying all objects for {src_db}")
            sql_lst,id_lst = self.__get_scripts_to_deploy(src_db)
            vd.scripts_exist(
                lst=sql_lst,
                deployment_status=f'{cfg._deployment_status_in_development}',
                src_db=src_db
            )
            for i in range(0,len(sql_lst)):
                qry=sql_lst[i]
                id=id_lst[i]
                self.logger.info(f"deploying: {qry}")
                self.logger.info(f"id  : {id}")
                if src_db.upper() in qry.upper():
                    qry=qry.replace(src_db,tgt_db)
                    self.run_query(qry=qry)
                    self.__update_record_deployment_dtls(id=id)
                    self.logger.info(f" deployed : {id}")
                else:
                    self.logger.info(f"{src_db.upper()} not found id {qry.upper()} ")
            self.logger.info(f" Deployment successfull for {src_db}")
        return 'Deployment Successful'

    def track_development(self,qry,user_id,object_type,object_database,object_schema,object_name):
        self.insert_into_deployment_script_table(obj_qry=qry, user_id=user_id)
        self.set_object_type(object_type)
        qry=self.escape_single_quotes_from_sql_query(qry=qry)
        self.set_query(value=qry)
        self.set_object_database(object_database)
        self.set_object_schema(object_schema)
        self.set_object_name(object_name)
        self.set_modified_by(user_id)
        self.set_deployment_status(cfg._deployment_status_in_development)
        self.insert_into_deploy_control_table()

    def get_objects_ready_for_deployment(self,deployment_status):
        self.logger.info(f" fetching objects ready for deployment : {deployment_status}")
        return self.__get_all_objects_ready_for_deployment(deployment_status=deployment_status)
    
    
