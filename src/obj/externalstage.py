import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))


from vars.gvobject import Config as cfg,Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from vars.obj.externalstage.gvexternalstage import ExternalStageTag as tags
from dep import deploy
from setup import privilege
from .baseobj import BaseObject 


class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.database_exist(session=instance.parent.session, database_name=value)
        #if vo.database_exist(value):
        instance._database = value

    def __delete__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.schema_exist(session=instance.parent.session, database_name=instance._database, schema_name=value)
        #if vo.schema_exist(instance._database,value):
        instance._schema = value

    def __delete__(self,instance):
        del instance._schema


class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)
    
    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_stage(session=instance.parent.session,database=instance._database,schema=instance._schema,stage=name,obj_type=instance.parent.__class__.__name__,obj_name=self.__class__.__name__)
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
                vo.stage_exist(session=instance.parent.session,database_name=instance._database,schema_name=instance._schema,stage_name=old_name)
                vo.is_new_stage(session=instance.parent.session,database=instance._database,schema=instance._schema,stage=new_name,obj_type=instance.parent.__class__.__name__,obj_name=self.__class__.__name__)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to

class FileFormat:   
    def __get__(self,instance,owner):
        return instance._file_format
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._file_format=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vo.file_format_exist(session=instance.parent.session,database_name=instance._database,schema_name=instance._schema,file_format_name=value)
            instance._file_format = value

    def __delete__(self,instance):
        del instance._file_format

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._comment=value
        else:
            instance._comment = f"'{value}'"

    def __delete__(self,instance):
        del instance._comment

class Url:
    def __get__(self,instance,owner):
        return instance._url
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._url = value
        else:
            vv.is_valid_url(value=value,allowed_protocols=tags.allowed_value_list().get(tags.PROTOCOLS),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._url = f"'{value}'"

    def __delete__(self,instance):
        del instance._url

class AwsAccessPointArn:
    def __get__(self,instance,owner):
        return instance._aws_access_point_arn
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._aws_access_point_arn = value
        else:
            vv.is_s3_alias(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,url=instance._url)
            instance._aws_access_point_arn = f"'{value}'"

    def __delete__(self,instance):
        del instance._aws_access_point_arn

class StorageIntegration:
    def __get__(self,instance,owner):
        return instance._storage_integration
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._storage_integration=value
        else:
            vo.integration_exist(session=instance.parent.session,integration_name=value)
            instance._storage_integration=value

    def __delete__(self,instance):
        del instance._storage_integration

class EncryptionType:
    def __get__(self,instance,owner):
        return instance._encryption_type
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._encryption_type=value
        else:
            if 's3' in instance._url.split(":")[0]:
                vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.S3_ENCRYPTION_TYPE),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                instance._encryption_type = value
            elif 'gcs' in instance._url.split(":")[0]:
                vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.GCS_ENCRYPTION_TYPE),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                instance._encryption_type=value
            elif 'azure' in instance._url.split(":")[0]:
                vv.is_allowed_value(value=value,allowed_list=tags.allowed_value_list().get(tags.AZURE_ENCRYPTION_TYPE),object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                instance._encryption_type=value

    def __delete__(self,instance):
        del instance._encryption_type

class EncryptionMasterKey:
    def __get__(self,instance,owner):
        return instance._encryption_master_key
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._encryption_master_key=value
        else:
            if 's3' in instance._url.split(":")[0]:
                vv.is_parent_attribute_compatible(value=value,object_type=instance.parent.__class__.__name__, attr_name=self.__class__.__name__,parent_attribute=instance._encryption_type.__class__.__name__,compatible_value_lst_parent_attribute=['AWS_CSE'])
                instance._encryption_master_key=value
            elif 'gcs' in instance._url.split(":")[0]:
                vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition='GCS')
            elif 'azure' in instance._url.split(":")[0]:
                vv.is_parent_attribute_compatible(value=value,object_type=instance.parent.__class__.__name__, attr_name=self.__class__.__name__,parent_attribute=instance._encryption_type.__class__.__name__,compatible_value_lst_parent_attribute=['AZURE_CSE'])
                instance._encryption_master_key=value     

    def __delete__(self,instance):
        del instance._encryption_master_key

