from databricks.connect import DatabricksSession
import os

class DbxSession:
    def __init__(self):
        self.host = "dbc-cdf6749f-447c.cloud.databricks.com"
        self.token = "dapic1831193e6dae964a67886c786849648"

    def __set_environment_variables(self):
        os.environ["DATABRICKS_HOST"] = f"https://{self.host}"
        os.environ["DATABRICKS_TOKEN"] = self.token

    def __get_serverless_connection(self):
        self.__set_environment_variables()
        session=DatabricksSession.builder.serverless(True).getOrCreate()
        return session
    
    def connect(self,connection_type):
        if connection_type=='SERVERLESS':
            session=self.__get_serverless_connection()
        return session

