import sys
import os 
import logging

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))


from vars.gvobject import CopyInto as gv
from vars.obj.copyinto.gvcopyinto import CopyIntoTag as tags
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from .baseobj import BaseObject 



class Database:
    def __get__(self,instance,owner):
        return instance._database

    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.database_exist(instance.parent.session,value)
        instance._database = value

    def __delete__(self,instance):
        del instance._database

    
class Schema:
    def __get__(self,instance,owner):
        return instance._schema

    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.schema_exist(session=instance.parent.session, database_name=instance._database, schema_name=value)
        instance._schema = value

    def __delete__(self,instance):
        del instance._schema


class Table:
    def __get__(self,instance,owner):
        return instance._table

    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.table_exist(session=instance.parent.session,database_name=instance._database,schema_name=instance._schema, table_name=value)
        instance._table = value

    def __delete__(self,instance):
        del instance._table

class Stage:
    def __get__(self,instance,owner):
        return instance._stage

    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.stage_exist(session=instance.parent.session, database_name=instance._database, schema_name=instance._schema, stage_name=value)
        instance._stage = value

    def __delete__(self,instance):
        del instance._stage


class FileFormat:
    def __get__(self,instance,owner):
        return instance._file_format

    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.file_format_exist(session=instance.parent.session, database_name=instance._database, schema_name=instance._schema, file_format_name=value)
        instance._file_format = value

    def __delete__(self,instance):
        del instance._file_format
    
class OnError:
    def __get__(self,instance,owner):
        return instance._on_error

    def __set__(self,instance,value):
        if value=="NONE":
            instance._on_error=value
        else:
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.ON_ERROR),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._on_error = value

    def __delete__(self,instance):
        del instance._on_error


class SizeLimit:
    def __get__(self,instance,owner):
        return instance._size_limit

    def __set__(self,instance,value):
        if value == "NONE":
            instance._size_limit = value
        else: 
            vv.is_positive_number(value,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._size_limit = value

    def __delete__(self,instance):
        del instance._size_limit


class Purge:
    def __get__(self,instance,owner):
        return instance._purge

    def __set__(self,instance,value):
        if value == "NONE":
            instance._purge = value
        else: 
            vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._purge = value

    def __delete__(self,instance):
        del instance._purge


class ReturnFailedOnly:
    def __get__(self,instance,owner):
        return instance._return_failed_only

    def __set__(self,instance,value):
        if value == "NONE":
            instance._return_failed_only = value
        else: 
            vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__)
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
            vv.allowed_value_check(value,tags.allowed_value_list().get(tags.MATCH_BY_COLUMN_NAME),instance.parent.__class__.__name__,self.__class__.__name__)
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
        else: 
            vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._enforce_length = value

    def __delete__(self,instance):
        del instance._enforce_length 

class TruncateColumns:
    def __get__(self,instance,owner):
        return instance._truncatecolumns

    def __set__(self,instance,value):
        if value == "NONE":
            instance._truncatecolumns = value
        else: 
            vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._truncatecolumns = value

    def __delete__(self,instance):
        del instance._truncatecolumns 


class Force:
    def __get__(self,instance,owner):
        return instance._force

    def __set__(self,instance,value):
        if value == "NONE":
            instance._force = value
        else: 
            vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__)
            instance._force = value
    def __delete__(self,instance):
        del instance._force 


class LoadUncertainFiles:
    def __get__(self,instance,owner):
        return instance._load_uncertain_files

    def __set__(self,instance,value):
        if value=="NONE":
            instance._load_uncertain_files=value
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._load_uncertain_files = value

    def __delete__(self,instance):
        del instance._load_uncertain_files


class FileProcessor:
    def __get__(self,instance,owner):
        return instance._file_processor

    def __set__(self,instance,value):
        if value=="NONE":
            instance._file_processor=value
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._file_processor = value

    def __delete__(self,instance):
        del instance._file_processor

class Scanner:
    def __get__(self,instance,owner):
        return instance._scanner

    def __set__(self,instance,value):
        if value=="NONE":
            instance._scanner=value
        else:
            vv.is_parent_attribute_compatible(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,parent_attribute="ON_ERROR",compatible_value_lst_parent_attribute=["ABORT_STATEMENT"])
            vv.is_conflicting_parameter_null(original_parameter_val=value,conflicting_parameter_val=instance._match_by_column_name,original_parameter=self.__class__.__name__,conflicting_parameter="MATCH_BY_COLUMN_NAME",object_type=instance.parent.__class__.__name__)
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.SCANNER),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._scanner = f"'{value}'"

    def __delete__(self,instance):
        del instance._scanner