class EncryptionKmsKeyId:
    def __get__(self,instance,owner):
        return instance._encryption_kms_key_id
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._encryption_kms_key_id = value
        else:
            if 's3' in instance._url.split(":")[0]:
                vv.is_parent_attribute_compatible(value=value,object_type=instance.parent.__class__.__name__, attr_name=self.__class__.__name__,parent_attribute=instance._encryption_type.__class__.__name__,compatible_value_lst_parent_attribute=['AWS_SSE_KMS'])
                instance._encryption_kms_key_id=value
            elif 'gcs' in instance._url.split(":")[0]:
                vv.is_parent_attribute_compatible(value=value,object_type=instance.parent.__class__.__name__, attr_name=self.__class__.__name__,parent_attribute=instance._encryption_type.__class__.__name__,compatible_value_lst_parent_attribute=['GCS_SSE_KMS'])
                instance._encryption_kms_key_id=value
            elif 'azure' in instance._url.split(":")[0]:
                vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition='AZURE')

    def __delete__(self,instance):
        del instance._encryption_kms_key_id


class UsePrivatelinkEndpoint:
    def __get__(self,instance,owner):
        return instance._use_privatelink_endpoint
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._use_privatelink_endpoint=value
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            if 's3' in instance._url.split(":")[0] or 'azure' in instance._url.split(":")[0]:
                instance._use_privatelink_endpoint=value
            else:
                vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition="GCS")

    def __delete__(self,instance):
        del instance._use_privatelink_endpoint

class Enable:
    def __get__(self,instance,owner):
        return instance._enable
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._enable = value
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._enable=value

    def __delete__(self,instance):
        del instance._enable    

class RefreshOnCreate:
    def __get__(self,instance,owner):
        return instance._refresh_on_create
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._refresh_on_create = value
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._refresh_on_create=value

    def __delete__(self,instance):
        del instance._refresh_on_create

class AutoRefresh:
    def __get__(self,instance,owner):
        return instance._auto_refresh
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._auto_refresh=value
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._auto_refresh=value

    def __delete__(self,instance):
        del instance._auto_refresh

class NotificationIntegration:
    def __get__(self,instance,owner):
        return instance._notification_integration
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._notification_integration=value
        else:
            if 'gcs' in instance._url.split(":")[0] or 'azure' in instance._url.split(":")[0]:
                vo.integration_exist(session=instance.parent.session,integration_name=value)
                instance._notification_integration = value
            else:
                vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition='S3')

    def __delete__(self,instance):
        del instance._notification_integration

class ExternalStageAttrs:
    def __init__(self,parent):
        self.parent = parent

    database=Database()
    schema=Schema()
    name = Name()
    file_format = FileFormat()
    comment = Comment()
    url = Url()
    aws_access_point_arn=AwsAccessPointArn()
    storage_integration = StorageIntegration()
    encryption_type = EncryptionType()
    encryption_master_key = EncryptionMasterKey()
    encryption_kms_key_id = EncryptionKmsKeyId()
    use_privatelink_endpoint = UsePrivatelinkEndpoint()
    enable=Enable()
    refresh_on_create = RefreshOnCreate()
    auto_refresh = AutoRefresh()
    notification_integration = NotificationIntegration()

