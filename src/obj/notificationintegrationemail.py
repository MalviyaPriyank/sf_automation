import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../processing'))



from vars.gvobject import NotificationIntegrationEmail as gv, Config as cfg , Privilege as gv_priv
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from dep import deploy
from setup import privilege 
from processing.stage import Stage
from .baseobj import BaseObject 
from vars.obj.notificationintegrationemail.gvnotificationintegrationemai import NotificationIntegrationEmailTag as tags

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.is_new_integration(session=instance.parent.session,object_type=instance.parent.__class__.__name__,object_name=value)
        if ( vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__) 
              and not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
              and not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__)
            ):
            instance._name = value

    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_integration(session=instance.parent.session,object_type=instance.parent.__class__.__name__,object_name=name)
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
                vo.integration_exist(session=instance.parent.session,integration_name=old_name)
                vo.is_new_integration(session=instance.parent.session,object_type=instance.parent.__class__.__name__,object_name=new_name)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"


    def __delete__(self,instance):
        del instance._name

class Enabled:
    def __get__(self,instance,owner):
        return instance._enabled
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vv.is_bool(value=value, object_type= instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
        instance._enabled = value

    
    def __delete__(self,instance):
        del instance._enabled

class Type:
    def __get__(self,instance,owner):
        return instance._type
    
    def __set__(self,instance,value):
        instance._type = value
    
    def __delete__(self,instance):
        del instance._type

class AllowedRecipients:
    def __get__(self,instance,owner):
        return instance._allowed_recipients
    
    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside allowed recipient to set {value}")
        if value=="NONE":
            instance._allowed_recipients=value
        else:
            value_str=""
            vv.is_list(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__) 
            instance.parent.logger.info(f"{value} passed list check")  
            for email in value:
                email=f"{email}"
                instance.parent.logger.info(f"checking if {email} is valid user")
                vo.is_valid_user_email(session=instance.parent.session,user_email=email)
                instance.parent.logger.info(f"{email} passed valid user check")
            for i in range(0,len(value)):
                if i != len(value)-1:
                    value_str=value_str+f"'{email}',"
                else:
                    value_str=value_str+f"'{email}'"
            instance._allowed_recipients=value_str

    def __delete__(self,instance):
        del instance._allowed_recipients

class DefaultRecipients:
    def __get__(self,instance,owner):
        return instance._default_recipients
    
    def __set__(self,instance,value):
        if value=='NONE':
            instance._default_recipients=value
        else:
            value_str=""
            vv.is_list(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            for email in value:
                email=f"{email}"
                vo.is_valid_user_email(session=instance.parent.session,user_email=email)
            for i in range(0,len(value)):
                if i != len(value)-1:
                    value_str=value_str+f"'{email}',"
                else:
                    value_str=value_str+f"'{email}'"
            instance._default_recipients=value_str

    def __delete__(self,instance):
        del instance._default_recipients

class DefaultSubject:
    def __get__(self,instance,owner):
        return instance._default_subject
    
    def __set__(self,instance,value):
        if value=='NONE':
            instance._default_subject=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            vv.is_string_of_allowed_length(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__,allowed_length=gv._allowed_length_subject)
            instance._default_subject = f"'{value}'"

    def __delete__(self,instance):
        del instance._default_subject

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        if value=='NONE':
            instance._comment=value
        else:
            vv.is_string(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._comment = f"'{value}'"

    def __delete__(self,instance):
        del instance._comment

class NotificationIntegrationEmailAttr:
    def __init__(self,parent):
        self.parent = parent

    name = Name()
    enabled = Enabled()
    type = Type()
    allowed_recipients = AllowedRecipients()
    default_recipients = DefaultRecipients()
    default_subject = DefaultSubject()
    comment = Comment()


class NotificationIntegrationEmail(BaseObject):
    def __init__(self, session, user_id, logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger)
        self.attr = NotificationIntegrationEmailAttr(self)

    def set_name(self, value):
        self.attr.name = value

    def set_enabled(self, value):
        self.attr.enabled = value

    def set_type(self, value):
        self.attr.type = value

    def set_allowed_recipients(self, value):
        self.attr.allowed_recipients = value

    def set_default_recipients(self, value):
        self.attr.default_recipients = value

    def set_default_subject(self, value):
        self.attr.default_subject = value

    def set_comment(self, value):
        self.attr.comment = value

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv._allowed_recepients_tag,"_allowed_recipients")
        set_flag(gv._default_recepients_tag,"default_recipients")
        set_flag(gv._default_subject_tag,"_default_subject")
        set_flag(gv._comment_tag,"_comment")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"CREATE NOTIFICATION INTEGRATION  {self.attr.name} TYPE = {self.attr.type} ENABLED = {self.attr.enabled} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gv._allowed_recepients_tag:
                    self.qry = f" {self.qry} {gv._allowed_recepients_tag} = ({self.attr.allowed_recipients}) "
                if prop == gv._default_recepients_tag:
                    self.qry = f" {self.qry} {gv._default_recepients_tag} = ({self.attr.default_recipients}) "
                if prop == gv._default_subject_tag:
                    self.qry = f" {self.qry} {gv._default_subject_tag} = {self.attr.default_subject} "
                if prop == gv._comment_tag:
                    self.qry = f" {self.qry} {gv._comment_tag} = {self.attr.comment} "
    
    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()

    def create_notification_integration(self):
        self.execute_final_query()

    def create_object(self,*largs,**kwargs):

        self.set_name(kwargs[gv._name_tag])
        self.set_enabled(kwargs[gv._enabled_tag])
        self.set_type(kwargs[gv._type_tag])
        self.set_allowed_recipients(kwargs[gv._allowed_recepients_tag])
        self.set_default_recipients(kwargs[gv._default_recepients_tag])
        self.set_default_subject(kwargs[gv._default_subject_tag])
        self.set_comment(kwargs[gv._comment_tag])

        self.prepare_query()
        self.create_notification_integration()

class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        obj_inst=NotificationIntegrationEmail(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info(f"set name {kwargs[tags.NAME]}")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        logger.info(f"set enabled {kwargs[tags.ENABLED]}")
        if tags.ENABLED in kwargs.keys():
            obj_inst.set_enabled(kwargs[tags.ENABLED])
        else:
            obj_inst.set_enabled('NONE')

        obj_inst.set_type('EMAIL')
        '''
        logger.info(f"set type {kwargs[tags.TYPE]}")
        if tags.TYPE in kwargs.keys():
            obj_inst.set_type(kwargs[tags.TYPE])
        else:
            obj_inst.set_type('NONE')
        '''

        logger.info(f"set allowed_recipients {kwargs[tags.ALLOWED_RECIPIENTS]}")
        if tags.ALLOWED_RECIPIENTS in kwargs.keys():
            obj_inst.set_allowed_recipients(kwargs[tags.ALLOWED_RECIPIENTS])
        else:
            obj_inst.set_allowed_recipients('NONE')

        logger.info("set default_recipients")
        if tags.DEFAULT_RECIPIENTS in kwargs.keys():
            obj_inst.set_default_recipients(kwargs[tags.DEFAULT_RECIPIENTS])
        else:
            obj_inst.set_default_recipients('NONE')

        logger.info("set default_subject")
        if tags.DEFAULT_SUBJECT in kwargs.keys():
            obj_inst.set_default_subject(kwargs[tags.DEFAULT_SUBJECT])
        else:
            obj_inst.set_default_subject('NONE')

        logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')


        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.write_file_to_git(object_name=obj_inst.attr.name[0],
                                   object_type=obj_inst.__class__.__name__,
                                   object_database='NA',
                                   object_schema='NA')
        #obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
