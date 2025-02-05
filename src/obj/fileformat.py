import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.global_vars import FileFormat as gv,Config as cfg, Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy
from validation.validateobject import ValidateObject as vo
from setup import privilege


class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if vo.database_exist(value):
            instance._database = value

    def __del__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if vo.schema_exist(instance._database,value):
            instance._schema = value

    def __del__(self,instance):
        del instance._schema


class Name:   
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._name = value

    def __del__(self,instance):
        del instance._name


class NameTag:   
    def __get__(self,instance,owner):
        return instance._name_tag
    
    def __set__(self,instance,value):
        instance._name_tag = value

    def __del__(self,instance):
        del instance._name_tag

class Type:
    def __get__(self,instance,owner):
        return instance._type
    
    def __set__(self,instance,value):
        instance._type = value

    def __del__(self,instance):
        del instance._type

class TypeTag:
    def __get__(self,instance,owner):
        return instance._type_tag
    
    def __set__(self,instance,value):
        instance._type_tag = value

    def __del__(self,instance):
        del instance._type_tag


class Compression:
    def __get__(self,instance,owner):
        return instance._compression
    
    def __set__(self,instance,value):
        if instance._type == gv._allowed_values_type[0]: #CSV
            if value not in gv._allowed_values_compression_for_csv:
                raise KeyError
            else:
                instance._compression = value
        elif instance._type == gv._allowed_values_type[1]: #JSON
            if value not in gv._allowed_values_compression_for_json:
                raise KeyError
            else:
                instance._compression = value
        elif instance._type == gv._allowed_values_type[2]: #AVRO
            if value not in gv._allowed_values_compression_for_avro:
                raise KeyError
            else:
                instance._compression = value
        elif instance._type == gv._allowed_values_type[3]: #ORC
            raise KeyError('Parameternot allowed')
        elif instance._type == gv._allowed_values_type[4]: #PARQUET
            if value not in gv._allowed_values_compression_for_parquet:
                raise KeyError
            else:
                instance._compression = value
        elif instance._type == gv._allowed_values_type[5]: #XML
            if value not in gv._allowed_values_compression_for_xml:
                raise KeyError
            else:
                instance._compression = value

    def __del__(self,instance):
        del instance._compression

class CompressionTag:
    def __get__(self,instance,owner):
        return instance._compression_tag
    
    def __set__(self,instance,value):
        instance._compression_tag = value

    def __del__(self,instance):
        del instance._compression_tag

class RecordDelimiter:
    def __get__(self,instance,owner):
        return instance._record_delimiter
    
    def __set__(self,instance,value):
        if instance._type == "DEFAULT":
            instance._record_delimiter = value
        elif instance._type == gv._allowed_values_type[0]:
            if type(value) != str:
                raise TypeError
            elif len(value) > 20:
                raise TypeError
            else:
                instance._record_delimiter = value
        else:
            raise ValueError

    def __del__(self,instance):
        del instance._record_delimiter

class RecordDelimiterTag:
    def __get__(self,instance,owner):
        return instance._record_delimiter_tag
    
    def __set__(self,instance,value):
        instance._record_delimiter_tag = value

    def __del__(self,instance):
        del instance._record_delimiter_tag

class FieldDelimiter:
    def __get__(self,instance,owner):
        return instance._field_delimiter
    
    def __set__(self,instance,value):
        if instance._type == "DEFAULT":
            instance._field_delimiter = ","
        if instance._type == gv._allowed_values_type[0]:
            if type(value) != str:
                raise ValueError
            elif len(value) > 20:
                raise KeyError
            else:
                instance._field_delimiter = value
        else:
            raise ValueError

    def __del__(self,instance):
        del instance._field_delimiter

class FieldDelimiterTag:
    def __get__(self,instance,owner):
        return instance._field_delimiter_tag
    
    def __set__(self,instance,value):
        instance._field_delimiter_tag = value

    def __del__(self,instance):
        del instance._field_delimiter_tag

class FileExtension:
    def __get__(self,instance,owner):
        return instance._file_extension
    
    def __set__(self,instance,value):
        if instance._type == "DEFAULT":
            instance._file_extension = value
        elif instance._type == gv._allowed_values_type[0]:
            if type(value) != str:
                raise KeyError
            else:
                instance._file_extension = value
        else:
            raise ValueError

    def __del__(self,instance):
        del instance._file_extension    

class FileExtensionTag:
    def __get__(self,instance,owner):
        return instance._file_extension_tag
    
    def __set__(self,instance,value):
        instance._file_extension_tag = value

    def __del__(self,instance):
        del instance._file_extension_tag    

class ParseHeader:
    def __get__(self,instance,owner):
        return instance._parse_header
    
    def __set__(self,instance,value):
        if instance._type == gv._allowed_values_type[0]:
            if value == "NONE":
                instance._parse_header = value
            else:
                if vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                    instance._parse_header = value
                else:
                    raise ValueError                
        else:
            raise ValueError

    def __del__(self,instance):
        del instance._parse_header

class ParseHeaderTag:
    def __get__(self,instance,owner):
        return instance._parse_header_tag
    
    def __set__(self,instance,value):
        instance._parse_header_tag = value

    def __del__(self,instance):
        del instance._parse_header_tag

class SkipHeader:
    def __get__(self,instance,owner):
        return instance._skip_header
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._skip_header = value  
        elif instance._type == "DEFAULT":
            instance._skip_header = "NONE"
        elif instance._type == gv._allowed_values_type[0]:
            instance._skip_header = value

    def __del__(self,instance):
        del instance._skip_header

class SkipHeaderTag:
    def __get__(self,instance,owner):
        return instance._skip_header_tag
    
    def __set__(self,instance,value):
        instance._skip_header_tag = value

    def __del__(self,instance):
        del instance._skip_header_tag


