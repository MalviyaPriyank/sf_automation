import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))


from global_vars import CopyInto as gv
from validatevalue import ValidateValue as vv

class Database:
    def __get__(self,instance,owner):
        return instance._database

    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._database = value

    def __delete__(self,instance):
        del instance._database

    
class Schema:
    def __get__(self,instance,owner):
        return instance._schema

    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._schema = value

    def __delete__(self,instance):
        del instance._schema


class Table:
    def __get__(self,instance,owner):
        return instance._table

    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._table = value

    def __delete__(self,instance):
        del instance._table

class Stage:
    def __get__(self,instance,owner):
        return instance._stage

    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._stage = value

    def __delete__(self,instance):
        del instance._stage


class FileFormat:
    def __get__(self,instance,owner):
        return instance._stage

    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
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

class MatchByColumnName:
    def __get__(self,instance,owner):
        return instance._match_by_column_name

    def __set__(self,instance,value):
        if value == "NONE":
            instance._match_by_column_name = value
        else:
            vv.allowed_value_check(value,gv._allowed_values_match_by_column_name,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._match_by_column_name = value

    def __delete__(self,instance):
        del instance._match_by_column_name  


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


class LoadUncertainFiles:
    def __get__(self,instance,owner):
        return instance._load_uncertain_files

    def __set__(self,instance,value):
        instance._load_uncertain_files = value

    def __delete__(self,instance):
        del instance._load_uncertain_files


class FileProcessor:
    def __get__(self,instance,owner):
        return instance._file_processor

    def __set__(self,instance,value):
        instance._file_processor = value

    def __delete__(self,instance):
        del instance._file_processor


class LoadMode:
    def __get__(self,instance,owner):
        return instance._load_mode

    def __set__(self,instance,value):
        if value == "NONE":
            instance._load_mode = value
        else:
            vv.allowed_value_check(value,gv._allowed_values_load_mode,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._load_mode = value

    def __delete__(self,instance):
        del instance._load_mode 


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

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv._on_error_tag,"_on_error")
        set_flag(gv._size_limit_tag,"_size_limit")
        set_flag(gv._purge_tag,"_purge")
        set_flag(gv._return_failed_only_tag,"_return_failed_only")
        set_flag(gv._match_by_column_name_tag,"_match_by_column_name")
        set_flag(gv._include_metadata_tag,"_include_metadata")
        set_flag(gv._enforce_length_tag,"_enforce_length")
        set_flag(gv._truncatecolumns_tag,"_truncatecolumns")
        set_flag(gv._force_tag,"_force")
        set_flag(gv._load_uncertain_files_tag,"_load_uncertain_files")
        set_flag(gv._file_processor_tag,"_file_processor")
        set_flag(gv._load_mode_tag,"_load_mode")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_copy_into_qry(self):
        self.qry = "COPY INTO {self.attr.database}.{self.attr.schema}.{self.attr.table} FROM @{self.attr.stage} FILE_FORMAT = {self.attr.file_format} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gv._on_error_tag:
                    self.qry = f" {self.qry} {gv._on_error_tag} = {self.attr.on_error} "
                if prop == gv._size_limit_tag:
                    self.qry = f" {self.qry} {gv._size_limit_tag} = {self.attr.size_limit} "
                if prop == gv._purge_tag:
                    self.qry = f" {self.qry} {gv._purge_tag} = {self.attr.purge} "
                if prop == gv._return_failed_only_tag:
                    self.qry = f" {self.qry} {gv._return_failed_only_tag} = {self.attr.return_failed_only} "
                if prop == gv._match_by_column_name_tag:
                    self.qry = f" {self.qry} {gv._match_by_column_name_tag} = {self.attr.match_by_column_name} "
                if prop == gv._include_metadata_tag:
                    self.qry = f" {self.qry} {gv._include_metadata_tag} = {self.attr.include_metadata} "
                if prop == gv._enforce_length_tag:
                    self.qry = f" {self.qry} {gv._enforce_length_tag} = {self.attr.enforce_length} "
                if prop == gv._truncatecolumns_tag:
                    self.qry = f" {self.qry} {gv._truncatecolumns_tag} = {self.attr.truncatecolumns} "
                if prop == gv._force_tag:
                    self.qry = f" {self.qry} {gv._force_tag} = {self.attr.force} "
                if prop == gv._load_uncertain_files_tag:
                    self.qry = f" {self.qry} {gv._load_uncertain_files_tag} = {self.attr.load_uncertain_files} "
                if prop == gv._file_processor_tag:
                    self.qry = f" {self.qry} {gv._file_processor_tag} = {self.attr.file_processor} "
                if prop == gv._load_mode_tag:
                    self.qry = f" {self.qry} {gv._load_mode_tag} = {self.attr.load_mode} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_copy_into_qry()
        self.add_properties_to_query()

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
        cpy_into.prepare_query()
        return cpy_into.qry

    

        