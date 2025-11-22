import os
import ast
import sys
import json
import time
import shutil
import inspect
import pandas as pd
from langchain_aws import ChatBedrock
from botocore.exceptions import ClientError
import ast

import re
import json
import importlib
import contextlib
import io
import boto3
import traceback
from snowflake.snowpark.functions import col

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../conf'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../schema'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
from conf import llm_config, readconf
from privileges.privilege import Privilege
from privileges.baseprivilege import BasePrivilege
from schema import llm_chat_schema as lcs
from schema import streamlit_schema as ss
#from salesforce import salesforceextract
import src.obj.utils as util
from src.obj import account,database,share,internalstage,snowpipe,externalstage,role,fileformat,resourcemonitor,user,warehouse,table,copyinto,schema,task,stream,alert,notificationintegrationemail,storageintegration,storedprocedure,cortexsearch
from src.infschema import tables, columns
from src.governance import maskingpolicy
from src.setup.initial import InitialSetup
from src.dep import deploy
from src.accountusage import copyhistory
from src.processing.stage import Stage
from src.pipeline import fullload
# from src.dependency import base_dependency
from vars.gvobject import Config as cfg
import traceback
from snowflake.snowpark.exceptions import SnowparkSQLException
from src.sqlserver.sqlserverconnection import SqlServerConnection as SSConn
from src.sqlserver.sqlserverconnection import SqlServerOperations as SSOpr
from src.cdc.cdc import CDC

