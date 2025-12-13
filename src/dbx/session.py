
# add import here 

class DatabricksSession:
    def __init__(self,):
        pass

    def __set_environment_variables(self):
        #set your envmt variables here
        pass

    def __get_serverless_connection(self):
        self.__set_environment_variables()
        session=DatabricksSession.builder.serverless(True).getOrCreate()
        return session
    
    def connect(self,connection_type):
        if connection_type=='SERVERLESS':
            session=self.__get_serverless_connection()
        return session

    