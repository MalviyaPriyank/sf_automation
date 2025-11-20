
# Define your connection string
from sqlserverconnection import SqlServerConnection as SSConn
from sqlserverconnection import SqlServerOperations as SSOpr
import logging 
import pandas as pd

logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger(__name__).setLevel(logging.INFO)
logger = logging.getLogger(__name__)

if __name__=='__main__':
    conn=SSConn(logger=logger)
    conn=conn.get_sql_server_connection()
    operation=SSOpr(connection=conn,logger=logger)
    operation.enable_cdc_on_database(db='GyrusExperiment')
    df,from_lsn,to_lsn=operation.get_incremental_data(table_name='customer')
    df = df.drop(columns=['__$start_lsn','__$seqval','__$update_mask','__$operation'])
    print(df)

    




#DECLARE @from_lsn binary(10), @to_lsn binary(10);
#SET @from_lsn = sys.fn_cdc_get_min_lsn('dbo_customer');
#SET @to_lsn = sys.fn_cdc_map_time_to_lsn('largest less than or equal', GETDATE());
#SELECT * FROM cdc.fn_cdc_get_all_changes_dbo_customer(@from_lsn, @to_lsn, 'all');