
import sys
import os 


from snowchainexception import SnowchainException

class ObjectException(SnowchainException):
    """Base class for attribute validation exceptions"""
    def __init__(self, object_type, message):
        self.object_type = object_type
        self.message = message
        self.error_message = f"{self.object_type} object {self.message}."
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

class IntegrationDoesNotExist(ObjectException):
    def __init__(self, integration_name):
        super().__init__("INTEGRATION", f" named {integration_name} does not exist")

class MustBeAnAdmin(ObjectException):
    def __init__(self, object_type):
        message=f"can only be operated on using ACCOUNTADMIN role"
        super().__init__(object_type, message)

class InvalidAttributesToAlter(ObjectException):
    def __init__(self, object_type, attribute_list):
        message = f" does not have following properties to alter {attribute_list}"
        super().__init__(object_type, message)


class IncompatibleValueForChildAttr(ObjectException):
    def __init__(self, object_type, child_attr_name,parent_attr_name,compatible_value):
        message=f" can have {child_attr_name} only when {parent_attr_name} is one of the following {compatible_value}"
        super().__init__(object_type, message)

class OperationNotSupported(SnowchainException):
    def __init__(self, error_message):
        super().__init__(error_message)

