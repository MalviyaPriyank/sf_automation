import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))


from global_vars import Warehouse as gv_wh
from global_vars import Config as cfg
from obj import role,warehouse,database,schema,internalstage
from setup import privilege 

class InitialSetup:
    def __init__(self,
                 session):
        self.session = session
        
    def create_default_role(self):
        for rl,description in cfg._default_role.items():
            role.Role.create_object(self.session,**{"NAME":rl,"COMMENT":description})
            priv_inst = privilege.Privilege(self.session)
            priv_inst.grant_role_to_role(rl,"ACCOUNTADMIN")
            priv_inst.grant_role_to_role(rl,"SECURITYADMIN")


            
    
    def create_default_warehouse(self):
        for warehouse_name,warehouse_size in cfg._default_warehouse.items():
            warehouse.Warehouse.create_object(self.session,**{"NAME":warehouse_name,"TYPE":"STANDARD","SIZE": warehouse_size})
            
    
    def create_config_database(self):
        database.Database.create_object(self.session,**{"NAME":cfg._config_database})
    
    def create_config_schema(self):
        schema.Schema.create_object(self.session,**{"NAME":cfg._config_schema})
    
    def create_config_stage(self):
        internalstage.InternalStage.create_object(self.session,**{"NAME":cfg._config_stage})
    
    def create_deployment_stage(self):
        internalstage.InternalStage.create_object(self.session,**{"NAME":cfg._deployment_stage})
    
    def perform_initial_setup(self):
        self.create_default_role()
        self.create_default_warehouse()
        self.create_config_database()
        self.create_config_schema()
        self.create_config_stage()
        self.create_deployment_stage()