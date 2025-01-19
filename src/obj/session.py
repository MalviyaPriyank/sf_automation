
import snowflake.snowpark as snowpark
from snowflake.core import Root



class User:
    def __get__(self,instance,owner):
        return instance._user
    
    def __set__(self,instance,value):
        instance._user = value

    def __delete__(self,instance):
        del instance._user

class Password:
    def __get__(self,instance,owner):
        return instance._password
    
    def __set__(self,instance,value):
        instance._password = value

    def __delete__(self,instance):
        del instance._password

class Account:
    def __get__(self,instance,owner):
        return instance._account
    
    def __set__(self,instance,value):
        instance._account = value

    def __delete__(self,instance):
        del instance._account

class Account:
    def __get__(self,instance,owner):
        return instance._account
    
    def __set__(self,instance,value):
        instance._account = value

    def __delete__(self,instance):
        del instance._account

class Session:
    def __get__(self,instance,owner):
        return instance._session
    
    def __set__(self,instance,value):
        instance._session = value

    def __delete__(self,instance):
        del instance._session

class SessionAttr:
    def __init__(self,parent):
        self.parent = parent

    user = User()
    password = Password()
    account = Account()
    session = Session()

class Session:
    def __init__(self):
        self.attr = SessionAttr(self)
    
    def set_user(self,value):
        self.attr.user = value
    
    def set_password(self,value):
        self.attr.password = value

    def set_account(self,value):
        self.attr.account = value

    def get_session(self):
        self.set_user(self.attr.user)
        self.set_password(self.attr.password)
        self.set_account(self.attr.account)
        self.attr.session = (snowpark.Session.builder.config("account",self.attr.account).config("user",self.attr.user).config("password",self.attr.password).create())
        return self.attr.session
    
    def get_root_object(self):
        root = Root(self.attr.session)
        return root




    

'''
def main():
    con = snowflake.connector.connect(
    user='rick',
    password='mejzyg-pafpov-9noXmi',
    account='TQNXPFG.BG28519',
    session_parameters={
        'QUERY_TAG': 'BOTRUN',
    }
    )
    return con
'''