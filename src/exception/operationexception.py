import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))


from snowchainexception import SnowchainException

class OperationException(SnowchainException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class PropertyNotSupported(OperationException):
    def __init__(self, object_type,property_name):
        message=f"Alter operation on {property_name} not allowed for {object_type}"
        super().__init__(message)