class SkipBlankLines:
    def __get__(self,instance,owner):
        return instance._skip_blank_lines
    
    def __set__(self,instance,value):
        if instance._type == gv._allowed_values_type[0]:
            if value == "NONE":
                instance._skip_blank_lines = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._skip_blank_lines = value   

    def __del__(self,instance):
        del instance._skip_blank_lines

class SkipBlankLinesTag:
    def __get__(self,instance,owner):
        return instance._skip_blank_lines_tag
    
    def __set__(self,instance,value):
        instance._skip_blank_lines_tag = value

    def __del__(self,instance):
        del instance._skip_blank_lines_tag

class DateFormat:
    def __get__(self,instance,owner):
        return instance._date_format
    
    def __set__(self,instance,value):
        if instance._type == "DEFAULT":
            instance._date_format = "DEFAULT"
        elif instance._type == gv._allowed_values_type[0] or instance._type == gv._allowed_values_type[1]:
            if type(value) != str:
                raise KeyError
            else:
                instance._date_format = value
        else:
            raise ValueError

    def __del__(self,instance):
        del instance._date_format

class DateFormatTag:
    def __get__(self,instance,owner):
        return instance._date_format_tag
    
    def __set__(self,instance,value):
        instance._date_format_tag = value

    def __del__(self,instance):
        del instance._date_format_tag

class TimeFormat:
    def __get__(self,instance,owner):
        return instance._time_format
    
    def __set__(self,instance,value):
        if instance._type == "DEFAULT":
            instance._time_format = "DEFAULT"
        elif instance._type == gv._allowed_values_type[0] or instance._type == gv._allowed_values_type[1]:
            if type(value) != str:
                raise KeyError
            else:
                instance._time_format = value
        else:
            raise ValueError

    def __del__(self,instance):
        del instance._time_format

class TimeFormatTag:
    def __get__(self,instance,owner):
        return instance._time_format_tag
    
    def __set__(self,instance,value):
        instance._time_format_tag = value

    def __del__(self,instance):
        del instance._time_format_tag

class TimestampFormat:
    def __get__(self,instance,owner):
        return instance._timestamp_format
    
    def __set__(self,instance,value):
        if instance._type == "NONE":
            instance._timestamp_format = "NONE"
        elif instance._type == gv._allowed_values_type[0] or instance._type == gv._allowed_values_type[1]:
            instance._timestamp_format = value
        else:
            raise ValueError

    def __del__(self,instance):
        del instance._timestamp_format

class TimestampFormatTag:
    def __get__(self,instance,owner):
        return instance._timestamp_format_tag
    
    def __set__(self,instance,value):
        instance._timestamp_format_tag = value

    def __del__(self,instance):
        del instance._timestamp_format_tag
   
class BinaryFormat:
    def __get__(self,instance,owner):
        return instance._binary_format
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._binary_format = value
        elif instance._type == gv._allowed_values_type[0] or instance._type == gv._allowed_values_type[1]:
            if value not in gv._allowed_values_binary_format:
                raise KeyError
            else:
                instance._binary_format = value

    def __del__(self,instance):
        del instance._binary_format

class BinaryFormatTag:
    def __get__(self,instance,owner):
        return instance._binary_format_tag
    
    def __set__(self,instance,value):
        instance._binary_format_tag = value

    def __del__(self,instance):
        del instance._binary_format_tag

class Escape:
    def __get__(self,instance,owner):
        return instance._escape
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._escape = value
        elif instance._type == gv._allowed_values_type[0]: #CSV
            instance._escape = value


    def __del__(self,instance):
        del instance._escape


class EscapeTag:
    def __get__(self,instance,owner):
        return instance._escape_tag
    
    def __set__(self,instance,value):
        instance._escape_tag = value

    def __del__(self,instance):
        del instance._escape_tag

class EscapeUnenclosedField:
    def __get__(self,instance,owner):
        return instance._escape_unenclosed_field
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._escape_unenclosed_field = value
        elif instance._type == gv._allowed_values_type[0]: #CSV
            instance._escape_unenclosed_field = value
        
    def __del__(self,instance):
        del instance._escape_unenclosed_field

class EscapeUnenclosedFieldTag:
    def __get__(self,instance,owner):
        return instance._escape_unenclosed_field_tag
    
    def __set__(self,instance,value):
        instance._escape_unenclosed_field_tag = value

    def __del__(self,instance):
        del instance._escape_unenclosed_field_tag

class TrimSpace:
    def __get__(self,instance,owner):
        return instance._trim_space
    
    def __set__(self,instance,value):
        if (instance._type == gv._allowed_values_type[0] or
            instance._type == gv._allowed_values_type[1] or
            instance._type == gv._allowed_values_type[2] or
            instance._type == gv._allowed_values_type[3] or
            instance._type == gv._allowed_values_type[4] ):
            if value == "NONE":
                instance._trim_space = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._trim_space = value

    def __del__(self,instance):
        del instance._trim_space

class TrimSpaceTag:
    def __get__(self,instance,owner):
        return instance._trim_space_tag
    
    def __set__(self,instance,value):
        instance._trim_space_tag = value

    def __del__(self,instance):
        del instance._trim_space_tag

class FieldOptionallyEnclosedBy:
    def __get__(self,instance,owner):
        return instance._field_optionally_enclosed_by
    
    def __set__(self,instance,value):
        instance._field_optionally_enclosed_by = value

    def __del__(self,instance):
        del instance._field_optionally_enclosed_by

class FieldOptionallyEnclosedByTag:
    def __get__(self,instance,owner):
        return instance._field_optionally_enclosed_by_tag
    
    def __set__(self,instance,value):
        if instance._type == gv._allowed_values_type[0]:
            instance._field_optionally_enclosed_by_tag = value
        else:
            raise ValueError

    def __del__(self,instance):
        del instance._field_optionally_enclosed_by_tag