class ProjectName:
    def __get__(self,instance,owner):
        return instance._project_name

    def __set__(self,instance,value):
        if value=="NONE":
            instance._project_name=value
        else:
            vv.is_parent_attribute_compatible(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,parent_attribute="ON_ERROR",compatible_value_lst_parent_attribute=["ABORT_STATEMENT"])
            vv.is_conflicting_parameter_null(original_parameter_val=value,conflicting_parameter_val=instance._match_by_column_name,original_parameter=self.__class__.__name__,conflicting_parameter="MATCH_BY_COLUMN_NAME",object_type=instance.parent.__class__.__name__)
            instance._project_name = f"'{value}'"

    def __delete__(self,instance):
        del instance._project_name

class ModelName:
    def __get__(self,instance,owner):
        return instance._model_name

    def __set__(self,instance,value):
        if instance._scanner=='document_ai':
            vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._model_name=f"'{value}'"
        else:
            if value=="NONE":
                instance._model_name=value
            else:
                vv.is_parent_attribute_compatible(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,parent_attribute="ON_ERROR",compatible_value_lst_parent_attribute=["ABORT_STATEMENT"])
                vv.is_conflicting_parameter_null(original_parameter_val=value,conflicting_parameter_val=instance._match_by_column_name,original_parameter=self.__class__.__name__,conflicting_parameter="MATCH_BY_COLUMN_NAME",object_type=instance.parent.__class__.__name__)
                instance._model_name = f"'{value}'"

    def __delete__(self,instance):
        del instance._model_name

class ModelVersion:
    def __get__(self,instance,owner):
        return instance._model_version

    def __set__(self,instance,value):
        if instance._scanner=='document_ai':
            vv.required_attribute_check(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._model_version=f"'{value}'"
        else:
            if value=="NONE":
                instance._model_version=value
            else:
                vv.is_parent_attribute_compatible(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,parent_attribute="ON_ERROR",compatible_value_lst_parent_attribute=["ABORT_STATEMENT"])
                vv.is_conflicting_parameter_null(original_parameter_val=value,conflicting_parameter_val=instance._match_by_column_name,original_parameter=self.__class__.__name__,conflicting_parameter="MATCH_BY_COLUMN_NAME",object_type=instance.parent.__class__.__name__)
                instance._model_version = f"'{value}'"

    def __delete__(self,instance):
        del instance._model_version

class LoadMode:
    def __get__(self,instance,owner):
        return instance._load_mode

    def __set__(self,instance,value):
        if value == "NONE":
            instance._load_mode = value
        else:
            vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.LOAD_MODE),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
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
    scanner=Scanner()
    project_name=ProjectName()
    model_name=ModelName()
    model_version=ModelVersion()
    load_mode = LoadMode()

