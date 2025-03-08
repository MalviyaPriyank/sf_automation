import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from vars.gvobject import InternalStage as gv, Config as cfg,Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from dep.deploy import Deploy
from validation.validateobject import ValidateObject as vo
from setup import privilege


class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.database_exist(session=instance.parent.session, database_name=value)
        #if vo.database_exist(value):
        instance._database = value
    
    def __delete__(self,instance):
        del instance._database_name


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
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.is_new_stage(session=instance.parent.session,database=instance._database,schema=instance._shcema,stage=value,obj_type=instance.parent.__class__.__name__,obj_name=self.__class__.__name__)
        if ( vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__) 
              and not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
              and not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__)
              ):
            instance._name = value

    def __del__(self,instance):
        del instance._name

class FileFormat:   
    def __get__(self,instance,owner):
        return instance._file_format
    
    def __set__(self,instance,value):
        if value=='NONE':
            instance._file_format=value
        else:
            vo.file_format_exist(session=instance.parent.session, database_name=instance._database, schema_name=instance._schema, file_format_name=value)
            instance._file_format = value

    def __del__(self,instance):
        del instance._file_format


class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = value


    def __del__(self,instance):
        del instance._comment

class Encryption:
    def __get__(self,instance,owner):
        return instance._encryption
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._encryption = value
        else:
            vv.is_allowed_value(value=value,allowed_list=gv._allowed_values_encryption,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._encryption = value

    def __del__(self,instance):
        del instance._encryption


class Enable:
    def __get__(self,instance,owner):
        return instance._enable
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._enable = value
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._enable = value

    def __del__(self,instance):
        del instance._enable


class RefreshOnCreate:
    def __get__(self,instance,owner):
        return instance._refresh_on_create
    
    def __set__(self,instance,value):
        if value == "NONE":
            instance._refresh_on_create = value
        else:
            if instance._enable != "NONE":
                vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
                instance._refresh_on_create = value
            else:
                vv.not_required(object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,condition=" when Directory table is not enabled")

    def __del__(self,instance):
        del instance._refresh_on_create


class InternalStageAttrs:
    def __init__(self,parent):
        self.parent = parent
    
    database = Database()
    schema = Schema()
    name = Name()
    file_format = FileFormat()
    comment = Comment()        
    encryption = Encryption()
    enable = Enable()
    refresh_on_create = RefreshOnCreate()
    


class InternalStage:
    def __init__(self,session,user_id,logger):
        self.session = session
        self.user_id = user_id
        self.sf_object_tag = "STAGE"
        self.qry = ""
        self.logger = logger
        self.attr = InternalStageAttrs(self)


    def set_database(self,val):
        self.attr.database = val

    def set_schema(self,val):
        self.attr.schema = val

    def set_name(self,val):
        self.attr.name = val

    def set_file_format(self,val):
        self.attr.file_format = val
    
    def set_comment(self,val):
        self.attr.comment = val

    def set_encryption(self,val):
        self.attr.encryption = val

    def set_enable(self,val):
        self.attr.enable = val

    def set_refresh_on_create(self,val):
        self.attr.refresh_on_create = val

    def set_qualified_name(self):
        self.qualified_name = f"{self.attr.database}.{self.attr.schema}.{self.attr.name}"

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv._name_tag,"_name")
        set_flag(gv._file_format_tag,"_file_format")
        set_flag(gv._comment_tag,"_comment")
        set_flag(gv._encryption_tag,"_encryption")
        set_flag(gv._enable_tag,"_enable")
        set_flag(gv._refresh_on_create_tag,"_refresh_on_create")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_qry(self):
        self.qry = f"CREATE STAGE  {self.attr.database}.{self.attr.schema}.{self.attr.name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gv._file_format_tag:
                    self.qry = f" {self.qry} {gv._file_format_tag} = {self.attr.file_format} "
                if prop == gv._comment_tag:
                    self.qry = f" {self.qry} {gv._comment_tag} = {self.attr.comment} "
                if prop == gv._encryption_tag:
                    self.qry = f" {self.qry} {gv._encryption_tag} = {self.attr.encryption} "
                if prop == gv._enable_tag:
                    self.qry = f" {self.qry} DIRECTORY = ( {gv._enable_tag} = {self.attr.enable} "
                    if prop == gv._refresh_on_create_tag:
                        self.qry = f" {self.qry} {gv._refresh_on_create_tag} = {self.attr.refresh_on_create} "
                    
                    self.qry=f" {self.qry} )"

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_qry()
        self.add_properties_to_query()

    def create_internal_stage(self):
        self.session.sql(self.qry).collect()

    def grant_default_privileges(self):
        priv_inst = privilege.Privilege(self.session)
        for role,privileges in cfg._default_role_privilege_set.items():
            if privileges in gv_priv._allowed_privileges[self.sf_object_tag]:
                priv_inst.grant_privilege_on_object_to_role(privilege_type = privileges,object_type = self.sf_object_tag,object_identifier=self.qualified_name,role = role)

    def create_deployment_entry(self):
        deploy_inst = Deploy(self.session)
        self.logger.info(f"Tracking for deployment internal stage object : {self.attr.name}")
        deploy_inst.insert_into_deployment_script_table(qry=self.qry, user_id=self.user_id)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database(self.attr.database)
        deploy_inst.set_object_schema(self.attr.schema)
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()

    def create_object(self,*largs,**kwargs):

        self.set_database(kwargs[gv._database_tag])
        self.set_schema(kwargs[gv._schema_tag])
        self.set_name(kwargs[gv._name_tag])
        self.set_file_format(kwargs[gv._file_format_tag])
        self.set_comment(kwargs[gv._comment_tag])
        self.set_encryption(kwargs[gv._encryption_tag])
        self.set_enable(kwargs[gv._enable_tag])
        self.set_refresh_on_create(kwargs[gv._refresh_on_create_tag])  
        self.set_qualified_name()
        self.prepare_query()
        self.logger.info(f"creating internal stage {self.attr.name}")
        self.create_internal_stage()
        if len(largs) == 0:
            self.create_deployment_entry()



        



