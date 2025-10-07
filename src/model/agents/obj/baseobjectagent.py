class BaseObjectAgent:
    def __init__(self,agent_type,model_id,temperature):
        self.agent_type=agent_type
        self.model_id=model_id
        self.temperature=temperature

    def init_metadata(self,logger,sf_session,user_id):
        self.logger=logger
        self.sf_session=sf_session
        self.user_id=user_id










        


    