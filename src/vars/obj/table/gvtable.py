class Table:
    _database="DATABASE"
    _schema="SCHEMA"
    _name="NAME"

class TempTable(Table):
    _scope="SCOPE"
    _allowed_values_scope=["LOCAL","GLOBAL"]