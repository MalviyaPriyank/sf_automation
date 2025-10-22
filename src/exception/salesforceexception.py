import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))


from snowchainexception import SnowchainException


class SalesforceException(SnowchainException):
    def __init__(self, error_message):
        super().__init__(error_message)



class InvalidColumnToPull(SalesforceException):
    def __init__(self, object_type,invalid_columns_list):
        columns_str=""
        for i in invalid_columns_list:
            columns_str=columns_str+i+" "
        error_message=f"For {object_type} object type following columns {columns_str} are invalid. Ask user to provide columns from available list of columns."
        super().__init__(error_message=error_message)