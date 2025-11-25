import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.gvobject import Config as cfg, Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from vars.obj.fileformat.gvfileformat import FileFormatTag as tags
from dep.deploy import Deploy
from validation.validateobject import ValidateObject as vo
from setup import privilege
from .baseobj import BaseObject 
from dep import deploy
from src.usr.user import ChatHistory



class Name:   
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)
    
    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        database_name=instance.parent.attr.database
        schema_name=instance.parent.attr.schema
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_file_format(session=instance.parent.session,database_name=database_name,schema_name=schema_name,file_format_name=name)
            if ( vv.starts_with_alphabet(name,instance.parent.__class__.__name__,self.__class__.__name__) 
                and not vv.has_space(name,instance.parent.__class__.__name__,self.__class__.__name__)
                and not vv.has_special_characters_except_underscore(name,instance.parent.__class__.__name__,self.__class__.__name__)
                ):
                instance._name = name
                instance._rename_to="NONE"
        else:
            instance.parent.logger.info(f" for alter operation")
            old_name=value["NAME"]
            instance.parent.logger.info(f"old name {old_name}")
            new_name=value.get("RENAME_TO","NONE")
            instance.parent.logger.info(f"new name {new_name}")
            if new_name!="NONE":
                instance.parent.logger.info(f" changing name from {old_name} to {new_name}")
                vv.required_attribute_check(old_name,instance.parent.__class__.__name__,self.__class__.__name__)
                vo.file_format_exist(session=instance.parent.session,database_name=instance.parent.attr.database,schema_name=instance.parent.attr.schema,file_format_name=old_name)
                vo.is_new_file_format(session=instance.parent.session,database_name=instance.parent.attr.database,schema_name=instance.parent.attr.schema,file_format_name=new_name)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"


    def __del__(self,instance):
        del instance._name
        del instance._rename_to


class Type:
    def __get__(self,instance,owner):
        return instance._type
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._type=value
        else:
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.TYPE),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._type = value

    def __del__(self,instance):
        del instance._type

class Compression:
    def __get__(self,instance,owner):
        return instance._compression
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._compression=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]: #CSV
            vv.is_allowed_value( value=value
                                ,allowed_list=tags.allowed_value_list().get(tags.COMPRESSION)[tags.allowed_value_list().get(tags.TYPE)[0]]
                                ,object_type=instance.parent.__class__.__name__
                                ,attr_name=self.__class__.__name__)
            instance._compression=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.is_allowed_value(value=value
                                ,allowed_list=tags.allowed_value_list().get(tags.COMPRESSION)[tags.allowed_value_list().get(tags.TYPE)[1]]
                                ,object_type=instance.parent.__class__.__name__
                                ,attr_name=self.__class__.__name__)
            instance._compression=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.is_allowed_value(value=value
                                ,allowed_list=tags.allowed_value_list().get(tags.COMPRESSION)[tags.allowed_value_list().get(tags.TYPE)[2]]
                                ,object_type=instance.parent.__class__.__name__
                                ,attr_name=self.__class__.__name__)
            instance._compression=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__
                            ,attr_name=self.__class__.__name__
                            ,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.is_allowed_value(value=value
                                ,allowed_list=tags.allowed_value_list().get(tags.COMPRESSION)[tags.allowed_value_list().get(tags.TYPE)[4]]
                                ,object_type=instance.parent.__class__.__name__
                                ,attr_name=self.__class__.__name__)
            instance._compression=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.is_allowed_value(value=value
                                ,allowed_list=tags.allowed_value_list().get(tags.COMPRESSION)[tags.allowed_value_list().get(tags.TYPE)[5]]
                                ,object_type=instance.parent.__class__.__name__
                                ,attr_name=self.__class__.__name__)
            instance._compression=value

    def __del__(self,instance):
        del instance._compression

class RecordDelimiter:
    def __get__(self,instance,owner):
        return instance._record_delimiter
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._record_delimiter = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]:#CSV
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._record_delimiter=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._record_delimiter

class FieldDelimiter:
    def __get__(self,instance,owner):
        return instance._field_delimiter
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._field_delimiter=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]:#CSV
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._field_delimiter=f"'{value}'"
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._field_delimiter

class MultiLine:
    def __get__(self,instance,owner):
        return instance._multi_line
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._multi_line=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0] 
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]):#CSV & JSON
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._multi_line=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")


    def __del__(self,instance):
        del instance._multi_line  

class FileExtension:
    def __get__(self,instance,owner):
        return instance._file_extension
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._file_extension=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]):#CSV
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._file_extension=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._file_extension      

class ParseHeader:
    def __get__(self,instance,owner):
        return instance._parse_header
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._parse_header=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]:#CSV
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._parse_header=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._parse_header

class SkipHeader:
    def __get__(self,instance,owner):
        return instance._skip_header
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._skip_header = value  
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]:#CSV
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._skip_header=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._skip_header

class SkipBlankLines:
    def __get__(self,instance,owner):
        return instance._skip_blank_lines
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._skip_blank_lines=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]:#CSV
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._skip_header=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
       
    def __del__(self,instance):
        del instance._skip_blank_lines

class DateFormat:
    def __get__(self,instance,owner):
        return instance._date_format
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._date_format=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]):#CSV
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._date_format=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._date_format

class TimeFormat:
    def __get__(self,instance,owner):
        return instance._time_format
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._time_format=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]):#CSV
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._time_format=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._time_format

