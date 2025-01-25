
class AutoIngest:
    def __get__(self,instance,owner):
        return instance._auto_ingest
    
    def __set__(self,instance,value):
        instance._auto_ingest = value
    
    def __delete__(self,instance):
        del instance._auto_ingest

class ErrorIntegration:
    def __get__(self,instance,owner):
        return instance._error_integration
    
    def __set__(self,instance,value):
        instance._error_integration = value
    
    def __delete__(self,instance):
        del instance._error_integration

class AwsSnsTopic:
    def __get__(self,instance,owner):
        return instance._aws_sns_topic
    
    def __set__(self,instance,value):
        instance._aws_sns_topic = value
    
    def __delete__(self,instance):
        del instance._aws_sns_topic

class Integration:
    def __get__(self,instance,owner):
        return instance._integration
    
    def __set__(self,instance,value):
        instance._integration = value
    
    def __delete__(self,instance):
        del instance._integration


class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = value
    
    def __delete__(self,instance):
        del instance._comment

class FileType:
    def __get__(self,instance,owner):
        return instance._file_type
    
    def __set__(self,instance,value):
        instance._file_type = value
    
    def __delete__(self,instance):
        del instance._file_type



class SnowpipeAttrs:
    auto_ingest = AutoIngest()
    error_integration = ErrorIntegration()
    aws_sns_topic = AwsSnsTopic()
    integration = Integration()
    comment = Comment()
    file_type = FileType()

class Snowpipe:
    def __init__(self):
        self.attr = SnowpipeAttrs()

    def set_auto_ingest(self,auto_ingest):
        self.attr.auto_ingest = auto_ingest

    def set_error_integration(self,error_integration):
        self.attr.error_integration = error_integration

    def set_aws_sns_topic(self,aws_sns_topic):
        self.attr.aws_sns_topic = aws_sns_topic

    def set_integration(self,integration):
        self.attr.integration = integration

    def set_comment(self,comment):
        self.attr.comment = comment

    def set_file_type(self,file_type):
        self.attr.file_type = file_type


    def set_match_by_column_name(self,value):
        self.attr.match_by_column_name = value


    def get_create_snowpipe_qry(self,ingest_inst):
        qry = f"CREATE OR REPLACE PIPE CONFIG_SCHEMA.pipe_{ingest_inst.attr.schema}_{ingest_inst.attr.table} AS COPY INTO {ingest_inst.attr.database}.{ingest_inst.attr.schema}.{ingest_inst.attr.table} from @{ingest_inst.attr.external_stage} file_format = ff_{self.attr.file_type}"

