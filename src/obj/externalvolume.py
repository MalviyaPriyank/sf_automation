import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.externalvolume.gvexternalvolume import ExternalVolumeTag as tags
from src.usr.user import ChatHistory
from src.validation.validatevalue import ValidateValue as vv
from src.validation.validateobject import ValidateObject as vo

class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)

    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(
                name,
                instance.parent.__class__.__name__,
                self.__class__.__name__
                )
            vo.is_new_object(
                session=instance.parent.session,
                object_type=instance.parent.object_type,
                object_name=name
            )
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
                vv.required_attribute_check(
                    old_name,
                    instance.parent.__class__.__name__,
                    self.__class__.__name__
                )
                vo.object_exist(
                    session=instance.parent.session,
                    object_type=instance.parent.object_type,
                    object_name=old_name
                )
                vo.is_new_object(
                    session=instance.parent.session,
                    object_type=instance.parent.object_type,
                    object_name=new_name
                )
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to

class StorageLocationName:
    def __get__(self, instance, owner):
        return instance._storage_location_name
    
    def __set__(self, instance, value):
        vv.required_attribute_check(
            value=value,
            object_type=instance.parent.object_type,
            attr_name=self.__class__.__name__
        )
        instance._storage_location_name = value
    def __delete__(self, instance):
        del instance._storage_location_name

class StorageProvider:
    def __get__(self, instance, owner):
        return instance._storage_provider
    
    def __set__(self, instance, value):
        vv.required_attribute_check(
            value=value,
            object_type=instance.parent.object_type,
            attr_name=self.__class__.__name__
        )
        vv.is_allowed_value(
            value=value,
            allowed_list=tags.allowed_value_list().get(tags.STORAGE_PROVIDER),
            object_type=instance.parent.object_type,
            attr_name=self.__class__.__name__
        )
        instance._storage_provider = value
    def __delete__(self, instance):
        del instance._storage_provider

class StorageAWSRoleARN: #only for S3
    def __get__(self, instance, owner):
        return instance._storage_aws_role_arn
    
    def __set__(self, instance, value):
        if instance._storage_provider in ['S3','S3GOV']:
            vv.required_attribute_check(
                value=value,
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._storage_aws_role_arn = value
        else:
            if value != "NONE":
                vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} can only be used when Storage Provider is S3 or S3Gov.")
            elif value=="NONE":
                instance._storage_aws_role_arn="NONE"

    def __delete__(self, instance):
        del instance._storage_aws_role_arn

class StorageBaseURL:
    def __get__(self, instance, owner):
        return instance._storage_base_url
    
    def __set__(self, instance, value):
        vv.required_attribute_check(
            value=value,
            object_type=instance.parent.object_type,
            attr_name=self.__class__.__name__
        )
        instance._storage_base_url = value

    def __delete__(self, instance):
        del instance._storage_base_url

class StorageAWSAccessPointARN:
    def __get__(self, instance, owner):
        return instance._storage_base_url
    
    def __set__(self, instance, value):
        if value=="NONE":
            instance._storage_aws_access_point_arn="NONE"
        else:
            if instance._storage_provider in ['S3','S3GOV']:
                if value=="NONE":
                    instance._storage_aws_access_point_arn="NONE"
                else:
                    instance._storage_aws_access_point_arn = value
            else:
                vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} can only be used for S3 storage providers.")

    def __delete__(self, instance):
        del instance._storage_aws_access_point_arn

class StorageAWSExternalID:
    def __get__(self, instance, owner):
        return instance._storage_aws_external_id
    
    def __set__(self, instance, value):
        if value=="NONE":
            instance._storage_aws_external_id="NONE"
        else:
            if instance._storage_provider in ['S3','S3GOV']:
                if value=="NONE":
                    instance._storage_aws_external_id="NONE"
                else:
                    instance._storage_aws_external_id = value
            else:
                vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} can only be used for S3 storage providers.")

    def __delete__(self, instance):
        del instance._storage_aws_external_id

