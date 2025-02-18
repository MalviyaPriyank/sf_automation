
import sys
import os 


from snowchainexception import SnowchainException

class ObjectException(SnowchainException):
    """Base class for attribute validation exceptions"""
    def __init__(self, object_type, message):
        self.object_type = object_type
        self.message = message
        self.error_message = f"{self.object_type} object {self.message}. Please retry."
        super().__init__(self.error_message)
    
class ObjectDoesNotExist(ObjectException):
     def __init__(self, object_type,object_name):
        super().__init__(object_type,f"with name {object_name} does not exist")

class DuplicateObject(ObjectException):
    def __init__(self, object_type, object_name):
        super().__init__(object_type, f"with name {object_name} already exist")

class ColumnDoesNotExist(ObjectException):
    def __init__(self, object_type, table_name, column_name):
        super().__init__(object_type, f" {table_name} does not have column named {column_name}")

class UserEmailDoesNotExist(ObjectException):
    def __init__(self, object_type, user_email):
        super().__init__(object_type, f" with email {user_email} does not exist")