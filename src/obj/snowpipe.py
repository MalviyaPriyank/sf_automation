import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.global_vars import Snowpipe as gv,Config as cfg
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy



class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        instance._database = value
    
    def __delete__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        instance._schema = value
    
    def __delete__(self,instance):
        del instance._schema

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
    database = Database()
    schema = Schema()
    name = Name()
    auto_ingest = AutoIngest()
    error_integration = ErrorIntegration()
    aws_sns_topic = AwsSnsTopic()
    integration = Integration()
    comment = Comment()
    file_type = FileType()

class Snowpipe:
    def __init__(self,session,copy_into_qry,stage,file_format,user_id):
        self.attr = SnowpipeAttrs()
        self.copy_into_qry = copy_into_qry
        self.stage = stage
        self.file_format = file_format
        self.user_id = user_id
        self.session = session

    def set_database(self,value):
        self.attr.database = value

    def set_schema(self,value):
        self.attr.schema = value

    def set_name(self,value):
        self.attr.name = value

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

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv._auto_ingest_tag,"_auto_ingest")
        set_flag(gv._error_integration_tag,"_error_integration")
        set_flag(gv._aws_sns_topic_tag,"_aws_sns_topic")
        set_flag(gv._integration_tag,"_integration")
        set_flag(gv._comment_tag,"_comment")
        set_flag(gv._file_type_tag,"_file_type")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_qry(self):
        self.qry = f"CREATE OR REPLACE PIPE {self.attr.database}.{self.attr.schema}.{self.attr.name} AS {self.copy_into_qry} from @{self.stage} file_format = {self.file_format} "


    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gv._auto_ingest_tag:
                    self.qry = f" {self.qry} {gv._auto_ingest_tag} = {self.attr.auto_ingest} "
                if prop == gv._error_integration_tag:
                    self.qry = f" {self.qry} {gv._error_integration_tag} = {self.attr.error_integration} "
                if prop == gv._aws_sns_topic_tag:
                    self.qry = f" {self.qry} {gv._aws_sns_topic_tag} = {self.attr.aws_sns_topic} "
                if prop == gv._integration_tag:
                    self.qry = f" {self.qry} {gv._integration_tag} = {self.attr.integration} "
                if prop == gv._comment_tag:
                    self.qry = f" {self.qry} {gv._comment_tag} = {self.attr.comment} "
                if prop == gv._file_type_tag:
                    self.qry = f" {self.qry} {gv._file_type_tag} = {self.attr.file_type} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_qry()
        self.add_properties_to_query()

    def create_snowpipe(self):
        self.session.sql(self.qry).collect()


    def create_object(self,**kwargs):
        self.set_database(kwargs[gv._database_tag])
        self.set_schema(kwargs[gv._schema_tag])
        self.set_name(kwargs[gv._name_tag])
        self.set_auto_ingest(kwargs[gv._auto_ingest_tag])
        self.set_error_integration(kwargs[gv._error_integration_tag])
        self.set_aws_sns_topic(kwargs[gv._aws_sns_topic_tag])
        self.set_integration(kwargs[gv._integration_tag])
        self.set_comment(kwargs[gv._comment_tag])
        self.set_file_type(kwargs[gv._file_type_tag])
        self.prepare_query()
        self.create_snowpipe()
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
