"""
Database Statement Builders
Builds MySQL CREATE, ALTER, and DROP DATABASE statements.
"""

from typing import Optional, Union
from .base import BaseMySql

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        instance._name=value

    def __delete__(self,instance):
        del instance._name


class CharacterSet:
    def __get__(self,instance,owner):
        return instance._character_set
    
    def __set__(self,instance,value):
        instance._character_set=value

    def __delete__(self,instance):
        del instance._character_set

class Collate:
    def __get__(self,instance,owner):
        return instance._collate
    
    def __set__(self,instance,value):
        instance._collate=value

    def __delete__(self,instance):
        del instance._collate

class Encryption:
    def __get__(self,instance,owner):
        return instance._encryption
    
    def __set__(self,instance,value):
        instance._encryption=value

    def __delete__(self,instance):
        del instance._encryption

class UseSchemaKeyword:
    def __get__(self,instance,owner):
        return instance._use_schema_keyword
    
    def __set__(self,instance,value):
        instance._use_schema_keyword=value

    def __delete__(self,instance):
        del instance._use_schema_keyword

class ReadOnly:
    def __get__(self,instance,owner):
        return instance._read_only
    
    def __set__(self,instance,value):
        #enforce this to be bool
        instance._read_only=value

    def __delete__(self,instance):
        del instance._read_only

class DatabaseAttrs:
    def __init__(self,parent):
        self.parent=parent

    name=Name()
    #if_not_exists=IfNotExists()
    character_set=CharacterSet()
    collate=Collate()
    encryption=Encryption()
    use_schema_keyword=UseSchemaKeyword()
    read_only=ReadOnly()

class Database(BaseMySql):
    def __init__(self,user_id,session,logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session=session,user_id=user_id,logger=logger)
        self.attr=DatabaseAttrs()

    def set_name(self,v): self.attr.name=v
    #def set_if_not_exists(self,v): self.attr.if_not_exists=v
    def set_character_set(self,v): self.attr.character_set=v
    def set_collate(self,v): self.attr.collate=v
    def set_encryption(self,v): self.attr.encryption=v
    def set_use_schema_keyword(self,v): self.attr.use_schema_keyword=v
    def set_read_only(self,v): self.attr.read_only=v

    def prepare_qry(self,operation_type):
        keyword = "SCHEMA" if self.attr.use_schema_keyword else "DATABASE"
        if operation_type=='CREATE':
            parts = [f"CREATE {keyword}"]
        
        #need to remove this as this will be a validation
        if self.if_not_exists:
            parts.append("IF NOT EXISTS")

        # Add database name (should be escaped in production)
        parts.append(self.__escape_identifier(self.attr.name))

        # Add options
        options = []

        if self.attr.character_set:
            escaped_charset = self.__escape_value(self.attr.character_set)
            options.append(f"CHARACTER SET = {escaped_charset}")

        if self.attr.collate:
            options.append(f"COLLATE = {self.__escape_value(self.attr.collate)}")

        if self.attr.encryption is not None:
            encryption_value = 'Y' if self.attr.encryption.upper() == 'Y' else 'N'
            options.append(f"ENCRYPTION = '{encryption_value}'")

        if operation_type=='ALTER':
            if self.attr.read_only is not None:
                # Handle different input types for read_only
                if isinstance(self.read_only, str):
                    if self.read_only.upper() == 'DEFAULT':
                        read_only_value = 'DEFAULT'
                    else:
                        read_only_value = '1' if self.read_only == '1' else '0'
                elif isinstance(self.read_only, bool):
                    read_only_value = '1' if self.read_only else '0'
                elif isinstance(self.read_only, int):
                    read_only_value = '1' if self.read_only == 1 else '0'
                else:
                    read_only_value = '0'

        # Build the final statement
        statement = " ".join(parts)

        if options:
            statement += "\n    " + "\n    ".join(options)
        
        self._qry=statement


    def __escape_identifier(self, identifier: str) -> str:
        """
        Escape database identifiers (backticks for MySQL).

        Args:
            identifier: The identifier to escape

        Returns:
            str: Escaped identifier
        """
        # For now, use backticks. In production, you might want more sophisticated escaping
        if '`' in identifier:
            identifier = identifier.replace('`', '``')
        return f"`{identifier}`"
    
    def __escape_value(self, value: str) -> str:
        """
        Escape string values for SQL.

        Args:
            value: The value to escape

        Returns:
            str: Escaped value
        """
        # For character sets and collations, they're typically unquoted in MySQL
        # But if they contain special characters, they might need quoting
        if not value:
            return "''"
        # Character set and collation names are usually identifiers, not strings
        return value


