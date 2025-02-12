import sys 
import os

from snowflake.snowpark.functions import col
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from vars.gvinformationschema import FileFormat
class FileFormats:
    def __init__(self,session):
        self.col = FileFormat().columns
        self.session = session

    def is_existing_file_format(self,db_name,schema_name,file_format_name):
        df = self.session.table(self.col._view).filter((col(self.col._file_format_catalog) == db_name) and (col(self.col._file_format_schema) == schema_name) and (col(self.col._file_format_name) == file_format_name))
        res = df.collect()
        if len(res) == 0:
            return False
        elif len(res) > 0:
            return True
        
    def is_new_file_format(self,db_name,schema_name,file_format_name):
        df = self.session.table(self.col._view).filter((col(self.col._file_format_catalog) == db_name) and (col(self.col._file_format_schema) == schema_name) and (col(self.col._file_format_name) == file_format_name))
        res = df.collect()
        if len(res) == 0:
            return True
        elif len(res) > 0:
            return False