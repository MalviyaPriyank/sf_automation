from enum import Enum
from abc import ABC,abstractmethod

class BaseTag(Enum):
    DATABASE="DATABASE"
    SCHEMA="SCHEMA"
    NAME="NAME"
    COMMENT="COMMENT"

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