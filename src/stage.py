import stagevars as SV

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        instance._name = value

    def __del__(self,instance):
        del instance._name

class NameLabel:
    def __get__(self,instance,owner):
        return instance._name_label
    
    def __set__(self,instance,value):
        instance._name_label = value

    def __del__(self,instance):
        del instance._name_label

class Type:
    def __get__(self,instance,owner):
        return instance._type
    
    def __set__(self,instance,value):
        instance._type = value

    def __del__(self,instance):
        del instance._type

class TypeLabel:
    def __get__(self,instance,owner):
        return instance._type_label
    
    def __set__(self,instance,value):
        instance._type_label = value

    def __del__(self,instance):
        del instance._type_label

class FileFormat:   
    def __get__(self,instance,owner):
        return instance._file_format
    
    def __set__(self,instance,value):
        instance._file_format = value

    def __del__(self,instance):
        del instance._file_format


class FileFormatLabel:   
    def __get__(self,instance,owner):
        return instance._file_format_label
    
    def __set__(self,instance,value):
        instance._file_format_label = value

    def __del__(self,instance):
        del instance._file_format_label

class FileType:
    def __get__(self,instance,owner):
        return instance._file_type
    
    def __set__(self,instance,value):
        if value not in SV._allowed_values_file_type:
            raise TypeError
        else:
            instance._file_type = value


    def __del__(self,instance):
        del instance._file_type

class FileTypeLabel:
    def __get__(self,instance,owner):
        return instance._file_type_label
    
    def __set__(self,instance,value):
        instance._file_type_label = value

    def __del__(self,instance):
        del instance._file_type_label

class Compression:
    def __get__(self,instance,owner):
        return instance._compression
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_vlaues_file_type[0]: #CSV
            if value not in SV._allowed_values_compression_for_csv:
                raise KeyError
            else:
                instance._compression = value
        elif instance._file_type == SV._allowed_vlaues_file_type[1]: #JSON
            if value not in SV._allowed_values_compression_for_json:
                raise KeyError
            else:
                instance._compression = value
        elif instance._file_type == SV._allowed_vlaues_file_type[2]: #AVRO
            if value not in SV._allowed_values_compression_for_avro:
                raise KeyError
            else:
                instance._compression = value
        elif instance._file_type == SV._allowed_vlaues_file_type[3]: #ORC
            raise KeyError('Parameternot allowed')
        elif instance._file_type == SV._allowed_vlaues_file_type[4]: #PARQUET
            if value not in SV._allowed_values_compression_for_parquet:
                raise KeyError
            else:
                instance._compression = value
        elif instance._file_type == SV._allowed_vlaues_file_type[5]: #XML
            if value not in SV._allowed_values_compression_for_xml:
                raise KeyError
            else:
                instance._compression = value
        


    def __del__(self,instance):
        del instance._compression

class CompressionLabel:
    def __get__(self,instance,owner):
        return instance._compression_label
    
    def __set__(self,instance,value):
        instance._compression_label = value

    def __del__(self,instance):
        del instance._compression_label

class RecordDelimiter:
    def __get__(self,instance,owner):
        return instance._record_delimiter
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_vlaues_file_type[0]:
            if type(value) != str:
                raise TypeError
            elif len(value) > 20:
                raise TypeError
            else:
                instance._record_delimiter = value
        else:
            raise 'Cant set for other file types'

    def __del__(self,instance):
        del instance._record_delimiter

class RecordDelimiterLabel:
    def __get__(self,instance,owner):
        return instance._record_delimiter_label
    
    def __set__(self,instance,value):
        instance._record_delimiter_label = value

    def __del__(self,instance):
        del instance._record_delimiter_label

class FieldDelimiter:
    def __get__(self,instance,owner):
        return instance._field_delimiter
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0]:
            if type(value) != str:
                raise ValueError
            elif len(value) > 20:
                raise KeyError
            else:
                instance._field_delimiter = value
        else:
            raise "cant set for other file types"

    def __del__(self,instance):
        del instance._field_delimiter

