
import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseMethod,BaseTag

class Table(BaseTag,BaseMethod):
    COLUMNS_LIST="COLUMNS_LIST"
    DATA_TYPES="DATA_TYPES"
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
        return allowed_types_dict
    
    @classmethod
    def get_attributes_with_description(cls):
        attr_dict=super().get_attributes_with_description()
        attr_dict["COLUMNS_LIST"]="user provided value for COLUMN_LIST for table object. if value is not provided by user, DEFAULT value is set to NONE.Pass all the columns user provide as a list."
        attr_dict["DATA_TYPES"]="user provided value for DATA TYPES of each column for table object. if value is not provided by user, DEFAULT value is set to NONE.Pass all the columns user provide as a list."
        
        return attr_dict
    
    @classmethod
    def allowed_value_list(cls):
        pass

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass



