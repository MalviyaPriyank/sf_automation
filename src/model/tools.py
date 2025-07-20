import os
import sys
import time
import shutil
import inspect
import pandas as pd
from langchain_aws import ChatBedrock
from botocore.exceptions import ClientError

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../conf'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../schema'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
from conf import llm_config, readconf
from schema import llm_chat_schema as lcs
from schema import streamlit_schema as ss
from src.obj import account,database,share,internalstage,snowpipe,externalstage,role,fileformat,resourcemonitor,user,warehouse,table,copyinto,schema,task,stream,alert,notificationintegrationemail,storageintegration,storedprocedure
from src.governance import maskingpolicy
from src.setup.initial import InitialSetup
from src.dep import deploy
from src.accountusage import copyhistory
from src.processing.stage import Stage
from vars.gvobject import Config as cfg

from valueexception import (
    AttributeValidationError,
    InvalidPassword
)

class LLMTools:
    def __init__(
                    self,
                    logger,
                    sf_session,
                    root,
                    retrieval_workflow,
                    region=llm_config.REGION,
                    temperature=llm_config.TEMPERATURE,
                    chat_model_id=llm_config.CHAT_MODEL_ID
                 ):
        self.retrieval_workflow = retrieval_workflow
        self.sf_session = sf_session
        self.root = root
        self.user_id = self.sf_session.sql("select current_user()").collect()[0][0]
        self.region = region
        self.logger = logger
        self.chat_llm = ChatBedrock(model_id=chat_model_id,
                                    model_kwargs=dict(temperature=temperature),
                                    aws_access_key_id=llm_config.ACCESS_KEY,
                                    aws_secret_access_key=llm_config.SECRET_KEY,
                                    region_name=self.region)
        self.obj_class_mapping = {ss.ACCOUNT_OBJ: account.Admin(self.sf_session, logger=self.logger),
                                  ss.DATABASE_OBJ: database.Database(session=self.sf_session, user_id=self.user_id, logger=self.logger),
                                  ss.EXTERNAL_STAGE_OBJ: externalstage.ExternalStage(self.sf_session,self.user_id, logger=self.logger),
                                  ss.ROLE_OBJ: role.Role(self.sf_session,self.user_id, logger=self.logger),
                                  ss.COPYINTO_OBJ:copyinto.CopyInto(session=self.sf_session, user_id=self.user_id, logger=self.logger),
                                  ss.INTERNAL_STAGE_OBJ: internalstage.InternalStage(session=self.sf_session, user_id=self.user_id, logger=self.logger),
                                  ss.SNOWPIPE_OBJ: snowpipe.Snowpipe(self.sf_session, user_id=self.user_id, logger=self.logger),
                                  ss.FILEFORMAT_OBJ: fileformat.FileFormat(session=self.sf_session, user_id=self.user_id, logger=self.logger),
                                  ss.RESOURCE_MONITOR_OBJ: resourcemonitor.ResourceMonitor(self.sf_session,self.user_id, logger=self.logger),
                                  ss.WAREHOUSE_OBJ: warehouse.Warehouse(self.sf_session,self.user_id, logger=self.logger),
                                  ss.SCHEMA_OBJ: schema.Schema(session=self.sf_session, user_id=self.user_id, logger=self.logger),
                                  #'share': share.Share(self.sf_session,self.user_id, logger=self.logger),
                                  ss.TABLE_OBJ: table.Table(session=self.sf_session, root=self.root, user_id=self.user_id, logger=self.logger),
                                  ss.MASKING_POLICY_OBJ: maskingpolicy.MaskingPolicy(session=self.sf_session, user_id=self.user_id, logger=self.logger),
                                  ss.TASK_OBJ: task.Task(session=self.sf_session, user_id=self.user_id,logger=self.logger),
                                  ss.COPY_HISTORY_OBJ: copyhistory.CopyHistory(session=self.sf_session),
                                  ss.STREAM_OBJ: stream.Stream(session=self.sf_session,user_id=self.user_id,logger=self.logger),
                                  ss.ALERT_OBJ: alert.Alerts(session=self.sf_session,user_id=self.user_id,logger=self.logger),
                                  ss.NOTIFICATION_OBJ: notificationintegrationemail.NotificationIntegrationEmail(session=self.sf_session,user_id=self.user_id,logger=self.logger),
                                  ss.STORAGE_INTEGRATION_OBJ: storageintegration.StorageIntegration(session=self.sf_session,user_id=self.user_id,logger=self.logger),
                                  ss.STORED_PROCEDURE_OBJ: storedprocedure.StoredProcedure(session=self.sf_session,user_id=self.user_id,logger=self.logger),
                                  #'user': user.User(self.sf_session,self.user_id, logger=self.logger)
                                  }


    def create_sf_object(self, obj_name, data_dict):
        #try:
        qry = self.obj_class_mapping[obj_name].create_object(**data_dict)
        self.logger.info(f"For {obj_name}, query returned: {qry}")
        self.logger.info(f'Object {obj_name} created successfully')
        #except AttributeValidationError as e:
        #    raise (e)
        return f'Object {obj_name} created successfully'


    def create_database_object(self, 
                               NAME, 
                               CATALOG="NONE", 
                               COMMENT="NONE",  
                               EXTERNAL_VOLUME="NONE", 
                               DEFAULT_DDL_COLLATION="NONE", 
                               LOG_LEVEL="NONE",
                               TRACE_LEVEL="NONE",
                               REPLACE_INVALID_CHARACTERS="NONE",
                               DATA_RETENTION_TIME_IN_DAYS="NONE",
                               STORAGE_SERIALIZATION_POLICY="NONE",
                               MAX_DATA_EXTENSION_TIME_IN_DAYS="NONE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.DATABASE_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.DATABASE_OBJ, data_dict)


    def create_stored_procedure_object(self, 
                                        DATABASE,
                                        SCHEMA,
                                        NAME,
                                        LOGIC,
                                        RETURN_TYPE,
                                        LANGUAGE,
                                        HANDLER,
                                        PACKAGES):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.STORED_PROCEDURE_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.STORED_PROCEDURE_OBJ, data_dict)


    def create_account_object(self,
                              ACCOUNT,
                              ADMIN_NAME,
                              ADMIN_PASSWORD,
                              ADMIN_USER_TYPE="PERSON",
                              FIRST_NAME="Priyank",
                              LAST_NAME="Malviya",
                              EMAIL="priyankmalviya0@gmail.com",
                              MUST_CHANGE_PASSWORD="TRUE",
                              EDITION="STANDARD",
                              REGION_GROUP="NONE",
                              REGION="NONE",
                              COMMENT="NONE",
                              POLARIS="TRUE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.ACCOUNT_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.ACCOUNT_OBJ, data_dict)


    def create_externalstage_object(self,
                                    NAME,
                                    DATABASE="DB_CONFIG",
                                    SCHEMA="SCH_CONFIG",
                                    FILE_FORMAT="NONE",
                                    COMMENT="NONE",
                                    URL="NONE",
                                    AWS_ACCESS_POINT_ARN="NONE",
                                    STORAGE_INTEGRATION="NONE",
                                    ENCRYPTION_TYPE="NONE",
                                    ENCRYPTION_MASTER_KEY="NONE",
                                    ENCRYPTION_KMS_KEY_ID="NONE",
                                    USE_PRIVATELINK_ENDPOINT="NONE",
                                    ENABLE="NONE",
                                    REFRESH_ON_CREATE="NONE",
                                    AUTO_REFRESH="NONE",
                                    NOTIFICATION_INTEGRATION="NONE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.EXTERNAL_STAGE_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.EXTERNAL_STAGE_OBJ, data_dict)


    def create_fileformat_object(self,
                                FILE_FORMAT,
                                DATABASE,
                                SCHEMA,
                                TYPE="CSV",
                                COMPRESSION="NONE",
                                RECORD_DELIMITER="NONE",
                                FIELD_DELIMITER="NONE",
                                MULTI_LINE="NONE",
                                FILE_EXTENSION="NONE",
                                PARSE_HEADER="NONE",
                                SKIP_HEADER="NONE",
                                SKIP_BLANK_LINES="NONE",
                                DATE_FORMAT="NONE",
                                TIME_FORMAT="NONE",
                                TIMESTAMP_FORMAT="NONE",
                                BINARY_FORMAT="NONE",
                                ESCAPE="NONE",
                                ESCAPE_UNENCLOSED_FIELD="NONE",
                                TRIM_SPACE="NONE",
                                FIELD_OPTIONALLY_ENCLOSED_BY="NONE",
                                NULL_IF="NONE",
                                ERROR_ON_COLUMN_COUNT_MISMATCH="NONE",
                                REPLACE_INVALID_CHARACTERS="NONE",
                                EMPTY_FIELD_AS_NULL="NONE",
                                SKIP_BYTE_ORDER_MARK="NONE",
                                ENCODING="NONE",
                                ENABLE_OCTAL="NONE",
                                ALLOW_DUPLICATE="NONE",
                                STRIP_OUTER_ARRAY="NONE",
                                STRIP_NULL_VALUES="NONE",
                                IGNORE_UTF8_ERRORS="NONE",
                                SNAPPY_COMPRESSION="NONE",
                                BINARY_AS_TEXT="NONE",
                                USE_LOGICAL_TYPE="NONE",
                                USE_VECTORIZED_SCANNER="NONE",
                                PRESERVE_SPACE="NONE",
                                STRIP_OUTER_ELEMENT="NONE",
                                DISABLE_SNOWFLAKE_DATA="NONE",
                                DISABLE_AUTO_CONVERT="NONE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.FILEFORMAT_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.FILEFORMAT_OBJ, data_dict)


    def create_internalstage_object(self,
                                    DATABASE,
                                    SCHEMA="NONE",
                                    NAME="NONE",
                                    FILE_FORMAT="NONE",
                                    COMMENT="NONE",
                                    TAG="NONE",
                                    ENCRYPTION="NONE",
                                    ENABLE="NONE",
                                    REFRESH_ON_CREATE="NONE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.INTERNAL_STAGE_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.INTERNAL_STAGE_OBJ, data_dict)


    def create_resourcemonitor_object(self,
                                    NAME,
                                    CREDIT_QUOTA="75",
                                    FREQUENCY="DAILY",
                                    START_TIMESTAMP="NONE",
                                    END_TIMESTAMP="NONE",
                                    NOTIFY_USERS="ADMIN",
                                    TRIGGERS_ON="75",
                                    THRESHOLD="NONE",
                                    ACTION="NONE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.RESOURCE_MONITOR_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.RESOURCE_MONITOR_OBJ, data_dict)


    def create_role_object(self, NAME, COMMENT="NONE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.ROLE_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.ROLE_OBJ, data_dict)


    def create_storage_integration_object(self,
                                            NAME,
                                            ENABLED,
                                            STORAGE_PROVIDER,
                                            TYPE="NONE",
                                            STORAGE_ALLOWED_LOCATIONS="NONE",
                                            STORAGE_BLOCKED_LOCATIONS="NONE",
                                            STORAGE_AWS_ROLE_ARN="NONE",
                                            STORAGE_AWS_EXTERNAL_ID="NONE",
                                            STORAGE_AWS_OBJECT_ACL="NONE",
                                            COMMENT="NONE",
                                            AZURE_TENANT_ID="NONE",
                                            USE_PRIVATELINK_ENDPOINT="NONE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.STORAGE_INTEGRATION_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.STORAGE_INTEGRATION_OBJ, data_dict)


    def create_schema_object(self,
                            DATABASE,
                            NAME,
                            WITH_MANAGED_ACCESS="NONE",
                            DATA_RETENTION_TIME_IN_DAYS="NONE",
                            MAX_DATA_EXTENSION_TIME_IN_DAYS="NONE",
                            EXTERNAL_VOLUME="NONE",
                            CATALOG="NONE",
                            REPLACE_INVALID_CHARACTERS="NONE",
                            DEFAULT_DDL_COLLATION="NONE",
                            LOG_LEVEL="NONE",
                            TRACE_LEVEL="NONE",
                            STORAGE_SERIALIZATION_POLICY="NONE",
                            CLASSIFICATION_PROFILE="NONE",
                            COMMENT="NONE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {}
        for arg in args[1:]:
            value = values[arg]
            if arg == 'WITH_MANAGED_ACCESS':
                arg = 'WITH MANAGED ACCESS'
            data_dict[arg] = value
        #data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.SCHEMA_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.SCHEMA_OBJ, data_dict)


    def create_user_object(self,
                            NAME,
                            PASSWORD,
                            LOGIN_NAME="DEFAULT",
                            DISPLAY_NAME="PERSON",
                            FIRST_NAME="DEFAULT",
                            LAST_NAME="DEFAULT",
                            EMAIL="DEFAULT",
                            MUST_CHANGE_PASSWORD="TRUE",
                            DISABLED="FALSE",
                            DAYS_TO_EXPIRY="20",
                            MINS_TO_UNLOCK="20",
                            DEFAULT_WAREHOUSE="DEFAULT",
                            DEFAULT_ROLE="DEFAULT",
                            DEFAULT_SECONDARY_ROLES="ALL",
                            MINS_TO_BY_PASS_MFA="20",
                            RSA_PUBLIC_KEY="DEFAULT",
                            RSA_PUBLIC_KEY_FP="DEFAULT",
                            RSA_PUBLIC_KEY_2="KEY2",
                            RSA_PUBLIC_KEY_2_FP="DEFAULT",
                            TYPE="PERSON",
                            COMMENT="DEFAULT",
                            ENABLE_UNREDACTED_QUERY_SYNTAX_ERROR="TRUE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.USER_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.USER_OBJ, data_dict)


    def create_warehouse_object(self,
                                NAME,
                                WAREHOUSE_SIZE="SMALL",
                                WAREHOUSE_TYPE="STANDARD",
                                RESOURCE_CONSTRAINT="NONE",
                                MAX_CLUSTER_COUNT="NONE",
                                MIN_CLUSTER_COUNT="NONE",
                                SCALING_POLICY="NONE",
                                AUTO_SUSPEND="NONE",
                                AUTO_RESUME="NONE",
                                INITIALLY_SUSPENDED="NONE",
                                RESOURCE_MONITOR="NONE",
                                COMMENT="NONE",
                                TAG="NONE",
                                ENABLE_QUERY_ACCELERATION="NONE",
                                QUERY_ACCELERATION_MAX_SCALE_FACTOR="NONE",
                                MAX_CONCURRENCY_LEVEL="NONE",
                                STATEMENT_QUEUED_TIMEOUT_IN_SECONDS="NONE",
                                STATEMENT_TIMEOUT_IN_SECONDS="NONE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.WAREHOUSE_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.WAREHOUSE_OBJ, data_dict)


    def create_multiple_table_object(self,
                            database,
                            schema):
        self.logger.info(f'creating {ss.TABLE_OBJ} object with database={database} and schema={schema}')
        if not os.path.isdir('tmp'): os.mkdir('tmp')
        table_list = self.obj_class_mapping[ss.TABLE_OBJ].create_table_using_files_from_stage(database,schema,filelist)
        self.logger.info(f"table list returned {table_list}")
        shutil.rmtree('tmp', ignore_errors=True)
        return f'Here is the list of tables created : [{table_list}]'

    def create_single_table_object(self,
                                   database,
                                   schema,
                                   filelist=[]):
        #stage = Stage(root=self.root, database=cfg._config_database, schema=cfg._config_schema)
        #stage.set_stage(cfg._config_stage)
        #stage.set_stage_reference()
        self.logger.info('listing_files')
        #for file in filelist: #os.listdir('tmp/'):
            #self.logger.info(file)
            #stage.upload_file_to_stage(file_path=f'tmp/{file}',upload_path='/')#f'/{database}/{schema}/')

        self.obj_class_mapping[ss.TABLE_OBJ].create_table_using_files_from_stage(database,schema,filelist)
        shutil.rmtree('tmp', ignore_errors=True)
        return 'Tables created successfully'


    def create_copyinto_object(self,
                                DATABASE="NONE",
                                SCHEMA="NONE",
                                TABLE="NONE",
                                STAGE="NONE",
                                FILE_FORMAT="NONE",
                                ON_ERROR="NONE",
                                SIZE_LIMIT="NONE",
                                PURGE="NONE",
                                RETURN_FAILED_ONLY="NONE",
                                MATCH_BY_COLUMN_NAME="NONE",
                                INCLUDE_METADATA="NONE",
                                ENFORCE_LENGTH="NONE",
                                TRUNCATECOLUMNS="NONE",
                                FORCE="NONE",
                                LOAD_UNCERTAIN_FILES="NONE",
                                FILE_PROCESSOR="NONE",
                                LOAD_MODE="NONE",
                                SCANNER="NONE",
                                PROJECT_NAME="NONE",
                                MODEL_NAME="NONE",
                                MODEL_VERSION="NONE"
                              ):
        
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f"Tables provided = {values['TABLE']}")
        copyinto_queries = []
        for value in values['TABLE'].split(','):
            self.logger.info(f'Creating copyinto query for table {value}')
            data_dict['TABLE'] = value.replace('[','').replace(']','').replace('"','')
            self.logger.info(data_dict)
            copyinto_queries.append(self.obj_class_mapping[ss.COPYINTO_OBJ].create_query(**data_dict))
        return f'COPYINTO queries created successfully. Heres the table-query mapping: {copyinto_queries}'


    def create_snowpipe_object(self,
                               DATABASE,
                               SCHEMA,
                               TABLE,
                               COPYINTO_QUERY,
                               AUTO_INGEST="NONE",
                               ERROR_INTEGRATION="NONE",
                               AWS_SNS_TOPIC="NONE",
                               INTEGRATION="NONE",
                               COMMENT="NONE"):
        
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f"Tables provided = {values['TABLE']}")
        self.logger.info(f"Copyinto provided = {values['COPYINTO_QUERY']}")
        
        table_values = values['TABLE'].split(',')
        copyinto_values = values['COPYINTO_QUERY'].split(',')
        for value in range(len(table_values)):
            self.logger.info(f'Creating snowpipe for table {table_values[value]} with copyinto query {copyinto_values[value]}')
            data_dict['TABLE'] = table_values[value].replace('[','').replace(']','').replace('"','')
            data_dict['NAME'] = f"PIPE_{data_dict['TABLE']}"
            data_dict['COPYINTO_QUERY'] = copyinto_values[value].replace('{table}', data_dict['TABLE'])
            snowpipe_obj = self.obj_class_mapping[ss.SNOWPIPE_OBJ].create_object(**data_dict)
        return f'SNOWPIPE object created successfully for all tables'


    def create_task_object(self,
                            DATABASE,
                            SCHEMA,
                            NAME,
                            SQL,
                            WAREHOUSE="NONE",
                            USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE="NONE",
                            SCHEDULE="NONE",
                            CONFIG="NONE",
                            ALLOW_OVERLAPPING_EXECUTION="NONE",
                            USER_TASK_TIMEOUT_MS="NONE",
                            SUSPEND_TASK_AFTER_NUM_FAILURES="NONE",
                            ERROR_INTEGRATION="NONE",
                            SUCCESS_INTEGRATION="NONE",
                            COMMENT="NONE",
                            AFTER="NONE",
                            WHEN="NONE",
                            TAG="NONE",
                            FINALIZE="NONE",
                            TASK_AUTO_RETRY_ATTEMPTS="NONE",
                            USER_TASK_MINIMUM_TRIGGER_INTERVAL_IN_SECONDS="NONE",
                            TARGET_COMPLETION_INTERVAL="NONE",
                            SERVERLESS_TASK_MIN_STATEMENT_SIZE="NONE",
                            SERVERLESS_TASK_MAX_STATEMENT_SIZE="NONE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.TASK_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.TASK_OBJ, data_dict)
        
    
    def create_maskingpolicy_object(self,
                                    ROLE,
                                    NAME,
                                    SIGNATURE,
                                    RETURNS,
                                    BODY,
                                    COMMENT="NONE",
                                    EXEMPT_OTHER_POLICIES="NONE"
                                    ):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.MASKINGPOLICY_OBJ} object with parameters: {data_dict}')
        return self.create_masking_policy(ss.MASKINGPOLICY_OBJ, data_dict)
        

    def sf_setup(self, query):
        init_setup = InitialSetup(logger=self.logger,session=self.sf_session,user_id = self.user_id)
        init_setup.perform_initial_setup()
        return 'Completed setup for role, warehouse, database, schema, and more'


    def get_workflow(self, query):
        try: return self.retrieval_workflow.run(query)
        except ClientError as e: return 'Bedrock service unavailable'


    def deploy_all_dev_to_test(self, query):
        deploy_obj = deploy.Deploy(session=self.sf_session,logger=self.logger)
        deploy_obj.deploy_from_dev_to_test()
        return 'All objects from dev are deployed to test successfully'


    def get_history_for_pipe(self,
                             pipe_db,
                             pipe_schema,
                             pipe_name):
        self.logger.info(f'Getting copyhistory for pipe')
        return self.obj_class_mapping[ss.COPY_HISTORY_OBJ].get_load_history_for_a_pipe(pipe_db=pipe_db,
                                                        pipe_schema=pipe_schema,
                                                        pipe_name=pipe_name)

    
    def get_history_for_table(self,
                             table_db,
                             table_schema,
                             table_name):
        self.logger.info(f'Getting copyhistory for table')
        return self.obj_class_mapping[ss.COPY_HISTORY_OBJ].get_load_history_for_a_table(table_db=table_db,
                                                        table_schema=table_schema,
                                                        table_name=table_name)


    def create_stream_object(self,
                            DATABASE,
                            SCHEMA,
                            NAME,
                            TABLE_NAME,
                            TAG="NONE",
                            AT="NONE",
                            APPEND_ONLY="NONE",
                            INSERT_ONLY="NONE",
                            SHOW_INITIAL_ROWS="NONE",
                            COMMENT="NONE",
                            BEFORE="NONE",
                            TIMESTAMP="NONE",
                            OFFSET="NONE",
                            STATEMENT="NONE",
                            OBJECT_TYPE="NONE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.STREAM_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.STREAM_OBJ, data_dict)

    
    def create_alert_object(self,
                            NAME,
                            SCHEDULE,
                            DATABASE,
                            SCHEMA,
                            CONDITION,
                            ACTION,
                            ACTION_TYPE,
                            IF="NONE",
                            THEN="NONE",
                            WAREHOUSE="NONE",
                            COMMENT="NONE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.ALERT_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.ALERT_OBJ, data_dict)


    def create_notification_object(self,
                                    NAME,
                                    ENABLED,
                                    TYPE="NONE",
                                    ALLOWED_RECIPIENTS="NONE",
                                    DEFAULT_RECIPIENTS="NONE",
                                    DEFAULT_SUBJECT="NONE",
                                    COMMENT="NONE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.NOTIFICATION_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.NOTIFICATION_OBJ, data_dict)


    def get_table_definitions_from_stage(self,
                                         TABLE):
        stage = Stage(root=self.root, database=cfg._config_database, schema=cfg._config_schema)
        stage.set_stage(cfg._config_stage)
        stage.set_stage_reference()
        data_dict = []
        table_list = [file for file in TABLE if any(file.endswith(f"{self.attr.database}/{self.attr.schema}/{table_name}.csv") for table_name in TABLE)]
            
        for table_name in table_list: 
            stage.download_file_from_stage(table_name,"tmp/")
            data_dict.append(pd.read_csv(f'tmp/{table_name}.csv'))
        return str(data_dict)


    def retrieve_data_from_table(self,
                                 SQL_QUERY):
        #add code for function call to execute query and return results
        #result = func_call()
        #return str(result)
        return 


    def tool_call(self, content, tool_result):
        func_name = content[lcs.TOOL_USE][lcs.NAME]
        params = content[lcs.TOOL_USE][lcs.INPUT]
        result = getattr(self, func_name)(**params)
        tool_result.append({lcs.TOOL_RESULT:{
            lcs.TOOL_USE_ID: content[lcs.TOOL_USE][lcs.TOOL_USE_ID],
            lcs.CONTENT: [{lcs.JSON: {lcs.RESULT: result}}]
        }})
        return tool_result
        