from dataclasses import dataclass
from abc import ABC,abstractmethod

@dataclass(frozen=True)
class BaseTag:
    DATABASE="DATABASE"
    SCHEMA="SCHEMA"
    NAME="NAME"
    COMMENT="COMMENT"
    IS_CREATE="IS_CREATE"

    @classmethod
    def get_attributes_with_description(cls):
        return {
            "DATABASE":"User provide value for name of the Database where object must be created. If the object is DATABASE itself then this will be NONE .",
            "SCHEMA":"User provide value for name of the Schema where object must be created. If the object is SCHEMA itself then this will be NONE .",
            "NAME":"this is a dictionary data type with keys {'NAME', 'RENAME_TO'} - pass value as a dictionary object. This is to be taken as input from user. DO NOT ASSUME values for NAME and RENAME_TO, these are to be taken from user. the format is a dictionary with key 'NAME' for the name, and 'RENAME_TO' key when the ask is to alter (IS_CREATE=TRUE).",
            "COMMENT":"This will be user defined comment for the object. If user does not define one add a proper comment as per your understanding and inform the user.",
            "IS_CREATE":"Set this to 'TRUE' if create object. set to 'FALSE' if alter object."
        }

@dataclass(frozen=True)
class BaseMethod(ABC):
    @classmethod
    @abstractmethod
    def allowed_value_list(cls):
        "Should return a dictionary of allowed values for specific tags"
        return {}

    @classmethod
    @abstractmethod
    def min_allowed_value(cls):
        "Should return a ditionary of min allowed value for specific tags"
        return {}

    @classmethod
    @abstractmethod
    def max_allowed_value(cls):
        "Should return a dictionary of max allowed value for specific tags"
        return {}