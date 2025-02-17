class InformationSchema:        
    def __init__(self):
        pass
    _information_schema="INFORMATION_SCHEMA"
    _database_view=f"{_information_schema}.DATABASES"
    _schema_view=f"{_information_schema}.SCHEMATA"
    _table_view=f"{_information_schema}.TABLES"
    _stage_view=f"{_information_schema}.STAGES"
    _file_format_view=f"{_information_schema}.FILE_FORMATS"
    _column_view=f"{_information_schema}.COLUMNS"


class DatabaseColumnList:
    _view = InformationSchema._database_view
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
    _view = InformationSchema._schema_view
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



class TableColumnList:
    _view = InformationSchema._table_view
    _table_catalog = "TABLE_CATALOG"
    _table_schema = "TABLE_SCHEMA"
    _table_name = "TABLE_NAME"
    _table_owner = "TABLE_OWNER"
    _table_type = "TABLE_TYPE"
    _is_transient = "IS_TRANSIENT"
    _clustering_key = "CLUSTERING_KEY"
    _row_count = "ROW_COUNT"
    _bytes = "BYTES"
    _retention_time = "RETENTION_TIME"
    _created = "CREATED"
    _last_altered = "LAST_ALTERED"
    _last_ddl = "LAST_DDL"
    _last_ddl_by = "LAST_DDL_BY"
    _auto_clustering_on = "AUTO_CLUSTERING_ON"
    _comment = "COMMENT"
    _is_temporary = "IS_TEMPORARY"
    _is_iceberg = "IS_ICEBERG"
    _is_dynamic="IS_DYNAMIC"
    _is_mutable="IS_IMMUTABLE"

class Table:
    def __init__(self):
        self.columns=TableColumnList()

class StageColumnList:
    _view = InformationSchema._stage_view
    _stage_catalog="STAGE_CATALOG"
    _stage_schema="STAGE_SCHEMA"
    _stage_name="STAGE_NAME"
    _stage_url="STAGE_URL"
    _stage_region="STAGE_REGION"
    _stage_type="STAGE_TYPE"
    _stage_owner="STAGE_OWNER"
    _comment="COMMENT"
    _created="CREATED"
    _last_altered="LAST_ALTERED"

class Stage:
    def __init__(self):
        self.columns=StageColumnList()

class FileFormatColumnList:
    _view = InformationSchema._file_format_view
    _file_format_catalog="FILE_FORMAT_CATALOG"
    _file_format_schema="FILE_FORMAT_SCHEMA"
    _file_format_name="FILE_FORMAT_NAME"
    _file_format_owner="FILE_FORMAT_OWNER"
    _file_format_type="FILE_FORMAT_TYPE"
    _record_delimiter="RECORD_DELIMITER"
    _field_delimiter="FIELD_DELIMITER"
    _skip_header="SKIP_HEADER"
    _date_format="DATE_FORMAT"
    _time_format="TIME_FORMAT"
    _timestamp_format="TIMESTAMP_FORMAT"
    _binary_format="BINARY_FORMAT"
    _escape="ESCAPE"
    _escape_unenclosed_field="ESCAPE_UNENCLOSED_FIELD"
    _trim_space="TRIM_SPACE"
    _field_optionally_enclosed_by="FIELD_OPTIONALLY_ENCLOSED_BY"
    _null_if="NULL_IF"
    _compression="COMPRESSION"
    _error_on_column_count_mismatch="ERROR_ON_COLUMN_COUNT_MISMATCH"
    _created="CREATED"
    _last_altered="LAST_ALTERED"
    _comment="COMMENT"

class FileFormat:
    def __init__(self):
        self.columns=FileFormatColumnList()

    _view = InformationSchema._file_format_view
    _file_format_catalog="FILE_FORMAT_CATALOG"
    _file_format_schema="FILE_FORMAT_SCHEMA"
    _file_format_name="FILE_FORMAT_NAME"
    _file_format_owner="FILE_FORMAT_OWNER"
    _file_format_type="FILE_FORMAT_TYPE"
    _record_delimiter="RECORD_DELIMITER"
    _field_delimiter="FIELD_DELIMITER"
    _skip_header="SKIP_HEADER"
    _date_format="DATE_FORMAT"
    _time_format="TIME_FORMAT"
    _timestamp_format="TIMESTAMP_FORMAT"
    _binary_format="BINARY_FORMAT"
    _escape="ESCAPE"
    _escape_unenclosed_field="ESCAPE_UNENCLOSED_FIELD"
    _trim_space="TRIM_SPACE"
    _field_optionally_enclosed_by="FIELD_OPTIONALLY_ENCLOSED_BY"
    _null_if="NULL_IF"
    _compression="COMPRESSION"
    _error_on_column_count_mismatch="ERROR_ON_COLUMN_COUNT_MISMATCH"
    _created="CREATED"
    _last_altered="LAST_ALTERED"
    _comment="COMMENT"

class ColumnColumnList:
    _view=InformationSchema._column_view
    _table_catalog="TABLE_CATALOG"
    _table_schema="TABLE_SCHEMA"
    _table_name="TABLE_NAME"
    _column_name="COLUMN_NAME"

class Column:
    def __init__(self):
        self.columns=ColumnColumnList()
