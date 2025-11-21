
class CdcMSSqlServer:
    def __init__(self):
        self.attr=CdcMSSqlServerColumnList()
    _database="DB_CONFIG"
    _schema="SCH_CONFIG"
    _table=f"{_database}.{_schema}.CDC_MS_SQL_SERVER"


class CdcMSSqlServerColumnList:
    _object_name="TABLE_NAME"
    _database_name="DATABASE_NAME"
    _lsn="LOG_SEQUENCE_NUMBER"
    _load_timestamp="LOAD_TIMESTAMP"

