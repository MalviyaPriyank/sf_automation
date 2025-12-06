from typing import Optional

from pydantic import BaseModel, Field

class DatabaseAttributes(BaseModel):
    """
    Attributes to pass for creating database
    """
    NAME: str = Field(description="Name of the database")
    DATA_RETENTION_TIME_IN_DAYS: Optional[int] = Field(default= 1,description="Specifies the number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the database, as well as specifying the default Time Travel retention time for all schemas created in the database. ")
    MAX_DATA_EXTENSION_TIME_IN_DAYS: Optional[int] = Field(default="NONE",description="Object parameter that specifies the maximum number of days for which Snowflake can extend the data retention period for tables in the database to prevent streams on the tables from becoming stale.")
    EXTERNAL_VOLUME: Optional[str] = Field(default="NONE",description="Object parameter that specifies the default external volume to use for Apache Iceberg™ tables")
    CATALOG: Optional[str] = Field(default="NONE",description="Object parameter that specifies the default catalog integration to use for Apache Iceberg™ tables")
    REPLACE_INVALID_CHARACTERS: Optional[bool] = Field(default=False,description="Specifies whether to replace invalid UTF-8 characters with the Unicode replacement character,you can only set this parameter for tables that use an external Iceberg catalog.")
    DEFAULT_DDL_COLLATION: Optional[str] = Field(default="NONE",description="Specifies a default collation specification for all schemas and tables added to the database. The default can be overridden at the schema and individual table level.")
    LOG_LEVEL: Optional[str] = Field(default="NONE",description="Specifies the severity level of messages that should be ingested and made available in the active event table. Messages at the specified level (and at more severe levels) are ingested.")
    TRACE_LEVEL: Optional[str] = Field(default="NONE",description="Controls how trace events are ingested into the event table.")
    STORAGE_SERIALIZATION_POLICY: Optional[str] = Field(default="Optimized",description="Specifies the storage serialization policy for Apache Iceberg™ tables that use Snowflake as the catalog")
    COMMENT: Optional[str] = Field(default="NONE",description="Specifies a comment for the database.")

class SchemaAttributes(BaseModel):
    """
    Attributes to pass for creating schema
    """
    DATABASE: str = Field(description="Name of the database where schema will be created.")
    NAME : str = Field(description="""
                       Specifies the identifier for the schema; must be unique for the database in which the schema is created.
                       In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters 
                       unless the entire identifier string is enclosed in double quotes (e.g. "My object"). 
                       Identifiers enclosed in double quotes are also case-sensitive.""")
    WITH_MANAGED_ACCESS: Optional[str] = Field(description="Specifies a managed schema. Managed access schemas centralize privilege management with the schema owner.")
    DATA_RETENTION_TIME_IN_DAYS : Optional[int] = Field(default= 1,description="""
                                              Specifies the number of days for which Time Travel actions (CLONE and UNDROP) can be performed on the schema, 
                                              as well as specifying the default Time Travel retention time for all tables created in the schema.""")
    MAX_DATA_EXTENSION_TIME_IN_DAYS : Optional[int] = Field(default=1, description="""
                                                  Object parameter that specifies the maximum number of days for which Snowflake can extend the data 
                                                  retention period for tables in the schema to prevent streams on the tables from becoming stale.""")
    EXTERNAL_VOLUME : Optional[str] = Field(description="Object parameter that specifies the default external volume to use for Apache Iceberg™ tables.")
    CATALOG : Optional[str] = Field(description="Object parameter that specifies the default catalog integration to use for Apache Iceberg™ tables.")
    DEFAULT_DDL_COLLATION : Optional[str] = Field(description="Specifies a default collation specification for all tables added to the schema. The default can be overridden at the individual table level.")
    REPLACE_INVALID_CHARACTERS : Optional[bool] = Field(default="False", description="""
                                                        Specifies whether to replace invalid UTF-8 characters with the Unicode replacement character 
                                                        in query results for an Iceberg table. You can only set this parameter for tables that use an 
                                                        external Iceberg catalog.""")
    LOG_LEVEL : Optional[str] = Field(default="NONE", description="""
                                      Specifies the severity level of messages that should be ingested and made available in the active event table. 
                                      Messages at the specified level (and at more severe levels) are ingested.""")
    TRACE_LEVEL : Optional[str] = Field(default="NONE",description="Controls how trace events are ingested into the event table.")
    STORAGE_SERIALIZATION_POLICY : Optional[str] = Field(default="Optimized", description="Specifies the storage serialization policy for Apache Iceberg™ tables that use Snowflake as the catalog")
    CLASSIFICATION_PROFILE : Optional[str] = Field(default="NONE",description="Associates the schema with a classification profile so that sensitive data in the schema is automatically classified.")
    COMMENT: Optional[str] = Field(default="NONE",description="Specifies a comment for the schema.")
