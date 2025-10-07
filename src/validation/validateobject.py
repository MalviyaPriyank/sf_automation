import sys
import os
from snowflake.snowpark.functions import col

sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../inf_schema'))


from infschema.databases import Databases as db
from infschema.schemata import Schemata as sch
from infschema.tables import Tables as tbl
from infschema.stages import Stages as stg
from infschema.fileformats import FileFormats as ff
from infschema.columns import Columns as cols
from infschema.pipes import Pipes as pipes
from exception.objectexception import ( 
    ObjectDoesNotExist,
    DuplicateObject,
    ColumnDoesNotExist,
    MustBeAnAdmin,
    InvalidAttributesToAlter
)


class ValidateObject:
    @staticmethod
    def database_exist(session,database_name):
        db_inst = db(session)
        if db_inst.is_existing_database(db_name= database_name):
            return True
        else:
            raise ObjectDoesNotExist('DATABASE',database_name)
        
    @staticmethod 
    def schema_exist(session,database_name,schema_name):
        sch_inst = sch(session=session)
        if sch_inst.is_existing_schema(database_name,schema_name):
            return True
        else:
            raise ObjectDoesNotExist('SCHEMA', schema_name)
        
    @staticmethod 
    def pipe_exist(session,database_name,schema_name,pipe_name):
        pipe_inst = pipes(session=session)
        if pipe_inst.is_existing_pipe(db_name=database_name,schema_name=schema_name,pipe_name=pipe_name):
            return True
        else:
            raise ObjectDoesNotExist('PIPE', schema_name)
    
    @staticmethod
    def table_exist(session,database_name,schema_name,table_name):
        tbl_inst = tbl(session=session)
        if tbl_inst.is_existing_table(database_name,schema_name,table_name):
            return True
        else:
            raise ObjectDoesNotExist('TABLE',table_name)

    @staticmethod
    def stage_exist(session,database_name,schema_name,stage_name):
        stg_inst = stg(session)
        if stg_inst.is_existing_stage(db_name=database_name, schema_name=schema_name, stage_name=stage_name):
            return True
        else:
            raise ObjectDoesNotExist('STAGE',stage_name)
        
    @staticmethod
    def file_format_exist(session,database_name,schema_name,file_format_name):
        ff_inst = ff(session)
        if ff_inst.is_existing_file_format(db_name=database_name, schema_name=schema_name, file_format_name=file_format_name):
            return True
        else:
            raise ObjectDoesNotExist('FILE_FORMAT',file_format_name)
        
    @staticmethod
    def is_new_database(session,database_name):
        db_inst = db(session)
        if db_inst.is_new_database(db_name= database_name):
            return True
        else:
            raise DuplicateObject('DATABASE',database_name)
        
    @staticmethod 
    def is_new_schema(session,database_name,schema_name):
        sch_inst = sch(session=session)
        if sch_inst.is_new_schema(database_name,schema_name):
            return True
        else:
            raise DuplicateObject('SCHEMA', schema_name)

    @staticmethod 
    def is_new_pipe(session,database_name,schema_name,pipe_name):
        pipe_inst = pipes(session=session)
        if pipe_inst.is_new_pipe(db_name=database_name,schema_name=schema_name,pipe_name=pipe_name):
            return True
        else:
            raise DuplicateObject('PIPE', schema_name)

    @staticmethod 
    def is_new_table(session,database_name,schema_name):
        tbl_inst = tbl(session=session)
        if tbl_inst.is_new_table(database_name,schema_name):
            return True
        else:
            raise DuplicateObject('TABLE', schema_name)
        
    @staticmethod
    def is_new_file_format(session,database_name,schema_name,file_format_name):
        ff_inst = ff(session)
        if ff_inst.is_new_file_format(db_name=database_name, schema_name=schema_name, file_format_name=file_format_name):
            return True
        else:
            raise DuplicateObject('FILE_FORMAT',file_format_name)
        
    @staticmethod
    def warehouse_exist(session,warehouse_name):
        df=session.sql("SHOW WAREHOUSES")
        df=df.select(col("*")).collect()
        wh_df=session.create_dataframe(df)
        wh_count=wh_df.filter(col("NAME")==warehouse_name.upper()).count()
        if wh_count:
            return True
        else:
            raise ObjectDoesNotExist(object_type='WAREHOUSE',object_name=warehouse_name)

    @staticmethod
    def object_exist(session,object_type,object_name):
        object_type=object_type.upper()
        object_name=object_name.upper()
        if object_type == "MASKINGPOLICY":
            qry="SHOW MASKING POLICIES"
        else:    
            qry=ValidateObject.return_show_query(object_type=object_type) # getting query SHOW STREAMS,TASKS etc
        df=session.sql(qry)
        df=df.select(col("*")).collect()
        df=session.create_dataframe(df)
        df_count=df.filter(col("NAME")==object_name).count()
        if df_count:
            return True
        else:
            raise ObjectDoesNotExist(object_type=object_type,object_name=object_name)

    @staticmethod
    def return_show_query(object_type):
        qry=f"SHOW {object_type.upper()}S"
        return qry
        
    @staticmethod
    def is_new_object(session,object_type,object_name):
        object_type=object_type.upper()
        object_name=object_name.upper()
        if object_type == "MASKINGPOLICY":
            qry="SHOW MASKING POLICIES"
        else: 
            qry=ValidateObject.return_show_query(object_type=object_type) # getting query SHOW STREAMS,TASKS etc
        df=session.sql(qry)
        df=df.select(col("*")).collect()
        if len(df) == 0: #if there is not even a single row of object_type, eg no tasks 
            return True
        else:
            df=session.create_dataframe(df)
            df_count=df.filter(col("NAME")==f'{object_name}').count()
            if df_count==0:
                return True
            else:
                raise DuplicateObject(object_type=object_type,object_name=object_name)



        
    @staticmethod
    def role_exist(session,role_name):
        df=session.sql("SHOW ROLES")
        df=df.select(col("*")).collect()
        role_df=session.create_dataframe(df)
        role_count=role_df.filter(col("NAME")==role_name.upper()).count()
        if role_count:
            return True
        else:
            raise ObjectDoesNotExist(object_type='ROLE',object_name=role_name)
        
    @staticmethod
    def column_exist(session,database,schema,table,column):
        cols_inst=cols(session=session)
        if cols_inst.column_exist_in_table(database_name=database,schema_name=schema,table_name=table,column_name=column):
            return True
        else:
            raise ColumnDoesNotExist(object_type='TABLE',table_name=table,column_name=column)
        
    @staticmethod    
    def task_exist(session,database,schema,task):
        session.sql(f"USE DATABASE {database}").collect()
        session.sql(f"USE SCHEMA {schema}").collect()
        df=session.sql(f"SHOW TASKS")
        df=df.select(col("*")).collect()
        task_df=session.create_dataframe(df)
        task_count=task_df.filter((col("NAME")==task.upper()) & ( col("DATABASE_NAME")==database.upper() )& (col("SCHEMA_NAME")==schema.upper()) ).count()
        if task_count:
            return True
        else:
            raise ObjectDoesNotExist(object_type='TASK',object_name=task)
        
    @staticmethod
    def is_valid_user_email(session,user_email):
        df=session.sql("SHOW USERS")
        df=df.select(col("*")).collect()
        df=session.create_dataframe(df)
        df_users=df.select(col("NAME"),col("EMAIL"))
        exist_count=df_users.filter(col("NAME")==user_email.upper()).union(df_users.filter(col("EMAIL")== user_email.upper())).count()
        if exist_count==0:
                raise ObjectDoesNotExist(object_type='USER',object_name=user_email)
        return True
    
    @staticmethod
    def is_valid_external_volume(session,external_volume_identifier,object_type):
        df=session.sql(f"SELECT SYSTEM$VERIFY_EXTERNAL_VOLUME('{external_volume_identifier}')").collect()
        for return_lst in df:
            for return_stmt in return_lst:
                if "ERROR" in return_stmt.upper():
                    raise ObjectDoesNotExist(object_type=object_type,object_name=external_volume_identifier)
        return True
    
    @staticmethod
    def is_valid_catalog(session,catalog_identifier,object_type):
        df=session.sql(f"SHOW INTEGRATIONS")
        df=df.select(col("*")).collect()
        df=session.create_dataframe(df)
        catalog_count=df.filter((col("TYPE")=="CATALOG") & (col("NAME")==catalog_identifier.upper()) ).count()
        if catalog_count:
            return True
        else:
            raise ObjectDoesNotExist(object_type=object_type,object_name=catalog_identifier)
        
    @staticmethod
    def is_new_stage(session,database,schema,stage,obj_type,obj_name):
        stg_inst=stg(session=session)
        res=stg_inst.is_new_stage(db_name=database,schema_name=schema,stage_name=stage)
        if res:
            return res
        else:
            raise DuplicateObject(object_type=obj_type,object_name=obj_name)
        
    @staticmethod
    def is_new_warehouse(session,object_type,object_name):
        df=session.sql("SHOW WAREHOUSES")
        df=df.select(col("*")).collect()
        int_df=session.create_dataframe(df)
        int_count=int_df.filter(col("NAME")==f'{object_name.upper()}').count()
        if int_count==0:
            return True
        else:
            raise DuplicateObject(object_type=object_type,object_name=object_name)

    @staticmethod
    def is_new_integration(session,object_type,object_name):
        df=session.sql("SHOW INTEGRATIONS")
        df=df.select(col("*")).collect()
        int_df=session.create_dataframe(df)
        int_count=int_df.filter(col("NAME")==f'{object_name.upper()}').count()
        if int_count==0:
            return True
        else:
            raise DuplicateObject(object_type=object_type,object_name=object_name)
    
    @staticmethod
    def integration_exist(session,integration_name):
        df=session.sql('SHOW INTEGRATIONS')
        df=df.select(col("*")).collect()
        int_df=session.create_dataframe(df)
        int_count=int_df.filter(col("NAME") ==f'{integration_name.upper()}').count()        
        if int_count:
            return True
        else:
            raise ObjectDoesNotExist(object_type="INTEGRATION",object_name=integration_name)

    @staticmethod    
    def resource_monitor_exist(session,resource_monitor_name):
        df=session.sql('SHOW RESOURCE MONITORS')
        df=df.select(col("*")).collect()
        rm_df=session.create_dataframe(df)
        rm_count=rm_df.filter(col("NAME") ==f'{resource_monitor_name.upper()}').count()        
        if rm_count:
            return True
        else:
            raise ObjectDoesNotExist(object_type="RESOURCE MONITOR",object_name=resource_monitor_name)

    @staticmethod    
    def is_new_alert(session,database,schema,alert_name):
        session.sql(f"USE DATABASE {database}").collect()
        session.sql(f"USE SCHEMA {schema}").collect()
        df=session.sql('SHOW ALERTS')
        df=df.select(col("*")).collect()
        alert_df=session.create_dataframe(df)
        alert_count=alert_df.filter(col("NAME") ==f'{alert_name.upper()}').count()        
        if alert_count == 0:
            return True
        else:
            raise DuplicateObject(object_type="ALERT",object_name=alert_name)
        
    @staticmethod    
    def alert_exist(session,object_type,database,schema,alert_name):
        session.sql(f"USE DATABASE {database}").collect()
        session.sql(f"USE SCHEMA {schema}").collect()
        df=session.sql('SHOW ALERTS')
        df=df.select(col("*")).collect()
        alert_df=session.create_dataframe(df)
        alert_count=alert_df.filter(col("NAME") ==f'{alert_name.upper()}').count()        
        if alert_count:
            return True
        else:
            raise ObjectDoesNotExist(object_type=object_type,object_name=alert_name)
        
    @staticmethod
    def is_account_admin(session,user,object_type):
        grants=session.sql(f"show grants to user {user}")
        df=grants.select(col("*")).collect()
        df=session.create_dataframe(df)
        count_df=df.filter(col("ROLE")=="ACCOUNTADMIN").count()
        if count_df == 0:
            raise MustBeAnAdmin(object_type=object_type)
        else:
            return True

    @staticmethod    
    def is_new_resource_monitor(session,resource_monitor_name):
        df=session.sql('SHOW RESOURCE MONITORS')
        df=df.select(col("*")).collect()
        rm_df=session.create_dataframe(df)
        rm_count=rm_df.filter(col("NAME") ==f'{resource_monitor_name.upper()}').count()        
        if rm_count == 0:
            return True
        else:
            raise DuplicateObject(object_type="RESOURCE MONITOR",object_name=resource_monitor_name)

    @staticmethod
    def user_exist(session,user_name):
        df=session.sql('SHOW USERS')
        user_df=df.select(col("*")).collect()
        df=session.create_dataframe(user_df)
        user_exist=df.filter(col("name")== user_name.upper()).count()
        if user_exist:
            return True
        else:
            raise ObjectDoesNotExist(object_type="USER", object_name=user_name)
        
    @staticmethod
    def is_new_user(session,user_name,object_type):
        df=session.sql('SHOW USERS')
        user_df=df.select(col("*")).collect()
        df=session.create_dataframe(user_df)
        user_count=df.filter(col("name")== user_name.upper()).count()
        if user_count == 0:
            return True
        else:
            raise DuplicateObject(object_type=object_type,object_name=user_name)
    
    @staticmethod
    def attribute_exist(object_type,alter_dictionary,attribute_list):
        attributes_to_alter=list(alter_dictionary.keys())
        diff_list=list(set(attributes_to_alter) - set(attribute_list))
        if len(diff_list):
            raise InvalidAttributesToAlter(object_type=object_type,attribute_list=diff_list)
        else:
            return True
        
        
