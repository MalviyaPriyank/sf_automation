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

class NoCDCRecordsFound(OperationException):
    def __init__(self, server,object_name,**kwargs):
        message=f"No incremental records found for {object_name}"
        super().__init__(message)