from valueexception import (
    AttributeValidationError,
    InvalidPassword,
    IsARequiredAttribute
)
from snowchainexception import (
    SnowchainException
)
class LLMTools:
    def __init__(
                    self,
                    logger,
                    sf_session,
                    root,
                    bedrock_obj,
                    user_chat_inst,
                    retrieval_workflow,
                    region=llm_config.REGION,
                    temperature=llm_config.TEMPERATURE,
                    chat_model_id=llm_config.CHAT_MODEL_ID
                 ):
        self.retrieval_workflow = retrieval_workflow
        self.sf_session = sf_session
        self.query_count=0
        self.root = root
        self.chat_model_id = chat_model_id
        self.user_id = self.sf_session.sql("select current_user()").collect()[0][0]
        self.region = region
        self.logger = logger.getChild(self.__class__.__name__)
        self.bedrock_obj = bedrock_obj
        self.user_chat_inst=user_chat_inst
        self.chat_llm = ChatBedrock(model_id=chat_model_id,
                                    model_kwargs=dict(temperature=temperature),
                                    aws_access_key_id=llm_config.ACCESS_KEY,
                                    aws_secret_access_key=llm_config.SECRET_KEY,
                                    region_name=self.region)
        self.obj_class_mapping = {#ss.ACCOUNT_OBJ: account.Admin(self.sf_session, logger=self.logger),
                                  ss.DATABASE_OBJ: database.Database(session=self.sf_session, user_id=self.user_id, logger=self.logger),
                                  #ss.EXTERNAL_STAGE_OBJ: externalstage.ExternalStage(self.sf_session,self.user_id, logger=self.logger),
                                  #ss.ROLE_OBJ: role.Role(self.sf_session,self.user_id, logger=self.logger),
                                  #ss.COPYINTO_OBJ:copyinto.CopyInto(session=self.sf_session, user_id=self.user_id, logger=self.logger),
                                  #ss.INTERNAL_STAGE_OBJ: internalstage.InternalStage(session=self.sf_session, user_id=self.user_id, logger=self.logger),
                                  #ss.SNOWPIPE_OBJ: snowpipe.Snowpipe(self.sf_session, user_id=self.user_id, logger=self.logger),
                                  #ss.FILEFORMAT_OBJ: fileformat.FileFormat(session=self.sf_session, user_id=self.user_id, logger=self.logger),
                                  #ss.RESOURCE_MONITOR_OBJ: resourcemonitor.ResourceMonitor(self.sf_session,self.user_id, logger=self.logger),
                                  #ss.WAREHOUSE_OBJ: warehouse.Warehouse(self.sf_session,self.user_id, logger=self.logger),
                                  ss.SCHEMA_OBJ: schema.Schema(session=self.sf_session, user_id=self.user_id, logger=self.logger),
                                  #ss.TABLE_OBJ: table.Table(session=self.sf_session, user_id=self.user_id, logger=self.logger),
                                  #ss.MASKING_POLICY_OBJ: maskingpolicy.MaskingPolicy(session=self.sf_session, user_id=self.user_id, logger=self.logger),
                                  #ss.TASK_OBJ: task.Task(session=self.sf_session, user_id=self.user_id,logger=self.logger),
                                  #ss.COPY_HISTORY_OBJ: copyhistory.CopyHistory(session=self.sf_session),
                                  #ss.STREAM_OBJ: stream.Stream(session=self.sf_session,user_id=self.user_id,logger=self.logger),
                                  #ss.ALERT_OBJ: alert.Alerts(session=self.sf_session,user_id=self.user_id,logger=self.logger),
                                  #ss.NOTIFICATION_OBJ: notificationintegrationemail.NotificationIntegrationEmail(session=self.sf_session,user_id=self.user_id,logger=self.logger),
                                  #ss.STORAGE_INTEGRATION_OBJ: storageintegration.StorageIntegration(session=self.sf_session,user_id=self.user_id,logger=self.logger),
                                  #ss.STORED_PROCEDURE_OBJ: storedprocedure.StoredProcedure(session=self.sf_session,user_id=self.user_id,logger=self.logger),
                                  #ss.FULL_LOAD_OBJ: fullload.FullLoad(session=self.sf_session,logger=self.logger),
                                  #ss.CORTEX_SEARCH_OBJ: cortexsearch.CortexSearch(session=self.sf_session,user_id=self.user_id,logger=self.logger),
                                  #ss.USER_OBJ: user.User(self.sf_session, self.user_id, logger=self.logger)
                                  }
    
    def __increment_query_count(self):
        self.query_count+=1

    def import_module(self, obj_type):
        module_path = f"src.obj.{obj_type.lower()}"
        self.logger.info(f"module path : {module_path}")
        module = importlib.import_module(module_path)
        OperationClass = getattr(module, "Operation")
        return OperationClass()

    def get_object_params(self, obj_type):
        operation = self.import_module(obj_type)
        self.logger.info(f" allowed keys for {obj_type} : {operation.get_attributes()}")
        return f"the allowed keys for {obj_type} are: {operation.get_attributes()}"

    # def get_obj_dependency(self, obj_type):
    #    return f"heres the list of dependencies for {obj_type}: {base_dependency.ObjectDependency().get_dependencies()}"

    def create_object(self, obj_type, data_dict):
        try:
            print(f"data dictioary : {data_dict}")
            data_dict = json.loads(data_dict)
            operation = self.import_module(obj_type)
            qry = operation.create_object(user_chat_inst=self.user_chat_inst,session=self.sf_session, user_id=self.user_id, logger=self.logger, kwargs=data_dict)
            self.logger.info(f"For {obj_type}, query returned: {qry}")
            self.logger.info(f'Object {obj_type} created successfully.')
            self.__increment_query_count()
            return f'Object {obj_type} created successfully, and returned {qry}'
        except (SnowchainException,SnowparkSQLException) as e:
            self.logger.warn(f"inside Snowchainexception")
            self.logger.warn(f"Error : {e}")
            return f"There was an error  creating object: {e}"
        except Exception as e:
            self.logger.warn("inside generic exception")
            self.logger.warn(f"Error : {e}")
            self.logger.warn(f"Traceback: {traceback.format_exc()}")
            return f"There was an error creating object : {e}"

    def ingestion_pipeline_instructions(self, question):
        return "to create an ingestion pipeline, you first create a file format object, then external stage object, then copy into object, and finally snowpipe object. for each object, be sure to get their input params using get_object_params tool. use the query returned from copy into as an input to snowpipe object."

    def deploy_all_dev_to_test(self, query):
        deploy_obj = deploy.Deploy(session=self.sf_session,logger=self.logger)
        deploy_obj.deploy_from_dev_to_test()
        return 'All objects from dev are deployed to test successfully'

    '''
    def get_salesforce_cols(self, object_type, object_identifier):
        salesforce_obj = salesforceextract.SForce()
        columns_list = salesforce_obj.get_columns_of_object(object_type=object_type)
        self.logger.info(f"Columns pulled {columns_list}")
        return f'please create a table, ask user which columns they want from this list: {columns_list}'

    def get_salesforce_data_into_table(self, object_type, object_identifier, columns_list, database, schema, table):
        # exec("columns_list = "+columns_list)
        columns_list = ast.literal_eval(columns_list)
        self.logger.info(f"columns list before getting data from salesforce: {columns_list}")
        salesforce_obj = salesforceextract.SForce()
        df = salesforce_obj.get_records_from_salesforce(object_type=object_type, 
                                                        logger=self.logger,
                                                        object_identifier=object_identifier, 
                                                        columns_list=columns_list)
        salesforce_obj.write_pandas_df_to_snowflake(self.sf_session,df,database,schema,table)
        return 'salesforce data successfully loaded into snowflake table'
    '''
    
    def find_privileges(self, object_type, object_identifier,database="NONE",schema="NONE"):
        privilege_obj = Privilege(session=self.sf_session,logger=self.logger,object_type=object_type,object_identifier=object_identifier,database=database,schema=schema)
        return f'Available privilege options are: {privilege_obj.find_privileges()}'

    def create_cdc(self,db,table_name):
        conn=SSConn(logger=self.logger)
        conn=conn.get_sql_server_connection()
        operation=SSOpr(connection=conn,logger=logger)
        cdc_inst=CDC(session=self.sf_session,logger=self.logger)
        df, from_lsn, to_lsn = operation.get_incremental_data(cdc_inst=cdc_inst, table_name=table_name, db_name=db)
        df = df.drop(columns=['__$start_lsn','__$seqval','__$update_mask','__$operation']) 
        util.write_pandas_df_to_snowflake(session=self.sf_session, df=df, database='SQL_SERVER_CDC_DB', schema='CDC_LANDING', table=table_name) 
        cdc_inst.log_cdc(server='MSSQL', **{'DATABASE':db, 'OBJECT':table_name, 'LSN':to_lsn.hex().upper()})
        return "incremental data from SQL Server to Snowflake pulled successfully"
    
    def grant_privilege_on_object(self, object_type, object_identifier, privilege, role,database_name="NONE",schema="NONE"):
        self.logger.info(f" Inside to grant privilege on  {object_type}: {object_identifier}, privilege:{privilege} to role : {role} at db.schema: {database_name}.{schema}")
        self.logger.info(f"type of db {type(database_name)}")
        if object_type.upper() != 'DATABASE':
            if database_name.upper() == 'NONE' or database_name == None:
                self.logger.info("since database is none using DB_CONFIG")
                self.sf_session.sql(f"USE DATABASE DB_CONFIG").collect()
            else:
                self.logger.info(f"switching to {database_name} database")
                self.sf_session.sql(f"USE DATABASE {database_name}").collect()
        privilege_obj = Privilege(session=self.sf_session,logger=self.logger,object_type=object_type,object_identifier=object_identifier,database=database_name,schema=schema)
        privilege_obj.grant_privilege(privilege_type=privilege, role=role)
        return f'Privilege {privilege} granted successfully'

    def tool_call(self, content, tool_result):
        func_name = content[lcs.TOOL_USE][lcs.NAME]
        params = content[lcs.TOOL_USE][lcs.INPUT]
        result = getattr(self, func_name)(**params)
        tool_result.append({lcs.TOOL_RESULT:{
            lcs.TOOL_USE_ID: content[lcs.TOOL_USE][lcs.TOOL_USE_ID],
            lcs.CONTENT: [{lcs.JSON: {lcs.RESULT: result}}]
        }})
        return tool_result