class CreateDatabase(SQLBuilder):
    """
    Builder for MySQL CREATE DATABASE statements.

    Based on MySQL 8.4 CREATE DATABASE syntax:
    CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name
        [create_option] ...

    create_option: [DEFAULT] {
        CHARACTER SET [=] charset_name
      | COLLATE [=] collation_name
      | ENCRYPTION [=] {'Y' | 'N'}
    }
    """

    def __init__(
        self,
        db_name: str,
        if_not_exists: bool = False,
        character_set: Optional[str] = None,
        collate: Optional[str] = None,
        encryption: Optional[str] = None,
        use_schema_keyword: bool = False
    ):
        """
        Initialize the CreateDatabase builder.

        Args:
            db_name (str): Name of the database (required)
            if_not_exists (bool): Add IF NOT EXISTS clause (default: False)
            character_set (str, optional): Character set for the database
            collate (str, optional): Collation for the database
            encryption (str, optional): Encryption setting ('Y' or 'N')
            use_schema_keyword (bool): Use SCHEMA instead of DATABASE (default: False)
        """
        super().__init__()
        self.db_name = db_name
        self.if_not_exists = if_not_exists
        self.character_set = character_set
        self.collate = collate
        self.encryption = encryption
        self.use_schema_keyword = use_schema_keyword

        # Store parameters for reference
        # Are all of these required
        self._parameters = {
            'db_name': db_name,
            'if_not_exists': if_not_exists,
            'character_set': character_set,
            'collate': collate,
            'encryption': encryption,
            'use_schema_keyword': use_schema_keyword,
        }

    def validate(self) -> bool:
        """
        Validate the database creation parameters.

        Returns:
            bool: True if valid

        Raises:
            ValueError: If validation fails
        """
        if not self.db_name or not isinstance(self.db_name, str):
            raise ValueError("db_name is required and must be a non-empty string")

        if self.encryption is not None and self.encryption.upper() not in ('Y', 'N'):
            raise ValueError("encryption must be 'Y' or 'N'")

        return True

    def build(self) -> str:
        """
        Build the CREATE DATABASE SQL statement.

        Returns:
            str: The generated SQL statement
        """
        # Validate before building
        self.validate()

        # Start building the statement
        keyword = "SCHEMA" if self.use_schema_keyword else "DATABASE"
        parts = [f"CREATE {keyword}"]

        # Add IF NOT EXISTS if specified
        if self.if_not_exists:
            parts.append("IF NOT EXISTS")

        # Add database name (should be escaped in production)
        parts.append(self._escape_identifier(self.db_name))

        # Add options
        options = []

        if self.character_set:
            escaped_charset = self._escape_value(self.character_set)
            options.append(f"CHARACTER SET = {escaped_charset}")

        if self.collate:
            options.append(f"COLLATE = {self._escape_value(self.collate)}")

        if self.encryption is not None:
            encryption_value = 'Y' if self.encryption.upper() == 'Y' else 'N'
            options.append(f"ENCRYPTION = '{encryption_value}'")

        # Build the final statement
        statement = " ".join(parts)

        if options:
            statement += "\n    " + "\n    ".join(options)

        return statement

    def _escape_identifier(self, identifier: str) -> str:
        """
        Escape database identifiers (backticks for MySQL).

        Args:
            identifier: The identifier to escape

        Returns:
            str: Escaped identifier
        """
        # For now, use backticks. In production, you might want more sophisticated escaping
        if '`' in identifier:
            identifier = identifier.replace('`', '``')
        return f"`{identifier}`"

    def _escape_value(self, value: str) -> str:
        """
        Escape string values for SQL.

        Args:
            value: The value to escape

        Returns:
            str: Escaped value
        """
        # For character sets and collations, they're typically unquoted in MySQL
        # But if they contain special characters, they might need quoting
        if not value:
            return "''"
        # Character set and collation names are usually identifiers, not strings
        return value

    def set_db_name(self, db_name: str) -> 'CreateDatabase':
        """Set the database name."""
        self.db_name = db_name
        self._parameters['db_name'] = db_name
        self._statement = None  # Reset cached statement
        return self

    def set_if_not_exists(self, if_not_exists: bool = True) -> 'CreateDatabase':
        """Set the IF NOT EXISTS flag."""
        self.if_not_exists = if_not_exists
        self._parameters['if_not_exists'] = if_not_exists
        self._statement = None
        return self

    def set_character_set(self, character_set: str) -> 'CreateDatabase':
        """Set the character set."""
        self.character_set = character_set
        self._parameters['character_set'] = character_set
        self._statement = None
        return self

    def set_collate(self, collate: str) -> 'CreateDatabase':
        """Set the collation."""
        self.collate = collate
        self._parameters['collate'] = collate
        self._statement = None
        return self

    def set_encryption(self, encryption: str) -> 'CreateDatabase':
        """Set the encryption setting ('Y' or 'N')."""
        if encryption.upper() not in ('Y', 'N'):
            raise ValueError("encryption must be 'Y' or 'N'")
        self.encryption = encryption.upper()
        self._parameters['encryption'] = self.encryption
        self._statement = None
        return self