class ExternalStage(BaseObject):
    def __init__(self, session, user_id, logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger)
        self.sf_object_tag = "STAGE"
        self.attr = ExternalStageAttrs(self)

    def set_database(self,val):
        self.attr.database=val

    def set_schema(self,val):
        self.attr.schema=val

    def set_name(self,val):
        self.attr.name = val

    def set_file_format(self,val):
        self.attr.file_format = val

    def set_comment(self,val):
        self.attr.comment = val

    def set_url(self,val):
        self.attr.url = val

    def set_aws_access_point_arn(self,val):
        self.attr.aws_access_point_arn=val

    def set_storage_integration(self,val):
        self.attr.storage_integration = val

    def set_encryption_type(self,val):
        self.attr.encryption_type = val

    def set_encryption_master_key(self,val):
        self.attr.encryption_master_key = val

    def set_encryption_kms_key_id(self,val):
        self.attr.encryption_kms_key_id = val

    def set_use_privatelink_endpoint(self,val):
        self.attr.use_privatelink_endpoint = val

    def set_enable(self,val):
        self.attr.enable=val

    def set_refresh_on_create(self,val):
        self.attr.refresh_on_create = val

    def set_auto_refresh(self,val):
        self.attr.auto_refresh = val

    def set_notification_integration(self,val):
        self.attr.notification_integration = val
    
    def set_qualified_name(self):
        self.qualified_name = f"{self.attr.database}.{self.attr.schema}.{self.attr.name}"

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.FILE_FORMAT,"_file_format")
        set_flag(tags.COMMENT,"_comment")
        set_flag(tags.URL,"_url")
        set_flag(tags.AWS_ACCESS_POINT_ARN,"_aws_access_point_arn")
        set_flag(tags.STORAGE_INTEGRATION,"_storage_integration")
        set_flag(tags.ENCRYPTION_TYPE,"_encryption_type")
        set_flag(tags.ENCRYPTION_MASTER_KEY,"_encryption_master_key")
        set_flag(tags.ENCRYPTION_KMS_KEY_ID,"_encryption_kms_key_id")
        set_flag(tags.USE_PRIVATELINK_ENDPOINT,"_use_privatelink_endpoint")
        set_flag(tags.ENABLE,"_enable")
        set_flag(tags.REFRESH_ON_CREATE,"_refresh_on_create")
        set_flag(tags.AUTO_REFRESH,"_auto_refresh")
        set_flag(tags.NOTIFICATION_INTEGRATION,"_notification_integration")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)


    def alter_object(self):        
        alter_object_name='STAGE'
        for prop in self.property_lst:
            if prop == tags.FILE_FORMAT:
                self.qry = f"ALTER {alter_object_name} {self.attr.name[0]} SET {tags.FILE_FORMAT} = {self.attr.file_format}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER {alter_object_name} {self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()
            if prop == tags.URL:
                self.qry = f"ALTER {alter_object_name} {self.attr.name[0]} SET {tags.URL} = {self.attr.url}"
                self.execute_final_query()
            if prop == tags.AWS_ACCESS_POINT_ARN:
                self.qry = f"ALTER {alter_object_name} {self.attr.name[0]} SET {tags.AWS_ACCESS_POINT_ARN} = {self.attr.aws_access_point_arn}"
                self.execute_final_query()
            if prop == tags.STORAGE_INTEGRATION:
                self.qry = f"ALTER {alter_object_name} {self.attr.name[0]} SET {tags.STORAGE_INTEGRATION} = {self.attr.storage_integration}"
                self.execute_final_query()
            if prop == tags.ENCRYPTION_TYPE:
                self.qry = f"ALTER {alter_object_name} {self.attr.name[0]} SET {tags.ENCRYPTION_TYPE} = {self.attr.encryption_type}"
                self.execute_final_query()
            if prop == tags.ENCRYPTION_MASTER_KEY:
                self.qry = f"ALTER {alter_object_name} {self.attr.name[0]} SET {tags.ENCRYPTION_MASTER_KEY} = {self.attr.encryption_master_key}"
                self.execute_final_query()
            if prop == tags.ENCRYPTION_KMS_KEY_ID:
                self.qry = f"ALTER {alter_object_name} {self.attr.name[0]} SET {tags.ENCRYPTION_KMS_KEY_ID} = {self.attr.encryption_kms_key_id}"
                self.execute_final_query()
            if prop == tags.USE_PRIVATELINK_ENDPOINT:
                self.qry = f"ALTER {alter_object_name} {self.attr.name[0]} SET {tags.USE_PRIVATELINK_ENDPOINT} = {self.attr.use_privatelink_endpoint}"
                self.execute_final_query()
            if prop == tags.ENABLE:
                self.qry = f"ALTER {alter_object_name} {self.attr.name[0]} SET {tags.ENABLE} = {self.attr.enable}"
                self.execute_final_query()
            if prop == tags.REFRESH_ON_CREATE:
                self.qry = f"ALTER {alter_object_name} {self.attr.name[0]} SET {tags.REFRESH_ON_CREATE} = {self.attr.refresh_on_create}"
                self.execute_final_query()
            if prop == tags.AUTO_REFRESH:
                self.qry = f"ALTER {alter_object_name} {self.attr.name[0]} SET {tags.AUTO_REFRESH} = {self.attr.auto_refresh}"
                self.execute_final_query()
            if prop == tags.NOTIFICATION_INTEGRATION:
                self.qry = f"ALTER {alter_object_name} {self.attr.name[0]} SET {tags.NOTIFICATION_INTEGRATION} = {self.attr.notification_integration}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER {alter_object_name} {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming {self.__class__.__name__} {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()


    def set_create_qry(self):
        self.qry = f"CREATE OR REPLACE STAGE {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.FILE_FORMAT:
                    self.qry = f" {self.qry} {tags.FILE_FORMAT} = {self.attr.database}.{self.attr.schema}.{self.attr.file_format} "
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "
                if prop == tags.URL:
                    self.qry = f" {self.qry} {tags.URL} = {self.attr.url} "
                if prop == tags.AWS_ACCESS_POINT_ARN:
                    self.qry = f" {self.qry} {tags.AWS_ACCESS_POINT_ARN} = {self.attr.aws_access_point_arn} "
                if prop == tags.STORAGE_INTEGRATION:
                    self.qry = f" {self.qry} {tags.STORAGE_INTEGRATION} = {self.attr.storage_integration} "
                if prop == tags.ENCRYPTION_TYPE:
                    self.qry = f" {self.qry} {tags.ENCRYPTION_TYPE} = {self.attr.encryption_type} "
                if prop == tags.ENCRYPTION_MASTER_KEY:
                    self.qry = f" {self.qry} {tags.ENCRYPTION_MASTER_KEY} = {self.attr.encryption_master_key} "
                if prop == tags.ENCRYPTION_KMS_KEY_ID:
                    self.qry = f" {self.qry} {tags.ENCRYPTION_KMS_KEY_ID} = {self.attr.encryption_kms_key_id} "
                if prop == tags.USE_PRIVATELINK_ENDPOINT:
                    self.qry = f" {self.qry} {tags.USE_PRIVATELINK_ENDPOINT} = {self.attr.use_privatelink_endpoint} "
                if prop == tags.ENABLE:
                    self.qry = f" {self.qry} DIRECTORY = ( {tags.ENABLE} = {self.attr.enable} "
                    if tags.REFRESH_ON_CREATE in self.property_lst:
                        self.qry=f" {self.qry} {tags.REFRESH_ON_CREATE} = {self.attr.refresh_on_create}"
                    if tags.AUTO_REFRESH in self.property_lst:
                        self.qry=f" {self.qry} {tags.AUTO_REFRESH} = {self.attr.auto_refresh}"
                    if tags.NOTIFICATION_INTEGRATION in self.property_lst:
                        self.qry=f" {self.qry} {tags.NOTIFICATION_INTEGRATION} = {self.attr.notification_integration}"
                    self.qry=f" {self.qry} )"

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == 'TRUE':
            self.set_create_qry()
            self.add_properties_to_query()
        elif self.is_create=='FALSE':
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()

    def create_external_stage(self):
        self.execute_final_query()

    def create_object(self,**kwargs):
        self.logger.info(f"Operating on {self.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        self.logger.info(f'dictionary passed {kwargs}')
        self.is_create=kwargs[tags.IS_CREATE]

        self.logger.info('set DATABASE')
        self.set_database(kwargs[tags.DATABASE])

        self.logger.info('set SCHEMA')
        self.set_schema(kwargs[tags.SCHEMA])
        
        self.logger.info('set NAME')
        self.set_name(kwargs[tags.NAME])

        self.logger.info('set FILE_FORMAT')
        self.set_file_format(kwargs[tags.FILE_FORMAT])

        self.logger.info('set COMMENT')
        self.set_comment(kwargs[tags.COMMENT])

        self.logger.info('set URL')
        self.set_url(kwargs[tags.URL])

        self.logger.info('set AWS_ACCESS_POINT_ARN')
        self.set_aws_access_point_arn(kwargs[tags.AWS_ACCESS_POINT_ARN])

        self.logger.info('set STORAGE_INTEGRATION')
        self.set_storage_integration(kwargs[tags.STORAGE_INTEGRATION])

        self.logger.info('set ENCRYPTION TYPE')
        self.set_encryption_type(kwargs[tags.ENCRYPTION_TYPE])

        self.logger.info('set ENCRYPTION_MASTER_KEY')
        self.set_encryption_master_key(kwargs[tags.ENCRYPTION_MASTER_KEY])

        self.logger.info('set ENCRYPTION_KMS_KEY_ID')
        self.set_encryption_kms_key_id(kwargs[tags.ENCRYPTION_KMS_KEY_ID])

        self.logger.info('set USE_PRIVATELINK_ENDPOINT')
        self.set_use_privatelink_endpoint(kwargs[tags.USE_PRIVATELINK_ENDPOINT])

        self.logger.info('set ENABLE')
        self.set_enable(kwargs[tags.ENABLE])

        self.logger.info('set REFRESH_ON_CREATE')
        self.set_refresh_on_create(kwargs[tags.REFRESH_ON_CREATE])

        self.logger.info('set AUTO_REFRESH')
        self.set_auto_refresh(kwargs[tags.AUTO_REFRESH])

        self.logger.info('set NOTIFICATION_INTEGRATION')
        self.set_notification_integration(kwargs[tags.NOTIFICATION_INTEGRATION])

        self.logger.info('set qualified name')
        self.set_qualified_name()

        self.logger.info('prepare query')
        self.prepare_query()
        self.execute_final_query()

        self.logger.info('execute query')
        self.create_external_stage()

        self.logger.info('grant default priv')

        self.logger.info('create deployment entry')
        self.create_deployment_entry(object_name=self.attr.name[0],
                                     object_type=self.__class__.__name__,
                                     object_database=self.attr.database,
                                     object_schema=self.attr.schema)
        self.write_file_to_git(object_name=self.attr.name[0],
                               object_type=self.__class__.__name__,
                               object_database=self.attr.database,
                               object_schema=self.attr.schema)
            
class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        obj_inst=ExternalStage(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info("set database")
        if tags.DATABASE in kwargs.keys():
            obj_inst.set_database(kwargs[tags.DATABASE])
        else:
            obj_inst.set_database('NONE')

        logger.info("set schema")
        if tags.SCHEMA in kwargs.keys():
            obj_inst.set_schema(kwargs[tags.SCHEMA])
        else:
            obj_inst.set_schema('NONE')

        logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        logger.info("set file_format")
        if tags.FILE_FORMAT in kwargs.keys():
            obj_inst.set_file_format(kwargs[tags.FILE_FORMAT])
        else:
            obj_inst.set_file_format('NONE')

        logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')

        logger.info("set url")
        if tags.URL in kwargs.keys():
            obj_inst.set_url(kwargs[tags.URL])
        else:
            obj_inst.set_url('NONE')

        logger.info("set aws_access_point_arn")
        if tags.AWS_ACCESS_POINT_ARN in kwargs.keys():
            obj_inst.set_aws_access_point_arn(kwargs[tags.AWS_ACCESS_POINT_ARN])
        else:
            obj_inst.set_aws_access_point_arn('NONE')

        logger.info("set storage_integration")
        if tags.STORAGE_INTEGRATION in kwargs.keys():
            obj_inst.set_storage_integration(kwargs[tags.STORAGE_INTEGRATION])
        else:
            obj_inst.set_storage_integration('NONE')

        logger.info("set encryption_type")
        if tags.ENCRYPTION_TYPE in kwargs.keys():
            obj_inst.set_encryption_type(kwargs[tags.ENCRYPTION_TYPE])
        else:
            obj_inst.set_encryption_type('NONE')

        logger.info("set encryption_master_key")
        if tags.ENCRYPTION_MASTER_KEY in kwargs.keys():
            obj_inst.set_encryption_master_key(kwargs[tags.ENCRYPTION_MASTER_KEY])
        else:
            obj_inst.set_encryption_master_key('NONE')

        logger.info("set encryption_kms_key_id")
        if tags.ENCRYPTION_KMS_KEY_ID in kwargs.keys():
            obj_inst.set_encryption_kms_key_id(kwargs[tags.ENCRYPTION_KMS_KEY_ID])
        else:
            obj_inst.set_encryption_kms_key_id('NONE')

        logger.info("set use_privatelink_endpoint")
        if tags.USE_PRIVATELINK_ENDPOINT in kwargs.keys():
            obj_inst.set_use_privatelink_endpoint(kwargs[tags.USE_PRIVATELINK_ENDPOINT])
        else:
            obj_inst.set_use_privatelink_endpoint('NONE')

        logger.info("set enable")
        if tags.ENABLE in kwargs.keys():
            obj_inst.set_enable(kwargs[tags.ENABLE])
        else:
            obj_inst.set_enable('NONE')

        logger.info("set refresh_on_create")
        if tags.REFRESH_ON_CREATE in kwargs.keys():
            obj_inst.set_refresh_on_create(kwargs[tags.REFRESH_ON_CREATE])
        else:
            obj_inst.set_refresh_on_create('NONE')

        logger.info("set auto_refresh")
        if tags.AUTO_REFRESH in kwargs.keys():
            obj_inst.set_auto_refresh(kwargs[tags.AUTO_REFRESH])
        else:
            obj_inst.set_auto_refresh('NONE')

        logger.info("set notification_integration")
        if tags.NOTIFICATION_INTEGRATION in kwargs.keys():
            obj_inst.set_notification_integration(kwargs[tags.NOTIFICATION_INTEGRATION])
        else:
            obj_inst.set_notification_integration('NONE')


        logger.info('prepare query')
        obj_inst.prepare_query()
        obj_inst.execute_final_query()
        
        obj_inst.logger.info('create deployment entry')
        obj_inst.create_deployment_entry(object_name=obj_inst.attr.name[0],
                                     object_type=obj_inst.__class__.__name__,
                                     object_database=obj_inst.attr.database,
                                     object_schema=obj_inst.attr.schema)
        obj_inst.write_file_to_git(object_name=obj_inst.attr.name[0],
                               object_type=obj_inst.__class__.__name__,
                               object_database=obj_inst.attr.database,
                               object_schema=obj_inst.attr.schema)


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
