class Table:
    _database="DATABASE"
    _schema="SCHEMA"
    _name="NAME"

    @classmethod
    def allowed_data_types(cls):
        allowed_types_dict= {
            "NUMBERIC":["NUMBER","DECIMAL","NUMERIC","INT","INTEGER","BIGINT","SMALLINT","TINYINT","BYTEINT","FLOAT","FLOAT4","FLOAT8","DOUBLE","DOUBLE PRECISION","REAL"],
            "STRING and BINARY":["VARCHAR","CHAR","CHARACTER","STRING","TEXT","BINARY","VARBINARY"],
            "LOGICAL":["BOOLEAN"],
            "DATE":["DATE","DATETIME","TIME","TIMESTAMP","TIMESTAMP_LTZ","TIMESTAMP_NTZ","TIMESTAMP_TZ"],
            "SEMI STRUCTURED":["ARRAY","OBJECT","MAP"],
            "UNSTRUCTURED":["FILE"],
            "GEOSPATIAL":["GEOGRAPHY","GEOMETRY"],
            "VECTOR":["VECTOR"]    
        }

class TempTable(Table):
    _scope="SCOPE"
    _allowed_values_scope=["LOCAL","GLOBAL"]
    _read_only_tag="READ_ONLY"


