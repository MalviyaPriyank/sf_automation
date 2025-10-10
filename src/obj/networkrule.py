
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from .baseobj import BaseObject 
from vars.obj.networkrule.gvnetworkrule import NetworkRuleTag as tags

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if not vv.starts_with_alphabet(value):
            raise ValueError
        elif not vv.is_enclosed_in_double_quotes(value):
            if vv.has_space(value):
                raise ValueError
            if vv.has_special_characters(value):
                raise ValueError
            else:
                instance._name = value

    def __delete__(self,instance):
        del instance._name

class Type:
    def __get__(self,instance,owner):
        return instance._type
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vv.is_allowed_value(value=value,
                            allowed_list=tags.allowed_value_list().get(f"{tags.TYPE}"),
                            object_type=instance.parent.__class__.__name__,
                            attr_name=self.__class__.__name__)
        instance._type = value
    
    def __delete__(self,instance):
        del instance._type


class ValueList:
    def __get__(self,instance,owner):
        return instance._value_list
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        if instance._type=="IPV4":
            vv.is_valid_cidr(object_type=instance.parent.__class__.__name__,
                             attribute_name=self.__class__.__name__,
                             cidr_str=value)
            instance._value_list=value
        elif instance._type=="AWSVPCEID":
            vv.is_valid_vpce_id(object_type=instance.parent.__class__.__name__,
                             attribute_name=self.__class__.__name__,
                             vpce_id=value)
            instance._value_list=value
        elif instance._type=="HOST_PORT":
            vv.is_valid_host_port(object_type=instance.parent.__class__.__name__,
                                  attribute_name=self.__class__.__name__,
                                  value=value)
            instance._value_list=value
    
    def __delete__(self,instance):
        del instance._value_list

class Mode:
    def __get__(self,instance,owner):
        return instance._mode
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        if instance._type == "HOST_PORT" or instance._type=="PRIVATE_HOST_PORT":
            instance._mode="EGRESS"
        else:
            vv.is_allowed_value(value=value,
                                allowed_list=tags.allowed_value_list().get(tags.MODE),
                                object_type=instance.parent.__class__.__name__,
                                attr_name=self.__class__.__name__)
            instance._mode=value
    
    def __delete__(self,instance):
        del instance._mode

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = value
    
    def __delete__(self,instance):
        del instance._comment

class NetworkRuleAttrs:
    def __init__(self,parent):
        self.parent = parent

    name = Name()
    type=Type()
    value_list=ValueList()
    mode=Mode()
    comment = Comment()


class NetworkRule(BaseObject):
    def __init__(self, session, user_id):
        super().__init__(session, user_id)
        self.attr = NetworkRuleAttrs(self)


    def set_name(self,val):
        self.attr.name = val

    def set_type(self,val):
        self.attr.type = val

    def set_value_list(self,val):
        self.attr.value_list = val

    def set_mode(self,val):
        self.attr.mode = val

    def set_comment(self,val):
        self.attr.comment = val

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
        set_flag(tags.COMMENT,"_comment")


    def alter_object(self):        
        for prop in self.property_lst:
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER NETWORK RULE {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming {self.__class__.__name__} {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()


    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_network_rule_qry(self):
        self.qry = f"CREATE NETWORK RULE  {self.attr.name} {tags.TYPE} = {self.attr.type} {tags.VALUE_LIST} = {self.attr.value_list} {tags.MODE} = {self.attr.mode}"

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = {self.attr.comment} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == 'TRUE':
            self.set_create_network_rule_qry()
            self.add_properties_to_query()
        elif self.is_create=='FALSE':
            self.logger.info(f"inside alter patch while preparing query rename to : {self.attr.name[1]}")
            if self.attr.name[1] != "NONE":
                self.property_lst.append(tags.NAME)
            self.alter_object()
    
    def create_database_role(self):
        self.execute_final_query()

    def create_object(self,**kwargs):
        self.logger.info(f"Operating on {self.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        self.logger.info(f'dictionary passed {kwargs}')
        self.is_create=kwargs[tags.IS_CREATE]


        self.set_name(kwargs[tags.NAME])
        self.set_type(kwargs[tags.TYPE])
        self.set_value_list(kwargs[tags.VALUE_LIST])
        self.set_mode(kwargs[tags.MODE])
        self.set_comment(kwargs[tags.COMMENT])

        self.prepare_query()
        self.create_database_role()

        self.logger.info('create deployment entry')
        self.create_deployment_entry(object_name=self.attr.name[0],object_type=self.__class__.__name__,object_database='NA',object_schema='NA')

        self.logger.info('writing file to git')
        self.write_file_to_git(object_name=self.attr.name[0],object_type=self.__class__.__name__,object_database='NA',object_schema='NA')

class Operation:
    @staticmethod
    def create_object(session,user_id,kwargs,*largs):
        obj_inst=NetworkRule(session=session,
                         user_id=user_id,
                         )
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        obj_inst.logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        obj_inst.logger.info("set type")
        if tags.TYPE in kwargs.keys():
            obj_inst.set_type(kwargs[tags.TYPE])
        else:
            obj_inst.set_type('NONE')

        obj_inst.logger.info("set value_list")
        if tags.VALUE_LIST in kwargs.keys():
            obj_inst.set_value_list(kwargs[tags.VALUE_LIST])
        else:
            obj_inst.set_value_list('NONE')

        obj_inst.logger.info("set mode")
        if tags.MODE in kwargs.keys():
            obj_inst.set_mode(kwargs[tags.MODE])
        else:
            obj_inst.set_mode('NONE')

        obj_inst.logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment('NONE')

        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        
        obj_inst.logger.info('execute query')
        obj_inst.execute_final_query()

        obj_inst.logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
