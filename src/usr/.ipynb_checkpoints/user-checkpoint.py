
from datetime import datetime
import uuid
import json

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

    def __register_session(self,user:User):
        qry=f"""
        INSERT INTO db_config.sch_config.user_session_log (
        session_id
        ,user_name
        )
        values(
        '{self.session_id}'
        ,'{user.user_name}'
        )
        """
        return qry

    def register_session(self,user:User,snowflake_session):
        register_qry=self.__register_session(user=user)
        snowflake_session.sql(register_qry).collect()

class ChatHistory:
    def __init__(self,user:User,session:Session):
        self.user_name=user.user_name
        self.session_id=session.session_id
        self.chat_id=str(uuid.uuid4())
        self.work_dict={}
        self.chat_history=[]

    def __add_object_to_work_dict(self,object_type,object_identifier,qry):
        if object_type not in self.work_dict:
            self.work_dict[f"{object_type}"] = {}
        self.work_dict[f"{object_type}"][f"{object_identifier}"]=f"{qry}"

    def __log_chat_details(self):
        # Produce valid compact JSON string
        work_dict = json.dumps(self.work_dict)

        # Escape $$ so that PARSE_JSON($$ ... $$) is safe
        work_dict = work_dict.replace('$$', '\\$\\$')

        qry = f"""
        INSERT INTO db_config.sch_config.frosty_work_log (
            session_id,
            user_name,
            chat_id,
            sql_qry,
            prompt
        )
        SELECT
            '{self.session_id}',
            '{self.user_name}',
            '{self.chat_id}',
            PARSE_JSON($${work_dict}$$),
            '{self.prompt.replace("'", "''")}'
        """
        return qry

    
    def add_prompt(self,prompt):
        self.prompt=prompt

    def add_to_chat_history(self, object_type, object_identifier, qry):
        cleaned = (
            qry
            .replace('\\', '\\\\')     # escape backslashes
            .replace('\n', '\\n')       # escape newlines
            .replace('$$', '\\$\\$')    # escape Snowflake $$ blocks
        )

        self.__add_object_to_work_dict(
            object_type=object_type,
            object_identifier=object_identifier,
            qry=cleaned
        )


    def store_chat_history(self,snowflake_session):
        qry=self.__log_chat_details()
        snowflake_session.sql(qry).collect()
        
