
import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))




from vars.gvgovernance import MaskingPolicy as gv_mp
from vars.gvobject import Config as cfg
from validation.validatevalue import ValidateValue as vv
from dep import deploy


class Role:
    def __get__(self,instance,owner):
        return instance._role
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._role = value

    def __delete__(self,instance):
        del instance._role

class MaskValue:
    def __get__(self,instance,owner):
        return instance._mask_value
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._mask_value = f"'{value}'"

    def __delete__(self,instance):
        del instance._mask_value

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

class Signature:
    def __get__(self,instance,owner):
        return instance._signature
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._signature = value

    def __delete__(self,instance):
        del instance._signature

class Returns:
    def __get__(self,instance,owner):
        return instance._signature
    
    def __set__(self,instance,value):
        value = instance._signature[0].split(' ')[1]
        instance._signature = value

    def __delete__(self,instance):
        del instance._signature

class Body:
    def __get__(self,instance,owner):
        return instance._body
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        instance._body = value

    def __delete__(self,instance):
        del instance._body

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = value

    def __delete__(self,instance):
        del instance._comment

class ExemptOtherPolicies:
    def __get__(self,instance,owner):
        return instance._exempt_other_policies
    
    def __set__(self,instance,value):
        instance._exempt_other_policies = value

    def __delete__(self,instance):
        del instance._exempt_other_policies

class MaskingPolicyAttr:
    role = Role()
    mask_value = MaskValue()
    name = Name()
    signature = Signature()
    returns = Returns()
    body = Body()
    comment = Comment()
    exempt_other_policies = ExemptOtherPolicies()


class MaskingPolicy:
    def __init__(self,session,user_id):
        self.attr = MaskingPolicyAttr()
        self.session = session
        self.user_id = user_id

    def set_role(self,value):
        self.attr.role = value
        
    def set_name(self,value):
        self.attr.name = value

    def set_signature(self,value):
        self.attr.signature = value

    def set_returns(self,value):
        self.attr.returns = value

    def set_body(self,value):
        self.attr.body = value

    def set_comment(self,value):
        self.attr.comment = value

    def set_exempt_other_policies(self,value):
        self.attr.exempt_other_policies = value

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv_mp._comment_tag,"_comment")
        set_flag(gv_mp._exempt_other_policies_tag,"_exempt_other_policies")


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_account_qry(self):
        self.qry = f"""
                    CREATE MASKING POLICY {self.attr.name} as ({self.attr.signature}) returns {self.attr.returns}
                    CASE 
                        WHEN 
                            current_role() in ( {self.attr.role} ) THEN {self.attr.signature[0].split(' ')[0]} 
                        ELSE 
                            {self.attr.mask_value}
                    END 
                    """

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gv_mp._comment_tag:
                    self.qry = f" {self.qry} {gv_mp._comment_tag} = {self.attr.comment} "
                if prop == gv_mp._exempt_other_policies_tag:
                    self.qry = f" {self.qry} {gv_mp._exempt_other_policies_tag} = {self.attr.exempt_other_policies} "


    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_account_qry()
        self.add_properties_to_query()

    def execute_query(self):
        self.session.sql(self.qry).collect()
    
    def create_masking_policy(self,**kwargs):
        self.set_name(kwargs[gv_mp._name_tag])
        self.set_signature(kwargs[gv_mp._signature_tag])
        self.set_returns(kwargs[gv_mp._returns_tag])
        self.set_body(kwargs[gv_mp._body_tag])
        self.set_comment(kwargs[gv_mp._comment_tag])
        self.set_exempt_other_policies(kwargs[gv_mp._exempt_other_policies_tag])
        self.prepare_query()
        self.execute_query()
        self.create_deployment_entry()

    def create_deployment_entry(self):
        deploy_inst = deploy.Deploy(self.session)
        deploy_inst.set_object_type(self.__class__.__name__)
        deploy_inst.set_object_database('NA')
        deploy_inst.set_object_schema('NA')
        deploy_inst.set_object_name(self.attr.name)
        deploy_inst.set_modified_by(self.user_id)
        deploy_inst.set_deployment_status(cfg._deployment_status_in_development)
        deploy_inst.set_deployment_id('NA')
        deploy_inst.insert_into_deploy_control_table()