class TimestampFormat:
    def __get__(self,instance,owner):
        return instance._timestamp_format
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._timestamp_format=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]):#CSV
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._timestamp_format=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")


    def __del__(self,instance):
        del instance._timestamp_format
   
class BinaryFormat:
    def __get__(self,instance,owner):
        return instance._binary_format
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._binary_format=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]):#CSV
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.BINARY_FORMAT),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._binary_format=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._binary_format

class Escape:
    def __get__(self,instance,owner):
        return instance._escape
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._escape = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]: #CSV
            vv.is_single_byte_characetr(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._escape = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._escape

class EscapeUnenclosedField:
    def __get__(self,instance,owner):
        return instance._escape_unenclosed_field
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._escape_unenclosed_field = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]: #CSV
            vv.is_single_byte_characetr(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._escape_unenclosed_field = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        
    def __del__(self,instance):
        del instance._escape_unenclosed_field

class TrimSpace:
    def __get__(self,instance,owner):
        return instance._trim_space
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._trim_space=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[2]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[3]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[4]):
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._trim_space=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]:
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._trim_space

class FieldOptionallyEnclosedBy:
    def __get__(self,instance,owner):
        return instance._field_optionally_enclosed_by
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._field_optionally_enclosed_by = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]: #CSV
            #vv.is_single_byte_characetr(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._field_optionally_enclosed_by = 'NONE'
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")


    def __del__(self,instance):
        del instance._field_optionally_enclosed_by

class NullIf:
    def __get__(self,instance,owner):
        return instance._null_if
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._null_if=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0] or
            instance._type == tags.allowed_value_list().get(tags.TYPE)[1] or
            instance._type == tags.allowed_value_list().get(tags.TYPE)[2] or
            instance._type == tags.allowed_value_list().get(tags.TYPE)[3] or
            instance._type == tags.allowed_value_list().get(tags.TYPE)[4]):
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._null_if=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._null_if

class ErrorOnColumnCountMismatch:
    def __get__(self,instance,owner):
        return instance._error_on_column_count_mismatch
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._error_on_column_count_mismatch = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]: #CSV
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._error_on_column_count_mismatch = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
            

    def __del__(self,instance):
        del instance._error_on_column_count_mismatch

class ReplaceInvalidCharacters:
    def __get__(self,instance,owner):
        return instance._replace_invalid_characters
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._replace_invalid_characters = value
        else: 
            vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._replace_invalid_characters = value
            
    def __del__(self,instance):
        del instance._replace_invalid_characters

class EmptyFieldAsNull:
    def __get__(self,instance,owner):
        return instance._empty_field_as_null
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._empty_field_as_null = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]: #CSV
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._empty_field_as_null = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._empty_field_as_null

class SkipByteOrderMark:
    def __get__(self,instance,owner):
        return instance._skip_byte_order_mark
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._skip_byte_order_mark = value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0] or
            instance._type == tags.allowed_value_list().get(tags.TYPE)[1] or 
            instance._type == tags.allowed_value_list().get(tags.TYPE)[5] ):
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._skip_byte_order_mark=value
        else:
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._skip_byte_order_mark

class Encoding:
    def __get__(self,instance,owner):
        return instance._encoding
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._encoding = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]: #CSV
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.ENCODING),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._encoding = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")


    def __del__(self,instance):
        del instance._encoding

class EnableOctal:
    def __get__(self,instance,owner):
        return instance._enable_octal
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._enable_octal = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]: #CSV
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._enable_octal=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._enable_octal    

class AllowDuplicate:
    def __get__(self,instance,owner):
        return instance._allow_duplicate
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._allow_duplicate = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]: #CSV
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._allow_duplicate=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")


    def __del__(self,instance):
        del instance._allow_duplicate


class StripOuterArray:
    def __get__(self,instance,owner):
        return instance._strip_outer_array
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._strip_outer_array = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]: #CSV
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._strip_outer_array=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

        
    def __del__(self,instance):
        del instance._strip_outer_array

class StripNullValues:
    def __get__(self,instance,owner):
        return instance._strip_null_values
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._strip_null_values = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[0]: #CSV
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[1]: #JSON
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._strip_null_values=value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[2]: #AVRO
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[3]: #ORC
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} Files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

        
    def __del__(self,instance):
        del instance._strip_null_values

class IgnoreUTF8Errors:
    def __get__(self,instance,owner):
        return instance._ignore_utf8_errors
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._ignore_utf8_errors = value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[1] or
            instance._type == tags.allowed_value_list().get(tags.TYPE)[5]) : #JSON and XML
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._ignore_utf8_errors=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[2]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[3]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[4]): #CSV
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        
    def __del__(self,instance):
        del instance._ignore_utf8_errors

class SnappyCompression:
    def __get__(self,instance,owner):
        return instance._snappy_compression
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._snappy_compression = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._snappy_compression=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[2]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[3]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[5]): #CSV
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")
        

    def __del__(self,instance):
        del instance._snappy_compression

        
class BinaryAsText:
    def __get__(self,instance,owner):
        return instance._binary_as_text
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._binary_as_text = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._binary_as_text=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[2]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[3]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[5]): #CSV
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")


    def __del__(self,instance):
        del instance._binary_as_text


class UseLogicalType:
    def __get__(self,instance,owner):
        return instance._use_logical_type
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._use_logical_type = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._use_logical_type=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[2]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[3]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[5]): #CSV
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._use_logical_type

