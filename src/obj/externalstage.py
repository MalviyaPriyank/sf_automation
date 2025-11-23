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
from src.usr.user import ChatHistory

class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)
    
    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_stage(session=instance.parent.session,database=instance.parent.attr.database,schema=instance.parent.attr.schema,stage=name,obj_type=instance.parent.__class__.__name__,obj_name=self.__class__.__name__)
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
                vo.stage_exist(session=instance.parent.session,database_name=instance.parent.attr.database,schema_name=instance.parent.attr.schema,stage_name=old_name)
                vo.is_new_stage(session=instance.parent.session,database=instance.parent.attr.database,schema=instance.parent.attr.schema,stage=new_name,obj_type=instance.parent.__class__.__name__,obj_name=self.__class__.__name__)
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
            vo.file_format_exist(session=instance.parent.session,database_name=instance.parent.attr.database,schema_name=instance.parent.attr.schema,file_format_name=value)
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
        super().__init__(session, user_id, logger,database_required=True,schema_required=True)
        self.sf_object_tag = "STAGE"
        self.attr = ExternalStageAttrs(self)

    def set_name(self,val):
        self.attr.name = val

    def set_file_format(self,val):
        self.attr.file_format = val


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
        set_flag(tags.COMMENT,"comment")
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
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.FILE_FORMAT} = {self.attr.file_format}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()
            if prop == tags.URL:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.URL} = {self.attr.url}"
                self.execute_final_query()
            if prop == tags.AWS_ACCESS_POINT_ARN:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.AWS_ACCESS_POINT_ARN} = {self.attr.aws_access_point_arn}"
                self.execute_final_query()
            if prop == tags.STORAGE_INTEGRATION:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.STORAGE_INTEGRATION} = {self.attr.storage_integration}"
                self.execute_final_query()
            if prop == tags.ENCRYPTION_TYPE:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.ENCRYPTION_TYPE} = {self.attr.encryption_type}"
                self.execute_final_query()
            if prop == tags.ENCRYPTION_MASTER_KEY:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.ENCRYPTION_MASTER_KEY} = {self.attr.encryption_master_key}"
                self.execute_final_query()
            if prop == tags.ENCRYPTION_KMS_KEY_ID:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.ENCRYPTION_KMS_KEY_ID} = {self.attr.encryption_kms_key_id}"
                self.execute_final_query()
            if prop == tags.USE_PRIVATELINK_ENDPOINT:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.USE_PRIVATELINK_ENDPOINT} = {self.attr.use_privatelink_endpoint}"
                self.execute_final_query()
            if prop == tags.ENABLE:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.ENABLE} = {self.attr.enable}"
                self.execute_final_query()
            if prop == tags.REFRESH_ON_CREATE:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.REFRESH_ON_CREATE} = {self.attr.refresh_on_create}"
                self.execute_final_query()
            if prop == tags.AUTO_REFRESH:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.AUTO_REFRESH} = {self.attr.auto_refresh}"
                self.execute_final_query()
            if prop == tags.NOTIFICATION_INTEGRATION:
                self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.NOTIFICATION_INTEGRATION} = {self.attr.notification_integration}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER {alter_object_name} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} RENAME TO {self.attr.database}.{self.attr.schema}.{self.attr.name[1]}"
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

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=ExternalStage(session=session,
                         user_id=user_id,
                         logger=logger)
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.set_base_attributes(kwargs=kwargs)

        
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')
        obj_inst.logger.info(f"set name {obj_inst.attr.name[0]}")

        
        if tags.FILE_FORMAT in kwargs.keys():
            obj_inst.set_file_format(kwargs[tags.FILE_FORMAT])
        else:
            obj_inst.set_file_format('NONE')
        obj_inst.logger.info(f"set file_format {obj_inst.attr.file_format}")


        
        if tags.URL in kwargs.keys():
            obj_inst.set_url(kwargs[tags.URL])
        else:
            obj_inst.set_url('NONE')
        obj_inst.logger.info(f"set url {obj_inst.attr.url}")

        
        if tags.AWS_ACCESS_POINT_ARN in kwargs.keys():
            obj_inst.set_aws_access_point_arn(kwargs[tags.AWS_ACCESS_POINT_ARN])
        else:
            obj_inst.set_aws_access_point_arn('NONE')
        obj_inst.logger.info(f"set aws_access_point_arn {obj_inst.attr.aws_access_point_arn}")

        
        if tags.STORAGE_INTEGRATION in kwargs.keys():
            obj_inst.set_storage_integration(kwargs[tags.STORAGE_INTEGRATION])
        else:
            obj_inst.set_storage_integration('NONE')
        obj_inst.logger.info(f"set storage_integration {obj_inst.attr.storage_integration}")

        
        if tags.ENCRYPTION_TYPE in kwargs.keys():
            obj_inst.set_encryption_type(kwargs[tags.ENCRYPTION_TYPE])
        else:
            obj_inst.set_encryption_type('NONE')
        obj_inst.logger.info(f"set encryption_type {obj_inst.attr.encryption_type}")

        
        if tags.ENCRYPTION_MASTER_KEY in kwargs.keys():
            obj_inst.set_encryption_master_key(kwargs[tags.ENCRYPTION_MASTER_KEY])
        else:
            obj_inst.set_encryption_master_key('NONE')
        obj_inst.logger.info(f"set encryption_master_key {obj_inst.attr.encryption_master_key}")

        
        if tags.ENCRYPTION_KMS_KEY_ID in kwargs.keys():
            obj_inst.set_encryption_kms_key_id(kwargs[tags.ENCRYPTION_KMS_KEY_ID])
        else:
            obj_inst.set_encryption_kms_key_id('NONE')
        obj_inst.logger.info(f"set encryption_kms_key_id {obj_inst.attr.encryption_kms_key_id}")

        
        if tags.USE_PRIVATELINK_ENDPOINT in kwargs.keys():
            obj_inst.set_use_privatelink_endpoint(kwargs[tags.USE_PRIVATELINK_ENDPOINT])
        else:
            obj_inst.set_use_privatelink_endpoint('NONE')
        obj_inst.logger.info(f"set use_privatelink_endpoint {obj_inst.attr.use_privatelink_endpoint}")

        
        if tags.ENABLE in kwargs.keys():
            obj_inst.set_enable(kwargs[tags.ENABLE])
        else:
            obj_inst.set_enable('NONE')
        obj_inst.logger.info(f"set enable {obj_inst.attr.enable}")

        
        if tags.REFRESH_ON_CREATE in kwargs.keys():
            obj_inst.set_refresh_on_create(kwargs[tags.REFRESH_ON_CREATE])
        else:
            obj_inst.set_refresh_on_create('NONE')
        obj_inst.logger.info(f"set refresh_on_create {obj_inst.attr.refresh_on_create}")

        
        if tags.AUTO_REFRESH in kwargs.keys():
            obj_inst.set_auto_refresh(kwargs[tags.AUTO_REFRESH])
        else:
            obj_inst.set_auto_refresh('NONE')
        obj_inst.logger.info(f"set auto_refresh {obj_inst.attr.auto_refresh}")

        
        if tags.NOTIFICATION_INTEGRATION in kwargs.keys():
            obj_inst.set_notification_integration(kwargs[tags.NOTIFICATION_INTEGRATION])
        else:
            obj_inst.set_notification_integration('NONE')
        obj_inst.logger.info(f"set notification_integration {obj_inst.attr.notification_integration}")


        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        obj_inst.execute_final_query()
        obj_inst.print_query()
        
        obj_inst.logger.info('create deployment entry')
        obj_inst.create_deployment_entry(object_name=obj_inst.attr.name[0],
                                     object_type=obj_inst.__class__.__name__,
                                     object_database=obj_inst.attr.database,
                                     object_schema=obj_inst.attr.schema)
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
