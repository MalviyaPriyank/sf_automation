
class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if ( vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__) 
              and not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
              and not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__)
              ):
            instance._name = value

    def __delete__(self,instance):
        del instance._name

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
    name = Name()
    auto_ingest = AutoIngest()
    error_integration = ErrorIntegration()
    aws_sns_topic = AwsSnsTopic()
    integration = Integration()
    comment = Comment()
    file_type = FileType()

class Snowpipe:
    def __init__(self,copy_into_qry,stage,file_format):
        self.attr = SnowpipeAttrs()
        self.copy_into_qry = copy_into_qry
        self.stage = stage
        self.file_format = file_format

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


    def get_create_snowpipe_qry(self,ingest_inst):
        qry = f"CREATE OR REPLACE PIPE CONFIG_SCHEMA.{self.attr.name} AS {self.copy_into_qry} from @{self.stage} file_format = {self.file_format}"