class AlterDatabase(SQLBuilder):
    """
    Builder for MySQL ALTER DATABASE statements.

    Based on MySQL 8.4 ALTER DATABASE syntax:
    ALTER {DATABASE | SCHEMA} [db_name]
        alter_option ...

    alter_option: {
        [DEFAULT] CHARACTER SET [=] charset_name
      | [DEFAULT] COLLATE [=] collation_name
      | [DEFAULT] ENCRYPTION [=] {'Y' | 'N'}
      | READ ONLY [=] {DEFAULT | 0 | 1}
    }
    """

    def __init__(
        self,
        db_name: Optional[str] = None,
        character_set: Optional[str] = None,
        collate: Optional[str] = None,
        encryption: Optional[str] = None,
        read_only: Optional[Union[bool, int, str]] = None,
        use_schema_keyword: bool = False
    ):
        """
        Initialize the AlterDatabase builder.

        Args:
            db_name (str, optional): Name of the database (optional, uses current if None)
            character_set (str, optional): Character set for the database
            collate (str, optional): Collation for the database
            encryption (str, optional): Encryption setting ('Y' or 'N')
            read_only (bool/int/str, optional): Read-only setting (True/1/'1' or False/0/'0')
            use_schema_keyword (bool): Use SCHEMA instead of DATABASE (default: False)
        """
        super().__init__()
        self.db_name = db_name
        self.character_set = character_set
        self.collate = collate
        self.encryption = encryption
        self.read_only = read_only
        self.use_schema_keyword = use_schema_keyword

        # Store parameters for reference
        self._parameters = {
            'db_name': db_name,
            'character_set': character_set,
            'collate': collate,
            'encryption': encryption,
            'read_only': read_only,
            'use_schema_keyword': use_schema_keyword,
        }

    def validate(self) -> bool:
        """
        Validate the database alteration parameters.

        Returns:
            bool: True if valid

        Raises:
            ValueError: If validation fails
        """
        # Check if at least one option is provided
        has_option = any([
            self.character_set,
            self.collate,
            self.encryption is not None,
            self.read_only is not None
        ])

        if not has_option:
            raise ValueError(
                "At least one alter option must be provided "
                "(character_set, collate, encryption, or read_only)"
            )

        if self.encryption is not None and self.encryption.upper() not in ('Y', 'N'):
            raise ValueError("encryption must be 'Y' or 'N'")

        # Validate read_only
        if self.read_only is not None:
            if isinstance(self.read_only, str):
                if self.read_only.upper() not in ('0', '1', 'DEFAULT'):
                    raise ValueError(
                        "read_only must be True/False, 0/1, or '0'/'1'/'DEFAULT'"
                    )
            elif not isinstance(self.read_only, (bool, int)):
                raise ValueError(
                    "read_only must be True/False, 0/1, or '0'/'1'/'DEFAULT'"
                )

        return True

    def build(self) -> str:
        """
        Build the ALTER DATABASE SQL statement.

        Returns:
            str: The generated SQL statement
        """
        # Validate before building
        self.validate()

        # Start building the statement
        keyword = "SCHEMA" if self.use_schema_keyword else "DATABASE"
        parts = [f"ALTER {keyword}"]

        # Add database name if provided (optional in ALTER DATABASE)
        if self.db_name:
            parts.append(self._escape_identifier(self.db_name))

        # Add options
        options = []

        if self.character_set:
            escaped_charset = self._escape_value(self.character_set)
            options.append(f"CHARACTER SET = {escaped_charset}")

        if self.collate:
            escaped_collate = self._escape_value(self.collate)
            options.append(f"COLLATE = {escaped_collate}")

        if self.encryption is not None:
            encryption_value = 'Y' if self.encryption.upper() == 'Y' else 'N'
            options.append(f"ENCRYPTION = '{encryption_value}'")

        if self.read_only is not None:
            # Handle different input types for read_only
            if isinstance(self.read_only, str):
                if self.read_only.upper() == 'DEFAULT':
                    read_only_value = 'DEFAULT'
                else:
                    read_only_value = '1' if self.read_only == '1' else '0'
            elif isinstance(self.read_only, bool):
                read_only_value = '1' if self.read_only else '0'
            elif isinstance(self.read_only, int):
                read_only_value = '1' if self.read_only == 1 else '0'
            else:
                read_only_value = '0'

            options.append(f"READ ONLY = {read_only_value}")

        # Build the final statement
        statement = " ".join(parts)

        if options:
            statement += "\n    " + "\n    ".join(options)

        return statement

    def _escape_identifier(self, identifier: str) -> str:
        """Escape database identifiers (backticks for MySQL)."""
        if '`' in identifier:
            identifier = identifier.replace('`', '``')
        return f"`{identifier}`"

    def _escape_value(self, value: str) -> str:
        """Escape string values for SQL."""
        if not value:
            return "''"
        return value

    def set_db_name(self, db_name: str) -> 'AlterDatabase':
        """Set the database name."""
        self.db_name = db_name
        self._parameters['db_name'] = db_name
        self._statement = None
        return self

    def set_character_set(self, character_set: str) -> 'AlterDatabase':
        """Set the character set."""
        self.character_set = character_set
        self._parameters['character_set'] = character_set
        self._statement = None
        return self

    def set_collate(self, collate: str) -> 'AlterDatabase':
        """Set the collation."""
        self.collate = collate
        self._parameters['collate'] = collate
        self._statement = None
        return self

    def set_encryption(self, encryption: str) -> 'AlterDatabase':
        """Set the encryption setting ('Y' or 'N')."""
        if encryption.upper() not in ('Y', 'N'):
            raise ValueError("encryption must be 'Y' or 'N'")
        self.encryption = encryption.upper()
        self._parameters['encryption'] = self.encryption
        self._statement = None
        return self

    def set_read_only(self, read_only: Union[bool, int, str]) -> 'AlterDatabase':
        """
        Set the read-only setting.

        Args:
            read_only: True/1/'1' for read-only, False/0/'0' for writable, 'DEFAULT' for default
        """
        self.read_only = read_only
        self._parameters['read_only'] = read_only
        self._statement = None
        return self


