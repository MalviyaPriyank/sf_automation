
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))


from typing import Type,Optional
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from obj.database import Database

class CreateDatabaseInput(BaseModel):
    NAME : str = Field(description="""
                       Specifies the identifier for the database; must be unique for your account.In addition, the identifier must start with an 
                       alphabetic character and cannot contain spaces or special characters unless the entire identifier string is enclosed in double quotes 
                       (e.g. "My object"). Identifiers enclosed in double quotes are also case-sensitive.""")
    CATALOG: Optional[str] = Field(description="""Object parameter that specifies the default catalog integration to use for Apache Iceberg tables""")
    COMMENT: Optional[str] = Field(description="""Specifies a comment for the database.""")  
    EXTERNAL_VOLUME: Optional[str] = Field(description="""Object parameter that specifies the default external volume to use for Apache Iceberg tables.""") 
    DEFAULT_DDL_COLLATION: Optional[str] = Field(description="""Specifies a default collation specification for all schemas 
                                       and tables added to the database. The default can be overridden at the schema and individual table level.""") 
    LOG_LEVEL: Optional[str] = Field(description="Specifies the severity level of messages that should be ingested and made available in the active event table. Messages at the specified level (and at more severe levels) are ingested.")
    TRACE_LEVEL: Optional[str] = Field(description=""" Controls how trace events are ingested into the event table. """)
    REPLACE_INVALID_CHARACTERS: Optional[str] = Field(description=""" Specifies whether to replace invalid UTF-8 characters with the Unicode replacement character in query results for an Iceberg table. 
                                            You can only set this parameter for tables that use an external Iceberg catalog.TRUE replaces invalid UTF-8 characters with the Unicode replacement character.
                                            FALSE leaves invalid UTF-8 characters unchanged. Snowflake returns a user error message when it encounters invalid UTF-8 characters in a Parquet data file. """)
    DATA_RETENTION_TIME_IN_DAYS: Optional[str] = Field(description=""" Specifies the number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the database, 
                                             as well as specifying the default Time Travel retention time for all schemas created in the database.  """)
    STORAGE_SERIALIZATION_POLICY: Optional[str] = Field(description=""" 
    Specifies the storage serialization policy for Apache Iceberg tables that use Snowflake as the catalog.
    COMPATIBLE: Snowflake performs encoding and compression of data files that ensures interoperability with third-party compute engines.
    OPTIMIZED: Snowflake performs encoding and compression of data files that ensures the best table performance within Snowflake.
    """)
    MAX_DATA_EXTENSION_TIME_IN_DAYS: Optional[str] = Field(description=""" 
    Object parameter that specifies the maximum number of days for which Snowflake can extend the data retention period 
    for tables in the database to prevent streams on the tables from becoming stale.                                                 
    """)

class CreateDatabase(BaseTool):
    name: str = "CreateDatabase"
    description: str = "Creates database object"
    #args_schema: Type[BaseModel] = CreateDatabaseInput

    def _run(self, arguments:CreateDatabaseInput) -> str:
        print(f"Inside run args passed {arguments}" )
        #Database().create_database(arguments.dict())
        return "Tool's result"