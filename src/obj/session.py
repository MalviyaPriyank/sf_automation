
#import snowflake

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

class SessionAttr:
    def __init__(self,parent):
        self.parent = parent

    user = User()
    password = Password()
    account = Account()

class Session:
    def __init__(self):
        self.attr = SessionAttr(self)
    
    def set_user(self,value):
        self.attr.user = value
    
    def set_password(self,value):
        self.attr.password = value

    def set_account(self,value):
        self.attr.account = value

    def get_connection(self,user,password,account):
        self.set_user(user)
        self.set_password(password)
        self.set_account(account)
        con = snowflake.connector.connect(
                user=self.attr.user,
                password=self.attr.password,
                account= self.attr.account,
                session_parameters={
                    'QUERY_TAG': 'BOTRUN',
                }
                )
        return con
    

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