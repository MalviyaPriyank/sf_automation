

import sys
import os

from .objectprivileges import (
    DatabasePrivileges,
    UserPrivileges,
    StagePrivileges,
    WarehousePrivileges,
    SchemaPrivileges,
    TablePrivileges,
    FileFormatPrivileges,
    SnowpipePrivileges,
    StreamPrivileges,
    TaskPrivileges)

sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))

from exception.privilegeexception import ObjectNotSupported

class Privilege:
    def __init__(self,cls,logger):
        self.logger=logger
        cls = cls.replace(' ','')
        if cls.upper()=='DATABASE':
            self.attr=DatabasePrivileges()
        if cls.upper()=='SCHEMA':
            self.attr=SchemaPrivileges()
        if cls.upper()=='WAREHOUSE':
            self.attr=WarehousePrivileges()
        if cls.upper()=='STAGE':
            self.attr=StagePrivileges()
        if cls.upper()=='TABLE':
            self.attr=TablePrivileges()
        if cls.upper()=='FILEFORMAT' or cls.upper()=='FILE_FORMAT':
            self.attr=FileFormatPrivileges()
        if cls.upper()=='SNOWPIPE':
            self.attr=SnowpipePrivileges()
        if cls.upper()=='STREAM':
            self.attr=StreamPrivileges()
        if cls.upper()=='TASK':
            self.attr=TaskPrivileges()
        if cls.upper()=='USER':
            self.attr=UserPrivileges()
        else:
            raise ObjectNotSupported(object_type=cls.upper())

    def get_allowed_privileges(self):
        self.logger.info(f"Getting privielges for  {self.attr.__class__.__name__}")
        self.attr.get_allowed_privileges()
        