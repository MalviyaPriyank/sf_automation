import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../obj'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from global_vars import Role as gv_rl
from global_vars import Warehouse as gv_wh
from global_vars import Config as cfg
from role import Role
from warehouse import Warehouse
from database import Database
from schema import Schema
from internalstage import InternalStage


class InitialSetup:
    def __init__(self,
                 session):
        self.session = session
        
    def create_default_role(self):
        for role,description in gv_rl._default_role.items():
            Role.create_object(self.session,{"NAME":role,"COMMENT":description})
    
    def create_default_warehouse(self):
        for warehouse_name,warehouse_size in gv_wh.__default_warehouse.items():
            Warehouse.create_object(self.session,{"NAME":warehouse_name,"TYPE":"STANDARD","SIZE": warehouse_size})
    
    def create_config_database(self):
        Database.create_object(self.session,{"NAME":cfg._config_database})
    
    def create_config_schema(self):
        Schema.create_object(self.session,{"NAME":cfg._config_schema})
    
    def create_config_stage(self):
        InternalStage.create_object(self.session,{"NAME":cfg._config_stage})
    
    def create_deployment_stage(self):
        InternalStage.create_object(self.session,{"NAME":cfg._deployment_stage})
    
    def perform_initial_setup():
        self.create_default_role()
        self.create_default_warehouse()
        self.create_config_database()
        self.create_config_schema()
        self.create_config_stage()
        self.create_deployment_stage()