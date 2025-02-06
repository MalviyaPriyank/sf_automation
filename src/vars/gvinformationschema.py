class InformationSchema:        
    def __init__(self):
        pass
    _information_schema = "INFORMATION_SCHEMA"
    _database_view = f"{_information_schema}.DATABASES"
    _schema_view = f"{_information_schema}.SCHEMATA"
    _table_view = f"{_information_schema}.TABLE"


class DatabaseColumnList:
    database_name = "DATABASE_NAME"
    database_owner = "DATABASE_OWNER"
    is_transient = "IS_TRANSIENT"
    comment = "COMMENT"
    created = "CREATED"
    last_altered = "LAST_ALTERED"
    retention_time = "RETENTION_TIME"
    type = "TYPE"
    owner_role_type = "OWNER_ROLE_TYPE"


class Database:
    def __init__(self):
        self.columns = DatabaseColumnList()


class SchemaColumnList:
    catalog_name = "CATALOG_NAME"
    schema_name = "SCHEMA_NAME"
    schema_owner = "SCHEMA_OWNER"
    is_transient = "IS_TRANSIENT"
    is_managed_access = "IS_MANAGED_ACCESS"
    retention_time = "RETENTION_TIME"
    default_character_set_catalog = "DEFAULT_CHARACTER_SET_CATALOG"
    default_character_set_schema = "DEFAULT_CHARACTER_SET_SCHEMA"
    default_character_set_name = "DEFAULT_CHARACTER_SET_NAME"
    sql_path = "SQL_PATH"
    created = "CREATED"
    last_altered = "LAST_ALTERED"
    comment = "COMMENT"



class Schema:
    def __init__(self):
        self.columns = SchemaColumnList()
