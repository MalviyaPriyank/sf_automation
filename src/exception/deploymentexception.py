import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))

from snowchainexception import SnowchainException


class DeploymentException(SnowchainException):
    def __init__(self, error_message):
        super().__init__(error_message)

class NoScriptsForObjectForDeployment(DeploymentException):
    def __init__(self, src_db,deployment_status,object):
        error_message=f"No scripts with status {deployment_status} for {object} found in {src_db}"
        super().__init__(error_message)

class NoScriptsForDeployment(DeploymentException):
    def __init__(self, src_db, deployment_status):
        error_message=f"No scripts with status {deployment_status} found in {src_db}"
        super().__init__(error_message)