class FieldDelimiterLabel:
    def __get__(self,instance,owner):
        return instance._field_delimiter_label
    
    def __set__(self,instance,value):
        instance._field_delimiter_label = value

    def __del__(self,instance):
        del instance._field_delimiter_label

class FileExtension:
    def __get__(self,instance,owner):
        return instance._file_extension
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0]:
            if type(value) != str:
                raise KeyError
            else:
                instance._file_extension = value
        else:
            raise "CANT SET FOR OTHERS"

    def __del__(self,instance):
        del instance._file_extension    

class FileExtensionLabel:
    def __get__(self,instance,owner):
        return instance._file_extension_label
    
    def __set__(self,instance,value):
        instance._file_extension_label = value

    def __del__(self,instance):
        del instance._file_extension_label    

class ParseHeader:
    def __get__(self,instance,owner):
        return instance._parse_header
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0]:
            if value not in SV._allowed_values_boolean:
                raise KeyError
            else:
                instance._parse_header = value
        else:
            raise "CANT SET FOR OTHERS"

    def __del__(self,instance):
        del instance._parse_header

class ParseHeaderLabel:
    def __get__(self,instance,owner):
        return instance._parse_header_label
    
    def __set__(self,instance,value):
        instance._parse_header_label = value

    def __del__(self,instance):
        del instance._parse_header_label

class SkipHeader:
    def __get__(self,instance,owner):
        return instance._skip_header
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0]:
            instance._skip_header = value
        else:
            raise "Cant set for others"

    def __del__(self,instance):
        del instance._skip_header

class SkipHeaderLabel:
    def __get__(self,instance,owner):
        return instance._skip_header_label
    
    def __set__(self,instance,value):
        instance._skip_header_label = value

    def __del__(self,instance):
        del instance._skip_header_label


class SkipBlankLines:
    def __get__(self,instance,owner):
        return instance._skip_blank_lines
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0]:
            if value not in SV._allowed_values_boolean:
                raise KeyError
            else:
                instance._skip_blank_lines = value
        else:
            raise "CANT SET FOR OTHERS"

    def __del__(self,instance):
        del instance._skip_blank_lines

class SkipBlankLinesLabel:
    def __get__(self,instance,owner):
        return instance._skip_blank_lines_label
    
    def __set__(self,instance,value):
        instance._skip_blank_lines_label = value

    def __del__(self,instance):
        del instance._skip_blank_lines_label

class DateFormat:
    def __get__(self,instance,owner):
        return instance._date_format
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0] or instance._file_type == SV._allowed_values_file_type[1]:
            if type(value) != str:
                raise KeyError
            else:
                instance._date_format = value
        else:
            raise "CANT SET FOR OTHERS"

    def __del__(self,instance):
        del instance._date_format

class DateFormatLabel:
    def __get__(self,instance,owner):
        return instance._date_format_label
    
    def __set__(self,instance,value):
        instance._date_format_label = value

    def __del__(self,instance):
        del instance._date_format_label

class TimeFormat:
    def __get__(self,instance,owner):
        return instance._time_format
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0] or instance._file_type == SV._allowed_values_file_type[1]:
            if type(value) != str:
                raise KeyError
            else:
                instance._time_format = value
        else:
            raise "CANT SET FOR OTHERS"

    def __del__(self,instance):
        del instance._time_format

class TimeFormatLabel:
    def __get__(self,instance,owner):
        return instance._time_format_label
    
    def __set__(self,instance,value):
        instance._time_format_label = value

    def __del__(self,instance):
        del instance._time_format_label

class TimestampFormat:
    def __get__(self,instance,owner):
        return instance._time_stamp_format
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0] or instance._file_type == SV._allowed_values_file_type[1]:
            instance._time_stamp_format = value
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._time_stamp_format

class TimestampFormatLabel:
    def __get__(self,instance,owner):
        return instance._time_stamp_format_label
    
    def __set__(self,instance,value):
        instance._time_stamp_format_label = value

    def __del__(self,instance):
        del instance._time_stamp_format_label
   