class NullIf:
    def __get__(self,instance,owner):
        return instance._null_if
    
    def __set__(self,instance,value):
        if (instance._type == gv._allowed_values_type[0] or
            instance._type == gv._allowed_values_type[1] or
            instance._type == gv._allowed_values_type[2] or
            instance._type == gv._allowed_values_type[3] or
            instance._type == gv._allowed_values_type[4]):
            if value == "NONE":
                instance._null_if = value
            elif type(value) != str:
                raise KeyError

    def __del__(self,instance):
        del instance._null_if

class NullIfTag:
    def __get__(self,instance,owner):
        return instance._null_if_tag
    
    def __set__(self,instance,value):
        instance._null_if_tag = value

    def __del__(self,instance):
        del instance._null_if_tag

class ErrorOnColumnCountMismatch:
    def __get__(self,instance,owner):
        return instance._error_on_column_count_mismatch
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._error_on_column_count_mismatch = value
        elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._error_on_column_count_mismatch = value
            

    def __del__(self,instance):
        del instance._error_on_column_count_mismatch

class ErrorOnColumnCountMismatchTag:
    def __get__(self,instance,owner):
        return instance._error_on_column_count_mismatch_tag
    
    def __set__(self,instance,value):
        if instance._type == gv._allowed_values_type[0]:
            instance._error_on_column_count_mismatch_tag = value
        else:
            raise ValueError

    def __del__(self,instance):
        del instance._error_on_column_count_mismatch_tag

class ReplaceInvalidCharacters:
    def __get__(self,instance,owner):
        return instance._replace_invalid_characters
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._replace_invalid_characters = value
        elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._replace_invalid_characters = value
            
    def __del__(self,instance):
        del instance._replace_invalid_characters

class ReplaceInvalidCharactersTag:
    def __get__(self,instance,owner):
        return instance._replace_invalid_characters_tag
    
    def __set__(self,instance,value):
        instance._replace_invalid_characters_tag = value

    def __del__(self,instance):
        del instance._replace_invalid_characters_tag

class EmptyFieldAsNull:
    def __get__(self,instance,owner):
        return instance._empty_field_as_null
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._empty_field_as_null = value
        elif instance._type == gv._allowed_values_type[0]:
            if value == "NONE":
                instance._type = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._empty_field_as_null = value

    def __del__(self,instance):
        del instance._empty_field_as_null

class EmptyFieldAsNullTag:
    def __get__(self,instance,owner):
        return instance._empty_field_as_null_tag
    
    def __set__(self,instance,value):
        instance._empty_field_as_null_tag = value

    def __del__(self,instance):
        del instance._empty_field_as_null_tag

class SkipByteOrderMark:
    def __get__(self,instance,owner):
        return instance._skip_byte_order_mark
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._skip_byte_order_mark = value
        elif (instance._type == gv._allowed_values_type[0] or
            instance._type == gv._allowed_values_type[1] or 
            instance._type == gv._allowed_values_type[5] ):
            if value == "NONE":
                instance._skip_byte_order_mark = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._skip_byte_order_mark = value    

    def __del__(self,instance):
        del instance._skip_byte_order_mark

class SkipByteOrderMarkTag:
    def __get__(self,instance,owner):
        return instance._skip_byte_order_mark_tag
    
    def __set__(self,instance,value):
        instance._skip_byte_order_mark_tag = value

    def __del__(self,instance):
        del instance._skip_byte_order_mark_tag

class Encoding:
    def __get__(self,instance,owner):
        return instance._encoding
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._encoding = value
        elif instance._type == gv._allowed_values_type[0]:
            if value == "NONE":
                instance._encoding = value
            elif type(value) != str:
                raise TypeError

    def __del__(self,instance):
        del instance._encoding

class EncodingTag:
    def __get__(self,instance,owner):
        return instance._encoding_tag
    
    def __set__(self,instance,value):
        instance._encoding_tag = value

    def __del__(self,instance):
        del instance._encoding_tag

class EnableOctal:
    def __get__(self,instance,owner):
        return instance._enable_octal
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._enable_octal = value
        elif instance._type == gv._allowed_values_type[1]:
            if value == "NONE":
                instance._enable_octal = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._enable_octal = value

    def __del__(self,instance):
        del instance._enable_octal    

class EnableOctalTag:
    def __get__(self,instance,owner):
        return instance._enable_octal_tag
    
    def __set__(self,instance,value):
        instance._enable_octal_tag = value

    def __del__(self,instance):
        del instance._enable_octal_tag

class AllowDuplicate:
    def __get__(self,instance,owner):
        return instance._allow_duplicate
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._allow_duplicate = value
        elif instance._type == gv._allowed_values_type[1]:
            if value == "NONE":
                instance._allow_duplicate = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._allow_duplicate = value

    def __del__(self,instance):
        del instance._allow_duplicate

class AllowDuplicateTag:
    def __get__(self,instance,owner):
        return instance._allow_duplicate_tag
    
    def __set__(self,instance,value):
        instance._allow_duplicate_tag = value

    def __del__(self,instance):
        del instance._allow_duplicate_tag

class StripOuterArray:
    def __get__(self,instance,owner):
        return instance._strip_outer_array
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._strip_outer_array = value
        elif instance._type == gv._allowed_values_type[1]: #JSON
            if value == "NONE":
                instance._strip_outer_array = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._strip_outer_array = value
        
    def __del__(self,instance):
        del instance._strip_outer_array

class StripOuterArrayTag:
    def __get__(self,instance,owner):
        return instance._strip_outer_array_tag
    
    def __set__(self,instance,value):
        instance._strip_outer_array_tag = value

    def __del__(self,instance):
        del instance._strip_outer_array_tag

class StripNullValues:
    def __get__(self,instance,owner):
        return instance._strip_null_values
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._strip_null_values = value
        if instance._type == gv._allowed_values_type[1]: #JSON
            if value == "NONE":
                instance._strip_null_values = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._strip_null_values = value
        
    def __del__(self,instance):
        del instance._strip_null_values