class EncryptionType:
    def __get__(self, instance, owner):
        return instance._encryption_type
    
    def __set__(self, instance, value):
        if value=="NONE":
            instance._encryption_type="NONE"
        else:
            if instance._storage_provider in ['S3','S3GOV','GCS']:
                if value=="NONE":
                    instance._encryption_type="NONE"
                else:
                    if instance._storage_provider == 'GCS':
                        vv.is_allowed_value(
                            value=value,
                            allowed_list=tags.allowed_value_list().get(tags.ENCRYPTION_TYPE).get('GCS'),
                            object_type=instance.parent.object_type,
                            attr_name=self.__class__.__name__
                            
                        )
                        instance._encryption_type = value
                    else: #for S3
                        vv.is_allowed_value(
                            value=value,
                            allowed_list=tags.allowed_value_list().get(tags.ENCRYPTION_TYPE).get('S3'),
                            object_type=instance.parent.object_type,
                            attr_name=self.__class__.__name__
                        )
                        instance._encryption_type=value
            else:
                vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} can only be used for S3 or GCS storage providers.")

    def __delete__(self, instance):
        del instance._encryption_type

class KMSKeyID:
    def __get__(self, instance, owner):
        return instance._kms_key_id
    
    def __set__(self, instance, value):
        if value=="NONE":
            instance._kms_key_id="NONE"
        else:
            if instance._encryption_type in ['GCS_SSE_KMS','AWS_SSE_KMS']:
                if value=="NONE":
                    instance._kms_key_id="NONE"
                else:
                    instance._kms_key_id=value
            else:
                vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} can only be used when Encryption type is GCS_SSE_KMS or AWS_SSE_KMS.")

    def __delete__(self, instance):
        del instance._kms_key_id       

class UsePrivateLinkEndpoint:
    def __get__(self, instance, owner):
        return instance._use_private_link_endpoint
    
    def __set__(self, instance, value):
        if value=="NONE":
            instance._use_private_link_endpoint="NONE"
        else:
            if instance._storage_provider in ['S3','S3GOV','AZURE']:
                if value=="NONE":
                    instance._use_private_link_endpoint="NONE"
                else:
                    vv.is_bool(
                        value=value,
                        object_type=instance.parent.object_type,
                        attr_name=self.__class__.__name__
                    )
                    instance._use_private_link_endpoint = value
            else:
                vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} can only be used for S3 or AZURE storage providers.")

    def __delete__(self, instance):
        del instance._use_private_link_endpoint

class AzureTenantID:
    def __get__(self, instance, owner):
        return instance._azure_tenant_id
    
    def __set__(self, instance, value):
        if instance._storage_provider =='AZURE':
            vv.required_attribute_check(
                value=value,
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._azure_tenant_id=value
        else:
            vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} can only be used for AZURE storage providers.")

    def __delete__(self, instance):
        del instance._azure_tenant_id


class AWSKeyID:
    def __get__(self, instance, owner):
        return instance._aws_key_id
    
    def __set__(self, instance, value):
        if instance._storage_provider =='S3COMPAT':
            vv.required_attribute_check(
                value=value,
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._aws_key_id=value
        else:
            vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} can only be used for S3COMPAT storage providers.")

    def __delete__(self, instance):
        del instance._aws_key_id

class AWSSecretKey:
    def __get__(self, instance, owner):
        return instance._aws_secret_key
    
    def __set__(self, instance, value):
        if instance._storage_provider =='S3COMPAT':
            vv.required_attribute_check(
                value=value,
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._aws_secret_key=value
        else:
            vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} can only be used for S3COMPAT storage providers.")

    def __delete__(self, instance):
        del instance._aws_secret_key

