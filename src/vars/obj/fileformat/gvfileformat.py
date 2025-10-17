import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.basetag import BaseTag,BaseMethod

class FileFormatTag(BaseTag,BaseMethod):
    TYPE="TYPE"
    COMPRESSION="COMPRESSION"
    RECORD_DELIMITER="RECORD_DELIMITER"
    FIELD_DELIMITER="FIELD_DELIMITER"   
    MULTI_LINE="MULTI_LINE"
    FILE_EXTENSION="FILE_EXTENSION"
    PARSE_HEADER="PARSE_HEADER"
    SKIP_HEADER="SKIP_HEADER"
    SKIP_BLANK_LINES="SKIP_BLANK_LINES"
    DATE_FORMAT="DATE_FORMAT"
    TIME_FORMAT="TIME_FORMAT"
    TIMESTAMP_FORMAT="TIMESTAMP_FORMAT"
    BINARY_FORMAT="BINARY_FORMAT"
    ESCAPE="ESCAPE"
    ESCAPE_UNENCLOSED_FIELD="ESCAPE_UNENCLOSED_FIELD"
    TRIM_SPACE="TRIM_SPACE"
    FIELD_OPTIONALLY_ENCLOSED_BY="FIELD_OPTIONALLY_ENCLOSED_BY"
    NULL_IF="NULL_IF"
    ERROR_ON_COLUMN_COUNT_MISMATCH="ERROR_ON_COLUMN_COUNT_MISMATCH"
    REPLACE_INVALID_CHARACTERS="REPLACE_INVALID_CHARACTERS"
    EMPTY_FIELD_AS_NULL="EMPTY_FIELD_AS_NULL"
    SKIP_BYTE_ORDER_MARK="SKIP_BYTE_ORDER_MARK"
    ENCODING="ENCODING"
    ENABLE_OCTAL="ENABLE_OCTAL"
    ALLOW_DUPLICATE="ALLOW_DUPLICATE"
    STRIP_OUTER_ARRAY="STRIP_OUTER_ARRAY"
    STRIP_NULL_VALUES="STRIP_NULL_VALUES"
    IGNORE_UTF8_ERRORS="IGNORE_UTF8_ERRORS"
    SNAPPY_COMPRESSION="SNAPPY_COMPRESSION"
    BINARY_AS_TEXT="BINARY_AS_TEXT"
    USE_LOGICAL_TYPE="USE_LOGICAL_TYPE"
    USE_VECTORIZED_SCANNER="USE_VECTORIZED_SCANNER"
    PRESERVE_SPACE="PRESERVE_SPACE"
    STRIP_OUTER_ELEMENT="STRIP_OUTER_ELEMENT"
    DISABLE_SNOWFLAKE_DATA="DISABLE_SNOWFLAKE_DATA"
    DISABLE_AUTO_CONVERT="DISABLE_AUTO_CONVERT"

    @classmethod
    def get_attributes_with_description(cls):
        attr_dict = super().get_attributes_with_description()
        attr_dict["TYPE"] = "user provided value for TYPE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["COMPRESSION"] = "user provided value for COMPRESSION for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["RECORD_DELIMITER"] = "user provided value for RECORD_DELIMITER for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["FIELD_DELIMITER"] = "user provided value for FIELD_DELIMITER for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["MULTI_LINE"] = "user provided value for MULTI_LINE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["FILE_EXTENSION"] = "user provided value for FILE_EXTENSION for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["PARSE_HEADER"] = "user provided value for PARSE_HEADER for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["SKIP_HEADER"] = "user provided value for SKIP_HEADER for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["SKIP_BLANK_LINES"] = "user provided value for SKIP_BLANK_LINES for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["DATE_FORMAT"] = "user provided value for DATE_FORMAT for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["TIME_FORMAT"] = "user provided value for TIME_FORMAT for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["TIMESTAMP_FORMAT"] = "user provided value for TIMESTAMP_FORMAT for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["BINARY_FORMAT"] = "user provided value for BINARY_FORMAT for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["ESCAPE"] = "user provided value for ESCAPE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["ESCAPE_UNENCLOSED_FIELD"] = "user provided value for ESCAPE_UNENCLOSED_FIELD for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["TRIM_SPACE"] = "user provided value for TRIM_SPACE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["FIELD_OPTIONALLY_ENCLOSED_BY"] = "user provided value for FIELD_OPTIONALLY_ENCLOSED_BY for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["NULL_IF"] = "user provided value for NULL_IF for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["ERROR_ON_COLUMN_COUNT_MISMATCH"] = "user provided value for ERROR_ON_COLUMN_COUNT_MISMATCH for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["REPLACE_INVALID_CHARACTERS"] = "user provided value for REPLACE_INVALID_CHARACTERS for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["EMPTY_FIELD_AS_NULL"] = "user provided value for EMPTY_FIELD_AS_NULL for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["SKIP_BYTE_ORDER_MARK"] = "user provided value for SKIP_BYTE_ORDER_MARK for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["ENCODING"] = "user provided value for ENCODING for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["ENABLE_OCTAL"] = "user provided value for ENABLE_OCTAL for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["ALLOW_DUPLICATE"] = "user provided value for ALLOW_DUPLICATE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["STRIP_OUTER_ARRAY"] = "user provided value for STRIP_OUTER_ARRAY for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["STRIP_NULL_VALUES"] = "user provided value for STRIP_NULL_VALUES for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["IGNORE_UTF8_ERRORS"] = "user provided value for IGNORE_UTF8_ERRORS for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["SNAPPY_COMPRESSION"] = "user provided value for SNAPPY_COMPRESSION for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["BINARY_AS_TEXT"] = "user provided value for BINARY_AS_TEXT for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["USE_LOGICAL_TYPE"] = "user provided value for USE_LOGICAL_TYPE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["USE_VECTORIZED_SCANNER"] = "user provided value for USE_VECTORIZED_SCANNER for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["PRESERVE_SPACE"] = "user provided value for PRESERVE_SPACE for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["STRIP_OUTER_ELEMENT"] = "user provided value for STRIP_OUTER_ELEMENT for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["DISABLE_SNOWFLAKE_DATA"] = "user provided value for DISABLE_SNOWFLAKE_DATA for database object. if value is not provided by user, DEFAULT value is set to NONE"
        attr_dict["DISABLE_AUTO_CONVERT"] = "user provided value for DISABLE_AUTO_CONVERT for database object. if value is not provided by user, DEFAULT value is set to NONE"
        return attr_dict


    @classmethod
    def allowed_value_list(cls):
        return {
            "TYPE":["CSV","JSON","AVRO","ORC","PARQUET","XML","DEFAULT"],
            "BINARY_FORMAT": ["HEX","BASE64","UTF8"],
            "COMPRESSION":{
                "CSV":["AUTO","GZIP","BZ2","BROTLI","ZSTD","DEFLATE","RAW_DEFLATE"],
                "JSON":["AUTO","GZIP","BZ2","BROTLI","ZSTD","DEFLATE","RAW_DEFLATE"],
                "AVRO":["AUTO","GZIP","BROTLI","ZSTD","DEFLATE","RAW_DEFLATE"],
                "PARQUET":["AUTO","LZO","SNAPPY"],
                "XML":["AUTO","GZIP","BZ2","BROTLI","ZSTD","DEFLATE","RAW_DEFLATE"]
            },
            "ENCODING":["BIG5","EUCJP","EUCKR","GB18030","IBM420","IBM424","IBM949","ISO2022CN","ISO2022JP","ISO2022KR","ISO88591","ISO88592","ISO88595","ISO88596","ISO88597","ISO88598","ISO88599","ISO885915","KOI8R","SHIFTJIS","UTF8","UTF16","UTF16BE","UTF16LE","UTF32","UTF32BE","UTF32LE","WINDOWS874","WINDOWS949","WINDOWS1250","WINDOWS1251","WINDOWS1252","WINDOWS1253","WINDOWS1254","WINDOWS1255","WINDOWS1256"]

        }

    @classmethod
    def max_allowed_value(cls):
        pass

    @classmethod
    def min_allowed_value(cls):
        pass
          
