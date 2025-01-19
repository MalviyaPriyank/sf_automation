import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../../vars/global'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))


from global_vars import ExternalStage as gv
from validatevalue import ValidateValue as vv

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        if value == "NONE" :
            raise KeyError
        elif not vv.starts_with_alphabet(value):
            raise ValueError
        elif not vv.is_enclosed_in_double_quotes(value):
            if vv.has_space(value):
                raise ValueError
            if vv.has_special_characters(value):
                raise ValueError
            else:
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
        instance._comment = value


    def __del__(self,instance):
        del instance._comment

class CommentTag:
    def __get__(self,instance,owner):
        return instance._comment_tag
    
    def __set__(self,instance,value):
        instance._comment_tag = value

    def __del__(self,instance):
        del instance._comment_tag

class Tag:
    def __get__(self,instance,owner):
        return instance._tag
    
    def __set__(self,instance,value):
        instance._tag = value


    def __del__(self,instance):
        del instance._tag

class TagTag:
    def __get__(self,instance,owner):
        return instance._tag_tag
    
    def __set__(self,instance,value):
        instance._tag_tag = value

    def __del__(self,instance):
        del instance._tag_tag

class Url:
    def __get__(self,instance,owner):
        return instance._url
    
    def __set__(self,instance,value):
        if vv.is_enclosed_in_single_quotes(value):
            instance._url = value
        else:
            raise ValueError

    def __del__(self,instance):
        del instance._url

