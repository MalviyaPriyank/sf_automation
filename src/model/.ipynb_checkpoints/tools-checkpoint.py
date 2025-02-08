import os
import sys
import time
import inspect
from langchain_aws import ChatBedrock
from botocore.exceptions import ClientError

sys.path.append(os.path.join(os.path.dirname(__file__),'../src'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../conf'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../../schema'))
from conf import llm_config, readconf
from schema import llm_chat_schema as lcs
from schema import streamlit_schema as ss
from src.obj import account,database,share,internalstage,snowpipe,externalstage,role,fileformat,resourcemonitor,user,warehouse,table,copyinto,schema
from src.governance import maskingpolicy
from src.setup.initial import InitialSetup
from src.dep import deploy

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
        self.obj_class_mapping = {'account': account.Admin(self.sf_session),
                                  'database': database.Database(session=self.sf_session, user_id=self.user_id),
                                  #'externalstage': externalstage.ExternalStage(self.sf_session,self.user_id),
                                  'role': role.Role(self.sf_session,self.user_id),
                                  'copyinto':copyinto.CopyInto(),
                                  'internalstage': internalstage.InternalStage(session=self.sf_session, user_id=self.user_id),
                                  'fileformat': fileformat.FileFormat(session=self.sf_session, user_id=self.user_id),
                                  #'resourcemonitor': resourcemonitor.ResourceMonitor(self.sf_session,self.user_id),
                                  'warehouse': warehouse.Warehouse(self.sf_session,self.user_id),
                                  'schema': schema.Schema(session=self.sf_session, user_id=self.user_id),
                                  #'share': share.Share(self.sf_session,self.user_id),
                                  'table': table.Table(session=self.sf_session, root=self.root, user_id=self.user_id),
                                  'maskingpolicy' : maskingpolicy.MaskingPolicy(session=self.sf_session, user_id=self.user_id)
                                  #'task': task.Task,
                                  #'user': user.User(self.sf_session,self.user_id)
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
                               REPLACE_INVALID_CHARACTERS="NONE",
                               DATA_RETENTION_TIME_IN_DAYS="NONE",
                               STORAGE_SERIALIZATION_POLICY="NONE",
                               MAX_DATA_EXTENSION_TIME_IN_DAYS="NONE"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.DATABASE_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.DATABASE_OBJ, data_dict)


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
                                    FILE_FORMAT,
                                    COMMENT="DEFAULT",
                                    TAG="DEF",
                                    URL="'DEF'",
                                    STORAGE_INTEGRATION="DEF",
                                    AWS_KEY_ID="DEF",
                                    AWS_SECRET_KEY="DEF",
                                    AWS_TOKEN="DEF",
                                    AZURE_SAS_TOKEN="DEF",
                                    AWS_ROLE="DEF",
                                    ENCRYPTION="SNOWFLAKE_FULL",
                                    ENCRYPTION_TYPE="DEF",
                                    ENCRYPTION_MASTER_KEY="DEF",
                                    ENCRYPTION_KMS_KEY_ID="DEF",
                                    USE_PRIVATELINK_ENDPOINT="DEF",
                                    DIRECTORY="TRUE",
                                    REFRESH_ON_CREATE="TRUE",
                                    AUTO_REFRESH="DEF",
                                    NOTIFICATION_INTEGRATION="DEF"):
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
                                    DIRECTORY="NONE",
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
                                    DO="SUSPEND"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.RESOURCE_MONITOR_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.RESOURCE_MONITOR_OBJ, data_dict)


    def create_role_object(self, NAME, COMMENT="DEFAULT"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.ROLE_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.ROLE_OBJ, data_dict)


    def create_schema_object(self,
                            DATABASE,
                            NAME,
                            WITH_MANAGED_ACCESS="NONE",
                            DATA_RETENTION_TIME_IN_DAYS="1",
                            MAX_DATA_EXTENSION_TIME_IN_DAYS="10",
                            EXTERNAL_VOLUME="NONE",
                            CATALOG="NONE",
                            REPLACE_INVALID_CHARACTERS="NONE",
                            DEFAULT_DDL_COLLATION="NONE",
                            LOG_LEVEL="NONE",
                            TRACE_LEVEL="NONE",
                            STORAGE_SERIALIZATION_POLICY="NONE",
                            CLASSIFICATION_PROFILE="NONE",
                            COMMENT="NONE",
                            TAG="NONE"):
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


    def create_share_object(self, NAME, COMMENT="DEFAULT"):
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        self.logger.info(f'creating {ss.SHARE_OBJ} object with parameters: {data_dict}')
        return self.create_sf_object(ss.SHARE_OBJ, data_dict)


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
        table_list = self.obj_class_mapping['table'].create_table_using_files_from_stage(database,schema)
        return f'{ss.TABLE_OBJ} created successfully for tables {table_list}'


    def create_single_table_object(self,
                                   name):
        return f'Table {name} created'


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
                                LOAD_MODE="NONE"
                              ):
        
        frame = inspect.currentframe()
        args, _, _, values = inspect.getargvalues(frame)
        data_dict = {arg: values[arg] for arg in args[1:]}
        
        for value in values['TABLE'].split(','):
            self.logger.info(f'Creating copyinto query for table {value}')
            data_dict['TABLE'] = value
            self.logger.info(data_dict)
            copyinto_query = self.obj_class_mapping['copyinto'].create_query(**data_dict)
            snowpipe_obj = snowpipe.Snowpipe(self.sf_session, 
                                             copy_into_qry=copyinto_query, 
                                             root= self.root,
                                             user_id=self.user_id)
            self.logger.info(f'Creating snowpipe object for table {value}')
            snowpipe_data_dict = {"DATABASE":DATABASE,
                                    "SCHEMA": SCHEMA,
                                    "NAME":f'PIPE_{value}',
                                    "AUTO_INGEST":"NONE",
                                    "ERROR_INTEGRATION":"NONE",
                                    "AWS_SNS_TOPIC":"NONE",
                                    "INTEGRATION":"NONE",
                                    "COMMENT":"NONE",
                                    "FILE_TYPE":"NONE"}
            snowpipe_obj.create_object(**snowpipe_data_dict)
            
        return f'COPYINTO queries and snowpipe objects created successfully'


    def create_snowpipe_object(self,
                               COPYINTO_QUERY,
                               DATABASE,
                               SCHEMA,
                               TABLE):
        snowpipe_obj = snowpipe.Snowpipe(self.sf_session, 
                                             copy_into_qry=COPYINTO_QUERY, 
                                             root= self.root,
                                             user_id=self.user_id)
        self.logger.info(f'Creating snowpipe object for table {TABLE}')
        snowpipe_data_dict = {"DATABASE":DATABASE,
                                "SCHEMA": SCHEMA,
                                "NAME":f'PIPE_{TABLE}',
                                "AUTO_INGEST":"NONE",
                                "ERROR_INTEGRATION":"NONE",
                                "AWS_SNS_TOPIC":"NONE",
                                "INTEGRATION":"NONE",
                                "COMMENT":"NONE",
                                "FILE_TYPE":"NONE"}
        snowpipe_obj.create_object(**snowpipe_data_dict)
        return f'SNOWPIPE object created for COPYINTO query: {COPYINTO_QUERY}'
        
    
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
        init_setup = InitialSetup(session=self.sf_session,user_id = self.user_id)
        init_setup.perform_initial_setup()
        return 'Completed setup for role, warehouse, database, schema, and more'


    def get_workflow(self, query):
        try: return self.retrieval_workflow.run(query)
        except ClientError as e: return 'Bedrock service unavailable'


    def deploy_all_dev_to_test(self):
        deploy.deploy_from_dev_to_test(self)
        return 'All objects from dev are deployed to test successfully'


    def tool_call(self, content, tool_result):
        func_name = content[lcs.TOOL_USE][lcs.NAME]
        params = content[lcs.TOOL_USE][lcs.INPUT]
        result = getattr(self, func_name)(**params)
        tool_result.append({lcs.TOOL_RESULT:{
            lcs.TOOL_USE_ID: content[lcs.TOOL_USE][lcs.TOOL_USE_ID],
            lcs.CONTENT: [{lcs.JSON: {lcs.RESULT: result}}]
        }})
        return tool_result
        