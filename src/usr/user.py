
from datetime import datetime
import uuid

class User:
    def __init__(self,user_name):
        self.user_name=user_name

    def queries(self,mode):
        if mode.upper()=="REGISTER":
            register_time = datetime.now()
            self.register_qry=f"INSERT INTO USER VALUES ('{self.user_name}','TRUE',{register_time})"
        if mode.upper()=="USER_IN_SESSION_VALIDATION":
            self.register_qry=f"SELECT FROM USER WHERE USER_NAME='{self.user_name}' and IN_SESSION='TRUE'"

    def register_user(self,sf_session):
        qry=self.queries('USER_IN_SESSION_VALIDATION')
        sf_session.sql(qry).count()
        qry=self.queries(mode='REGISTER')
        sf_session.sql(qry).collect()
        return f"{self.user_name} registered"
    
    def suspend_active_users(self):
        pass

class Session:
    def __init__(self):
        self.session_id=str(uuid.uuid4())



class ChatHistory:
    def __init__(self,user_name):
        self.user_name=user_name
        self.chat_id=str(uuid.uuid4())
        self.work_dict={}

    def __add_object_to_work_dict(self,object_type,object_identifier,qry):
        if object_type not in self.work_dict:
            self.work_dict[object_type] = {}            
        self.work_dict[object_type][object_identifier]=qry

    def __log_chat_details(self,snowflake_session):
        qry=f"""
        INSERT INTO db_config.sch_config.frosty_work_log (
        session_id,
        user_name,
        chat_id,
        sql_qry
        )
        SELECT
        '{snowflake_session.session_id}'
        ,'{self.user_name}'
        ,'{self.chat_id}'
        ,PARSE_JSON({f'{self.work_dict}'}
        """

    def add_to_chat_history(self,object_type,object_identifier,qry):
        self.__add_object_to_work_dict(object_type=object_type,object_identifier=object_identifier,qry=qry)

    def store_chat_history(self,snowflake_session):
        self.__log_chat_details(snowflake_session)

        