class DropDatabase(SQLBuilder):
    """
    Builder for MySQL DROP DATABASE statements.

    Based on MySQL 8.4 DROP DATABASE syntax:
    DROP {DATABASE | SCHEMA} [IF EXISTS] db_name
    """

    def __init__(
        self,
        db_name: str,
        if_exists: bool = False,
        use_schema_keyword: bool = False
    ):
        """
        Initialize the DropDatabase builder.

        Args:
            db_name (str): Name of the database (required)
            if_exists (bool): Add IF EXISTS clause (default: False)
            use_schema_keyword (bool): Use SCHEMA instead of DATABASE (default: False)
        """
        super().__init__()
        self.db_name = db_name
        self.if_exists = if_exists
        self.use_schema_keyword = use_schema_keyword

        # Store parameters for reference
        self._parameters = {
            'db_name': db_name,
            'if_exists': if_exists,
            'use_schema_keyword': use_schema_keyword,
        }

    def validate(self) -> bool:
        """
        Validate the database drop parameters.

        Returns:
            bool: True if valid

        Raises:
            ValueError: If validation fails
        """
        if not self.db_name or not isinstance(self.db_name, str):
            raise ValueError("db_name is required and must be a non-empty string")

        return True

    def build(self) -> str:
        """
        Build the DROP DATABASE SQL statement.

        Returns:
            str: The generated SQL statement
        """
        # Validate before building
        self.validate()

        # Start building the statement
        keyword = "SCHEMA" if self.use_schema_keyword else "DATABASE"
        parts = [f"DROP {keyword}"]

        # Add IF EXISTS if specified
        if self.if_exists:
            parts.append("IF EXISTS")

        # Add database name
        parts.append(self._escape_identifier(self.db_name))

        return " ".join(parts)

    def _escape_identifier(self, identifier: str) -> str:
        """Escape database identifiers (backticks for MySQL)."""
        if '`' in identifier:
            identifier = identifier.replace('`', '``')
        return f"`{identifier}`"

    def set_db_name(self, db_name: str) -> 'DropDatabase':
        """Set the database name."""
        self.db_name = db_name
        self._parameters['db_name'] = db_name
        self._statement = None
        return self

    def set_if_exists(self, if_exists: bool = True) -> 'DropDatabase':
        """Set the IF EXISTS flag."""
        self.if_exists = if_exists
        self._parameters['if_exists'] = if_exists
        self._statement = None
        return self