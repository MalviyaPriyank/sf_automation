import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))


from vars.gvobject import ExternalStage as gvextstg,Config as cfg,Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from dep.deploy import Deploy
from setup import privilege


class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.database_exist(session=instance.parent.session, database_name=value)
        #if vo.database_exist(value):
        instance._database = value

    def __del__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.schema_exist(session=instance.parent.session, database_name=instance._database, schema_name=value)
        #if vo.schema_exist(instance._database,value):
        instance._schema = value

    def __del__(self,instance):
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
            vo.is_new_stage(session=instance.parent.session,database=instance._database,schema=instance._schema,stage=value,obj_type=instance.parent.__class__.__name__,obj_name=self.__class__.__name__)
            instance._name = value

    def __del__(self,instance):
        del instance._name

class NameTag:
    def __get__(self,instance,owner):
        return instance._name_tag
    
    def __set__(self,instance,value):
        instance._name_tag = value

    def __del__(self,instance):
        del instance._name_tag



class FileFormat:   
    def __get__(self,instance,owner):
        return instance._file_format
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._file_format=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vo.is_new_file_format(session=instance.parent.session,database_name=instance._database,schema_name=instance._schema,file_format_name=value)
            instance._file_format = value

    def __del__(self,instance):
        del instance._file_format


class FileFormatTag:   
    def __get__(self,instance,owner):
        return instance._file_format_tag
    
    def __set__(self,instance,value):
        instance._file_format_tag = value

    def __del__(self,instance):
        del instance._file_format_tag

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        if value=="NONE":
            instance._comment=value
        else:
            instance._comment = f"'{value}'"

    def __del__(self,instance):
        del instance._comment

class CommentTag:
    def __get__(self,instance,owner):
        return instance._comment_tag
    
    def __set__(self,instance,value):
        instance._comment_tag = value

    def __del__(self,instance):
        del instance._comment_tag