class BinaryFormat:
    def __get__(self,instance,owner):
        return instance._binary_format
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0] or instance._file_type == SV._allowed_values_file_type[1]:
            if value not in SV._allowed_values_binary_format:
                raise KeyError
            else:
                instance._binary_format = value
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._binary_format

class BinaryFormatLabel:
    def __get__(self,instance,owner):
        return instance._binary_format_label
    
    def __set__(self,instance,value):
        instance._binary_format_label = value

    def __del__(self,instance):
        del instance._binary_format_label

class Escape:
    def __get__(self,instance,owner):
        return instance._escape
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0]: #CSV
            if type(value) != chr:
                raise KeyError
            else:
                instance._escape = value
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._escape


class EscapeLabel:
    def __get__(self,instance,owner):
        return instance._escape_label
    
    def __set__(self,instance,value):
        instance._escape_label = value

    def __del__(self,instance):
        del instance._escape_label

class EscapeUnenclosedField:
    def __get__(self,instance,owner):
        return instance._escape_unenclosed_field
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0]: #CSV
            if type(value) != chr:
                raise KeyError
            else:
                instance._escape_unenclosed_field = value
        else:
            raise "CANT SET"
        
    def __del__(self,instance):
        del instance._escape_unenclosed_field

class EscapeUnenclosedFieldLabel:
    def __get__(self,instance,owner):
        return instance._escape_unenclosed_field_label
    
    def __set__(self,instance,value):
        instance._escape_unenclosed_field_label = value

    def __del__(self,instance):
        del instance._escape_unenclosed_field_label

class TrimSpace:
    def __get__(self,instance,owner):
        return instance._trim_space
    
    def __set__(self,instance,value):
        if (instance._file_type == SV._allowed_values_file_type[0] or
            instance._file_type == SV._allowed_values_file_type[1] or
            instance._file_type == SV._allowed_values_file_type[2] or
            instance._file_type == SV._allowed_values_file_type[3] or
            instance._file_type == SV._allowed_values_file_type[4] ):
            if value not in SV._allowed_values_boolean:
                raise KeyError
            else:
                instance._trim_space = value
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._trim_space

class TrimSpaceLabel:
    def __get__(self,instance,owner):
        return instance._trim_space_label
    
    def __set__(self,instance,value):
        instance._trim_space_label = value

    def __del__(self,instance):
        del instance._trim_space_label

class FieldOptionallyEnclosedBy:
    def __get__(self,instance,owner):
        return instance._field_optionally_enclosed_by
    
    def __set__(self,instance,value):
        if type(value) != chr:
            raise KeyError
        else:
            instance._field_optionally_enclosed_by = value

    def __del__(self,instance):
        del instance._field_optionally_enclosed_by

class FieldOptionallyEnclosedByLabel:
    def __get__(self,instance,owner):
        return instance._field_optionally_enclosed_by_label
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0]:
            instance._field_optionally_enclosed_by_label = value
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._field_optionally_enclosed_by_label

class NullIf:
    def __get__(self,instance,owner):
        return instance._null_if
    
    def __set__(self,instance,value):
        if (instance._file_type == SV._allowed_values_file_type[0] or
            instance._file_type == SV._allowed_values_file_type[1] or
            instance._file_type == SV._allowed_values_file_type[2] or
            instance._file_type == SV._allowed_values_file_type[3] or
            instance._file_type == SV._allowed_values_file_type[4]):
            if type(value) != str:
                raise KeyError
            else:
                instance._null_if = value
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._null_if

class NullIfLabel:
    def __get__(self,instance,owner):
        return instance._null_if_label
    
    def __set__(self,instance,value):
        instance._null_if_label = value

    def __del__(self,instance):
        del instance._null_if_label

class ErrorOnColumnCountMismatch:
    def __get__(self,instance,owner):
        return instance._error_on_column_count_mismatch
    
    def __set__(self,instance,value):
        if value not in SV._allowed_values_boolean:
            raise KeyError
        else:
            instance._error_on_column_count_mismatch = value

    def __del__(self,instance):
        del instance._error_on_column_count_mismatch

