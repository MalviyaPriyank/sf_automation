

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
    def __init__(self,session,logger,object_type,object_identifier):
        object_type = object_type.replace(' ','')
        if object_type.upper()=='DATABASE':
            self.obj=DatabasePrivileges(session=session,logger=logger,object_identifier=object_identifier)
        if object_type.upper()=='SCHEMA':
            self.obj=SchemaPrivileges(session=session,logger=logger,object_identifier=object_identifier)
        if object_type.upper()=='WAREHOUSE':
            self.obj=WarehousePrivileges(session=session,logger=logger,object_identifier=object_identifier)
        if object_type.upper()=='STAGE':
            self.obj=StagePrivileges(session=session,logger=logger,object_identifier=object_identifier)
        if object_type.upper()=='TABLE':
            self.obj=TablePrivileges(session=session,logger=logger,object_identifier=object_identifier)
        if object_type.upper()=='FILEFORMAT' or object_type.upper()=='FILE_FORMAT':
            self.obj=FileFormatPrivileges(session=session,logger=logger,object_identifier=object_identifier)
        if object_type.upper()=='SNOWPIPE':
            self.obj=SnowpipePrivileges(session=session,logger=logger,object_identifier=object_identifier)
        if object_type.upper()=='STREAM':
            self.obj=StreamPrivileges(session=session,logger=logger,object_identifier=object_identifier)
        if object_type.upper()=='TASK':
            self.obj=TaskPrivileges(session=session,logger=logger,object_identifier=object_identifier)
        if object_type.upper()=='USER':
            self.obj=UserPrivileges(session=session,logger=logger,object_identifier=object_identifier)
        else:
            raise ObjectNotSupported(object_type=object_type.upper())

    def find_privileges(self):
        return self.obj.get_allowed_privileges()
    
    def grant_privilege(self,privelege_type,role):
        self.obj.grant_privilege_on_object_to_role(privlege_type=privelege_type,role=role)
        
        