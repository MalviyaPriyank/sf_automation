import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../infschema'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))

from infschema.columns import Columns

class FullLoad:
    def __init__(self,session,logger):
        self.information=Columns(session=session)
        self.session=session
        self.logger=logger

    def get_columns_of_table(self,database_name,schema_name,table_name):
        col_lst=self.information.get_all_columns_of_a_table(database_name=database_name,schema_name=schema_name,table_name=table_name)
        return col_lst
    
    def get_append_string_for_insert(self,tgt_col_lst):
        append_strng="( "
        for i in range(0,len(tgt_col_lst)):
            if i!= len(tgt_col_lst)-1:
                append_strng=append_strng+tgt_col_lst[i]+ ", "
            elif i == len(tgt_col_lst)-1:
                append_strng=append_strng+tgt_col_lst[i] +")"

        return append_strng
    
    def get_append_string_for_select(self,src_col_lst):
        self.logger.info(f"src col lst :{src_col_lst}")
        append_strng= " SELECT "
        for i in range(0,len(src_col_lst)):
            if i != len(src_col_lst)-1:
                append_strng = append_strng + src_col_lst[i] + ", "
            elif i==len(src_col_lst)-1:
                append_strng = append_strng + src_col_lst[i] +" FROM " 
        return append_strng
    
    def insert_from_src_to_target(self,src_database,src_schema,src_table,tgt_database,tgt_schema,tgt_table):
        src_col_lst=self.get_columns_of_table(database_name=src_database,schema_name=src_schema,table_name=src_table)
        tgt_col_lst=self.get_columns_of_table(database_name=tgt_database,schema_name=tgt_schema,table_name=tgt_table)
        sql_script= f"""
        INSERT INTO 
        {tgt_database}.{tgt_schema}.{tgt_table}
        """
        insert_strng=self.get_append_string_for_insert(tgt_col_lst=tgt_col_lst)
        sql_script = sql_script + insert_strng 
        select_strng=self.get_append_string_for_select(src_col_lst=src_col_lst)
        
        sql_script = sql_script + select_strng + f"{src_database}.{src_schema}.{src_table};"
        return sql_script
    
    def truncate_table(self,db,schema,table):
        truncate_script = f"TRUNCATE TABLE {db}.{schema}.{table}"
        self.logger.info(f" running {truncate_script}")
        self.session.sql(truncate_script).collect()
    
    def load_data_from_src_to_target(self,src_database,src_schema,src_table,tgt_database,tgt_schema,tgt_table):
        self.logger.info("Truncating target table ")
        self.truncate_table(db=tgt_database,schema=tgt_schema,table=tgt_table)
        self.logger.info("Generating sql to load data")
        sql_script=self.insert_from_src_to_target(src_database=src_database,
                                       src_schema=src_schema,
                                       src_table=src_table,
                                       tgt_database=tgt_database,
                                       tgt_schema=tgt_schema,
                                       tgt_table=tgt_table)
        self.logger.info(f"Script generated :{sql_script}")
        self.logger.info("Going to load data")
        return sql_script      
        
            
    

    