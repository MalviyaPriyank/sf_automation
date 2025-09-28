from .baseprivilege import BasePrivilege

class DatabasePrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='DATABASE')
        super().set_object_identifier(val=object_identifier)
    
class UserPrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='USER')
        super().set_object_identifier(val=object_identifier)
    
class StagePrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='STAGE')
        super().set_object_identifier(val=object_identifier)
    
class WarehousePrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='WAREHOUSE')
        super().set_object_identifier(val=object_identifier)
    
class SchemaPrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='SCHEMA')
        super().set_object_identifier(val=object_identifier)

class TablePrivileges(BasePrivilege):
     def __init__(self,session,logger,object_identifier):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='TABLE')
        super().set_object_identifier(val=object_identifier)
    
class FileFormatPrivileges(BasePrivilege):
    def __init__(self,session,logger,object_identifier):
        super().__init__(session=session,logger=logger)
        super().set_object_type(val='FILE_FORMAT')
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