class UseVectorizedScanner:
    def __get__(self,instance,owner):
        return instance._use_vectorized_scanner
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._use_vectorized_scanner = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[4]: #PARQUET
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._use_vectorized_scanner=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[2]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[3]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[5]): #CSV
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._use_vectorized_scanner

class PreserveSpace:
    def __get__(self,instance,owner):
        return instance._preserve_space
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._preserve_space = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._preserve_space=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[2]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[3]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[4]): 
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._preserve_space

class StripOuterElement:
    def __get__(self,instance,owner):
        return instance._strip_outer_element
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._strip_outer_element = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._strip_outer_element=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[2]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[3]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[4]): 
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._strip_outer_element

class DisableSnowflakeData:
    def __get__(self,instance,owner):
        return instance._disable_snowflake_data
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._disable_snowflake_data = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._disable_snowflake_data=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[2]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[3]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[4]): 
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._disable_snowflake_data

class DisableAutoConvert:
    def __get__(self,instance,owner):
        return instance._disable_auto_convert
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._disable_auto_convert = value
        elif instance._type == tags.allowed_value_list().get(tags.TYPE)[5]: #XML
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._disable_auto_convert=value
        elif (instance._type == tags.allowed_value_list().get(tags.TYPE)[0]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[1]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[2]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[3]
              or instance._type == tags.allowed_value_list().get(tags.TYPE)[4]): 
            vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=f" for {instance._type} files ")

    def __del__(self,instance):
        del instance._disable_auto_convert


class FileFormatAttrs:
    def __init__(self,parent):
        self.parent = parent

    type = Type()
    name = Name()
    compression = Compression()
    record_delimiter = RecordDelimiter()
    field_delimiter = FieldDelimiter()
    multi_line=MultiLine()
    file_extension = FileExtension()
    parse_header = ParseHeader()
    skip_header = SkipHeader()
    skip_blank_lines = SkipBlankLines()
    date_format = DateFormat()
    time_format = TimeFormat()
    timestamp_format = TimestampFormat()
    binary_format = BinaryFormat()
    escape = Escape()
    escape_unenclosed_field = EscapeUnenclosedField()
    trim_space = TrimSpace()
    field_optionally_enclosed_by = FieldOptionallyEnclosedBy()
    null_if = NullIf()
    error_on_column_count_mismatch = ErrorOnColumnCountMismatch()
    replace_invalid_characters = ReplaceInvalidCharacters()
    empty_field_as_null = EmptyFieldAsNull()
    skip_byte_order_mark = SkipByteOrderMark()
    encoding = Encoding()
    enable_octal = EnableOctal()
    allow_duplicate = AllowDuplicate()
    strip_outer_array = StripOuterArray()
    strip_null_values = StripNullValues()
    ignore_utf8_errors = IgnoreUTF8Errors()
    snappy_compression = SnappyCompression()
    binary_as_text = BinaryAsText()
    use_logical_type = UseLogicalType()
    use_vectorized_scanner = UseVectorizedScanner()
    preserve_space = PreserveSpace()
    strip_outer_element = StripOuterElement()
    disable_snowflake_data = DisableSnowflakeData()
    disable_auto_convert = DisableAutoConvert()

