import sys 
import os

from snowflake.snowpark.functions import col
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from vars.gvaccountusage import CopyHistoryView


class CopyHistory:
    def __init__(self,session):
        self.attr=CopyHistoryView().attr
        self.session=session

    def get_load_history_for_a_pipe(self,pipe_db,pipe_schema,pipe_name):
        df=self.session.table(self.attr._view)\
            .filter((col(self.attr._pipe_catalog_name)==pipe_db)\
                    &(col(self.attr._pipe_schema_name)==pipe_schema)\
                    &(col(self.attr._pipe_name)==pipe_name))\
            .select(col(self.attr._status),col(self.attr._file_name),col(self.attr._row_count))\
            .sort(col(self.attr._last_load_time).desc()).limit(10)
        return df
        
    def get_load_history_for_a_table(self,table_db,table_schema,table_name):
        """
        df=self.session.table(self.attr._view)\
                    .filter(col((self.attr._table_catalog_name)==table_db)\
                            & (col(self.attr._table_schema_name)==table_schema)\
                            &(col(self.attr._table_name))==table_name)\
                    .select(col(self.attr._status),col(self.attr._file_name),col(self.attr._row_count))\
                    .sort(col(self.attr._last_load_time).desc()).limit(10)
        """
        self.session.sql(f"use database {table_db}").collect()
        self.session.sql(f"use schema {table_schema}").collect()
        df=self.session.sql(f"select * from table(information_schema.copy_history(TABLE_NAME=>{table_name}, START_TIME=> DATEADD(hours, -24, CURRENT_TIMESTAMP())))").collect()
        return df
    