class ErrorOnColumnCountMismatchLabel:
    def __get__(self,instance,owner):
        return instance._error_on_column_count_mismatch_label
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0]:
            instance._error_on_column_count_mismatch_label = value
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._error_on_column_count_mismatch_label

class ReplaceInvalidCharacters:
    def __get__(self,instance,owner):
        return instance._replace_invalid_characters
    
    def __set__(self,instance,value):
        if value not in SV._allowed_values_boolean:
            raise KeyError
        else:
            instance._replace_invalid_characters = value

    def __del__(self,instance):
        del instance._replace_invalid_characters

class ReplaceInvalidCharactersLabel:
    def __get__(self,instance,owner):
        return instance._replace_invalid_characters_label
    
    def __set__(self,instance,value):
        instance._replace_invalid_characters_label = value

    def __del__(self,instance):
        del instance._replace_invalid_characters_label

class EmptyFieldAsNull:
    def __get__(self,instance,owner):
        return instance._empty_field_as_null
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0]:
            if value not in SV._allowed_values_boolean:
                raise KeyError
            else:
                instance._empty_field_as_null = value

    def __del__(self,instance):
        del instance._empty_field_as_null

class EmptyFieldAsNullLabel:
    def __get__(self,instance,owner):
        return instance._empty_field_as_null_label
    
    def __set__(self,instance,value):
        instance._empty_field_as_null_label = value

    def __del__(self,instance):
        del instance._empty_field_as_null_label

class SkipByteOrderMark:
    def __get__(self,instance,owner):
        return instance._skip_byte_order_mark
    
    def __set__(self,instance,value):
        if (instance._file_type == SV._allowed_values_file_type[0] or
            instance._file_type == SV._allowed_values_file_type[1] or 
            instance._file_type == SV._allowed_values_file_type[5] ):
            if value not in SV._allowed_values_boolean:
                raise KeyError
            else:
                instance._skip_byte_order_mark = value
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._skip_byte_order_mark

class SkipByteOrderMarkLabel:
    def __get__(self,instance,owner):
        return instance._skip_byte_order_mark_label
    
    def __set__(self,instance,value):
        instance._skip_byte_order_mark_label = value

    def __del__(self,instance):
        del instance._skip_byte_order_mark_label

class Encoding:
    def __get__(self,instance,owner):
        return instance._encoding
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[0]:
            if type(value) != str:
                raise TypeError
            else:
                instance._encoding = value

    def __del__(self,instance):
        del instance._encoding

class EncodingLabel:
    def __get__(self,instance,owner):
        return instance._encoding_label
    
    def __set__(self,instance,value):
        instance._encoding_label = value

    def __del__(self,instance):
        del instance._encoding_label

class EnableOctal:
    def __get__(self,instance,owner):
        return instance._enable_octal
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[1]:
            if value in SV._allowed_values_boolean:
                instance._enable_octal = value
            else:
                raise TypeError
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._enable_octal    

class EnableOctalLabel:
    def __get__(self,instance,owner):
        return instance._enable_octal_label
    
    def __set__(self,instance,value):
        instance._enable_octal_label = value

    def __del__(self,instance):
        del instance._enable_octal_label

class AllowDuplicate:
    def __get__(self,instance,owner):
        return instance._allow_duplicate
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[1]:
            if value in SV._allowed_values_boolean:
                instance._allow_duplicate = value
            else:
                raise TypeError
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._allow_duplicate

class AllowDuplicateLabel:
    def __get__(self,instance,owner):
        return instance._allow_duplicate_label
    
    def __set__(self,instance,value):
        instance._allow_duplicate_label = value

    def __del__(self,instance):
        del instance._allow_duplicate_label

class StripOuterArray:
    def __get__(self,instance,owner):
        return instance._strip_outer_array
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[1]: #JSON
            if value in SV._allowed_values_boolean:
                instance._strip_outer_array = value
            else:
                raise TypeError
        else:
            raise "CANT SET"
        
    def __del__(self,instance):
        del instance._strip_outer_array

