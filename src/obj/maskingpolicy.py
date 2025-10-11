import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))

from .baseobj import BaseObject
from vars.obj.maskingpolicy.gvmaskingpolicy import MaskingPolicyTag as tags
from validation.validateobject import ValidateObject as vo
from validation.validatevalue import ValidateValue as vv

class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)

    def __set__(self,instance,value):
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_object(session=instance.parent.session, object_type=instance.parent.__class__.__name__,object_name=name)
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
                vo.object_exist(session=instance.parent.session,object_type=instance.parent.__class__.__name__,object_name=old_name)
                vo.is_new_object(session=instance.parent.session,object_type=instance.parent.__class__.__name__,object_name=new_name)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to

class MaskingPolicyAs:
    def __get__(self,instance,owner):
        return instance._masking_policy_as
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__, 
                                    attr_name=self.__class__.__name__)
        value_list=value.split(",")
        for i in range(0,len(value_list)): #iterating through each value eg : ['email varchar', ' gmail varchar']
            datatype=value_list[i].split(" ") #splitting on space to get datatype
            datatype=datatype.strip() # removing extra space in case
            vv.is_allowed_data_type(data_type=datatype)
        
        instance.parent.logger.info("all the data types are validated ")
        instance.parent.logger.info("setting AS for masking policy ")
        instance._masking_policy_as=f"({value})" #making it a tuple

    def __delete__(self,instance):
        del instance._masking_policy_as

class Returns:
    def __get__(self,instance,owner):
        return instance._returns
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        value=value.split(",").split(" ")[1] #setting returns as datatype of first argument 
        instance._returns = value

    def __delete__(self,instance):
        del instance._returns

class Body:
    def __get__(self,instance,owner):
        return instance._body
    
    def __set__(self,instance,value):
        instance._body = value

    def __delete__(self,instance):
        del instance._body

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = f"'{value}'"

    def __delete__(self,instance):
        del instance._comment

class ExemptOtherPolicies:
    def __get__(self,instance,owner):
        return instance._exempt_other_policies
    
    def __set__(self,instance,value):
        if value == 'NONE':
            instance._exempt_other_policies = "NONE"
        else:
            vv.is_bool(value=value,object_type=instance.parent.__class__.__name__,attr_name=self.__class__.__name__)
            instance._exempt_other_policies = value

    def __delete__(self,instance):
        del instance._exempt_other_policies



class MaskingPolicyAttrs:
    def __init__(self):
        self.parent=self
    name = Name()
    masking_policy_as = MaskingPolicyAs()
    returns = Returns()
    body = Body()
    comment = Comment()
    exempt_other_policies = ExemptOtherPolicies()