class CopyInto(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session, user_id, logger)
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

    def set_file_processor(self,value):
        self.attr.file_processor = value

    def set_scanner(self,value):
        self.attr.scanner = value

    def set_project_name(self,value):
        self.attr.project_name = value

    def set_model_name(self,value):
        self.attr.model_name = value

    def set_model_version(self,value):
        self.attr.model_version = value

    def set_load_mode(self,value):
        self.attr.load_mode = value

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.ON_ERROR,"_on_error")
        set_flag(tags.SIZE_LIMIT,"_size_limit")
        set_flag(tags.PURGE,"_purge")
        set_flag(tags.RETURN_FAILED_ONLY,"_return_failed_only")
        set_flag(tags.MATCH_BY_COLUMN_NAME,"_match_by_column_name")
        set_flag(tags.INCLUDE_METADATA,"_include_metadata")
        set_flag(tags.ENFORCE_LENGTH,"_enforce_length")
        set_flag(tags.TRUNCATECOLUMNS,"_truncatecolumns")
        set_flag(tags.FORCE,"_force")
        set_flag(tags.LOAD_UNCERTAIN_FILES,"_load_uncertain_files")
        set_flag(tags.FILE_PROCESSOR,"_file_processor")
        set_flag(tags.SCANNER,"_scanner")
        set_flag(tags.PROJECT_NAME,"_project_name")
        set_flag(tags.MODEL_NAME,"_model_name")
        set_flag(tags.MODEL_VERSION,"_model_version")
        set_flag(tags.LOAD_MODE,"_load_mode")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_copy_into_qry(self):
        self.qry = f"COPY INTO {self.attr.database}.{self.attr.schema}.{self.attr.table} FROM @{self.attr.database}.{self.attr.schema}.{self.attr.stage}/{self.attr.table} FILE_FORMAT = {self.attr.file_format} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.ON_ERROR:
                    self.qry = f" {self.qry} {tags.ON_ERROR} = {self.attr.on_error} "
                if prop == tags.SIZE_LIMIT:
                    self.qry = f" {self.qry} {tags.SIZE_LIMIT} = {self.attr.size_limit} "
                if prop == tags.PURGE:
                    self.qry = f" {self.qry} {tags.PURGE} = {self.attr.purge} "
                if prop == tags.RETURN_FAILED_ONLY:
                    self.qry = f" {self.qry} {tags.RETURN_FAILED_ONLY} = {self.attr.return_failed_only} "
                if prop == tags.MATCH_BY_COLUMN_NAME:
                    self.qry = f" {self.qry} {tags.MATCH_BY_COLUMN_NAME} = {self.attr.match_by_column_name} "
                if prop == tags.INCLUDE_METADATA:
                    self.qry = f" {self.qry} {tags.INCLUDE_METADATA} = {self.attr.include_metadata} "
                if prop == tags.ENFORCE_LENGTH:
                    self.qry = f" {self.qry} {tags.ENFORCE_LENGTH} = {self.attr.enforce_length} "
                if prop == tags.TRUNCATECOLUMNS:
                    self.qry = f" {self.qry} {tags.TRUNCATECOLUMNS} = {self.attr.truncatecolumns} "
                if prop == tags.FORCE:
                    self.qry = f" {self.qry} {tags.FORCE} = {self.attr.force} "
                if prop == tags.LOAD_UNCERTAIN_FILES:
                    self.qry = f" {self.qry} {tags.LOAD_UNCERTAIN_FILES} = {self.attr.load_uncertain_files} "
                if prop == tags.SCANNER:
                    self.qry = f" {self.qry} {tags.FILE_PROCESSOR} = ( {tags.SCANNER} = {self.attr.scanner} SCANNER_OPTIONS=("
                    if tags.PROJECT_NAME in self.property_lst:
                        self.qry=f" {self.qry} {tags.PROJECT_NAME} = {self.attr.project_name}"
                    if tags.MODEL_NAME in self.property_lst:
                        self.qry=f" {self.qry} {tags.MODEL_NAME} = {self.attr.model_name}"
                    if tags.MODEL_VERSION in self.property_lst:
                        self.qry=f" {self.qry} {tags.MODEL_VERSION} = {self.attr.model_version}"
                    self.qry=f"{self.qry} ))"
                if prop == tags.LOAD_MODE:
                    self.qry = f" {self.qry} {tags.LOAD_MODE} = {self.attr.load_mode} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_copy_into_qry()
        self.add_properties_to_query()

    def create_query(self,**kwargs):
        self.logger.info(f'dictionary passed {kwargs}')

        self.logger.info('set database')
        self.set_database(kwargs[tags.DATABASE])

        self.logger.info('set _schema')
        self.set_schema(kwargs[tags.SCHEMA])

        self.logger.info('set _table')
        self.set_table(kwargs[tags.TABLE])

        self.logger.info('set _stage')
        self.set_stage(kwargs[tags.STAGE])

        self.logger.info('set _file_format')
        self.set_file_format(kwargs[tags.FILE_FORMAT])

        self.logger.info('set _on_error')
        self.set_on_error(kwargs[tags.ON_ERROR])

        self.logger.info('set _size_limit')
        self.set_size_limit(kwargs[tags.SIZE_LIMIT])

        self.logger.info('set _purge')
        self.set_purge(kwargs[tags.PURGE])

        self.logger.info('set _return_failed_only')
        self.set_return_failed_only(kwargs[tags.RETURN_FAILED_ONLY])

        self.logger.info('set _match_by_column_name')
        self.set_match_by_column_name(kwargs[tags.MATCH_BY_COLUMN_NAME])

        self.logger.info('set _include_metadata')
        self.set_include_metadata(kwargs[tags.INCLUDE_METADATA])

        self.logger.info('set _enforce_length')
        self.set_enforce_length(kwargs[tags.ENFORCE_LENGTH])

        self.logger.info('set _truncatecolumns')
        self.set_truncatecolumns(kwargs[tags.TRUNCATECOLUMNS])

        self.logger.info('set _force')
        self.set_force(kwargs[tags.FORCE])

        self.logger.info('set _load_uncertain_files')
        self.set_load_uncertain_files(kwargs[tags.LOAD_UNCERTAIN_FILES])

        self.logger.info('set _file_processor')
        self.set_file_processor(kwargs[tags.FILE_PROCESSOR])

        self.logger.info('set _scanner')
        self.set_scanner(kwargs[tags.SCANNER])

        self.logger.info('set _project_name')
        self.set_project_name(kwargs[tags.PROJECT_NAME])

        self.logger.info('set _model_name')
        self.set_model_name(kwargs[tags.MODEL_NAME])

        self.logger.info('set _model_version')
        self.set_model_version(kwargs[tags.MODEL_VERSION])

        self.logger.info('set _load_mode')
        self.set_load_mode(kwargs[tags.LOAD_MODE])

        self.logger.info(f"preparing copy into for {self.attr.table}")
        self.prepare_query()
        return self.qry

    

        