class StripOuterArrayLabel:
    def __get__(self,instance,owner):
        return instance._strip_outer_array_label
    
    def __set__(self,instance,value):
        instance._strip_outer_array_label = value

    def __del__(self,instance):
        del instance._strip_outer_array_label

class StripNullValues:
    def __get__(self,instance,owner):
        return instance._strip_null_values
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[1]: #JSON
            if value in SV._allowed_values_boolean:
                instance._strip_null_values = value
            else:
                raise ValueError
        else:
            raise "CANT SET"
        
    def __del__(self,instance):
        del instance._strip_null_values

class StripNullValuesLabel:
    def __get__(self,instance,owner):
        return instance._strip_null_values_label
    
    def __set__(self,instance,value):
        instance._strip_null_values_label = value

    def __del__(self,instance):
        del instance._strip_null_values_label

class IgnoreUTF8Errors:
    def __get__(self,instance,owner):
        return instance._ignore_utf8_errors
    
    def __set__(self,instance,value):
        if (instance._file_type == SV._allowed_values_file_type[1] or
            instance._file_type == SV._allowed_values_file_type[5]): #JSON and XML
            if value in SV._allowed_values_boolean:
                instance._ignore_utf8_errors = value
            else:
                raise TypeError
        else:
            raise "CANT SET"
        
    def __del__(self,instance):
        del instance._ignore_utf8_errors

class IgnoreUTF8ErrorsLabel:
    def __get__(self,instance,owner):
        return instance._ignore_utf8_errors_label
    
    def __set__(self,instance,value):
        instance._ignore_utf8_errors_label = value

    def __del__(self,instance):
        del instance._ignore_utf8_errors_label


class SnappyCompression:
    def __get__(self,instance,owner):
        return instance._snappy_compression
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[4]: #PARQUET
            if value in SV._allowed_values_boolean:
                instance._snappy_compression = value
            else:
                raise TypeError
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._snappy_compression

class SnappyCompressionLabel:
    def __get__(self,instance,owner):
        return instance._snappy_compression_label
    
    def __set__(self,instance,value):
        instance._snappy_compression_label = value

    def __del__(self,instance):
        del instance._snappy_compression_label
        
class BinaryAsText:
    def __get__(self,instance,owner):
        return instance._binary_as_text
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[4]: #PARQUET
            if value in SV._allowed_values_boolean:
                instance._binary_as_text = value
            else:
                raise TypeError
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._binary_as_text

class BinaryAsTextLabel:
    def __get__(self,instance,owner):
        return instance._binary_as_text_label
    
    def __set__(self,instance,value):
        instance._binary_as_text_label = value

    def __del__(self,instance):
        del instance._binary_as_text_label

class UseLogicalType:
    def __get__(self,instance,owner):
        return instance._use_logical_type
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[4]: #PARQUET
            if value in SV._allowed_values_boolean:
                instance._use_logical_type = value
            else:
                raise TypeError
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._use_logical_type

class UseLogicalTypeLabel:
    def __get__(self,instance,owner):
        return instance._use_logical_type_label
    
    def __set__(self,instance,value):
        instance._use_logical_type_label = value

    def __del__(self,instance):
        del instance._use_logical_type_label

class PreserveSpace:
    def __get__(self,instance,owner):
        return instance._preserve_space
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[5]: #XML
            if value in SV._allowed_values_boolean:
                instance._preserve_space = value
            else:
                raise TypeError
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._preserve_space

class PreserveSpaceLabel:
    def __get__(self,instance,owner):
        return instance._preserve_space_label
    
    def __set__(self,instance,value):
        instance._preserve_space_label = value

    def __del__(self,instance):
        del instance._preserve_space_label

class StripOuterElement:
    def __get__(self,instance,owner):
        return instance._strip_outer_element
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[5]: #XML
            if value in SV._allowed_values_boolean:
                instance._strip_outer_element = value
            else:
                raise TypeError
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._strip_outer_element