class StripNullValuesTag:
    def __get__(self,instance,owner):
        return instance._strip_null_values_tag
    
    def __set__(self,instance,value):
        instance._strip_null_values_tag = value

    def __del__(self,instance):
        del instance._strip_null_values_tag

class IgnoreUTF8Errors:
    def __get__(self,instance,owner):
        return instance._ignore_utf8_errors
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._ignore_utf8_errors = value
        elif (instance._type == gv._allowed_values_type[1] or
            instance._type == gv._allowed_values_type[5]) : #JSON and XML
            if value == "NONE":
                instance._ignore_utf8_errors = value
            if vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._ignore_utf8_errors = value
            else:
                raise TypeError
        else:
            instance._ignore_utf8_errors = value
        
    def __del__(self,instance):
        del instance._ignore_utf8_errors

class IgnoreUTF8ErrorsTag:
    def __get__(self,instance,owner):
        return instance._ignore_utf8_errors_tag
    
    def __set__(self,instance,value):
        instance._ignore_utf8_errors_tag = value

    def __del__(self,instance):
        del instance._ignore_utf8_errors_tag


class SnappyCompression:
    def __get__(self,instance,owner):
        return instance._snappy_compression
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._snappy_compression = value
        elif instance._type == gv._allowed_values_type[4]: #PARQUET
            if value == "NONE":
                instance._snappy_compression = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._snappy_compression = value

    def __del__(self,instance):
        del instance._snappy_compression

class SnappyCompressionTag:
    def __get__(self,instance,owner):
        return instance._snappy_compression_tag
    
    def __set__(self,instance,value):
        instance._snappy_compression_tag = value

    def __del__(self,instance):
        del instance._snappy_compression_tag
        
class BinaryAsText:
    def __get__(self,instance,owner):
        return instance._binary_as_text
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._binary_as_text = value
        elif instance._type == gv._allowed_values_type[4]: #PARQUET
            if value == "NONE":
                instance._binary_as_text = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._binary_as_text = value

    def __del__(self,instance):
        del instance._binary_as_text

class BinaryAsTextTag:
    def __get__(self,instance,owner):
        return instance._binary_as_text_tag
    
    def __set__(self,instance,value):
        instance._binary_as_text_tag = value

    def __del__(self,instance):
        del instance._binary_as_text_tag

class UseLogicalType:
    def __get__(self,instance,owner):
        return instance._use_logical_type
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._use_logical_type = value
        elif instance._type == gv._allowed_values_type[4]: #PARQUET
            if value == "NONE":
                instance._use_logical_type = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._use_logical_type = value

    def __del__(self,instance):
        del instance._use_logical_type

class UseLogicalTypeTag:
    def __get__(self,instance,owner):
        return instance._use_logical_type_tag
    
    def __set__(self,instance,value):
        instance._use_logical_type_tag = value

    def __del__(self,instance):
        del instance._use_logical_type_tag

class UseVectorizedScanner:
    def __get__(self,instance,owner):
        return instance._use_vectorized_scanner
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._use_vectorized_scanner = value
        elif instance._type == gv._allowed_values_type[4]: #PARQUET
            if value == "NONE":
                instance._use_vectorized_scanner = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._use_vectorized_scanner = value

    def __del__(self,instance):
        del instance._use_vectorized_scanner

class UseVectorizedScannerTag:
    def __get__(self,instance,owner):
        return instance._use_vectorized_scanner_tag
    
    def __set__(self,instance,value):
        instance._use_vectorized_scanner_tag = value

    def __del__(self,instance):
        del instance._use_vectorized_scanner_tag

class PreserveSpace:
    def __get__(self,instance,owner):
        return instance._preserve_space
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._preserve_space = value
        elif instance._type == gv._allowed_values_type[5]: #XML
            if value == "NONE":
                instance._preserve_space = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._preserve_space = value

    def __del__(self,instance):
        del instance._preserve_space

class PreserveSpaceTag:
    def __get__(self,instance,owner):
        return instance._preserve_space_tag
    
    def __set__(self,instance,value):
        instance._preserve_space_tag = value

    def __del__(self,instance):
        del instance._preserve_space_tag

class StripOuterElement:
    def __get__(self,instance,owner):
        return instance._strip_outer_element
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._strip_outer_element = value
        elif instance._type == gv._allowed_values_type[5]: #XML
            if value == "NONE":
                instance._strip_outer_element = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._strip_outer_element = value

    def __del__(self,instance):
        del instance._strip_outer_element

class StripOuterElementTag:
    def __get__(self,instance,owner):
        return instance._strip_outer_element_tag
    
    def __set__(self,instance,value):
        instance._strip_outer_element_tag = value

    def __del__(self,instance):
        del instance._strip_outer_element_tag

class DisableSnowflakeData:
    def __get__(self,instance,owner):
        return instance._disable_snowflake_data
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._disable_snowflake_data = value
        elif instance._type == gv._allowed_values_type[5]: #XML
            if value == "NONE":
                instance._disable_snowflake_data = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._disable_snowflake_data = value

    def __del__(self,instance):
        del instance._disable_snowflake_data

class DisableSnowflakeDataTag:
    def __get__(self,instance,owner):
        return instance._disable_snowflake_data_tag
    
    def __set__(self,instance,value):
        instance._disable_snowflake_data_tag = value

    def __del__(self,instance):
        del instance._disable_snowflake_data_tag

class DisableAutoConvert:
    def __get__(self,instance,owner):
        return instance._disable_auto_convert
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._disable_auto_convert = value
        elif instance._type == gv._allowed_values_type[5]: #XML
            if value == "NONE":
                instance._disable_auto_convert = value
            elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
                instance._disable_auto_convert = value

    def __del__(self,instance):
        del instance._disable_auto_convert


class DisableAutoConvertTag:
    def __get__(self,instance,owner):
        return instance._disable_auto_convert_tag
    
    def __set__(self,instance,value):
        instance._disable_auto_convert_tag = value

    def __del__(self,instance):
        del instance._disable_auto_convert_tag

