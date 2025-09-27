import sys 
import os

from snowflake.snowpark.functions import col
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from vars.gvinformationschema import Column
class Columns:
    def __init__(self,session):
        self.col = Column().columns
        self.session = session

    def column_exist_in_table(self,database_name,schema_name,table_name,column_name):
        df=self.session.table(self.col._view).select(col(self.col._column_name))\
            .filter(col(self.col._table_catalog)==database_name.upper() \
                    & col(self.col._table_schema)==schema_name.upper()\
                    & col(self.col._table_name)==table_name.upper
                    & col(self.col._column_name)==column_name.upper())
        res=df.collect()

        if len(res)==0:
            return False
        elif len(res)>0:
            return True
        
    def get_all_columns_of_a_table(self,database_name,schema_name,table_name):
        """
        Returns:
            All columns of a table in a list.
        """
        lst=[]
        df=self.session.table(self.col._view)\
            .select(col(self.col._column_name))\
            .filter(col(self.col._table_catalog)==database_name.upper()\
                    & col(self.col._table_schema)==schema_name.upper()\
                    & col(self.col._table_name)==table_name.upper())
        res=df.collect()
        for i in res:
            lst.append(i[0])
        return lst