class MaskingPolicy(BaseObject):
    def __init__(self,session,user_id,logger):
        self.attr = MaskingPolicyAttrs(self)
        self.session = session
        self.logger = logger
        self.user_id = user_id

    def set_name(self,val=None):
        self.attr.name = val

    def set_masking_policy_as(self,val=None):
        self.attr.masking_policy_as = val

    def set_returns(self,val=None):
        self.attr.returns = val

    def set_body(self,val=None):
        self.attr.body = val

    def set_comment(self,val=None):
        self.attr.comment = val

    def set_exempt_other_policies(self,val=None):
        self.attr.exempt_other_policies = val

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.MASKING_POLICY_AS,"masking_policy_as")
        set_flag(tags.RETURNS,"returns")
        set_flag(tags.BODY,"body")
        set_flag(tags.COMMENT,"comment")
        set_flag(tags.EXEMPT_OTHER_POLICIES,"exempt_other_policies")

    def alter_object(self):        
        for prop in self.property_lst:
            if prop == tags.MASKING_POLICY_AS:
                self.qry = f"ALTER MASKING POLICY {self.attr.name[0]} SET {tags.MASKING_POLICY_AS} = {self.attr.masking_policy_as}"
                self.execute_final_query()
            if prop == tags.RETURNS:
                self.qry = f"ALTER MASKING POLICY {self.attr.name[0]} SET {tags.RETURNS} = {self.attr.returns}"
                self.execute_final_query()
            
            if prop == tags.BODY:
                self.qry = f"ALTER MASKING POLICY {self.attr.name[0]} SET {tags.BODY} = {self.attr.body}"
                self.execute_final_query()
            
            if prop == tags.COMMENT:
                self.qry = f"ALTER MASKING POLICY {self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()
                
            if prop == tags.EXEMPT_OTHER_POLICIES:
                self.qry = f"ALTER MASKING POLICY {self.attr.name[0]} SET {tags.EXEMPT_OTHER_POLICIES} = {self.attr.exempt_other_policies}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER MASKING POLICY {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming masking policy {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.MASKING_POLICY_AS:
                    self.qry = f" {self.qry} {tags.MASKING_POLICY_AS} {self.attr.masking_policy_as} "
                if prop == tags.RETURNS:
                    self.qry = f" {self.qry} {tags.RETURNS} {self.attr.returns} "
                if prop == tags.BODY:
                    self.qry = f" {self.qry} -> {self.attr.body} "
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "
                if prop == tags.EXEMPT_OTHER_POLICIES:
                    self.qry = f" {self.qry} {tags.EXEMPT_OTHER_POLICIES} = {self.attr.exempt_other_policies} "

    def set_create_masking_policy_qry(self):
        self.qry = f"CREATE MASKING POLICY {self.attr.name[0]} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == 'TRUE':
            self.set_create_masking_policy_qry()
            self.add_properties_to_query()
        elif self.is_create == 'FALSE':
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()

    def create_masking_policy(self):
        self.execute_final_query()

    def create_object(self,*largs,**kwargs):
        self.logger.info(f"Operating on {self.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        self.logger.info(f'dictionary passed {kwargs}')
        self.is_create = kwargs[tags.IS_CREATE]

        self.set_name(kwargs[tags.NAME])

        self.logger.info('set MASKING_POLICY_AS')
        self.set_masking_policy_as(kwargs[tags.MASKING_POLICY_AS])

        self.logger.info('set RETURNS')
        self.set_returns(kwargs[tags.MASKING_POLICY_AS])


        self.logger.info('set COMMENT')
        self.set_comment(kwargs[tags.COMMENT])

        self.logger.info('set EXEMPT_OTHER_POLICIES')
        self.set_exempt_other_policies(kwargs[tags.EXEMPT_OTHER_POLICIES])

        self.logger.info('prepare query')
        self.prepare_query()

        self.logger.info('execute query')
        self.create_masking_policy()

        self.create_deployment_entry(object_name=self.attr.name,
                                     object_type=self.__class__.__name__,
                                     object_database='NA',
                                     object_schema='NA')

        self.write_file_to_git(object_name=self.attr.name,
                               object_type=self.__class__.__name__,
                               object_database='NA',
                               object_schema='NA')

class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        obj_inst=MaskingPolicy(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        logger.info("set masking_policy_as")
        if tags.MASKING_POLICY_AS in kwargs.keys():
            obj_inst.set_masking_policy_as(kwargs[tags.MASKING_POLICY_AS])
        else:
            obj_inst.set_masking_policy_as('NONE')

        logger.info("set returns")
        if tags.RETURNS in kwargs.keys():
            obj_inst.set_returns(kwargs[tags.RETURNS])
        else:
            obj_inst.set_returns('NONE')

        logger.info("set body")
        if tags.BODY in kwargs.keys():
            obj_inst.set_body(kwargs[tags.BODY])
        else:
            obj_inst.set_body('NONE')

        logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')

        logger.info("set exempt_other_policies")
        if tags.EXEMPT_OTHER_POLICIES in kwargs.keys():
            obj_inst.set_exempt_other_policies(kwargs[tags.EXEMPT_OTHER_POLICIES])
        else:
            obj_inst.set_exempt_other_policies('NONE')

        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
