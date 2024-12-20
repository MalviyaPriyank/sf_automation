import os 
import snowflake.connector
from snowflake.core import Root

class Account:
    def __get__(self,instance,owner):
        return instance._account
    
    def __set__(self,instance,value):
        instance._account = value
    
    def __delete__(self,instance):
        del instance._account

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

class Role:
    def __get__(self,instance,owner):
        return instance._role
    
    def __set__(self,instance,value):
        instance._role = value
    
    def __delete__(self,instance):
        del instance._role

class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        instance._database = value
    
    def __delete__(self,instance):
        del instance._database

class Warehouse:
    def __get__(self,instance,owner):
        return instance._warehouse
    
    def __set__(self,instance,value):
        instance._warehouse = value
    
    def __delete__(self,instance):
        del instance._warehouse


class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        instance._schema = value
    
    def __delete__(self,instance):
        del instance._schema


class ConnectionAttrs:
    account = Account()
    user = User()
    password = Password()
    role = Role()
    database = Database()
    warehouse = Warehouse()
    schema = Schema()

class Connection:
    def __init__(self,session):
        self.session = session
        self.attr = ConnectionAttrs()

    def set_account(self,account):
        self.attr.account = account

    def set_user(self,user):
        self.attr.user = user
    
    def set_password(self,password):
        self.attr.password = password

    def set_role(self,role):
        self.attr.role = role
    
    def set_database(self,database):
        self.attr.database = database

    def set_warehouse(self,warehouse):
        self.attr.warehouse = warehouse

    def set_schema(self,schema):
        self.attr.schema = schema

    def get_connection(self):
        con = snowflake.connector.connect(
            user = self.attr.user,
            password = self.attr.password,
            account = self.attr.account,
            warehouse = self.attr.warehouse,
            database = self.attr.database,
            schema = self.attr.schema
        )
        return con

    def get_root(self,connection):
        return Root(connection)


