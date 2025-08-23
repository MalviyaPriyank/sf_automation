import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../conf'))
#sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))

from obj import role,warehouse,database,schema,internalstage
from setup import privilege 
#from conf import readconf
from dep.deploy import Deploy
from vars.gvobject import Config as cfg, Warehouse as gv_wh, Privilege as gv_priv


class InitialSetup:
    def __init__(self,
                 session,
                 logger,
                 user_id):
        self.session = session
        self.user_id = user_id
        self.logger=logger
        
    def create_default_role(self):
        for rl,description in cfg._default_role.items():
            self.logger.info(f"creatin role {rl} for {description}")
            role_inst = role.Role(session= self.session,user_id=self.user_id,logger=self.logger)
            self.logger.info("before create object")
            role_inst.create_object(*['initial'],**{"NAME":rl,"COMMENT":description})
            self.logger.info("after create object")
            priv_inst = privilege.Privilege(self.session)
            priv_inst.grant_role_to_role(rl,"ACCOUNTADMIN")
            priv_inst.grant_role_to_role(rl,"SECURITYADMIN")

    def create_default_warehouse(self):
        data_dict = readconf.main("warehouse")
        for warehouse_name,warehouse_size in cfg._default_warehouse.items():
            data_dict["NAME"] = warehouse_name
            data_dict["WAREHOUSE_SIZE"] = warehouse_size
            wh_inst = warehouse.Warehouse(session=self.session, user_id= self.user_id,logger=self.logger)
            wh_inst.create_object(*['initial'],**data_dict)
            priv_inst = privilege.Privilege(self.session)
            for role,privileges in cfg._default_role_privilege_set.items():
                if privileges in gv_priv._allowed_privileges["WAREHOUSE"]:
                    priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "WAREHOUSE",object_identifier=warehouse_name,role = role)

    
    def create_config_database(self):
        data_dict = readconf.main("database")
        data_dict["NAME"] = cfg._config_database
        db_inst = database.Database(session= self.session, user_id= self.user_id,logger=self.logger)
        db_inst.create_object(*['initial'],**data_dict)
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges["DATABASE"]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "DATABASE",object_identifier=cfg._config_database,role = role)
    

    
    def create_config_schema(self):
        data_dict = readconf.main("schema")
        data_dict["DATABASE"] = cfg._config_database
        data_dict["NAME"] = cfg._config_schema
        self.logger.info('getting schema instance')
        sch_inst = schema.Schema(session= self.session, user_id=self.user_id, logger=self.logger)
        self.logger.info('calling create object for schema')
        sch_inst.create_object(*['initial'],**data_dict)
        self.logger.info('after creating schema')
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges["SCHEMA"]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "SCHEMA",object_identifier=cfg._config_schema,role = role)


    
    def create_config_stage(self):
        data_dict = readconf.main("internalstage")
        data_dict["DATABASE"] = cfg._config_database
        data_dict["SCHEMA"] = cfg._config_schema
        data_dict["NAME"] = cfg._config_stage
        stg_inst = internalstage.InternalStage(session=self.session, user_id=self.user_id,logger=self.logger)
        stg_inst.create_object(*['initial'],**data_dict)
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges["STAGE"]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "STAGE",object_identifier=f'{cfg._config_database}.{cfg._config_schema}.{cfg._config_stage}',role = role)

        data_dict["NAME"] = cfg._deployment_stage
        stg_inst.create_object(*['initial'],**data_dict)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges["STAGE"]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "STAGE",object_identifier=f'{cfg._config_database}.{cfg._config_schema}.{cfg._deployment_stage}',role = role)

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

        deploy_inst.create_deploy_reference_table()
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges["TABLE"]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "TABLE",object_identifier=f"{cfg._config_database}.{cfg._config_schema}.{cfg._deployment_reference_table}",role = role)

        deploy_inst.create_deploy_scripts_table()
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges["TABLE"]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = "TABLE",object_identifier=f"{cfg._config_database}.{cfg._config_schema}.{cfg._deployment_scripts_table}",role = role)


    def perform_initial_setup(self):
        self.logger.info("before role setup")
        #self.create_default_role()
        self.logger.info("after role setup")
        self.create_default_warehouse()
        self.create_config_database()
        self.create_config_schema()
        self.create_config_stage()
        self.create_deployment_tables()

