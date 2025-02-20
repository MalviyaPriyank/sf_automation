class AccountUsageViews:
    _copy_history_view="COPY_HISTORY"


class CopyHistoryColumnList:
    _view=AccountUsageViews._copy_history_view
    _file_name="FILE_NAME"
    _stage_location="STAGE_LOCATION"
    _last_load_time="LAST_LOAD_TIME"
    _row_count="ROW_COUNT"
    _row_parsed="ROW_PARSED"
    _file_size="FILE_SIZE"
    _first_error_message="FIRST_ERROR_MESSAGE"
    _first_error_line_number="FIRST_ERROR_LINE_NUMBER"
    _first_error_character_pos="FIRST_ERROR_CHARACTER_POS"
    _first_error_column_name="FIRST_ERROR_COLUMN_NAME"
    _error_count="ERROR_COUNT"
    _error_limit="ERROR_LIMIT"
    _status="STATUS"
    _table_id="TABLE_ID"
    _table_name="TABLE_NAME"
    _table_schema_id="TABLE_SCHEMA_ID"
    _table_schema_name="TABLE_SCHEMA_NAME"
    _table_catalog_id="TABLE_CATALOG_ID"
    _table_catalog_name="TABLE_CATALOG_NAME"
    _pipe_catalog_name="PIPE_CATALOG_NAME"
    _pipe_schema_name="PIPE_SCHEMA_NAME"
    _pipe_name="PIPE_NAME"
    _pipe_received_time="PIPE_RECEIVED_TIME"
    _first_commit_time="FIRST_COMMIT_TIME"

class CopyHistoryView:
    def __init__(self):
        self.attr=CopyHistoryColumnList()