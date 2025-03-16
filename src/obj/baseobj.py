from abc import ABC,abstractmethod

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