class FileFormatAttrs:
    def __init__(self,parent):
        self.parent = parent

    database = Database()
    schema = Schema()
    type = Type()
    type_tag = TypeTag()
    name = Name()
    name_tag = NameTag()
    compression = Compression()
    compression_tag = CompressionTag()
    record_delimiter = RecordDelimiter()
    record_delimiter_tag = RecordDelimiterTag()
    field_delimiter = FieldDelimiter()
    field_delimiter_tag = FieldDelimiterTag()
    file_extension = FileExtension()
    file_extension_tag = FileExtensionTag()
    parse_header = ParseHeader()
    parse_header_tag = ParseHeaderTag()
    skip_header = SkipHeader()
    skip_header_tag = SkipHeaderTag()
    skip_blank_lines = SkipBlankLines()
    skip_blank_lines_tag = SkipBlankLinesTag()
    date_format = DateFormat()
    date_format_tag = DateFormatTag()
    time_format = TimeFormat()
    time_format_tag = TimeFormatTag()
    timestamp_format = TimestampFormat()
    timestamp_format_tag = TimestampFormatTag()
    binary_format = BinaryFormat()
    binary_format_tag = BinaryFormatTag()
    escape = Escape()
    escape_tag = EscapeTag()
    escape_unenclosed_field = EscapeUnenclosedField()
    escape_unenclosed_field_tag = EscapeUnenclosedFieldTag()
    trim_space = TrimSpace()
    trim_space_tag = TrimSpaceTag()
    field_optionally_enclosed_by = FieldOptionallyEnclosedBy()
    field_optionally_enclosed_by_tag = FieldOptionallyEnclosedByTag()
    null_if = NullIf()
    null_if_tag = NullIfTag()
    error_on_column_count_mismatch = ErrorOnColumnCountMismatch()
    error_on_column_count_mismatch_tag = ErrorOnColumnCountMismatchTag()
    replace_invalid_characters = ReplaceInvalidCharacters()
    replace_invalid_characters_tag = ReplaceInvalidCharactersTag()
    empty_field_as_null = EmptyFieldAsNull()
    empty_field_as_null_tag = EmptyFieldAsNullTag()
    skip_byte_order_mark = SkipByteOrderMark()
    skip_byte_order_mark_tag = SkipByteOrderMarkTag()
    encoding = Encoding()
    encoding_tag = EncodingTag()
    enable_octal = EnableOctal()
    enable_octal_tag = EnableOctalTag()
    allow_duplicate = AllowDuplicate()
    allow_duplicate_tag = AllowDuplicateTag()
    strip_outer_array = StripOuterArray()
    strip_outer_array_tag = StripOuterArrayTag()
    strip_null_values = StripNullValues()
    strip_null_values_tag = StripNullValuesTag()
    ignore_utf8_errors = IgnoreUTF8Errors()
    ignore_utf8_errors_tag = IgnoreUTF8ErrorsTag()
    snappy_compression = SnappyCompression()
    snappy_compression_tag = SnappyCompressionTag()
    binary_as_text = BinaryAsText()
    binary_as_text_tag = BinaryAsTextTag()
    use_logical_type = UseLogicalType()
    use_logical_type_tag = UseLogicalTypeTag()
    use_vectorized_scanner = UseVectorizedScanner()
    use_vectorized_scanner_tag = UseVectorizedScannerTag()
    preserve_space = PreserveSpace()
    preserve_space_tag = PreserveSpaceTag()
    strip_outer_element = StripOuterElement()
    strip_outer_element_tag = StripOuterElementTag()
    disable_snowflake_data = DisableSnowflakeData()
    disable_snowflake_data_tag = DisableSnowflakeDataTag()
    disable_auto_convert = DisableAutoConvert()
    disable_auto_convert_tag = DisableAutoConvertTag()