class StorageEndPoint:
    def __get__(self, instance, owner):
        return instance._storage_end_point
    
    def __set__(self, instance, value):
        if instance._storage_provider =='S3COMPAT':
            vv.required_attribute_check(
                value=value,
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._storage_end_point=value
        else:
            vo.operation_on_object_not_suppported(message=f"{self.__class__.__name__} can only be used for AZURE storage providers.")

    def __delete__(self, instance):
        del instance._storage_end_point

class AllowWrites:
    def __get__(self, instance, owner):
        return instance._allow_writes
    
    def __set__(self, instance, value):
        if value=="NONE":
            instance._allow_writes="NONE"
        else:
            vv.is_bool(
                value=value,
                object_type=instance.parent.object_type,
                attr_name=self.__class__.__name__
            )
            instance._allow_writes=value

    def __delete__(self, instance):
        del instance._allow_writes

class ExternalVolumeAttrs:
    def __init__(self,parent):
        self.parent=parent
    name = Name()
    storage_location_name=StorageLocationName()
    storage_provider=StorageProvider()
    storage_aws_role_arn=StorageAWSRoleARN()
    storage_base_url=StorageBaseURL()
    storage_aws_access_point_arn=StorageAWSAccessPointARN()
    storage_aws_external_id=StorageAWSExternalID()
    encryption_type=EncryptionType()
    kms_key_id=KMSKeyID()
    use_private_link_endpoint=UsePrivateLinkEndpoint()
    azure_tenant_id=AzureTenantID()
    aws_key_id=AWSKeyID()
    aws_secret_key=AWSSecretKey()
    storage_end_point=StorageEndPoint()
    allow_writes=AllowWrites()

class ExternalVolume(BaseObject):
    def __init__(self, session, user_id, logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger,database_required=False,schema_required=False)
        self.attr = ExternalVolumeAttrs(self)
        self.object_type=self.__class__.__name__


    def set_name(self, value): self.attr.name = value
    def set_storage_location_name(self,value):self.attr.storage_location_name=value
    def set_storage_provider(self,value):self.attr.storage_provider=value
    def set_storage_aws_role_arn(self,value):self.attr.storage_aws_role_arn=value
    def set_storage_base_url(self,value):self.attr.storage_base_url=value
    def set_storage_aws_access_point_arn(self,value):self.attr.storage_aws_access_point_arn=value
    def set_storage_aws_external_id(self,value):self.attr.storage_aws_external_id=value
    def set_encryption_type(self,value):self.attr.encryption_type=value
    def set_kms_key_id(self,value):self.attr.kms_key_id=value
    def set_use_private_link_endpoint(self,value):self.attr.use_private_link_endpoint=value
    def set_azure_tenant_id(self,value):self.attr.azure_tenant_id=value
    def set_aws_key_id(self,value):self.attr.aws_key_id=value
    def set_aws_secret_key(self,value):self.attr.aws_secret_key=value
    def set_storage_end_point(self,value):self.attr.storage_end_point=value
    def set_allow_writes(self,value): self.attr.allow_writes=value
    def set_comment(self, val):super().set_comment(val=val)

    def set_object_properties_flag(self):
        self.flag_dic = {}
        def set_flag(tag, attrname):
            self.flag_dic[tag] = 1 if getattr(self.attr, attrname, None) != "NONE" else 0

        if self.attr.storage_provider in ['S3','S3GOV']:
            set_flag(tags.STORAGE_AWS_ACCESS_POINT_ARN, "_storage_aws_access_point_arn")
            set_flag(tags.STORAGE_AWS_EXTERNAL_ID, "_storage_aws_external_id")
            set_flag(tags.ENCRYPTION_TYPE, "_encryption_type")
            set_flag(tags.KMS_KEY_ID, "_kms_key_id")
            set_flag(tags.USE_PRIVATELINK_ENDPOINT, "_use_private_link_endpoint")
        elif self.attr.storage_provider == 'GCS':
            set_flag(tags.ENCRYPTION_TYPE, "_encryption_type")
            set_flag(tags.KMS_KEY_ID, "_kms_key_id")
        elif self.attr.storage_provider=='AZURE':
            set_flag(tags.USE_PRIVATELINK_ENDPOINT, "_use_private_link_endpoint")

        set_flag(tags.ALLOW_WRITES,"_allow_writes")
        set_flag(tags.COMMENT, "comment")

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_query(self):
        self.qry = f"""
        CREATE EXTERNAL VOLUME {self.attr.name[0]} 
        STORAGE_LOCATIONS = (
            (
                NAME = '{self.attr.storage_location_name}'
                {tags.STORAGE_PROVIDER} = '{self.attr.storage_provider}'
        """
        if self.attr.storage_provider in ['S3','S3GOV']:
            self.qry += f"""
            {tags.STORAGE_AWS_ROLE_ARN} = '{self.attr.storage_aws_role_arn}'
            {tags.STORAGE_BASE_URL} = '{self.attr.storage_base_url}'
            """
        elif self.attr.storage_provider=='GCS':
            self.qry+=f"""
            {tags.STORAGE_BASE_URL} = '{self.attr.storage_base_url}'
            """
        elif self.attr.storage_provider=='AZURE':
            self.qry+=f"""
            {tags.AZURE_TENANT_ID} = '{self.attr.azure_tenant_id}'
            {tags.STORAGE_BASE_URL} = '{self.attr.storage_base_url}'
            """
        elif self.attr.storage_provider=='S3COMPAT':
            self.qry+=f"""
            {tags.STORAGE_BASE_URL} = '{self.attr.storage_base_url}'
            CREDENTIALS = 
            (
                {tags.AWS_KEY_ID} = '{self.attr.aws_key_id}' {tags.AWS_SECRET_KEY} = '{self.attr.aws_secret_key}'
            )
            {tags.STORAGE_ENDPOINT} = '{self.attr.storage_end_point}'
            """

    def add_properties_to_query(self):
        if self.attr.storage_provider in ['S3','S3GOV']:
            if tags.STORAGE_AWS_ACCESS_POINT_ARN in self.property_lst:
                self.qry += f" {tags.STORAGE_AWS_ACCESS_POINT_ARN} = '{self.attr.storage_aws_access_point_arn}' "
            if tags.STORAGE_AWS_EXTERNAL_ID in self.property_lst:
                self.qry += f" {tags.STORAGE_AWS_EXTERNAL_ID} = '{self.attr.storage_aws_external_id}' "
            if tags.ENCRYPTION_TYPE in self.property_lst:
                self.qry += f" ENCRYPTION = ( TYPE = '{self.attr.encryption_type}' "
                if tags.KMS_KEY_ID in self.property_lst:
                    self.qry+=f" {tags.KMS_KEY_ID} = '{self.attr.kms_key_id}' ) "
            if tags.USE_PRIVATELINK_ENDPOINT in self.property_lst:
                self.qry+=f" {tags.USE_PRIVATELINK_ENDPOINT} = {self.attr.use_private_link_endpoint} "
        elif self.attr.storage_provider == 'GCS':
            if tags.ENCRYPTION_TYPE in self.property_lst:
                self.qry += f" ENCRYPTION = ( TYPE = '{self.attr.encryption_type}' "
                if tags.KMS_KEY_ID in self.property_lst:
                    self.qry+=f" {tags.KMS_KEY_ID} = '{self.attr.kms_key_id}' ) "
        elif self.attr.storage_provider == 'AZURE':
            if tags.USE_PRIVATELINK_ENDPOINT in self.property_lst:
                self.qry+=f" {tags.USE_PRIVATELINK_ENDPOINT} = {self.attr.use_private_link_endpoint} "

        self.qry+=  " )) "
        if tags.ALLOW_WRITES in self.property_lst:
            self.qry+= f" {tags.ALLOW_WRITES} = {self.attr.allow_writes} "
        if tags.COMMENT in self.property_lst:
            self.qry+= f" {tags.COMMENT} = {self.attr.comment} "

    def alter_object(self):
        for prop in self.property_lst:
            self.qry = f"ALTER EXTERNAL VOLUME {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER EXTERNAL VOLUME {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming external volume {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == 'TRUE':
            self.set_create_query()
            self.add_properties_to_query()
        elif self.is_create=='FALSE':
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=ExternalVolume(session=session,
                         user_id=user_id,
                         logger=logger)
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        
        obj_inst.set_base_attributes(kwargs=kwargs)


        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')
        obj_inst.logger.info(f"name : {obj_inst.attr.name}")



        if tags.STORAGE_LOCATION_NAME in kwargs.keys():
            obj_inst.set_storage_location_name(kwargs[tags.STORAGE_LOCATION_NAME])
        else:
            obj_inst.set_storage_location_name('NONE')
        obj_inst.logger.info(f"STORAGE_LOCATION_NAME : {obj_inst.attr.storage_location_name}")


        if tags.STORAGE_PROVIDER in kwargs.keys():
            obj_inst.set_storage_provider(kwargs[tags.STORAGE_PROVIDER])
        else:
            obj_inst.set_storage_provider('NONE')
        obj_inst.logger.info(f"STORAGE_PROVIDER : {obj_inst.attr.storage_provider}")


        if tags.STORAGE_BASE_URL in kwargs.keys():
            obj_inst.set_storage_base_url(kwargs[tags.STORAGE_BASE_URL])
        else:
            obj_inst.set_storage_base_url('NONE')
        obj_inst.logger.info(f"STORAGE_BASE_URL : {obj_inst.attr.storage_base_url}")

        if obj_inst.attr.storage_provider in ['S3','S3GOV']:

            obj_inst.logger.info(f" STORAGE_PROVIDER S3 | S3GOV Params")

            if tags.STORAGE_AWS_ROLE_ARN in kwargs.keys():
                obj_inst.set_storage_aws_role_arn(kwargs[tags.STORAGE_AWS_ROLE_ARN])
            else:
                obj_inst.set_storage_aws_role_arn('NONE')
            obj_inst.logger.info(f"STORAGE_AWS_ROLE_ARN : {obj_inst.attr.storage_aws_role_arn}")


            if tags.STORAGE_AWS_ACCESS_POINT_ARN in kwargs.keys():
                obj_inst.set_storage_aws_access_point_arn(kwargs[tags.STORAGE_AWS_ACCESS_POINT_ARN])
            else:
                obj_inst.set_storage_aws_access_point_arn('NONE')
            obj_inst.logger.info(f"STORAGE_AWS_ACCESS_POINT_ARN : {obj_inst.attr.storage_aws_access_point_arn}")


            if tags.STORAGE_AWS_EXTERNAL_ID in kwargs.keys():
                obj_inst.set_storage_aws_external_id(kwargs[tags.STORAGE_AWS_EXTERNAL_ID])
            else:
                obj_inst.set_storage_aws_external_id('NONE')
            obj_inst.logger.info(f"STORAGE_AWS_EXTERNAL_ID : {obj_inst.attr.storage_aws_external_id}")
        

            if tags.ENCRYPTION_TYPE in kwargs.keys():
                obj_inst.set_encryption_type(kwargs[tags.ENCRYPTION_TYPE])
            else:
                obj_inst.set_encryption_type('NONE')
            obj_inst.logger.info(f"ENCRYPTION_TYPE : {obj_inst.attr.encryption_type}")


            if tags.KMS_KEY_ID in kwargs.keys():
                obj_inst.set_kms_key_id(kwargs[tags.KMS_KEY_ID])
            else:
                obj_inst.set_kms_key_id('NONE')
            obj_inst.logger.info(f"KMS_KEY_ID : {obj_inst.attr.kms_key_id}")

            obj_inst.logger.info("set set_use_private_link_endpoint")
            if tags.USE_PRIVATELINK_ENDPOINT in kwargs.keys():
                obj_inst.set_use_private_link_endpoint(kwargs[tags.USE_PRIVATELINK_ENDPOINT])
            else:
                obj_inst.set_use_private_link_endpoint('NONE')
            obj_inst.logger.info(f"USE_PRIVATELINK_ENDPOINT : {obj_inst.attr.use_private_link_endpoint}")
        
        elif obj_inst.attr.storage_provider=='GCS':
            obj_inst.logger.info(f" STORAGE_PROVIDER : GCS Params")
            if tags.ENCRYPTION_TYPE in kwargs.keys():
                obj_inst.set_encryption_type(kwargs[tags.ENCRYPTION_TYPE])
            else:
                obj_inst.set_encryption_type('NONE')
            obj_inst.logger.info(f"ENCRYPTION_TYPE : {obj_inst.attr.encryption_type}")


            if tags.KMS_KEY_ID in kwargs.keys():
                obj_inst.set_kms_key_id(kwargs[tags.KMS_KEY_ID])
            else:
                obj_inst.set_kms_key_id('NONE')
            obj_inst.logger.info(f"KMS_KEY_ID : {obj_inst.attr.kms_key_id}")
        
        elif obj_inst.attr.storage_provider=='AZURE':
            obj_inst.logger.info("STORAGE_PROVIDER : AZURE Params ")

            if tags.AZURE_TENANT_ID in kwargs.keys():
                obj_inst.set_azure_tenant_id(kwargs[tags.AZURE_TENANT_ID])
            else:
                obj_inst.set_azure_tenant_id('NONE')
            obj_inst.logger.info(f"AZURE_TENANT_ID : {obj_inst.attr.azure_tenant_id}")

            if tags.USE_PRIVATELINK_ENDPOINT in kwargs.keys():
                obj_inst.set_use_private_link_endpoint(kwargs[tags.USE_PRIVATELINK_ENDPOINT])
            else:
                obj_inst.set_use_private_link_endpoint('NONE')
            obj_inst.logger.info(f"USE_PRIVATELINK_ENDPOINT : {obj_inst.attr.use_private_link_endpoint}")

        elif obj_inst.attr.storage_provider=='S3COMPAT':
            obj_inst.logger.info("STORAGE_PROVIDER : S3COMPAT Params")
            if tags.AWS_KEY_ID in kwargs.keys():
                obj_inst.set_aws_key_id(kwargs[tags.AWS_KEY_ID])
            else:
                obj_inst.set_aws_key_id('NONE')
            obj_inst.logger.info(f"AWS_KEY_ID : {obj_inst.attr.aws_key_id}")

            if tags.AWS_SECRET_KEY in kwargs.keys():
                obj_inst.set_aws_secret_key(kwargs[tags.AWS_SECRET_KEY])
            else:
                obj_inst.set_aws_secret_key('NONE')
            obj_inst.logger.info(f"AWS_SECRET_KEY : {obj_inst.attr.aws_secret_key}")
            

            if tags.STORAGE_ENDPOINT in kwargs.keys():
                obj_inst.set_storage_end_point(kwargs[tags.STORAGE_ENDPOINT])
            else:
                obj_inst.set_storage_end_point('NONE')
            obj_inst.logger.info(f"STORAGE_ENDPOINT : {obj_inst.attr.storage_end_point}")

        obj_inst.logger.info("set set_allow_writes")
        if tags.ALLOW_WRITES in kwargs.keys():
            obj_inst.set_allow_writes(kwargs[tags.ALLOW_WRITES])
        else:
            obj_inst.set_allow_writes('NONE')
        obj_inst.logger.info(f"ALLOW_WRITES : {obj_inst.attr.allow_writes}")

        logger.info('prepare query')
        obj_inst.prepare_query()    
        obj_inst.print_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.write_file_to_git(
            object_name=obj_inst.attr.name[0],
            object_type=obj_inst.object_type,
            object_database='NA',
            object_schema='NA'
        )
        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                        object_identifier=obj_inst.attr.name[0],
                                        qry=obj_inst.qry)

    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()