class FileFormat(BaseObject):
    def __init__(self, session, user_id, logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger,database_required=True,schema_required=True)
        self.attr = FileFormatAttrs(self)

    def set_name(self,val):
        self.attr.name = val

    def set_type(self,type):
        self.attr.type = type

    def set_compression(self,val):
        self.attr.compression = val
    
    def set_record_delimiter(self,val):
        self.attr.record_delimiter = val

    def set_field_delimiter(self,val):
        self.attr.field_delimiter = val
    
    def set_multi_line(self,val):
        self.attr.multi_line = val

    def set_file_extension(self,val):
        self.attr.file_extension = val

    def set_parse_header(self, val):
        self.attr.parse_header = val

    def set_skip_header(self, val):
        self.attr.skip_header = val

    def set_skip_blank_lines(self, val):
        self.attr.skip_blank_lines = val

    def set_date_format(self, val):
        self.attr.date_format = val

    def set_time_format(self, val):
        self.attr.time_format = val

    def set_timestamp_format(self, val):
        self.attr.timestamp_format = val

    def set_binary_format(self, val):
        self.attr.binary_format = val

    def set_escape(self,val):
        self.attr.escape = val

    def set_escape_unenclosed_field(self, val):
        self.attr.escape_unenclosed_field = val

    def set_trim_space(self, val):
        self.attr.trim_space = val

    def set_field_optionally_enclosed_by(self, val):
        self.attr.field_optionally_enclosed_by = val

    def set_null_if(self, val):
        self.attr.null_if = val

    def set_error_on_column_count_mismatch(self, val):
        self.attr.error_on_column_count_mismatch = val

    def set_replace_invalid_characters(self, val):
        self.attr.replace_invalid_characters = val

    def set_empty_field_as_null(self, val):
        self.attr.empty_field_as_null = val

    def set_skip_byte_order_mark(self, val):
        self.attr.skip_byte_order_mark = val

    def set_encoding(self, val):
        self.attr.encoding = val

    def set_enable_octal(self, val):
        self.attr.enable_octal = val

    def set_allow_duplicate(self, val):
        self.attr.allow_duplicate = val

    def set_strip_outer_array(self, val):
        self.attr.strip_outer_array = val

    def set_strip_null_values(self, val):
        self.attr.strip_null_values = val

    def set_ignore_utf8_errors(self, val):
        self.attr.ignore_utf8_errors = val

    def set_snappy_compression(self, val):
        self.attr.snappy_compression = val

    def set_binary_as_text(self, val):
        self.attr.binary_as_text = val

    def set_use_logical_type(self, val):
        self.attr.use_logical_type = val

    def set_use_vectorized_scanner(self, val):
        self.attr.use_vectorized_scanner = val

    def set_preserve_space(self, val):
        self.attr.preserve_space = val

    def set_strip_outer_element(self, val):
        self.attr.strip_outer_element = val

    def set_disable_snowflake_data(self, val):
        self.attr.disable_snowflake_data = val

    def set_disable_auto_convert(self, val):
        self.attr.disable_auto_convert = val

    def set_qualified_name(self):
        self.qualified_name = f"{self.attr.database}.{self.attr.schema}.{self.attr.name}"

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.TYPE,"_type")
        set_flag(tags.COMPRESSION,"_compression")
        set_flag(tags.RECORD_DELIMITER,"_record_delimiter")
        set_flag(tags.FIELD_DELIMITER,"_field_delimiter")
        set_flag(tags.MULTI_LINE,"_multi_line")
        set_flag(tags.FILE_EXTENSION,"_file_extension")
        set_flag(tags.PARSE_HEADER, "_parse_header")
        set_flag(tags.SKIP_HEADER, "_skip_header")
        set_flag(tags.SKIP_BLANK_LINES, "_skip_blank_lines")
        set_flag(tags.DATE_FORMAT, "_date_format")
        set_flag(tags.TIME_FORMAT, "_time_format")
        set_flag(tags.TIMESTAMP_FORMAT, "_timestamp_format")
        set_flag(tags.BINARY_FORMAT, "_binary_format")
        set_flag(tags.ESCAPE, "_escape")
        set_flag(tags.ESCAPE_UNENCLOSED_FIELD, "_escape_unenclosed_field")
        set_flag(tags.TRIM_SPACE, "_trim_space")
        set_flag(tags.FIELD_OPTIONALLY_ENCLOSED_BY, "_field_optionally_enclosed_by")
        set_flag(tags.NULL_IF, "_null_if")
        set_flag(tags.ERROR_ON_COLUMN_COUNT_MISMATCH, "_error_on_column_count_mismatch")
        set_flag(tags.REPLACE_INVALID_CHARACTERS, "_replace_invalid_characters")
        set_flag(tags.EMPTY_FIELD_AS_NULL, "_empty_field_as_null")
        set_flag(tags.SKIP_BYTE_ORDER_MARK, "_skip_byte_order_mark")
        set_flag(tags.ENCODING, "_encoding")
        set_flag(tags.ENABLE_OCTAL, "_enable_octal")
        set_flag(tags.ALLOW_DUPLICATE, "_allow_duplicate")
        set_flag(tags.STRIP_OUTER_ARRAY, "_strip_outer_array")
        set_flag(tags.STRIP_NULL_VALUES, "_strip_null_values")
        set_flag(tags.IGNORE_UTF8_ERRORS, "_ignore_utf8_errors")
        set_flag(tags.SNAPPY_COMPRESSION, "_snappy_compression")
        set_flag(tags.BINARY_AS_TEXT, "_binary_as_text")
        set_flag(tags.USE_LOGICAL_TYPE, "_use_logical_type")
        set_flag(tags.USE_VECTORIZED_SCANNER, "_use_vectorized_scanner")
        set_flag(tags.PRESERVE_SPACE, "_preserve_space")
        set_flag(tags.STRIP_OUTER_ELEMENT, "_strip_outer_element")
        set_flag(tags.DISABLE_SNOWFLAKE_DATA, "_disable_snowflake_data")
        set_flag(tags.DISABLE_AUTO_CONVERT, "_disable_auto_convert")
        set_flag(tags.COMMENT,"comment")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_qry(self):
        self.qry = f"CREATE OR REPLACE FILE FORMAT  {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.TYPE:
                    self.qry = f" {self.qry} {tags.TYPE} = {self.attr.type} "
                if prop == tags.COMPRESSION:
                    self.qry = f" {self.qry} {tags.COMPRESSION} = {self.attr.compression} "
                if prop == tags.RECORD_DELIMITER:
                    self.qry = f" {self.qry} {tags.RECORD_DELIMITER} = {self.attr.record_delimiter} "
                if prop == tags.FIELD_DELIMITER:
                    self.qry = f" {self.qry} {tags.FIELD_DELIMITER} = {self.attr.field_delimiter} "
                if prop == tags.MULTI_LINE:
                    self.qry = f" {self.qry} {tags.MULTI_LINE} = {self.attr.multi_line} "
                if prop == tags.FILE_EXTENSION:
                    self.qry = f" {self.qry} {tags.FILE_EXTENSION} = {self.attr.file_extension} "
                if prop == tags.PARSE_HEADER:
                    self.qry = f" {self.qry} {tags.PARSE_HEADER} = {self.attr.parse_header} "
                if prop == tags.SKIP_HEADER:
                    self.qry = f" {self.qry} {tags.SKIP_HEADER} = {self.attr.skip_header} "
                if prop == tags.SKIP_BLANK_LINES:
                    self.qry = f" {self.qry} {tags.SKIP_BLANK_LINES} = {self.attr.skip_blank_lines} "
                if prop == tags.DATE_FORMAT:
                    self.qry = f" {self.qry} {tags.DATE_FORMAT} = {self.attr.date_format} "
                if prop == tags.TIME_FORMAT:
                    self.qry = f" {self.qry} {tags.TIME_FORMAT} = {self.attr.time_format} "
                if prop == tags.TIMESTAMP_FORMAT:
                    self.qry = f" {self.qry} {tags.TIMESTAMP_FORMAT} = {self.attr.timestamp_format} "
                if prop == tags.BINARY_FORMAT:
                    self.qry = f" {self.qry} {tags.BINARY_FORMAT} = {self.attr.binary_format} "
                if prop == tags.ESCAPE:
                    self.qry = f" {self.qry} {tags.ESCAPE} = {self.attr.escape} "
                if prop == tags.ESCAPE_UNENCLOSED_FIELD:
                    self.qry = f" {self.qry} {tags.ESCAPE_UNENCLOSED_FIELD} = {self.attr.escape_unenclosed_field} "
                if prop == tags.TRIM_SPACE:
                    self.qry = f" {self.qry} {tags.TRIM_SPACE} = {self.attr.trim_space} "
                if prop == tags.FIELD_OPTIONALLY_ENCLOSED_BY:
                    self.qry = f" {self.qry} {tags.FIELD_OPTIONALLY_ENCLOSED_BY} = {self.attr.field_optionally_enclosed_by} "
                if prop == tags.NULL_IF:
                    self.qry = f" {self.qry} {tags.NULL_IF} = {self.attr.null_if} "
                if prop == tags.ERROR_ON_COLUMN_COUNT_MISMATCH:
                    self.qry = f" {self.qry} {tags.ERROR_ON_COLUMN_COUNT_MISMATCH} = {self.attr.error_on_column_count_mismatch} "
                if prop == tags.REPLACE_INVALID_CHARACTERS:
                    self.qry = f" {self.qry} {tags.REPLACE_INVALID_CHARACTERS} = {self.attr.replace_invalid_characters} "
                if prop == tags.EMPTY_FIELD_AS_NULL:
                    self.qry = f" {self.qry} {tags.EMPTY_FIELD_AS_NULL} = {self.attr.empty_field_as_null} "
                if prop == tags.SKIP_BYTE_ORDER_MARK:
                    self.qry = f" {self.qry} {tags.SKIP_BYTE_ORDER_MARK} = {self.attr.skip_byte_order_mark} "
                if prop == tags.ENCODING:
                    self.qry = f" {self.qry} {tags.ENCODING} = {self.attr.encoding} "
                if prop == tags.ENABLE_OCTAL:
                    self.qry = f" {self.qry} {tags.ENABLE_OCTAL} = {self.attr.enable_octal} "
                if prop == tags.ALLOW_DUPLICATE:
                    self.qry = f" {self.qry} {tags.ALLOW_DUPLICATE} = {self.attr.allow_duplicate} "
                if prop == tags.STRIP_OUTER_ARRAY:
                    self.qry = f" {self.qry} {tags.STRIP_OUTER_ARRAY} = {self.attr.strip_outer_array} "
                if prop == tags.STRIP_NULL_VALUES:
                    self.qry = f" {self.qry} {tags.STRIP_NULL_VALUES} = {self.attr.strip_null_values} "
                if prop == tags.IGNORE_UTF8_ERRORS:
                    self.qry = f" {self.qry} {tags.IGNORE_UTF8_ERRORS} = {self.attr.ignore_utf8_errors} "
                if prop == tags.SNAPPY_COMPRESSION:
                    self.qry = f" {self.qry} {tags.SNAPPY_COMPRESSION} = {self.attr.snappy_compression} "
                if prop == tags.BINARY_AS_TEXT:
                    self.qry = f" {self.qry} {tags.BINARY_AS_TEXT} = {self.attr.binary_as_text} "
                if prop == tags.USE_LOGICAL_TYPE:
                    self.qry = f" {self.qry} {tags.USE_LOGICAL_TYPE} = {self.attr.use_logical_type} "
                if prop == tags.USE_VECTORIZED_SCANNER:
                    self.qry = f" {self.qry} {tags.USE_VECTORIZED_SCANNER} = {self.attr.use_vectorized_scanner} "
                if prop == tags.PRESERVE_SPACE:
                    self.qry = f" {self.qry} {tags.PRESERVE_SPACE} = {self.attr.preserve_space} "
                if prop == tags.STRIP_OUTER_ELEMENT:
                    self.qry = f" {self.qry} {tags.STRIP_OUTER_ELEMENT} = {self.attr.strip_outer_element} "
                if prop == tags.DISABLE_SNOWFLAKE_DATA:
                    self.qry = f" {self.qry} {tags.DISABLE_SNOWFLAKE_DATA} = {self.attr.disable_snowflake_data} "
                if prop == tags.DISABLE_AUTO_CONVERT:
                    self.qry = f" {self.qry} {tags.DISABLE_AUTO_CONVERT} = {self.attr.disable_auto_convert} "
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = '{self.attr.comment}' "

    def alter_object(self):
        alter_object_name='FILE FORMAT'
        for prop in self.property_lst:
            if prop == tags.TYPE:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.TYPE} = {self.attr.type}"
                self.execute_final_query()
            if prop == tags.COMPRESSION:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.COMPRESSION} = {self.attr.compression}"
                self.execute_final_query()
            if prop == tags.RECORD_DELIMITER:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.RECORD_DELIMITER} = {self.attr.record_delimiter}"
                self.execute_final_query()
            if prop == tags.FIELD_DELIMITER:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.FIELD_DELIMITER} = {self.attr.field_delimiter}"
                self.execute_final_query()
            if prop == tags.MULTI_LINE:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.MULTI_LINE} = {self.attr.multi_line}"
                self.execute_final_query()
            if prop == tags.FILE_EXTENSION:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.FILE_EXTENSION} = {self.attr.file_extension}"
                self.execute_final_query()
            if prop == tags.PARSE_HEADER:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.PARSE_HEADER} = {self.attr.parse_header}"
                self.execute_final_query()
            if prop == tags.SKIP_HEADER:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.SKIP_HEADER} = {self.attr.skip_header}"
                self.execute_final_query()
            if prop == tags.SKIP_BLANK_LINES:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.SKIP_BLANK_LINES} = {self.attr.skip_blank_lines}"
                self.execute_final_query()
            if prop == tags.DATE_FORMAT:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.DATE_FORMAT} = {self.attr.date_format}"
                self.execute_final_query()
            if prop == tags.TIME_FORMAT:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.TIME_FORMAT} = {self.attr.time_format}"
                self.execute_final_query()
            if prop == tags.TIMESTAMP_FORMAT:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.TIMESTAMP_FORMAT} = {self.attr.timestamp_format}"
                self.execute_final_query()
            if prop == tags.BINARY_FORMAT:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.BINARY_FORMAT} = {self.attr.binary_format}"
                self.execute_final_query()
            if prop == tags.ESCAPE:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.ESCAPE} = {self.attr.escape}"
                self.execute_final_query()
            if prop == tags.ESCAPE_UNENCLOSED_FIELD:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.ESCAPE_UNENCLOSED_FIELD} = {self.attr.escape_unenclosed_field}"
                self.execute_final_query()
            if prop == tags.TRIM_SPACE:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.TRIM_SPACE} = {self.attr.trim_space}"
                self.execute_final_query()
            if prop == tags.FIELD_OPTIONALLY_ENCLOSED_BY:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.FIELD_OPTIONALLY_ENCLOSED_BY} = {self.attr.field_optionally_enclosed_by}"
                self.execute_final_query()
            if prop == tags.NULL_IF:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.NULL_IF} = {self.attr.null_if}"
                self.execute_final_query()
            if prop == tags.ERROR_ON_COLUMN_COUNT_MISMATCH:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.ERROR_ON_COLUMN_COUNT_MISMATCH} = {self.attr.error_on_column_count_mismatch}"
                self.execute_final_query()
            if prop == tags.REPLACE_INVALID_CHARACTERS:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.REPLACE_INVALID_CHARACTERS} = {self.attr.replace_invalid_characters}"
                self.execute_final_query()
            if prop == tags.EMPTY_FIELD_AS_NULL:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.EMPTY_FIELD_AS_NULL} = {self.attr.empty_field_as_null}"
                self.execute_final_query()
            if prop == tags.SKIP_BYTE_ORDER_MARK:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.SKIP_BYTE_ORDER_MARK} = {self.attr.skip_byte_order_mark}"
                self.execute_final_query()
            if prop == tags.ENCODING:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.ENCODING} = {self.attr.encoding}"
                self.execute_final_query()
            if prop == tags.ENABLE_OCTAL:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.ENABLE_OCTAL} = {self.attr.enable_octal}"
                self.execute_final_query()
            if prop == tags.ALLOW_DUPLICATE:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.ALLOW_DUPLICATE} = {self.attr.allow_duplicate}"
                self.execute_final_query()
            if prop == tags.STRIP_OUTER_ARRAY:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.STRIP_OUTER_ARRAY} = {self.attr.strip_outer_array}"
                self.execute_final_query()
            if prop == tags.STRIP_NULL_VALUES:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.STRIP_NULL_VALUES} = {self.attr.strip_null_values}"
                self.execute_final_query()
            if prop == tags.IGNORE_UTF8_ERRORS:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.IGNORE_UTF8_ERRORS} = {self.attr.ignore_utf8_errors}"
                self.execute_final_query()
            if prop == tags.SNAPPY_COMPRESSION:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.SNAPPY_COMPRESSION} = {self.attr.snappy_compression}"
                self.execute_final_query()
            if prop == tags.BINARY_AS_TEXT:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.BINARY_AS_TEXT} = {self.attr.binary_as_text}"
                self.execute_final_query()
            if prop == tags.USE_LOGICAL_TYPE:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.USE_LOGICAL_TYPE} = {self.attr.use_logical_type}"
                self.execute_final_query()
            if prop == tags.USE_VECTORIZED_SCANNER:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.USE_VECTORIZED_SCANNER} = {self.attr.use_vectorized_scanner}"
                self.execute_final_query()
            if prop == tags.PRESERVE_SPACE:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.PRESERVE_SPACE} = {self.attr.preserve_space}"
                self.execute_final_query()
            if prop == tags.STRIP_OUTER_ELEMENT:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.STRIP_OUTER_ELEMENT} = {self.attr.strip_outer_element}"
                self.execute_final_query()
            if prop == tags.DISABLE_SNOWFLAKE_DATA:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.DISABLE_SNOWFLAKE_DATA} = {self.attr.disable_snowflake_data}"
                self.execute_final_query()
            if prop == tags.DISABLE_AUTO_CONVERT:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.DISABLE_AUTO_CONVERT} = {self.attr.disable_auto_convert}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} RENAME TO {self.attr.database}.{self.attr.schema}.{self.attr.name[1]}"
            self.logger.info(f"Renaming {self.__class__.__name__} {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create=="TRUE":
            self.set_create_qry()
            self.add_properties_to_query()
        elif self.is_create=="FALSE":
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()

    def create_file_format(self):
        self.execute_final_query()

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=FileFormat(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        obj_inst.set_base_attributes(kwargs=kwargs)

        obj_inst.logger.info("set type")
        if tags.TYPE in kwargs.keys():
            obj_inst.set_type(kwargs[tags.TYPE])
        else:
            obj_inst.set_type('NONE')

        obj_inst.logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        obj_inst.logger.info("set compression")
        if tags.COMPRESSION in kwargs.keys():
            obj_inst.set_compression(kwargs[tags.COMPRESSION])
        else:
            obj_inst.set_compression('NONE')

        obj_inst.logger.info("set record_delimiter")
        if tags.RECORD_DELIMITER in kwargs.keys():
            obj_inst.set_record_delimiter(kwargs[tags.RECORD_DELIMITER])
        else:
            obj_inst.set_record_delimiter('NONE')

        obj_inst.logger.info("set field_delimiter")
        if tags.FIELD_DELIMITER in kwargs.keys():
            obj_inst.set_field_delimiter(kwargs[tags.FIELD_DELIMITER])
        else:
            obj_inst.set_field_delimiter('NONE')

        obj_inst.logger.info("set multi_line")
        if tags.MULTI_LINE in kwargs.keys():
            obj_inst.set_multi_line(kwargs[tags.MULTI_LINE])
        else:
            obj_inst.set_multi_line('NONE')

        obj_inst.logger.info("set file_extension")
        if tags.FILE_EXTENSION in kwargs.keys():
            obj_inst.set_file_extension(kwargs[tags.FILE_EXTENSION])
        else:
            obj_inst.set_file_extension('NONE')

        obj_inst.logger.info("set parse_header")
        if tags.PARSE_HEADER in kwargs.keys():
            obj_inst.set_parse_header(kwargs[tags.PARSE_HEADER])
        else:
            obj_inst.set_parse_header('NONE')

        obj_inst.logger.info("set skip_header")
        if tags.SKIP_HEADER in kwargs.keys():
            obj_inst.set_skip_header(kwargs[tags.SKIP_HEADER])
        else:
            obj_inst.set_skip_header('NONE')

        obj_inst.logger.info("set skip_blank_lines")
        if tags.SKIP_BLANK_LINES in kwargs.keys():
            obj_inst.set_skip_blank_lines(kwargs[tags.SKIP_BLANK_LINES])
        else:
            obj_inst.set_skip_blank_lines('NONE')

        obj_inst.logger.info("set date_format")
        if tags.DATE_FORMAT in kwargs.keys():
            obj_inst.set_date_format(kwargs[tags.DATE_FORMAT])
        else:
            obj_inst.set_date_format('NONE')

        obj_inst.logger.info("set time_format")
        if tags.TIME_FORMAT in kwargs.keys():
            obj_inst.set_time_format(kwargs[tags.TIME_FORMAT])
        else:
            obj_inst.set_time_format('NONE')

        obj_inst.logger.info("set timestamp_format")
        if tags.TIMESTAMP_FORMAT in kwargs.keys():
            obj_inst.set_timestamp_format(kwargs[tags.TIMESTAMP_FORMAT])
        else:
            obj_inst.set_timestamp_format('NONE')

        obj_inst.logger.info("set binary_format")
        if tags.BINARY_FORMAT in kwargs.keys():
            obj_inst.set_binary_format(kwargs[tags.BINARY_FORMAT])
        else:
            obj_inst.set_binary_format('NONE')

        obj_inst.logger.info("set escape")
        if tags.ESCAPE in kwargs.keys():
            obj_inst.set_escape(kwargs[tags.ESCAPE])
        else:
            obj_inst.set_escape('NONE')

        obj_inst.logger.info("set escape_unenclosed_field")
        if tags.ESCAPE_UNENCLOSED_FIELD in kwargs.keys():
            obj_inst.set_escape_unenclosed_field(kwargs[tags.ESCAPE_UNENCLOSED_FIELD])
        else:
            obj_inst.set_escape_unenclosed_field('NONE')

        logger.info("set trim_space")
        if tags.TRIM_SPACE in kwargs.keys():
            obj_inst.set_trim_space(kwargs[tags.TRIM_SPACE])
        else:
            obj_inst.set_trim_space('NONE')

        logger.info("set field_optionally_enclosed_by")
        if tags.FIELD_OPTIONALLY_ENCLOSED_BY in kwargs.keys():
            obj_inst.set_field_optionally_enclosed_by(kwargs[tags.FIELD_OPTIONALLY_ENCLOSED_BY])
        else:
            obj_inst.set_field_optionally_enclosed_by('NONE')

        logger.info("set null_if")
        if tags.NULL_IF in kwargs.keys():
            obj_inst.set_null_if(kwargs[tags.NULL_IF])
        else:
            obj_inst.set_null_if('NONE')

        logger.info("set error_on_column_count_mismatch")
        if tags.ERROR_ON_COLUMN_COUNT_MISMATCH in kwargs.keys():
            obj_inst.set_error_on_column_count_mismatch(kwargs[tags.ERROR_ON_COLUMN_COUNT_MISMATCH])
        else:
            obj_inst.set_error_on_column_count_mismatch('NONE')

        logger.info("set replace_invalid_characters")
        if tags.REPLACE_INVALID_CHARACTERS in kwargs.keys():
            obj_inst.set_replace_invalid_characters(kwargs[tags.REPLACE_INVALID_CHARACTERS])
        else:
            obj_inst.set_replace_invalid_characters('NONE')

        logger.info("set empty_field_as_null")
        if tags.EMPTY_FIELD_AS_NULL in kwargs.keys():
            obj_inst.set_empty_field_as_null(kwargs[tags.EMPTY_FIELD_AS_NULL])
        else:
            obj_inst.set_empty_field_as_null('NONE')

        logger.info("set skip_byte_order_mark")
        if tags.SKIP_BYTE_ORDER_MARK in kwargs.keys():
            obj_inst.set_skip_byte_order_mark(kwargs[tags.SKIP_BYTE_ORDER_MARK])
        else:
            obj_inst.set_skip_byte_order_mark('NONE')

        logger.info("set encoding")
        if tags.ENCODING in kwargs.keys():
            obj_inst.set_encoding(kwargs[tags.ENCODING])
        else:
            obj_inst.set_encoding('NONE')

        logger.info("set enable_octal")
        if tags.ENABLE_OCTAL in kwargs.keys():
            obj_inst.set_enable_octal(kwargs[tags.ENABLE_OCTAL])
        else:
            obj_inst.set_enable_octal('NONE')

        logger.info("set allow_duplicate")
        if tags.ALLOW_DUPLICATE in kwargs.keys():
            obj_inst.set_allow_duplicate(kwargs[tags.ALLOW_DUPLICATE])
        else:
            obj_inst.set_allow_duplicate('NONE')

        logger.info("set strip_outer_array")
        if tags.STRIP_OUTER_ARRAY in kwargs.keys():
            obj_inst.set_strip_outer_array(kwargs[tags.STRIP_OUTER_ARRAY])
        else:
            obj_inst.set_strip_outer_array('NONE')

        logger.info("set strip_null_values")
        if tags.STRIP_NULL_VALUES in kwargs.keys():
            obj_inst.set_strip_null_values(kwargs[tags.STRIP_NULL_VALUES])
        else:
            obj_inst.set_strip_null_values('NONE')

        logger.info("set ignore_utf8_errors")
        if tags.IGNORE_UTF8_ERRORS in kwargs.keys():
            obj_inst.set_ignore_utf8_errors(kwargs[tags.IGNORE_UTF8_ERRORS])
        else:
            obj_inst.set_ignore_utf8_errors('NONE')

        logger.info("set snappy_compression")
        if tags.SNAPPY_COMPRESSION in kwargs.keys():
            obj_inst.set_snappy_compression(kwargs[tags.SNAPPY_COMPRESSION])
        else:
            obj_inst.set_snappy_compression('NONE')

        logger.info("set binary_as_text")
        if tags.BINARY_AS_TEXT in kwargs.keys():
            obj_inst.set_binary_as_text(kwargs[tags.BINARY_AS_TEXT])
        else:
            obj_inst.set_binary_as_text('NONE')

        logger.info("set use_logical_type")
        if tags.USE_LOGICAL_TYPE in kwargs.keys():
            obj_inst.set_use_logical_type(kwargs[tags.USE_LOGICAL_TYPE])
        else:
            obj_inst.set_use_logical_type('NONE')

        logger.info("set use_vectorized_scanner")
        if tags.USE_VECTORIZED_SCANNER in kwargs.keys():
            obj_inst.set_use_vectorized_scanner(kwargs[tags.USE_VECTORIZED_SCANNER])
        else:
            obj_inst.set_use_vectorized_scanner('NONE')

        logger.info("set preserve_space")
        if tags.PRESERVE_SPACE in kwargs.keys():
            obj_inst.set_preserve_space(kwargs[tags.PRESERVE_SPACE])
        else:
            obj_inst.set_preserve_space('NONE')

        logger.info("set strip_outer_element")
        if tags.STRIP_OUTER_ELEMENT in kwargs.keys():
            obj_inst.set_strip_outer_element(kwargs[tags.STRIP_OUTER_ELEMENT])
        else:
            obj_inst.set_strip_outer_element('NONE')

        logger.info("set disable_snowflake_data")
        if tags.DISABLE_SNOWFLAKE_DATA in kwargs.keys():
            obj_inst.set_disable_snowflake_data(kwargs[tags.DISABLE_SNOWFLAKE_DATA])
        else:
            obj_inst.set_disable_snowflake_data('NONE')

        logger.info("set disable_auto_convert")
        if tags.DISABLE_AUTO_CONVERT in kwargs.keys():
            obj_inst.set_disable_auto_convert(kwargs[tags.DISABLE_AUTO_CONVERT])
        else:
            obj_inst.set_disable_auto_convert('NONE')

        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry(object_name=obj_inst.attr.name[0],
                                         object_type=obj_inst.__class__.__name__,
                                         object_database=obj_inst.attr.database,
                                         object_schema=obj_inst.attr.schema)
        
        logger.info('writing to git')
        obj_inst.write_file_to_git(object_name=obj_inst.attr.name[0],
                                         object_type=obj_inst.__class__.__name__,
                                         object_database=obj_inst.attr.database,
                                         object_schema=obj_inst.attr.schema)
        
        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                        object_identifier=obj_inst.attr.name[0],
                                        qry=obj_inst.qry)


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
