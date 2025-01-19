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

 
def create_default_role(session):
    for role,description in gv_rl._default_role.items():
        Role.create_object(session,{"NAME":role,"COMMENT":description})

def create_default_warehouse(session):
    for warehouse_name,warehouse_size in gv_wh.__default_warehouse.items():
        Warehouse.create_object(session,{"NAME":warehouse_name,"TYPE":"STANDARD","SIZE": warehouse_size})

def create_config_database(session):
    Database.create_object(session,{"NAME":cfg._config_database})

def create_config_schema(session):
    Schema.create_object(session,{"NAME":cfg._config_schema})

def create_config_stage(session):
    InternalStage.create_object(session,{"NAME":cfg._config_stage})

def create_deployment_stage(session):
    InternalStage.create_object(session,{"NAME":cfg._deployment_stage})


def main(session):
    create_default_role(session)
    create_default_warehouse(session)
    create_config_database(session)
    create_config_schema(session)
    create_config_stage(session)
    create_deployment_stage(session)

    
    