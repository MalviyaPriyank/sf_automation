class GvBase:
    def __init__(self):
        self._name_tag="NAME"

class GvDatabase(GvBase):
    def __init__(self):
        super().__init__()
        self._replace_invalid_characters_tag = "REPLACE_INVALID_CHARACTERS"
        self._data_retention_time_in_days_tag = "DATA_RETENTION_TIME_IN_DAYS"
        self._max_data_extension_time_in_days_tag = "MAX_DATA_EXTENSION_TIME_IN_DAYS"
        self._external_volume_tag = "EXTERNAL_VOLUME"
        self._catalog_tag = "CATALOG"
        self._default_ddl_collation_tag = "DEFAULT_DDL_COLLATION"
        self._log_level_tag="LOG_LEVEL"
        self._trace_level_tag="TRACE_LEVEL"
        self._storage_serialization_policy_tag = "STORAGE_SERIALIZATION_POLICY"
        self._comment_tag = "COMMENT"
        self._allowed_values_storage_serialization_policy = ["COMPATIBLE","OPTIMIZED"]
        self._max_allowed_value_data_retention_time_in_days=1
        self._min_allowed_value_data_retention_time_in_days=0
        self._max_allowed_value_max_data_extension_time_in_days=1
        self._min_allowed_value_max_data_extension_time_in_days=0
        self._allowed_values_log_level=['TRACE','DEBUG','INFO','WARN','ERROR','FATAL','OFF']
        self._allowed_values_trace_level=['ALWAYS','ON_EVENT','OFF']
        self._allowed_collation_specifiers=['de','ci','pi','en','en_US','fr','fr_CA','cs','ci','as','ai','ps','pi','fl','fu','upper','lower','trim','ltrim','rtrim']
    