class Url:
    def __get__(self,instance,owner):
        return instance._url
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._url = value
        else:
            vv.is_valid_url(value=value,allowed_protocols=gvextstg._allowed_values_protocols,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._url = f"'{value}'"

    def __del__(self,instance):
        del instance._url

class UrlTag:
    def __get__(self,instance,owner):
        return instance._url_tag
    
    def __set__(self,instance,value):
        instance._url_tag = value

    def __del__(self,instance):
        del instance._url_tag

class AwsAccessPointArn:
    def __get__(self,instance,owner):
        return instance._aws_access_point_arn
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._aws_access_point_arn = value
        else:
            instance._aws_access_point_arn = f"'{value}'"

    def __del__(self,instance):
        del instance._aws_access_point_arn

class StorageIntegration:
    def __get__(self,instance,owner):
        return instance._storage_integration
    
    def __set__(self,instance,value):
        instance._storage_integration = value

    def __del__(self,instance):
        del instance._storage_integration

class StorageIntegrationTag:
    def __get__(self,instance,owner):
        return instance._storage_integration_tag
    
    def __set__(self,instance,value):
        instance._storage_integration_tag = value

    def __del__(self,instance):
        del instance._storage_integration_tag

class AwsKeyId:
    def __get__(self,instance,owner):
        return instance._aws_key_id
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._aws_key_id=value
        else:
            instance._aws_key_id=f"'{value}'"

    def __del__(self,instance):
        del instance._aws_key_id

class AwsKeyIdTag:
    def __get__(self,instance,owner):
        return instance._aws_key_id_tag
    
    def __set__(self,instance,value):
        instance._aws_key_id_tag = value

    def __del__(self,instance):
        del instance._aws_key_id_tag

class AwsSecretKey:
    def __get__(self,instance,owner):
        return instance._aws_secret_key
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._aws_secret_key=value
        else:
            instance._aws_secret_key = f"'{value}'"

    def __del__(self,instance):
        del instance._aws_secret_key

class AwsSecretKeyTag:
    def __get__(self,instance,owner):
        return instance._aws_secret_key_tag
    
    def __set__(self,instance,value):
        instance._aws_secret_key_tag = value

    def __del__(self,instance):
        del instance._aws_secret_key_tag

class AwsToken:
    def __get__(self,instance,owner):
        return instance._aws_token
    
    def __set__(self,instance,value):
        instance._aws_token = value


    def __del__(self,instance):
        del instance._aws_token

class AwsTokenTag:
    def __get__(self,instance,owner):
        return instance._aws_token_tag
    
    def __set__(self,instance,value):
        instance._aws_token_tag = value

    def __del__(self,instance):
        del instance._aws_token_tag

class AzureSasToken:
    def __get__(self,instance,owner):
        return instance._azure_sas_token
    
    def __set__(self,instance,value):
        instance._azure_sas_token = value

    def __del__(self,instance):
        del instance._azure_sas_token

class AzureSasTokenTag:
    def __get__(self,instance,owner):
        return instance._azure_sas_token_tag
    
    def __set__(self,instance,value):
        instance._azure_sas_token_tag = value

    def __del__(self,instance):
        del instance._azure_sas_token_tag

class AwsRole:
    def __get__(self,instance,owner):
        return instance._aws_role
    
    def __set__(self,instance,value):
        instance._aws_role = value

    def __del__(self,instance):
        del instance._aws_role

class AwsRoleTag:
    def __get__(self,instance,owner):
        return instance._aws_role_tag
    
    def __set__(self,instance,value):
        instance._aws_role_tag = value

    def __del__(self,instance):
        del instance._aws_role_tag

class Encryption:
    def __get__(self,instance,owner):
        return instance._encryption
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._encryption=value
        else:
            instance._encryption=value

    def __del__(self,instance):
        del instance._encryption

class EncryptionTag:
    def __get__(self,instance,owner):
        return instance._encryption_tag
    
    def __set__(self,instance,value):
        instance._encryption_tag = value

    def __del__(self,instance):
        del instance._encryption_tag

class EncryptionType:
    def __get__(self,instance,owner):
        return instance._encryption_type
    
    def __set__(self,instance,value):
        instance._encryption_type = value

    def __del__(self,instance):
        del instance._encryption_type

class EncryptionTypeTag:
    def __get__(self,instance,owner):
        return instance._encryption_type_tag
    
    def __set__(self,instance,value):
        instance._encryption_type_tag = value

    def __del__(self,instance):
        del instance._encryption_type_tag

class EncryptionMasterKey:
    def __get__(self,instance,owner):
        return instance._encryption_master_key
    
    def __set__(self,instance,value):
        instance._encryption_master_key = value

    def __del__(self,instance):
        del instance._encryption_master_key

class EncryptionMasterKeyTag:
    def __get__(self,instance,owner):
        return instance._encryption_master_key_tag
    
    def __set__(self,instance,value):
        instance._encryption_master_key_tag = value

    def __del__(self,instance):
        del instance._encryption_master_key_tag

class EncryptionKmsKeyId:
    def __get__(self,instance,owner):
        return instance._encryption_kms_key_id
    
    def __set__(self,instance,value):
        instance._encryption_kms_key_id = value

    def __del__(self,instance):
        del instance._encryption_kms_key_id

class EncryptionKmsKeyIdTag:
    def __get__(self,instance,owner):
        return instance._encryption_kms_key_id_tag
    
    def __set__(self,instance,value):
        instance._encryption_kms_key_id_tag = value

    def __del__(self,instance):
        del instance._encryption_kms_key_id_tag

class UsePrivatelinkEndpoint:
    def __get__(self,instance,owner):
        return instance._use_privatelink_endpoint
    
    def __set__(self,instance,value):
        instance._use_privatelink_endpoint = value

    def __del__(self,instance):
        del instance._use_privatelink_endpoint

class UsePrivatelinkEndpointTag:
    def __get__(self,instance,owner):
        return instance._use_privatelink_endpoint_tag
    
    def __set__(self,instance,value):
        instance._use_privatelink_endpoint_tag = value

    def __del__(self,instance):
        del instance._use_privatelink_endpoint_tag

class Directory:
    def __get__(self,instance,owner):
        return instance._directory
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._directory = value
        elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._directory = value


    def __del__(self,instance):
        del instance._directory

class DirectoryTag:
    def __get__(self,instance,owner):
        return instance._directory_tag
    
    def __set__(self,instance,value):
        instance._directory_tag = value

    def __del__(self,instance):
        del instance._directory_tag

class RefreshOnCreate:
    def __get__(self,instance,owner):
        return instance._refresh_on_create
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._refresh_on_create = value
        elif vv.is_bool(value,instance.parent.__class__.__name__,self.__class__.__name__):
            instance._refresh_on_create = value
        else:
            raise ValueError

    def __del__(self,instance):
        del instance._refresh_on_create

class RefreshOnCreateTag:
    def __get__(self,instance,owner):
        return instance._refresh_on_create_tag
    
    def __set__(self,instance,value):
        instance._refresh_on_create_tag = value

    def __del__(self,instance):
        del instance._refresh_on_create_tag

class AutoRefresh:
    def __get__(self,instance,owner):
        return instance._auto_refresh
    
    def __set__(self,instance,value):
        instance._auto_refresh = value


    def __del__(self,instance):
        del instance._auto_refresh

class AutoRefreshTag:
    def __get__(self,instance,owner):
        return instance._auto_refresh_tag
    
    def __set__(self,instance,value):
        instance._auto_refresh_tag = value

    def __del__(self,instance):
        del instance._auto_refresh_tag

class NotificationIntegration:
    def __get__(self,instance,owner):
        return instance._notification_integration
    
    def __set__(self,instance,value):
        instance._notification_integration = value

    def __del__(self,instance):
        del instance._notification_integration

class NotificationIntegrationTag:
    def __get__(self,instance,owner):
        return instance._notification_integration_tag
    
    def __set__(self,instance,value):
        instance._notification_integration_tag = value

    def __del__(self,instance):
        del instance._notification_integration_tag

class ExternalStageAttrs:
    def __init__(self,parent):
        self.parent = parent

    database=Database()
    schema=Schema()

    name = Name()
    name_tag = NameTag()

    file_format = FileFormat()
    file_format_tag = FileFormatTag()

    comment = Comment()
    comment_tag = CommentTag()
    
    tag = Tag()
    tag_tag = TagTag()

    url = Url()
    url_tag = UrlTag()

    aws_access_point_arn=AwsAccessPointArn()

    storage_integration = StorageIntegration()
    storage_integration_tag = StorageIntegrationTag()

    aws_key_id = AwsKeyId()
    aws_key_id_tag = AwsKeyIdTag()

    aws_secret_key = AwsSecretKey()
    aws_secret_key_tag = AwsSecretKeyTag()

    aws_token = AwsToken()
    aws_token_tag = AwsTokenTag()

    azure_sas_token = AzureSasToken()
    azure_sas_token_tag = AzureSasTokenTag()

    aws_role = AwsRole()
    aws_role_tag = AwsRoleTag()

    encryption = Encryption()
    encryption_tag = EncryptionTag()

    encryption_type = EncryptionType()
    encryption_type_tag = EncryptionTypeTag()

    encryption_master_key = EncryptionMasterKey()
    encryption_master_key_tag = EncryptionMasterKeyTag()

    encryption_kms_key_id = EncryptionKmsKeyId()
    encryption_kms_key_id_tag = EncryptionKmsKeyIdTag()

    use_privatelink_endpoint = UsePrivatelinkEndpoint()
    use_privatelink_endpoint_tag = UsePrivatelinkEndpointTag()

    directory = Directory()
    directory_tag = DirectoryTag()

    refresh_on_create = RefreshOnCreate()
    refresh_on_create_tag = RefreshOnCreateTag()

    auto_refresh = AutoRefresh()
    auto_refresh_tag = AutoRefreshTag()

    notification_integration = NotificationIntegration()
    notification_integration_tag = NotificationIntegrationTag()

class ExternalStage:
    def __init__(self,session,user_id,logger):
        self.session = session
        self.sf_object_tag = "STAGE"
        self.qry = ""
        self.logger = logger
        self.user_id=user_id
        self.attr = ExternalStageAttrs(self)

    def set_database(self,val):
        self.attr.database=val

    def set_schema(self,val):
        self.attr.schema=val

    def set_name(self,val):
        self.attr.name = val
    
    def set_name_tag(self,val):
        self.attr.name_tag = val

    def set_file_format(self,val):
        self.attr.file_format = val
    
    def set_file_format_tag(self,val):
        self.attr.file_format_tag = val
    
    def set_comment(self,val):
        self.attr.comment = val
    
    def set_comment_tag(self,val):
        self.attr.comment_tag = val

    def set_tag(self,val):
        self.attr.tag = val
    
    def set_tag_tag(self,val):
        self.attr.tag_tag = val

    def set_url(self,val):
        self.attr.url = val
    
    def set_url_tag(self,val):
        self.attr.url_tag = val

    def set_aws_access_point_arn(self,val):
        self.attr.aws_access_point_arn=val

    def set_storage_integration(self,val):
        self.attr.storage_integration = val
    
    def set_storage_integration_tag(self,val):
        self.attr.storage_integration_tag = val

    def set_aws_key_id(self,val):
        self.attr.aws_key_id = val
    
    def set_aws_key_id_tag(self,val):
        self.attr.aws_key_id_tag = val

    def set_aws_secret_key(self,val):
        self.attr.aws_secret_key = val
    
    def set_aws_secret_key_tag(self,val):
        self.attr.aws_secret_key_tag = val

    def set_aws_token(self,val):
        self.attr.aws_token = val
    
    def set_aws_token_tag(self,val):
        self.attr.aws_token_tag = val

    def set_azure_sas_token(self,val):
        self.attr.azure_sas_token = val
    
    def set_azure_sas_token_tag(self,val):
        self.attr.azure_sas_token_tag = val

    def set_aws_role(self,val):
        self.attr.aws_role = val
    
    def set_aws_role_tag(self,val):
        self.attr.aws_role_tag = val

    def set_encryption(self,val):
        self.attr.encryption = val
    
    def set_encryption_tag(self,val):
        self.attr.encryption_tag = val

    def set_encryption_type(self,val):
        self.attr.encryption_type = val
    
    def set_encryption_type_tag(self,val):
        self.attr.encryption_type_tag = val

    def set_encryption_master_key(self,val):
        self.attr.encryption_master_key = val
    
    def set_encryption_master_key_tag(self,val):
        self.attr.encryption_master_key_tag = val

    def set_encryption_kms_key_id(self,val):
        self.attr.encryption_kms_key_id = val
    
    def set_encryption_kms_key_id_tag(self,val):
        self.attr.encryption_kms_key_id_tag = val

    def set_use_privatelink_endpoint(self,val):
        self.attr.use_privatelink_endpoint = val
    
    def set_use_privatelink_endpoint_tag(self,val):
        self.attr.use_privatelink_endpoint_tag = val

    def set_directory(self,val):
        self.attr.directory = val
    
    def set_directory_tag(self,val):
        self.attr.directory_tag = val

    def set_refresh_on_create(self,val):
        self.attr.refresh_on_create = val
    
    def set_refresh_on_create_tag(self,val):
        self.attr.refresh_on_create_tag = val

    def set_auto_refresh(self,val):
        self.attr.auto_refresh = val
    
    def set_auto_refresh_tag(self,val):
        self.attr.auto_refresh_tag = val

    def set_notification_integration(self,val):
        self.attr.notification_integration = val

    def set_notification_integration_tag(self,val):
        self.attr.notification_integration_tag = val
    
    def set_qualified_name(self):
        self.qualified_name = f"{self.attr.database}.{self.attr.schema}.{self.attr.name}"

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gvextstg._name_tag,"_name")
        set_flag(gvextstg._file_format_tag,"_file_format")
        set_flag(gvextstg._comment_tag,"_comment")
        set_flag(gvextstg._tag_tag,"_tag")
        set_flag(gvextstg._url_tag,"_url")
        set_flag(gvextstg._aws_access_point_arn_tag,"_aws_access_point_arn")
        set_flag(gvextstg._storage_integration_tag,"_storage_integration")
        set_flag(gvextstg._aws_key_id_tag,"_aws_key_id")
        set_flag(gvextstg._aws_secret_key_tag,"_aws_secret_key")
        set_flag(gvextstg._aws_token_tag,"_aws_token")
        set_flag(gvextstg._azure_sas_token_tag,"_azure_sas_token")
        set_flag(gvextstg._aws_role_tag,"_aws_role")
        set_flag(gvextstg._encryption_tag,"_encryption")
        set_flag(gvextstg._encryption_type_tag,"_encryption_type")
        set_flag(gvextstg._encryption_master_key_tag,"_encryption_master_key")
        set_flag(gvextstg._encryption_kms_key_id_tag,"_encryption_kms_key_id")
        set_flag(gvextstg._use_privatelink_endpoint_tag,"_use_privatelink_endpoint")
        set_flag(gvextstg._directory_tag,"_directory")
        set_flag(gvextstg._refresh_on_create_tag,"_refresh_on_create")
        set_flag(gvextstg._auto_refresh_tag,"_auto_refresh")
        set_flag(gvextstg._notification_integration_tag,"_notification_integration")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_qry(self):
        self.qry = f"CREATE STAGE {self.attr.database}.{self.attr.schema}.{self.attr.name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gvextstg._file_format_tag:
                    self.qry = f" {self.qry} {self.attr.file_format_tag} = {self.attr.file_format} "
                if prop == gvextstg._comment_tag:
                    self.qry = f" {self.qry} {self.attr.comment_tag} = {self.attr.comment} "
                if prop == gvextstg._tag_tag:
                    self.qry = f" {self.qry} {self.attr.tag_tag} = {self.attr.tag} "
                if prop == gvextstg._url_tag:
                    self.qry = f" {self.qry} {self.attr.url_tag} = {self.attr.url} "
                if prop == gvextstg._aws_access_point_arn_tag:
                    self.qry = f" {self.qry} {gvextstg._aws_access_point_arn_tag} = {self.attr.aws_access_point_arn} "
                if prop == gvextstg._storage_integration_tag:
                    self.qry = f" {self.qry} {self.attr.storage_integration_tag} = {self.attr.storage_integration} "
                if prop == gvextstg._aws_key_id_tag:
                    self.qry = f" {self.qry} {self.attr.aws_key_id_tag} = {self.attr.aws_key_id} "
                if prop == gvextstg._aws_secret_key_tag:
                    self.qry = f" {self.qry} {self.attr.aws_secret_key_tag} = {self.attr.aws_secret_key} "
                if prop == gvextstg._aws_token_tag:
                    self.qry = f" {self.qry} {self.attr.aws_token_tag} = {self.attr.aws_token} "
                if prop == gvextstg._azure_sas_token_tag:
                    self.qry = f" {self.qry} {self.attr.azure_sas_token_tag} = {self.attr.azure_sas_token} "
                if prop == gvextstg._aws_role_tag:
                    self.qry = f" {self.qry} {self.attr.aws_role_tag} = {self.attr.aws_role} "
                if prop == gvextstg._encryption_tag:
                    self.qry = f" {self.qry} {self.attr.encryption_tag} = {self.attr.encryption} "
                if prop == gvextstg._encryption_type_tag:
                    self.qry = f" {self.qry} {self.attr.encryption_type_tag} = {self.attr.encryption_type} "
                if prop == gvextstg._encryption_master_key_tag:
                    self.qry = f" {self.qry} {self.attr.encryption_master_key_tag} = {self.attr.encryption_master_key} "
                if prop == gvextstg._encryption_kms_key_id_tag:
                    self.qry = f" {self.qry} {self.attr.encryption_kms_key_id_tag} = {self.attr.encryption_kms_key_id} "
                if prop == gvextstg._use_privatelink_endpoint_tag:
                    self.qry = f" {self.qry} {self.attr.use_privatelink_endpoint_tag} = {self.attr.use_privatelink_endpoint} "
                if prop == gvextstg._directory_tag:
                    self.qry = f" {self.qry} {self.attr.directory_tag} = {self.attr.directory} "
                if prop == gvextstg._refresh_on_create_tag:
                    self.qry = f" {self.qry} {self.attr.refresh_on_create_tag} = {self.attr.refresh_on_create} "
                if prop == gvextstg._auto_refresh_tag:
                    self.qry = f" {self.qry} {self.attr.auto_refresh_tag} = {self.attr.auto_refresh} "
                if prop == gvextstg._notification_integration_tag:
                    self.qry = f" {self.qry} {self.attr.notification_integration_tag} = {self.attr.notification_integration} "
        self.qry = f'{self.qry} STORAGE_INTEGRATION=SNOWCHAIN_S3_INT'

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_qry()
        self.add_properties_to_query()

    def grant_default_privileges(self):
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges[self.sf_object_tag]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = self.sf_object_tag,object_identifier=self.qualified_name,role = role)


    def create_deployment_entry(self):
        deploy_inst = Deploy(self.session)
        self.logger.info(f"Tracking for deployment internal stage object : {self.attr.name}")
        deploy_inst.insert_into_deployment_script_table(obj_qry=self.qry, user_id=self.user_id)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database(self.attr.database)
        deploy_inst.set_object_schema(self.attr.schema)
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()

    def create_external_stage(self):
        self.session.sql(self.qry).collect()

    def create_object(self,**kwargs):

        self.set_database(kwargs[gvextstg._database_tag])
        self.set_schema(kwargs[gvextstg._schema_tag])
        
        self.set_name(kwargs[gvextstg._name_tag])
        self.set_name_tag(gvextstg._name_tag)

        self.set_file_format(kwargs[gvextstg._file_format_tag])
        self.set_file_format_tag(gvextstg._file_format_tag)

        self.set_comment(kwargs[gvextstg._comment_tag])
        self.set_comment_tag(gvextstg._comment_tag)

        self.set_tag(kwargs[gvextstg._tag_tag])
        self.set_tag_tag(gvextstg._tag_tag)

        self.set_url(kwargs[gvextstg._url_tag])
        self.set_url_tag(gvextstg._url_tag)

        self.set_aws_access_point_arn(kwargs[gvextstg._aws_access_point_arn_tag])

        self.set_storage_integration(kwargs[gvextstg._storage_integration_tag])
        self.set_storage_integration_tag(gvextstg._storage_integration_tag)

        self.set_aws_key_id(kwargs[gvextstg._aws_key_id_tag])
        self.set_aws_key_id_tag(gvextstg._aws_key_id_tag)

        self.set_aws_secret_key(kwargs[gvextstg._aws_secret_key_tag])
        self.set_aws_secret_key_tag(gvextstg._aws_secret_key_tag)

        self.set_aws_token(kwargs[gvextstg._aws_token_tag])
        self.set_aws_token_tag(gvextstg._aws_token_tag)

        self.set_azure_sas_token(kwargs[gvextstg._azure_sas_token_tag])
        self.set_azure_sas_token_tag(gvextstg._azure_sas_token_tag)

        self.set_aws_role(kwargs[gvextstg._aws_role_tag])
        self.set_aws_role_tag(gvextstg._aws_role_tag)

        self.set_encryption(kwargs[gvextstg._encryption_tag])
        self.set_encryption_tag(gvextstg._encryption_tag)

        self.set_encryption_type(kwargs[gvextstg._encryption_type_tag])
        self.set_encryption_type_tag(gvextstg._encryption_type_tag)

        self.set_encryption_master_key(kwargs[gvextstg._encryption_master_key_tag])
        self.set_encryption_master_key_tag(gvextstg._encryption_master_key_tag)

        self.set_encryption_kms_key_id(kwargs[gvextstg._encryption_kms_key_id_tag])
        self.set_encryption_kms_key_id_tag(gvextstg._encryption_kms_key_id_tag)

        self.set_use_privatelink_endpoint(kwargs[gvextstg._use_privatelink_endpoint_tag])
        self.set_use_privatelink_endpoint_tag(gvextstg._use_privatelink_endpoint_tag)

        self.set_directory(kwargs[gvextstg._directory_tag])
        self.set_directory_tag(gvextstg._directory_tag)

        self.set_refresh_on_create(kwargs[gvextstg._refresh_on_create_tag])
        self.set_refresh_on_create_tag(gvextstg._refresh_on_create_tag)

        self.set_auto_refresh(kwargs[gvextstg._auto_refresh_tag])
        self.set_auto_refresh_tag(gvextstg._auto_refresh_tag)

        self.set_notification_integration(kwargs[gvextstg._notification_integration_tag])
        self.set_notification_integration_tag(gvextstg._notification_integration_tag)

        self.set_qualified_name()
        self.prepare_query()
        self.create_external_stage()
        self.grant_default_privileges()
        self.create_deployment_entry()

        