class UrlTag:
    def __get__(self,instance,owner):
        return instance._url_tag
    
    def __set__(self,instance,value):
        instance._url_tag = value

    def __del__(self,instance):
        del instance._url_tag

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
        instance._aws_key_id = value

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
        instance._aws_secret_key = value

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
        if value not in gv._allowed_values_encryption:
            raise ValueError
        else:
            instance._encryption = value

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
        if vv.is_bool(value):
            instance._directory = value
        else:
            raise ValueError

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
        if vv.is_bool(value):
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
    def __init__(self,session):
        self.attr = ExternalStageAttrs()
        self.session = session
        self.qry = ""

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

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv._name_tag,"_name")
        set_flag(gv._file_format_tag,"_file_format")
        set_flag(gv._comment_tag,"_comment")
        set_flag(gv._tag_tag,"_tag")
        set_flag(gv._url_tag,"_url")
        set_flag(gv._storage_integration_tag,"_storage_integration")
        set_flag(gv._aws_key_id_tag,"_aws_key_id")
        set_flag(gv._aws_secret_key_tag,"_aws_secret_key")
        set_flag(gv._aws_token_tag,"_aws_token")
        set_flag(gv._azure_sas_token_tag,"_azure_sas_token")
        set_flag(gv._aws_role_tag,"_aws_role")
        set_flag(gv._encryption_tag,"_encryption")
        set_flag(gv._encryption_type_tag,"_encryption_type")
        set_flag(gv._encryption_master_key_tag,"_encryption_master_key")
        set_flag(gv._encryption_kms_key_id_tag,"_encryption_kms_key_id")
        set_flag(gv._use_privatelink_endpoint_tag,"_use_privatelink_endpoint")
        set_flag(gv._directory_tag,"_directory")
        set_flag(gv._refresh_on_create_tag,"_refresh_on_create")
        set_flag(gv._auto_refresh_tag,"_auto_refresh")
        set_flag(gv._notification_integration_tag,"_notification_integration")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_qry(self):
        self.qry = f"CREATE STAGE  {self.attr.name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gv._file_format_tag:
                    self.qry = f" {self.qry} {self.attr.file_format_tag} = {self.attr.file_format} "
                if prop == gv._comment_tag:
                    self.qry = f" {self.qry} {self.attr.comment_tag} = {self.attr.comment} "
                if prop == gv._tag_tag:
                    self.qry = f" {self.qry} {self.attr.tag_tag} = {self.attr.tag} "
                if prop == gv._url_tag:
                    self.qry = f" {self.qry} {self.attr.url_tag} = {self.attr.url} "
                if prop == gv._storage_integration_tag:
                    self.qry = f" {self.qry} {self.attr.storage_integration_tag} = {self.attr.storage_integration} "
                if prop == gv._aws_key_id_tag:
                    self.qry = f" {self.qry} {self.attr.aws_key_id_tag} = {self.attr.aws_key_id} "
                if prop == gv._aws_secret_key_tag:
                    self.qry = f" {self.qry} {self.attr.aws_secret_key_tag} = {self.attr.aws_secret_key} "
                if prop == gv._aws_token_tag:
                    self.qry = f" {self.qry} {self.attr.aws_token_tag} = {self.attr.aws_token} "
                if prop == gv._azure_sas_token_tag:
                    self.qry = f" {self.qry} {self.attr.azure_sas_token_tag} = {self.attr.azure_sas_token} "
                if prop == gv._aws_role_tag:
                    self.qry = f" {self.qry} {self.attr.aws_role_tag} = {self.attr.aws_role} "
                if prop == gv._encryption_tag:
                    self.qry = f" {self.qry} {self.attr.encryption_tag} = {self.attr.encryption} "
                if prop == gv._encryption_type_tag:
                    self.qry = f" {self.qry} {self.attr.encryption_type_tag} = {self.attr.encryption_type} "
                if prop == gv._encryption_master_key_tag:
                    self.qry = f" {self.qry} {self.attr.encryption_master_key_tag} = {self.attr.encryption_master_key} "
                if prop == gv._encryption_kms_key_id_tag:
                    self.qry = f" {self.qry} {self.attr.encryption_kms_key_id_tag} = {self.attr.encryption_kms_key_id} "
                if prop == gv._use_privatelink_endpoint_tag:
                    self.qry = f" {self.qry} {self.attr.use_privatelink_endpoint_tag} = {self.attr.use_privatelink_endpoint} "
                if prop == gv._directory_tag:
                    self.qry = f" {self.qry} {self.attr.directory_tag} = {self.attr.directory} "
                if prop == gv._refresh_on_create_tag:
                    self.qry = f" {self.qry} {self.attr.refresh_on_create_tag} = {self.attr.refresh_on_create} "
                if prop == gv._auto_refresh_tag:
                    self.qry = f" {self.qry} {self.attr.auto_refresh_tag} = {self.attr.auto_refresh} "
                if prop == gv._notification_integration_tag:
                    self.qry = f" {self.qry} {self.attr.notification_integration_tag} = {self.attr.notification_integration} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_qry()
        self.add_properties_to_query()

    def create_external_stage(self):
        self.session.sql(self.qry)

    def create_object(session,**kwargs):
        external_stage = ExternalStage(session)

        external_stage.set_name(kwargs[gv._name_tag])
        external_stage.set_name_tag(gv._name_tag)

        external_stage.set_file_format(kwargs[gv._file_format_tag])
        external_stage.set_file_format_tag(gv._file_format_tag)

        external_stage.set_comment(kwargs[gv._comment_tag])
        external_stage.set_comment_tag(gv._comment_tag)

        external_stage.set_tag(kwargs[gv._tag_tag])
        external_stage.set_tag_tag(gv._tag_tag)

        external_stage.set_url(kwargs[gv._url_tag])
        external_stage.set_url_tag(gv._url_tag)

        external_stage.set_storage_integration(kwargs[gv._storage_integration_tag])
        external_stage.set_storage_integration_tag(gv._storage_integration_tag)

        external_stage.set_aws_key_id(kwargs[gv._aws_key_id_tag])
        external_stage.set_aws_key_id_tag(gv._aws_key_id_tag)

        external_stage.set_aws_secret_key(kwargs[gv._aws_secret_key_tag])
        external_stage.set_aws_secret_key_tag(gv._aws_secret_key_tag)

        external_stage.set_aws_token(kwargs[gv._aws_token_tag])
        external_stage.set_aws_token_tag(gv._aws_token_tag)

        external_stage.set_azure_sas_token(kwargs[gv._azure_sas_token_tag])
        external_stage.set_azure_sas_token_tag(gv._azure_sas_token_tag)

        external_stage.set_aws_role(kwargs[gv._aws_role_tag])
        external_stage.set_aws_role_tag(gv._aws_role_tag)

        external_stage.set_encryption(kwargs[gv._encryption_tag])
        external_stage.set_encryption_tag(gv._encryption_tag)

        external_stage.set_encryption_type(kwargs[gv._encryption_type_tag])
        external_stage.set_encryption_type_tag(gv._encryption_type_tag)

        external_stage.set_encryption_master_key(kwargs[gv._encryption_master_key_tag])
        external_stage.set_encryption_master_key_tag(gv._encryption_master_key_tag)

        external_stage.set_encryption_kms_key_id(kwargs[gv._encryption_kms_key_id_tag])
        external_stage.set_encryption_kms_key_id_tag(gv._encryption_kms_key_id_tag)

        external_stage.set_use_privatelink_endpoint(kwargs[gv._use_privatelink_endpoint_tag])
        external_stage.set_use_privatelink_endpoint_tag(gv._use_privatelink_endpoint_tag)

        external_stage.set_directory(kwargs[gv._directory_tag])
        external_stage.set_directory_tag(gv._directory_tag)

        external_stage.set_refresh_on_create(kwargs[gv._refresh_on_create_tag])
        external_stage.set_refresh_on_create_tag(gv._refresh_on_create_tag)

        external_stage.set_auto_refresh(kwargs[gv._auto_refresh_tag])
        external_stage.set_auto_refresh_tag(gv._auto_refresh_tag)

        external_stage.set_notification_integration(kwargs[gv._notification_integration_tag])
        external_stage.set_notification_integration_tag(gv._notification_integration_tag)

        external_stage.prepare_query()
        external_stage.create_external_stage()

        



