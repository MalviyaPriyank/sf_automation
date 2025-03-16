from abc import ABC,abstractmethod
from enum import Enum

class BaseTag(Enum,ABC):
    DATABASE="DATABASE"
    SCHEMA="SCHEMA"
    NAME="NAME"
    COMMENT="COMMENT"

    @classmethod
    @abstractmethod
    def allowed_value_list(cls):
        "Should return a dictionary of allowed values for specific tags"
        pass

    @classmethod
    @abstractmethod
    def min_allowed_value(cls):
        "Should return a ditionary of min allowed value for specific tags"
        pass

    @classmethod
    @abstractmethod
    def max_allowed_value(cls):
        "Should return a dictionary of max allowed value for specific tags"
        pass