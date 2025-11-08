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
    
    def execute_final_query(self,**kwargs):
        if 'DATABASE' in kwargs.keys():
            self.session.sql(f"USE DATABASE {kwargs['DATABASE']}").collect()
        
        self.session.sql(self.qry).collect()
    
    def print_query(self):
        self.logger.info(f" Query : {self.qry}")
    def create_deployment_entry(self,object_name,object_type,object_database,object_schema):
        deploy_inst = deploy.Deploy(self.session,logger=self.logger)
        self.logger.info(f"Tracking for deployment database object : {object_name}")
        deploy_inst.track_development(qry=self.qry,
                                      user_id=self.user_id,
                                      object_type=object_type,
                                      object_database=object_database,
                                      object_schema=object_schema,
                                      object_name=object_name)

    def write_file_to_git(self,object_name,object_type,object_database,object_schema):
        self.logger.info(f" BEGIN: write_file_to_git")
        commit_msg=f"Modify {object_type} {object_name} by {self.user_id}"
        self.logger.info(f"{commit_msg}")
        if object_database != 'NA' and object_schema != 'NA':
            filepath=f"Database/{object_database}/Schemas/{object_schema}/{object_type}/{object_name}.sql"
        elif object_database !='NA' and object_schema == 'NA':
            filepath=f"Database/{object_database}/Schemas/DDL/{object_name}.sql"
        elif object_database =='NA' and object_schema != 'NA':
            filepath=f"Database/{object_name}/DDL/{object_name}.sql"
        elif object_database =='NA' and object_schema == 'NA':
            filepath=f"{object_type}/{object_name}/DDL/{object_name}.sql"
        self.logger.info(f"Writing file for {object_type} {object_name} in database {object_database} and schema {object_schema} to repo")
        self.logger.info("Before cloning")
        repo = Repository(self.logger)
        repo.sync_repo(filepath=filepath,qry=self.qry,commit_msg=commit_msg)
        self.logger.info(f" EXIT: write_file_to_git")