class StripOuterElementLabel:
    def __get__(self,instance,owner):
        return instance._strip_outer_element_label
    
    def __set__(self,instance,value):
        instance._strip_outer_element_label = value

    def __del__(self,instance):
        del instance._strip_outer_element_label

class DisableSnowflakeData:
    def __get__(self,instance,owner):
        return instance._disable_snowflake_data
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[5]: #XML
            if value in SV._allowed_values_boolean:
                instance._disable_snowflake_data = value
            else:
                raise TypeError
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._disable_snowflake_data

class DisableSnowflakeDataLabel:
    def __get__(self,instance,owner):
        return instance._disable_snowflake_data_label
    
    def __set__(self,instance,value):
        instance._disable_snowflake_data_label = value

    def __del__(self,instance):
        del instance._disable_snowflake_data_label

class DisableAutoConvert:
    def __get__(self,instance,owner):
        return instance._disable_auto_convert
    
    def __set__(self,instance,value):
        if instance._file_type == SV._allowed_values_file_type[5]: #XML
            if value in SV._allowed_values_boolean:
                instance._disable_auto_convert = value
            else:
                raise TypeError
        else:
            raise "CANT SET"

    def __del__(self,instance):
        del instance._disable_auto_convert


class DisableAutoConvertLabel:
    def __get__(self,instance,owner):
        return instance._disable_auto_convert_label
    
    def __set__(self,instance,value):
        instance._disable_auto_convert_label = value

    def __del__(self,instance):
        del instance._disable_auto_convert_label
    

class StageAttrs:
    name = Name()
    name_label = NameLabel()
    type = Type()
    type_label = TypeLabel()
    file_format = FileFormat()
    file_format_label = FileFormatLabel()
    file_type = FileType()
    file_type_label = FileTypeLabel()
    compression = Compression()
    compression_label = CompressionLabel()
    record_delimiter = RecordDelimiter()
    record_delimiter_label = RecordDelimiterLabel()
    field_delimiter = FieldDelimiter()
    field_delimiter_label = FieldDelimiterLabel()
    file_extension = FileExtension()
    file_extension_label = FileExtensionLabel()
    parse_header = ParseHeader()
    parse_header_label = ParseHeaderLabel()
    skip_header = SkipHeader()
    skip_header_label = SkipHeaderLabel()
    skip_blank_line = SkipBlankLines()
    skip_blank_line_label = SkipBlankLinesLabel()
    date_format = DateFormat()
    date_format_label = DateFormatLabel()
    time_format = TimeFormat()
    time_format_label = TimeFormatLabel()
    timestamp_format = TimestampFormat()
    timestamp_format_label = TimestampFormatLabel()
    binary_format = BinaryFormat()
    binary_format_label = BinaryFormatLabel()
    escape = Escape()
    escape_label = EscapeLabel()
    escape_unenclosed_field = EscapeUnenclosedField()
    escape_unenclosed_field_label = EscapeUnenclosedFieldLabel()
    trim_space = TrimSpace()
    trim_space_label = TrimSpaceLabel()
    field_optionally_enclosed_by = FieldOptionallyEnclosedBy()
    field_optionally_enclosed_by_label = FieldOptionallyEnclosedByLabel()
    null_if = NullIf()
    null_if_label = NullIfLabel()
    error_on_column_count_mismatch = ErrorOnColumnCountMismatch()
    error_on_column_count_mismatch_label = ErrorOnColumnCountMismatchLabel()
    replace_invalid_characters = ReplaceInvalidCharacters()
    replace_invalid_characters_label = ReplaceInvalidCharactersLabel()
    empty_field_as_null = EmptyFieldAsNull()
    empty_field_as_null_label = EmptyFieldAsNullLabel()
    skip_byte_order_mark = SkipByteOrderMark()
    skip_byte_order_mark_label = SkipByteOrderMarkLabel()
    encoding = Encoding()
    encoding_label = EncodingLabel()
    enable_octal = EnableOctal()
    enable_octal_label = EnableOctalLabel()
    allow_duplicate = AllowDuplicate()
    allow_duplicate_label = AllowDuplicateLabel()
    strip_outer_array = StripOuterArray()
    strip_outer_array_label = StripOuterArrayLabel()
    strip_null_values = StripNullValues()
    strip_null_values_label = StripNullValuesLabel()
    ignore_utf8_errors = IgnoreUTF8Errors()
    ignore_utf8_errors_label = IgnoreUTF8ErrorsLabel()
    snappy_compression = SnappyCompression()
    snappy_compression_label = SnappyCompressionLabel()
    binary_as_text = BinaryAsText()
    binary_as_text_label = BinaryAsTextLabel()
    use_logical_type = UseLogicalType()
    use_logical_type_label = UseLogicalTypeLabel()
    preserve_space = PreserveSpace()
    preserve_space_label = PreserveSpaceLabel()
    strip_outer_element = StripOuterElement()
    strip_outer_element_label = StripOuterElementLabel()
    disable_snowflake_data = DisableSnowflakeData()
    disable_snowflake_data_label = DisableSnowflakeDataLabel()
    disable_auto_convert = DisableAutoConvert()
    disable_auto_convert_label = DisableAutoConvertLabel()


