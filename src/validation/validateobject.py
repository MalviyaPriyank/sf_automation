import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../inf_schema'))


from infschema.databases import Databases as db
from infschema.schemata import Schemata as sch
from infschema.tables import Tables as tbl
from infschema.stages import Stages as stg
from infschema.fileformats import FileFormats as ff
from exception.objectexception import ( 
    ObjectDoesNotExist,
    DuplicateObject
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
    def is_new_table(session,database_name,schema_name):
        tbl_inst = tbl(session=session)
        if tbl_inst.is_new_table(database_name,schema_name):
            return True
        else:
            raise DuplicateObject('TABLE', schema_name)
        
    @staticmethod
    def is_new_stage(session,database_name,schema_name,stage_name):
        stg_inst = stg(session)
        if stg_inst.is_new_stage(db_name=database_name, schema_name=schema_name, stage_name=stage_name):
            return True
        else:
            raise DuplicateObject('STAGE',stage_name)
        
    @staticmethod
    def is_new_file_format(session,database_name,schema_name,file_format_name):
        ff_inst = ff(session)
        if ff_inst.is_new_file_format(db_name=database_name, schema_name=schema_name, file_format_name=file_format_name):
            return True
        else:
            raise DuplicateObject('FILE_FORMAT',file_format_name)

        


