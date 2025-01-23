class TargetTable:
    def __get__(self,instance,owner):
        return instance._target_table

    def __set__(self,instance,value):
        instance._target_table = value

    def __delete__(self,instance):
        del instance._target_table

class Stage:
    def __get__(self,instance,owner):
        return instance._stage

    def __set__(self,instance,value):
        instance._stage = value

    def __delete__(self,instance):
        del instance._stage

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

class SizeLimit:
    def __get__(self,instance,owner):
        return instance._size_limit

    def __set__(self,instance,value):
        instance._size_limit = value

    def __delete__(self,instance):
        del instance._size_limit

class Purge:
    def __get__(self,instance,owner):
        return instance._purge

    def __set__(self,instance,value):
        instance._purge = value

    def __delete__(self,instance):
        del instance._purge

class ReturnFailedOnly:
    def __get__(self,instance,owner):
        return instance._return_failed_only

    def __set__(self,instance,value):
        instance._return_failed_only = value

    def __delete__(self,instance):
        del instance._return_failed_only

class MatchByColumnName:
    def __get__(self,instance,owner):
        return instance._match_by_column_name

    def __set__(self,instance,value):
        instance._match_by_column_name = value

    def __delete__(self,instance):
        del instance._match_by_column_name    

class IncludeMetadata:
    def __get__(self,instance,owner):
        return instance._include_metadata

    def __set__(self,instance,value):
        instance._include_metadata = value

    def __delete__(self,instance):
        del instance._include_metadata 

class EnforceLength:
    def __get__(self,instance,owner):
        return instance._enforce_length

    def __set__(self,instance,value):
        instance._enforce_length = value

    def __delete__(self,instance):
        del instance._enforce_length 

class TruncateColumns:
    def __get__(self,instance,owner):
        return instance._truncatecolumns

    def __set__(self,instance,value):
        instance._truncatecolumns = value

    def __delete__(self,instance):
        del instance._truncatecolumns 

class Force:
    def __get__(self,instance,owner):
        return instance._force

    def __set__(self,instance,value):
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
        instance._load_mode = value

    def __delete__(self,instance):
        del instance._load_mode 


class CopyIntoAttrs:
    def __init__(self,parent):
        self.parent = parent
    
    target_table = TargetTable()
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

    def set_target_table(self,value):
        self.attr.target_table = value

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

    

        