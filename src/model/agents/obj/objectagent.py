from baseobjectagent import BaseObjectAgent
class DatabaseAgent(BaseObjectAgent):
    def __init__(self,model_id, temperature,logger,sf_session,user_id):
        super().__init__(agent_type='DATABASE',model_id=model_id, temperature=temperature)
        super().init_metadata(logger=logger,sf_session=sf_session,user_id=user_id)

class SchemaAgent(BaseObjectAgent):
    def __init__(self, model_id, temperature,logger,sf_session,user_id):
        super().__init__(agent_type='SCHEMA',model_id=model_id, temperature=temperature)
        super().init_metadata(logger=logger,sf_session=sf_session,user_id=user_id)

class FileFormatAgent(BaseObjectAgent):
    def __init__(self, model_id, temperature,logger,sf_session,user_id):
        super().__init__(agent_type='FILEFORMAT',model_id=model_id, temperature=temperature)
        super().init_metadata(logger=logger,sf_session=sf_session,user_id=user_id)