class Stage:
    def __init__(self,session):
        self.attr = StageAttrs()
        self.session = session
        self.qry = ""

    def set_name(self,name):
        self.attr.name = name
    
    def set_name_label(self):
        self.attr.name_label = SV._name_label

    def set_type(self,type):
        self.attr.type = type
    
    def set_type_label(self):
        self.attr.type_label = SV._type_label

    def set_file_format(self,file_format):
        self.attr.file_format = file_format
    
    def set_file_format_label(self):
        self.attr.file_format_label = SV._file_format_label
    
    def set_file_type(self,file_type):
        self.attr.file_type = file_type
    
    def set_file_type_label(self):
        self.attr.file_type_label = SV._file_type_label

    def set_compression(self,compression):
        self.attr.compression = compression
    
    def set_compression_label(self):
        self.attr.compression_label = SV._compression_label

    def set_record_delimiter(self):
        self.attr.record_delimiter = record_delimiter
    
    def set_record_delimiter_label(self,record_delimiter_label):
        self.attr.record_delimiter_label = SV._record_delimiter_label

    def set_field_delimiter(self,field_delimiter):
        self.attr.field_delimiter = field_delimiter
    
    def set_field_delimiter_label(self,field_delimiter_label):
        self.attr.field_delimiter_label = SV._field_delimiter_label

    def set_file_extension(self,file_extension):
        self.attr.file_extension = file_extension
    
    def set_file_extension_label(self,file_extension_label):
        self.attr.file_extension_label = SV._file_extension_label

    def set_parse_header(self,parse_header):
        self.attr.parse_header = parse_header
    
    def set_parse_header_label(self,parse_header_label):
        self.attr.parse_header_label = SV._parse_header_label

    def set_skip_header(self,skip_header):
        self.attr.skip_header = skip_header
    
    def set_skip_header_label(self,skip_header_label):
        self.attr.skip_header_label = SV._skip_header_label

    def set_skip_blank_line(self,skip_blank_line):
        self.attr.skip_blank_line = skip_blank_line
    
    def set_skip_blank_line_label(self,skip_blank_line_label):
        self.attr.skip_blank_line_label = SV._skip_blank_line_label

    def set_date_format(self,date_format):
        self.attr.date_format = date_format
    
    def set_date_format_label(self,date_format_label):
        self.attr.date_format_label = SV._date_format_label

    def set_time_format(self,time_format):
        self.attr.time_format = time_format
    
    def set_time_format_label(self,time_format_label):
        self.attr.time_format_label = SV._time_format_label

    def set_timestamp_format(self,timestamp_format):
        self.attr.timestamp_format = timestamp_format
    
    def set_timestamp_format_label(self):
        self.attr.timestamp_format_label = SV._timestamp_format_label

    def set_binary_format(self,binary_format):
        self.attr.binary_format = binary_format
    
    def set_binary_format_label(self):
        self.attr.binary_format_label = SV._binary_format_label

        



