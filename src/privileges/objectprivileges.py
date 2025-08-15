from .baseprivilege import BasePrivilege

class DatabasePrivileges(BasePrivilege):
    def __init__(self):
        super().__init__()

    def set_object_type(self):
        super().set_object_type('DATABASE')
    
class UserPrivileges(BasePrivilege):
    def __init__(self):
        super().__init__()

    def set_object_type(self):
        super().set_object_type('USER')
    
class StagePrivileges(BasePrivilege):
    def __init__(self):
        super().__init__()

    def set_object_type(self):
        super().set_object_type('STAGE')
    
class WarehousePrivileges(BasePrivilege):
    def __init__(self):
        super().__init__()

    def set_object_type(self):
        super().set_object_type('WAREHOUSE')
    
class SchemaPrivileges(BasePrivilege):
    def __init__(self):
        super().__init__()

    def set_object_type(self):
        super().set_object_type('SCHEMA')

class TablePrivileges(BasePrivilege):
    def __init__(self):
        super().__init__()

    def set_object_type(self):
        super().set_object_type('TABLE')
    
class FileFormatPrivileges(BasePrivilege):
    def __init__(self):
        super().__init__()

    def set_object_type(self):
        super().set_object_type('FILE FORMAT')
    
class SnowpipePrivileges(BasePrivilege):
    def __init__(self):
        super().__init__()

    def set_object_type(self):
        super().set_object_type('PIPE')
    
class StreamPrivileges(BasePrivilege):
    def __init__(self):
        super().__init__()

    def set_object_type(self):
        super().set_object_type('STREAM')
    
class TaskPrivileges(BasePrivilege):
    def __init__(self):
        super().__init__()

    def set_object_type(self):
        super().set_object_type('TASK')