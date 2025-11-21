
import sys
import os 


from .sqlserverconnection import SqlServerConnection as SSConn
from .sqlserverconnection import SqlServerOperations as SSOpr

import logging 
import pandas as pd
from src.obj import session as snowflake_session
import src.obj.utils as util
from src.cdc.cdc import CDC

logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger(__name__).setLevel(logging.INFO)
logger = logging.getLogger(__name__)

if __name__=='__main__':
    db = 'GyrusExperiment'
    table_name='customer'
    session_inst = snowflake_session.Session()
    session_inst.set_user('frosty')
    session_inst.set_password('Hellopehlaadmi@24')
    session_inst.set_account('kzekzkb-pm40264')
    session_state = session_inst.get_session()
    #SQL Server connection
    conn=SSConn(logger=logger)
    conn=conn.get_sql_server_connection()
    operation=SSOpr(connection=conn,logger=logger)
    cdc_inst=CDC(session=session_state,logger=logger)
    #User : Pull data from table ABC to Snowflake
    #Response : Is it first time load or incremental.
    #If its first time then ZEUS need to enable cdc
    #Tool to enable CDC on Datbase (requires database name)
    operation.enable_cdc_on_database(db=db)
    df,from_lsn,to_lsn=operation.get_incremental_data(cdc_inst=cdc_inst,table_name=table_name,db_name=db)
    df = df.drop(columns=['__$start_lsn','__$seqval','__$update_mask','__$operation'])
    util.write_pandas_df_to_snowflake(session=session_state,df=df,database='SQL_SERVER_CDC_DB',schema='CDC_LANDING',table=table_name)
    cdc_inst.log_cdc(server='MSSQL',**{'DATABASE':db,'OBJECT':table_name,'LSN':to_lsn.hex().upper()})
    

    




#DECLARE @from_lsn binary(10), @to_lsn binary(10);
#SET @from_lsn = sys.fn_cdc_get_min_lsn('dbo_customer');
#SET @to_lsn = sys.fn_cdc_map_time_to_lsn('largest less than or equal', GETDATE());
#SELECT * FROM cdc.fn_cdc_get_all_changes_dbo_customer(@from_lsn, @to_lsn, 'all');