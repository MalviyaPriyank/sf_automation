import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../obj'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from role import Role
from warehouse import Warehouse
from global_vars import Role as RL 
from global_vars import Warehouse as WH 
 
def create_default_role(session):
    for role,description in RL._default_role.items():
        Role.create_object(session,{"NAME":role,"COMMENT":description})

def create_default_warehouse(session):
    for warehouse_name,warehouse_size in WH.__default_warehouse.items():
        Warehouse.create_object(session,{"NAME":warehouse_name,"TYPE":"STANDARD","SIZE": warehouse_size})

def main(session):
    create_default_role(session)
    create_default_warehouse(session)

    
    