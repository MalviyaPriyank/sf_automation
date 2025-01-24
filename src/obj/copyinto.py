import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))


from global_vars import CopyInto as gv
from validatevalue import ValidateValue as vv
from valueexception import IsARequiredAttribute,ValueNotAllowed

class Database:
    def __get__(self,instance,owner):
        return instance._database

    def __set__(self,instance,value):
        instance._database = value

    def __delete__(self,instance):
        del instance._database

    def __str__(self):
        definition = """Specifies the name of the database into which data is loaded."""
        return definition 
    
class Schema:
    def __get__(self,instance,owner):
        return instance._schema

    def __set__(self,instance,value):
        instance._schema = value

    def __delete__(self,instance):
        del instance._schema

    def __str__(self):
        definition = """Specifies the name of the schema into which data is loaded."""
        return definition 

class Table:
    def __get__(self,instance,owner):
        return instance._table

    def __set__(self,instance,value):
        instance._table = value

    def __delete__(self,instance):
        del instance._table

    def __str__(self):
        definition = """Specifies the name of the table into which data is loaded."""
        return definition

class Stage:
    def __get__(self,instance,owner):
        return instance._stage

    def __set__(self,instance,value):
        instance._stage = value

    def __delete__(self,instance):
        del instance._stage

    def __str__(self):
        definition = """ Specifies the internal or external location where the files containing data to be loaded are staged"""
        return definition

class FileFormat:
    def __get__(self,instance,owner):
        return instance._stage

    def __set__(self,instance,value):
        instance._stage = value

    def __delete__(self,instance):
        del instance._stage
    
class OnError:
    def __get__(self,instance,owner):
        return instance._on_error

    def __set__(self,instance,value):
        instance._on_error = value

    def __delete__(self,instance):
        del instance._on_error

    def __str__(self):
        definition = """String (constant) that specifies the error handling for the load operation."""
        return definition


