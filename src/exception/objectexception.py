class ObjectException(Exception):
    """Base class for attribute validation exceptions"""
    def __init__(self, object_type, message):
        self.object_type = object_type
        self.message = message
    
    def __str__(self):
        return f"ERROR : {self.object_type} object {self.message}"
    
class ObjectDoesNotExist(ObjectException):
     def __init__(self, object_type,object_name):
        super().__init__(object_type,f"with name {object_name} does not exist")

class DuplicateObject(ObjectException):
    def __init__(self, object_type, object_name):
        super().__init__(object_type, f"with name {object_name} already exist")