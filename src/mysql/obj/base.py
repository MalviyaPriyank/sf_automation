"""
Base SQL Builder Class
Provides common functionality for all SQL statement builders.
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any


class AbsMySql(ABC):
    """Base class for all SQL statement builders."""

    def __init__(self,session,user_id,logger):
        self.session=session
        self.user_id=user_id
        self.logger=logger
        self._qry=""

    @abstractmethod
    def execute_final_query(self) -> str:
        """
        Build the SQL statement from the provided parameters.

        Returns:
            str: The generated SQL statement
        """
        pass


    def __str__(self) -> str:
        """String representation returns the SQL statement."""
        return self.get_statement()

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"{self.__class__.__name__}(statement={self.get_statement()})"
    

class BaseMySql(AbsMySql):
    def __init__(self, session, user_id, logger):
        super().__init__(session, user_id, logger)

    def execute_final_query(self):
        # Add execute statement here
        return True #placeholder for now 