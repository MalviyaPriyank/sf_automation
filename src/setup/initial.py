import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../conf'))
#sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))

from obj import role,warehouse,database,schema,internalstage
from setup import privilege 
from conf import readconf
from deploy.deploy import Deploy
from vars.global_vars import Config as cfg, Warehouse as gv_wh, Privilege as gv_priv


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
        data_dict = readconf.main("warehouse")
        for warehouse_name,warehouse_size in cfg._default_warehouse.items():
            data_dict["NAME"] = warehouse_name
            data_dict["WAREHOUSE_SIZE"] = warehouse_size

            warehouse.Warehouse.create_object(self.session,**data_dict)
            priv_inst = privilege.Privilege(self.session)
            for role,privileges in cfg._default_role_privilege_set.items():
                if privileges in gv_priv._allowed_privileges["WAREHOUSE"]:
                    priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "WAREHOUSE",object_identifier=warehouse_name,role = role)

    
    def create_config_database(self):
        data_dict = readconf.main("database")
        data_dict["NAME"] = cfg._config_database
        database.Database.create_object(self.session,**data_dict)
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges["DATABASE"]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "DATABASE",object_identifier=cfg._config_database,role = role)
    

    
    def create_config_schema(self):
        data_dict = readconf.main("schema")
        data_dict["DATABASE"] = cfg._config_database
        data_dict["NAME"] = cfg._config_schema
        schema.Schema.create_object(self.session,**data_dict)
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges["SCHEMA"]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "SCHEMA",object_identifier=cfg._config_schema,role = role)


    
    def create_config_stage(self):
        data_dict = readconf.main("internalstage")
        data_dict["DATABASE"] = cfg._config_database
        data_dict["SCHEMA"] = cfg._config_schema
        data_dict["NAME"] = cfg._config_stage
        internalstage.InternalStage.create_object(self.session,**data_dict)
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges["STAGE"]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "STAGE",object_identifier=cfg._config_stage,role = role)

    
    def create_deployment_stage(self):
        data_dict = readconf.main("internalstage")
        data_dict["DATABASE"] = cfg._config_database
        data_dict["SCHEMA"] = cfg._config_schema
        data_dict["NAME"] = cfg._deployment_stage
        internalstage.InternalStage.create_object(self.session,**data_dict)
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges["STAGE"]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "STAGE",object_identifier=cfg._config_stage,role = role)


    def create_deployment_tables(self):
        deploy_inst = Deploy(self.session)
        priv_inst = privilege.Privilege(self.session)
        
        deploy_inst.create_deploy_control_table()
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges["TABLE"]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "TABLE",object_identifier=f"{cfg._config_database}.{cfg._config_schema}.{cfg._deployment_control_table}",role = role)
       
        deploy_inst.create_deploy_history_table()
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges["TABLE"]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "TABLE",object_identifier=f"{cfg._config_database}.{cfg._config_schema}.{cfg._deployment_history_table}",role = role)
        
        deploy_inst.create_deploy_log_table()
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges["TABLE"]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "TABLE",object_identifier=f"{cfg._config_database}.{cfg._config_schema}.{cfg._deployment_log_table}",role = role)



    def perform_initial_setup(self):
        self.create_default_role()
        self.create_default_warehouse()
        self.create_config_database()
        self.create_config_schema()
        self.create_config_stage()
        self.create_deployment_stage()
        self.create_deployment_tables()

