from abc import ABC,abstractmethod
import sys
import os 
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../git'))

from dep import deploy
from vars.gvobject import Config as cfg
from repository import Repository   

class AbstractObject(ABC):
    def __init__(self,session,user_id,logger):
        self.session=session
        self.user_id=user_id
        self.logger=logger
        self.qry=""

    @abstractmethod
    def execute_final_query(self):
        pass

class BaseObject(AbstractObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session = session, user_id = user_id, logger = logger)
    
    def execute_final_query(self):
        self.session.sql(self.qry).collect()

    def create_deployment_entry(self,object_name,object_type,object_database,object_schema):
        deploy_inst = deploy.Deploy(self.session,logger=self.logger)
        self.logger.info(f"Tracking for deployment database object : {object_name}")
        deploy_inst.insert_into_deployment_script_table(obj_qry=self.qry, user_id=self.user_id)
        deploy_inst.set_object_type(object_type)
        deploy_inst.set_object_database(object_database)
        deploy_inst.set_object_schema(object_schema)
        deploy_inst.set_object_name(object_name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()

    def write_file_to_git(self,object_name,object_type,object_database,object_schema):
        commit_msg=f"Modify {object_type} {object_name} by {self.user_id}"
        self.logger.info(f"{commit_msg}")
        if object_database != 'NA' and object_schema != 'NA':
            filepath=f"Database/{object_database}/Schemas/{object_schema}/{object_type}/{object_name}.sql"
            repo = Repository()
            self.logger.info(f"Writing file for {object_type} {object_name} in database {object_database} and schema {object_schema} to repo")
            self.logger.info("Before cloning")
            repo.clone_repo()
            self.logger.info("After cloning")
            repo.instantiate_repo()
            repo.write_file_to_local(filepath=filepath,content=self.qry)
            repo.add_file_for_push(filepath=filepath,commit_msg=commit_msg)
            repo.push_file_to_remote()
        elif object_database !='NA' and object_schema == 'NA':
            filepath=f"Database/{object_database}/Schemas/{object_name}.sql"
            repo = Repository()
            self.logger.info(f"Writing file for {object_type} {object_name} in database {object_database} to repo")
            self.logger.info("Before cloning")
            repo.clone_repo()
            self.logger.info("After cloning")
            repo.instantiate_repo()
            repo.write_file_to_local(filepath=filepath,content=self.qry)
            repo.add_file_for_push(filepath=filepath,commit_msg=commit_msg)
            repo.push_file_to_remote()
        elif object_database =='NA':
            filepath=f"Database/{object_name}/{object_name}.sql"
            repo = Repository()
            self.logger.info(f"Writing file for {object_type} {object_name} to repo")
            self.logger.info("Before cloning")
            repo.clone_repo()
            self.logger.info("After cloning")
            repo.instantiate_repo()
            repo.write_file_to_local(filepath=filepath,content=self.qry)
            repo.add_file_for_push(filepath=filepath,commit_msg=commit_msg)
            repo.push_file_to_remote()
            