class FileFormat:
    def __init__(self,session,user_id):
        self.attr = FileFormatAttrs(self)
        self.session = session
        self.user_id = user_id
        self.qry = ""

    def set_name(self,val):
        self.attr.name = val
    
    def set_database(self,val):
        self.attr.database = val
    
    def set_schema(self,val):
        self.attr.schema = val

    def set_name_tag(self,val):
        self.attr.name_tag = val

    def set_type(self,type):
        self.attr.type = type
    
    def set_type_tag(self,val):
        self.attr.type_tag = val


    def set_compression(self,val):
        self.attr.compression = val
    
    def set_compression_tag(self,val):
        self.attr.compression_tag = val

    def set_record_delimiter(self,val):
        self.attr.record_delimiter = val
    
    def set_record_delimiter_tag(self,val):
        self.attr.record_delimiter_tag = val

    def set_field_delimiter(self,val):
        self.attr.field_delimiter = val
    
    def set_field_delimiter_tag(self,val):
        self.attr.field_delimiter_tag = val

    def set_file_extension(self,val):
        self.attr.file_extension = val
    
    def set_file_extension_tag(self,val):
        self.attr.file_extension_tag = val

    def set_parse_header(self, val):
        self.attr.parse_header = val

    def set_parse_header_tag(self, val):
        self.attr.parse_header_tag = val

    def set_skip_header(self, val):
        self.attr.skip_header = val

    def set_skip_header_tag(self, val):
        self.attr.skip_header_tag = val

    def set_skip_blank_lines(self, val):
        self.attr.skip_blank_lines = val

    def set_skip_blank_lines_tag(self, val):
        self.attr.skip_blank_lines_tag = val

    def set_date_format(self, val):
        self.attr.date_format = val

    def set_date_format_tag(self, val):
        self.attr.date_format_tag = val

    def set_time_format(self, val):
        self.attr.time_format = val

    def set_time_format_tag(self, val):
        self.attr.time_format_tag = val

    def set_timestamp_format(self, val):
        self.attr.timestamp_format = val

    def set_timestamp_format_tag(self, val):
        self.attr.timestamp_format_tag = val

    def set_binary_format(self, val):
        self.attr.binary_format = val

    def set_binary_format_tag(self, val):
        self.attr.binary_format_tag = val

    def set_escape(self,val):
        self.attr.escape = val
        
    def set_escape_tag(self,val):
        self.attr.escape_tag = val

    def set_escape_unenclosed_field(self, val):
        self.attr.escape_unenclosed_field = val

    def set_escape_unenclosed_field_tag(self, val):
        self.attr.escape_unenclosed_field_tag = val
    def set_trim_space(self, val):
        self.attr.trim_space = val

    def set_trim_space_tag(self, val):
        self.attr.trim_space_tag = val

    def set_field_optionally_enclosed_by(self, val):
        self.attr.field_optionally_enclosed_by = val

    def set_field_optionally_enclosed_by_tag(self, val):
        self.attr.field_optionally_enclosed_by_tag = val

    def set_null_if(self, val):
        self.attr.null_if = val

    def set_null_if_tag(self, val):
        self.attr.null_if_tag = val

    def set_error_on_column_count_mismatch(self, val):
        self.attr.error_on_column_count_mismatch = val

    def set_error_on_column_count_mismatch_tag(self, val):
        self.attr.error_on_column_count_mismatch_tag = val

    def set_replace_invalid_characters(self, val):
        self.attr.replace_invalid_characters = val

    def set_replace_invalid_characters_tag(self, val):
        self.attr.replace_invalid_characters_tag = val

    def set_empty_field_as_null(self, val):
        self.attr.empty_field_as_null = val

    def set_empty_field_as_null_tag(self, val):
        self.attr.empty_field_as_null_tag = val

    def set_skip_byte_order_mark(self, val):
        self.attr.skip_byte_order_mark = val

    def set_skip_byte_order_mark_tag(self, val):
        self.attr.skip_byte_order_mark_tag = val

    def set_encoding(self, val):
        self.attr.encoding = val

    def set_encoding_tag(self, val):
        self.attr.encoding_tag = val

    def set_enable_octal(self, val):
        self.attr.enable_octal = val

    def set_enable_octal_tag(self, val):
        self.attr.enable_octal_tag = val

    def set_allow_duplicate(self, val):
        self.attr.allow_duplicate = val

    def set_allow_duplicate_tag(self, val):
        self.attr.allow_duplicate_tag = val

    def set_strip_outer_array(self, val):
        self.attr.strip_outer_array = val

    def set_strip_outer_array_tag(self, val):
        self.attr.strip_outer_array_tag = val

    def set_strip_null_values(self, val):
        self.attr.strip_null_values = val

    def set_strip_null_values_tag(self, val):
        self.attr.strip_null_values_tag = val

    def set_ignore_utf8_errors(self, val):
        self.attr.ignore_utf8_errors = val

    def set_ignore_utf8_errors_tag(self, val):
        self.attr.ignore_utf8_errors_tag = val

    def set_snappy_compression(self, val):
        self.attr.snappy_compression = val

    def set_snappy_compression_tag(self, val):
        self.attr.snappy_compression_tag = val

    def set_binary_as_text(self, val):
        self.attr.binary_as_text = val

    def set_binary_as_text_tag(self, val):
        self.attr.binary_as_text_tag = val

    def set_use_logical_type(self, val):
        self.attr.use_logical_type = val

    def set_use_logical_type_tag(self, val):
        self.attr.use_logical_type_tag = val

    def set_use_vectorized_scanner(self, val):
        self.attr.use_vectorized_scanner = val

    def set_use_vectorized_scanner_tag(self, val):
        self.attr.use_vectorized_scanner_tag = val

    def set_preserve_space(self, val):
        self.attr.preserve_space = val

    def set_preserve_space_tag(self, val):
        self.attr.preserve_space_tag = val

    def set_strip_outer_element(self, val):
        self.attr.strip_outer_element = val

    def set_strip_outer_element_tag(self, val):
        self.attr.strip_outer_element_tag = val

    def set_disable_snowflake_data(self, val):
        self.attr.disable_snowflake_data = val

    def set_disable_snowflake_data_tag(self, val):
        self.attr.disable_snowflake_data_tag = val

    def set_disable_auto_convert(self, val):
        self.attr.disable_auto_convert = val

    def set_disable_auto_convert_tag(self, val):
        self.attr.disable_auto_convert_tag = val

    def set_qualified_name(self):
        self.qualified_name = f"{self.attr.database}.{self.attr.schema}.{self.attr.name}"

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv._type_tag,"_type")
        set_flag(gv._parse_header_tag, "_parse_header")
        set_flag(gv._skip_header_tag, "_skip_header")
        set_flag(gv._skip_blank_lines_tag, "_skip_blank_lines")
        set_flag(gv._date_format_tag, "_date_format")
        set_flag(gv._time_format_tag, "_time_format")
        set_flag(gv._timestamp_format_tag, "_timestamp_format")
        set_flag(gv._binary_format_tag, "_binary_format")
        set_flag(gv._escape_tag, "_escape")
        set_flag(gv._escape_unenclosed_field_tag, "_escape_unenclosed_field")
        set_flag(gv._trim_space_tag, "_trim_space")
        set_flag(gv._field_optionally_enclosed_by_tag, "_field_optionally_enclosed_by")
        set_flag(gv._null_if_tag, "_null_if")
        set_flag(gv._error_on_column_count_mismatch_tag, "_error_on_column_count_mismatch")
        set_flag(gv._replace_invalid_characters_tag, "_replace_invalid_characters")
        set_flag(gv._empty_field_as_null_tag, "_empty_field_as_null")
        set_flag(gv._skip_byte_order_mark_tag, "_skip_byte_order_mark")
        set_flag(gv._encoding_tag, "_encoding")
        set_flag(gv._enable_octal_tag, "_enable_octal")
        set_flag(gv._allow_duplicate_tag, "_allow_duplicate")
        set_flag(gv._strip_outer_array_tag, "_strip_outer_array")
        set_flag(gv._strip_null_values_tag, "_strip_null_values")
        set_flag(gv._ignore_utf8_errors_tag, "_ignore_utf8_errors")
        set_flag(gv._snappy_compression_tag, "_snappy_compression")
        set_flag(gv._binary_as_text_tag, "_binary_as_text")
        set_flag(gv._use_logical_type_tag, "_use_logical_type")
        set_flag(gv._use_vectorized_scanner_tag, "_use_vectorized_scanner")
        set_flag(gv._preserve_space_tag, "_preserve_space")
        set_flag(gv._strip_outer_element_tag, "_strip_outer_element")
        set_flag(gv._disable_snowflake_data_tag, "_disable_snowflake_data")
        set_flag(gv._disable_auto_convert_tag, "_disable_auto_convert")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_qry(self):
        self.qry = f"CREATE FILE FORMAT  {self.attr.database}.{self.attr.schema}.{self.attr.name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gv._type_tag:
                    self.qry = f" {self.qry} {self.attr.type_tag} = {self.attr.type} "
                if prop == gv._parse_header_tag:
                    self.qry = f" {self.qry} {self.attr.parse_header_tag} = {self.attr.parse_header} "
                if prop == gv._skip_header_tag:
                    self.qry = f" {self.qry} {self.attr.skip_header_tag} = {self.attr.skip_header} "
                if prop == gv._skip_blank_lines_tag:
                    self.qry = f" {self.qry} {self.attr.skip_blank_lines_tag} = {self.attr.skip_blank_lines} "
                if prop == gv._date_format_tag:
                    self.qry = f" {self.qry} {self.attr.date_format_tag} = {self.attr.date_format} "
                if prop == gv._time_format_tag:
                    self.qry = f" {self.qry} {self.attr.time_format_tag} = {self.attr.time_format} "
                if prop == gv._timestamp_format_tag:
                    self.qry = f" {self.qry} {self.attr.timestamp_format_tag} = {self.attr.timestamp_format} "
                if prop == gv._binary_format_tag:
                    self.qry = f" {self.qry} {self.attr.binary_format_tag} = {self.attr.binary_format} "
                if prop == gv._escape_tag:
                    self.qry = f" {self.qry} {self.attr.escape_tag} = {self.attr.escape} "
                if prop == gv._escape_unenclosed_field_tag:
                    self.qry = f" {self.qry} {self.attr.escape_unenclosed_field_tag} = {self.attr.escape_unenclosed_field} "
                if prop == gv._trim_space_tag:
                    self.qry = f" {self.qry} {self.attr.trim_space_tag} = {self.attr.trim_space} "
                if prop == gv._field_optionally_enclosed_by_tag:
                    self.qry = f" {self.qry} {self.attr.field_optionally_enclosed_by_tag} = {self.attr.field_optionally_enclosed_by} "
                if prop == gv._null_if_tag:
                    self.qry = f" {self.qry} {self.attr.null_if_tag} = {self.attr.null_if} "
                if prop == gv._error_on_column_count_mismatch_tag:
                    self.qry = f" {self.qry} {self.attr.error_on_column_count_mismatch_tag} = {self.attr.error_on_column_count_mismatch} "
                if prop == gv._replace_invalid_characters_tag:
                    self.qry = f" {self.qry} {self.attr.replace_invalid_characters_tag} = {self.attr.replace_invalid_characters} "
                if prop == gv._empty_field_as_null_tag:
                    self.qry = f" {self.qry} {self.attr.empty_field_as_null_tag} = {self.attr.empty_field_as_null} "
                if prop == gv._skip_byte_order_mark_tag:
                    self.qry = f" {self.qry} {self.attr.skip_byte_order_mark_tag} = {self.attr.skip_byte_order_mark} "
                if prop == gv._encoding_tag:
                    self.qry = f" {self.qry} {self.attr.encoding_tag} = {self.attr.encoding} "
                if prop == gv._enable_octal_tag:
                    self.qry = f" {self.qry} {self.attr.enable_octal_tag} = {self.attr.enable_octal} "
                if prop == gv._allow_duplicate_tag:
                    self.qry = f" {self.qry} {self.attr.allow_duplicate_tag} = {self.attr.allow_duplicate} "
                if prop == gv._strip_outer_array_tag:
                    self.qry = f" {self.qry} {self.attr.strip_outer_array_tag} = {self.attr.strip_outer_array} "
                if prop == gv._strip_null_values_tag:
                    self.qry = f" {self.qry} {self.attr.strip_null_values_tag} = {self.attr.strip_null_values} "
                if prop == gv._ignore_utf8_errors_tag:
                    self.qry = f" {self.qry} {self.attr.ignore_utf8_errors_tag} = {self.attr.ignore_utf8_errors} "
                if prop == gv._snappy_compression_tag:
                    self.qry = f" {self.qry} {self.attr.snappy_compression_tag} = {self.attr.snappy_compression} "
                if prop == gv._binary_as_text_tag:
                    self.qry = f" {self.qry} {self.attr.binary_as_text_tag} = {self.attr.binary_as_text} "
                if prop == gv._use_logical_type_tag:
                    self.qry = f" {self.qry} {self.attr.use_logical_type_tag} = {self.attr.use_logical_type} "
                if prop == gv._use_vectorized_scanner_tag:
                    self.qry = f" {self.qry} {self.attr.use_vectorized_scanner_tag} = {self.attr.use_vectorized_scanner} "
                if prop == gv._preserve_space_tag:
                    self.qry = f" {self.qry} {self.attr.preserve_space_tag} = {self.attr.preserve_space} "
                if prop == gv._strip_outer_element_tag:
                    self.qry = f" {self.qry} {self.attr.strip_outer_element_tag} = {self.attr.strip_outer_element} "
                if prop == gv._disable_snowflake_data_tag:
                    self.qry = f" {self.qry} {self.attr.disable_snowflake_data_tag} = {self.attr.disable_snowflake_data} "
                if prop == gv._disable_auto_convert_tag:
                    self.qry = f" {self.qry} {self.attr.disable_auto_convert_tag} = {self.attr.disable_auto_convert} "
        
    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_qry()
        self.add_properties_to_query()

    def create_file_format(self):
        self.session.sql(self.qry).collect()

    def grant_default_privileges(self):
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges[self.__class__.__name__.upper()]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = self.__class__.__name__.upper(),object_identifier=self.qualified_name,role = role)


    def create_object(self,**kwargs):

        self.set_database(kwargs[gv._database_tag])
        self.set_schema(kwargs[gv._schema_tag])

        self.set_name(kwargs[gv._name_tag])
        self.set_name_tag(gv._name_tag)

        self.set_type(kwargs[gv._type_tag])
        self.set_type_tag(gv._type_tag)

        self.set_parse_header(kwargs[gv._parse_header_tag])
        self.set_parse_header_tag(gv._parse_header_tag)

        self.set_skip_header(kwargs[gv._skip_header_tag])
        self.set_skip_header_tag(gv._skip_header_tag)

        self.set_skip_blank_lines(kwargs[gv._skip_blank_lines_tag])
        self.set_skip_blank_lines_tag(gv._skip_blank_lines_tag)

        self.set_date_format(kwargs[gv._date_format_tag])
        self.set_date_format_tag(gv._date_format_tag)

        self.set_time_format(kwargs[gv._time_format_tag])
        self.set_time_format_tag(gv._time_format_tag)

        self.set_timestamp_format(kwargs[gv._timestamp_format_tag])
        self.set_timestamp_format_tag(gv._timestamp_format_tag)

        self.set_binary_format(kwargs[gv._binary_format_tag])
        self.set_binary_format_tag(gv._binary_format_tag)

        self.set_escape(kwargs[gv._escape_tag])
        self.set_escape_tag(gv._escape_tag)

        self.set_escape_unenclosed_field(kwargs[gv._escape_unenclosed_field_tag])
        self.set_escape_unenclosed_field_tag(gv._escape_unenclosed_field_tag)

        self.set_trim_space(kwargs[gv._trim_space_tag])
        self.set_trim_space_tag(gv._trim_space_tag)

        self.set_field_optionally_enclosed_by(kwargs[gv._field_optionally_enclosed_by_tag])
        self.set_field_optionally_enclosed_by_tag(gv._field_optionally_enclosed_by_tag)

        self.set_null_if(kwargs[gv._null_if_tag])
        self.set_null_if_tag(gv._null_if_tag)

        self.set_error_on_column_count_mismatch(kwargs[gv._error_on_column_count_mismatch_tag])
        self.set_error_on_column_count_mismatch_tag(gv._error_on_column_count_mismatch_tag)

        self.set_replace_invalid_characters(kwargs[gv._replace_invalid_characters_tag])
        self.set_replace_invalid_characters_tag(gv._replace_invalid_characters_tag)

        self.set_empty_field_as_null(kwargs[gv._empty_field_as_null_tag])
        self.set_empty_field_as_null_tag(gv._empty_field_as_null_tag)

        self.set_skip_byte_order_mark(kwargs[gv._skip_byte_order_mark_tag])
        self.set_skip_byte_order_mark_tag(gv._skip_byte_order_mark_tag)

        self.set_encoding(kwargs[gv._encoding_tag])
        self.set_encoding_tag(gv._encoding_tag)

        self.set_enable_octal(kwargs[gv._enable_octal_tag])
        self.set_enable_octal_tag(gv._enable_octal_tag)

        self.set_allow_duplicate(kwargs[gv._allow_duplicate_tag])
        self.set_allow_duplicate_tag(gv._allow_duplicate_tag)

        self.set_strip_outer_array(kwargs[gv._strip_outer_array_tag])
        self.set_strip_outer_array_tag(gv._strip_outer_array_tag)

        self.set_strip_null_values(kwargs[gv._strip_null_values_tag])
        self.set_strip_null_values_tag(gv._strip_null_values_tag)

        self.set_ignore_utf8_errors(kwargs[gv._ignore_utf8_errors_tag])
        self.set_ignore_utf8_errors_tag(gv._ignore_utf8_errors_tag)

        self.set_snappy_compression(kwargs[gv._snappy_compression_tag])
        self.set_snappy_compression_tag(gv._snappy_compression_tag)

        self.set_binary_as_text(kwargs[gv._binary_as_text_tag])
        self.set_binary_as_text_tag(gv._binary_as_text_tag)

        self.set_use_logical_type(kwargs[gv._use_logical_type_tag])
        self.set_use_logical_type_tag(gv._use_logical_type_tag)

        self.set_use_vectorized_scanner(kwargs[gv._use_vectorized_scanner_tag])
        self.set_use_vectorized_scanner_tag(gv._use_vectorized_scanner_tag)

        self.set_preserve_space(kwargs[gv._preserve_space_tag])
        self.set_preserve_space_tag(gv._preserve_space_tag)

        self.set_strip_outer_element(kwargs[gv._strip_outer_element_tag])
        self.set_strip_outer_element_tag(gv._strip_outer_element_tag)

        self.set_disable_snowflake_data(kwargs[gv._disable_snowflake_data_tag])
        self.set_disable_snowflake_data_tag(gv._disable_snowflake_data_tag)

        self.set_disable_auto_convert(kwargs[gv._disable_auto_convert_tag])
        self.set_disable_auto_convert_tag(gv._disable_auto_convert_tag)
        self.set_qualified_name()
        self.prepare_query()
        self.create_file_format()
        self.grant_default_privileges()
        self.create_deployment_entry()



    def create_deployment_entry(self):
        deploy_inst = Deploy(self.session)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database(self.attr.database)
        deploy_inst.set_object_schema(self.attr.schema)
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()