class SizeLimit:
    def __get__(self,instance,owner):
        return instance._size_limit

    def __set__(self,instance,value):
        if value == "NONE":
            instance._size_limit = value
        elif vv.is_positive_number(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._size_limit = value

    def __delete__(self,instance):
        del instance._size_limit

    def __str__(self):
        definition = """
        Number (> 0) that specifies the maximum size (in bytes) of data to be loaded for a given COPY statement. 
        When the threshold is exceeded, the COPY operation discontinues loading files. 
        This option is commonly used to load a common group of files using multiple COPY statements. 
        For each statement, the data load continues until the specified SIZE_LIMIT is exceeded, 
        before moving on to the next statement."""
        return definition

class Purge:
    def __get__(self,instance,owner):
        return instance._purge

    def __set__(self,instance,value):
        if value == "NONE":
            instance._purge = value
        elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._purge = value

    def __delete__(self,instance):
        del instance._purge

    def __str__(self):
        definition = """
        Boolean that specifies whether to remove the data files from the stage 
        automatically after the data is loaded successfully."""
        return definition

class ReturnFailedOnly:
    def __get__(self,instance,owner):
        return instance._return_failed_only

    def __set__(self,instance,value):
        if value == "NONE":
            instance._return_failed_only = value
        elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._return_failed_only = value

    def __delete__(self,instance):
        del instance._return_failed_only

    def __str__(self):
        definition = """
        Boolean that specifies whether to return only files that have failed to load in the statement result."""
        return definition

class MatchByColumnName:
    def __get__(self,instance,owner):
        return instance._match_by_column_name

    def __set__(self,instance,value):
        if value == "NONE":
            instance._match_by_column_name = value
        elif value in gv._allowed_values_match_by_column_name:
            instance._match_by_column_name = value
        elif value not in gv._allowed_values_match_by_column_name:
            raise ValueNotAllowed(instance.parent.__class__.__name__,self.__class__.__name__,gv._allowed_values_match_by_column_name)

    def __delete__(self,instance):
        del instance._match_by_column_name  

    def __str__(self):
        definition = """
        String that specifies whether to load semi-structured data into columns in the 
        target table that match corresponding columns represented in the data."""  
        return definition

class IncludeMetadata:
    def __get__(self,instance,owner):
        return instance._include_metadata

    def __set__(self,instance,value):
        if value == "NONE":
            instance._include_metadata = value
        elif not vv.is_dependent_param_null(instance._match_by_column_name,instance.parent.__class__.__name__,self.__class__.__name__,'MatchByColumnName'):
            instance._include_metadata = value

    def __delete__(self,instance):
        del instance._include_metadata 

    def __str__(self):
        definition = """
        A user-defined mapping between a target table’s existing columns to its METADATA$ columns. 
        This copy option can only be used with the MATCH_BY_COLUMN_NAME copy option."""
        return definition

class EnforceLength:
    def __get__(self,instance,owner):
        return instance._enforce_length

    def __set__(self,instance,value):
        if value == "NONE":
            instance._enforce_length = value
        elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._enforce_length = value

    def __delete__(self,instance):
        del instance._enforce_length 

    def __str__(self):
        definition = """Boolean that specifies whether to truncate text strings that exceed the target column length"""
        return definition

class TruncateColumns:
    def __get__(self,instance,owner):
        return instance._truncatecolumns

    def __set__(self,instance,value):
        if value == "NONE":
            instance._truncatecolumns = value
        elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._truncatecolumns = value

    def __delete__(self,instance):
        del instance._truncatecolumns 

    def __str__(self):
        definition = """Boolean that specifies whether to truncate text strings that exceed the target column length"""
        return definition

class Force:
    def __get__(self,instance,owner):
        return instance._force

    def __set__(self,instance,value):
        if value == "NONE":
            instance._force = value
        elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._force = value
    def __delete__(self,instance):
        del instance._force 

    def __str__(self):
        definition = """ 
                Boolean that specifies to load all files, regardless of whether they’ve been loaded previously 
                and have not changed since they were loaded. Note that this option reloads files, 
                potentially duplicating data in a table.
                """
        return definition

class LoadUncertainFiles:
    def __get__(self,instance,owner):
        return instance._load_uncertain_files

    def __set__(self,instance,value):
        instance._load_uncertain_files = value

    def __delete__(self,instance):
        del instance._load_uncertain_files

    def __str__(self):
        definition = """
                    Boolean that specifies to load files for which the load status is unknown. 
                    The COPY command skips these files by default.
                    """
        return definition

class FileProcessor:
    def __get__(self,instance,owner):
        return instance._file_processor

    def __set__(self,instance,value):
        instance._file_processor = value

    def __delete__(self,instance):
        del instance._file_processor

    def __str__(self):
        definition = """ Specifies the scanner and the scanner options used for processing unstructured data. """  
        return definition

class LoadMode:
    def __get__(self,instance,owner):
        return instance._load_mode

    def __set__(self,instance,value):
        if value == "NONE":
            instance._load_mode = value
        elif value not in gv._allowed_values_load_mode:
            raise ValueNotAllowed(instance.parent.__class__.__name__,self.__class__.__name__,gv._allowed_values_load_mode)
        else:
            instance._load_mode = value

    def __delete__(self,instance):
        del instance._load_mode 

    def __str__(self):
        definition = """Specifies the mode to use when loading data from Parquet files into a Snowflake-managed Iceberg table."""
        return definition


class CopyIntoAttrs:
    def __init__(self,parent):
        self.parent = parent
    
    table = Table()
    schema = Schema()
    database = Database()
    stage = Stage()
    file_format = FileFormat()
    on_error = OnError()
    size_limit = SizeLimit()
    purge = Purge()
    return_failed_only = ReturnFailedOnly()
    match_by_column_name = MatchByColumnName()
    include_metadata = IncludeMetadata()
    enforce_length = EnforceLength()
    truncatecolumns = TruncateColumns()
    force = Force()
    load_uncertain_files = LoadUncertainFiles()
    file_processor = FileProcessor()
    load_mode = LoadMode()

class CopyInto:
    def __init__(self):
        self.attr = CopyIntoAttrs(self)

    def set_table(self,value):
        self.attr.table = value

    def set_schema(self,value):
        self.attr.schema = value

    def set_database(self,value):
        self.attr.database = value

    def set_stage(self,value):
        self.attr.stage = value

    def set_file_format(self,value):
        self.attr.file_format = value

    def set_on_error(self,value):
        self.attr.on_error = value

    def set_size_limit(self,value):
        self.attr.size_limit = value

    def set_purge(self,value):
        self.attr.purge = value

    def set_return_failed_only(self,value):
        self.attr.return_failed_only = value

    def set_match_by_column_name(self,value):
        self.attr.match_by_column_name = value

    def set_include_metadata(self,value):
        self.attr.include_metadata = value

    def set_enforce_length(self,value):
        self.attr.enforce_length = value

    def set_truncatecolumns(self,value):
        self.attr.truncatecolumns = value

    def set_force(self,value):
        self.attr.force = value
    
    def set_load_uncertain_files(self,value):
        self.attr.load_uncertain_files = value

    def set_file_processor(self,value):
        self.attr.file_processor = value

    def set_load_mode(self,value):
        self.attr.load_mode = value

    def create_object(session,**kwargs):
        cpy_into = CopyInto(session)

        cpy_into.set_table(kwargs[gv._table_tag])
        cpy_into.set_schema(kwargs[gv._schema_tag])
        cpy_into.set_database(kwargs[gv._database_tag])
        cpy_into.set_stage(kwargs[gv._stage_tag])
        cpy_into.set_file_format(kwargs[gv._file_format_tag])
        cpy_into.set_on_error(kwargs[gv._on_error_tag])
        cpy_into.set_size_limit(kwargs[gv._size_limit_tag])
        cpy_into.set_purge(kwargs[gv._purge_tag])
        cpy_into.set_return_failed_only(kwargs[gv._return_failed_only_tag])
        cpy_into.set_match_by_column_name(kwargs[gv._match_by_column_name_tag])
        cpy_into.set_include_metadata(kwargs[gv._include_metadata_tag])
        cpy_into.set_enforce_length(kwargs[gv._enforce_length_tag])
        cpy_into.set_truncatecolumns(kwargs[gv._truncatecolumns_tag])
        cpy_into.set_force(kwargs[gv._force_tag])
        cpy_into.set_load_uncertain_files(kwargs[gv._load_uncertain_files_tag])
        cpy_into.set_file_processor(kwargs[gv._file_processor_tag])
        cpy_into.set_load_mode(kwargs[gv._load_mode_tag])

    

        