from dataclasses import dataclass

dataclass(frozen=True)
class DataTypes:
    __data_type_dict ={
        'NUMBER':['NUMBER'],
        'DECIMAL':['DECIMAL','DEC','NUMERIC'],
        'INTEGER':['INT','BIGINT','SMALLINT','TINYINT','BYTEINT'],
        'FLOAT':['FLOAT','FLOAT4','FLOAT8'],
        'DOUBLE':['DOUBLE','DOUBLE PRECISION','REAL'],
        'VARCHAR':['VARCHAR','CHAR','CHARACTER','NCHAR','STRING','TEXT','NVARCHAR','NVARCHAR2','CHAR VARYING','NCHAR VARYING'],
        'BINARY_STRING':['BINARY','VARBINARY'],
        'BOOLEAN':['BOOLEAN'],  
        'Date':['DATE'],
        'Time':['TIME'],
        'DateTime':['DATETIME'],
        'Timestamp':['TIMESTAMP','TIMESTAMP_LTZ','TIMESTAMP_NTZ','TIMESTAMP_TZ'],
        'Variant':['VARIANT'],
        'Object':['OBJECT'],
        'Array':['ARRAY']  
    }

    @classmethod
    def get_allowed_data_types(cls):
        return cls.__data_type_dict
    

