import sys
import os
from .baseprivilege import BasePrivilege
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
from validation.validateobject import ValidateObject as vo

class DatabasePrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='DATABASE')
        vo.database_exist(session=session,database_name=object_identifier)
        super().set_object_identifier(val=object_identifier)
    
class UserPrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='USER')
        vo.user_exist(session=session,user_name=object_identifier)
        super().set_object_identifier(val=object_identifier)
    
class StagePrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier,database,schema):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='STAGE')
        vo.stage_exist(session=session,database_name=database,schema_name=schema)
        super().set_object_identifier(val=object_identifier)
    
class WarehousePrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='WAREHOUSE')
        vo.warehouse_exist(session=session,warehouse_name=object_identifier)
        super().set_object_identifier(val=object_identifier)
    
class SchemaPrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier,database):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='SCHEMA')
        vo.schema_exist(session=session,database_name=database,schema_name=object_identifier)
        super().set_object_identifier(val=object_identifier)

class TablePrivileges(BasePrivilege):
     def __init__(self,session,logger,object_identifier,database,schema):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='TABLE')
        vo.table_exist(session=session,database_name=database,schema_name=schema,table_name=object_identifier)
        object_identifier=f"{database}.{schema}.{object_identifier}"
        super().set_object_identifier(val=object_identifier)
    
class FileFormatPrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier,database,schema):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='FILE_FORMAT')
        vo.file_format_exist(session=session,database_name=database,schema_name=schema,file_format_name=object_identifier)
        object_identifier=f"{database}.{schema}.{object_identifier}"
        super().set_object_identifier(val=object_identifier)
    
class SnowpipePrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='PIPE')
        super().set_object_identifier(val=object_identifier)
    
class StreamPrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='STREAM')
        super().set_object_identifier(val=object_identifier)
    
class TaskPrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='TASK')
        super().set_object_identifier(val=object_identifier)