
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../deploy'))


from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from src.obj.baseobj import BaseObject 
from vars.obj.networkrule.gvnetworkrule import NetworkRuleTag as tags
from src.usr.user import ChatHistory


class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)

    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        instance.parent.logger.info(f"inside to set name {value}")
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            instance.parent.logger.info(f" for create operation setting name: {name}")
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
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to

class Type:
    def __get__(self,instance,owner):
        return instance._type
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        instance._type = value
    
    def __delete__(self,instance):
        del instance._type


class ValueList:
    def __get__(self,instance,owner):
        return instance._value_list
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if isinstance(value,list):
            instance.parent.logger.info("Value received as list")
            val_string=""
            for i in range(0,len(value)):
                instance.parent.logger.info(f"Validating {value[i]} for CIDR notation")
                if i != len(value)-1:
                    val_string=val_string+f"'{value[i]}',"
                elif i == len(value)-1:
                    val_string=val_string+f"'{value[i]}'"
            instance.parent.logger.info(f" final value string : {val_string}")
            instance._value_list=f"({val_string})"
        elif isinstance(value,str):
            vv.is_valid_cidr(object_type=instance.parent.__class__.__name__,
                                attribute_name=self.__class__.__name__,
                                cidr_str=value)
            instance._value_list=f"('{value}')"
    
    def __delete__(self,instance):
        del instance._value_list

class Mode:
    def __get__(self,instance,owner):
        return instance._mode
    
    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if instance._type == "HOST_PORT" or instance._type=="PRIVATE_HOST_PORT":
            instance._mode="EGRESS"
        else:
            instance._mode=value
    
    def __delete__(self,instance):
        del instance._mode


class NetworkRuleAttrs:
    def __init__(self,parent):
        self.parent = parent

    name = Name()
    type=Type()
    value_list=ValueList()
    mode=Mode()


class NetworkRule(BaseObject):
    def __init__(self, session, user_id, logger):
        logger=logger.getChild(self.__class__.__name__)
        super().__init__(session, user_id, logger,database_required=True,schema_required=True)
        self.attr = NetworkRuleAttrs(self)


    def set_name(self,val):
        self.attr.name = val

    def set_type(self,val):
        self.attr.type = val

    def set_value_list(self,val):
        self.attr.value_list = val

    def set_mode(self,val):
        self.attr.mode = val


    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0
        set_flag(tags.COMMENT,"comment")


    def alter_object(self):        
        for prop in self.property_lst:
            if prop == tags.VALUE_LIST:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.VALUE_LIST} = {self.attr.value_list}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER {self.__class__.__name__} {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
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
        self.qry = f"""
        CREATE NETWORK RULE  
        {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} 
        {tags.TYPE} = {self.attr.type} 
        {tags.VALUE_LIST} = {self.attr.value_list} 
        {tags.MODE} = {self.attr.mode}
        """

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == tags.COMMENT:
                    self.qry = f" {self.qry} {tags.COMMENT} = '{self.attr.comment}' "

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

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=NetworkRule(session=session,
                         user_id=user_id,
                         logger=logger)
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.set_base_attributes(kwargs=kwargs)


        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')
        obj_inst.logger.info(f"set name {obj_inst.attr.name}")

        
        if tags.TYPE in kwargs.keys():
            obj_inst.set_type(kwargs[tags.TYPE])
        else:
            obj_inst.set_type('NONE')
        obj_inst.logger.info(f"set type {obj_inst.attr.type}")


        if tags.VALUE_LIST in kwargs.keys():
            obj_inst.set_value_list(kwargs[tags.VALUE_LIST])
        else:
            obj_inst.set_value_list('NONE')
        obj_inst.logger.info(f"set VALUE_LIST {obj_inst.attr.value_list}")


        if tags.MODE in kwargs.keys():
            obj_inst.set_mode(kwargs[tags.MODE])
        else:
            obj_inst.set_mode('NONE')
        obj_inst.logger.info(f"set mode {obj_inst.attr.mode}")


        logger.info('prepare query')
        obj_inst.prepare_query()
        obj_inst.print_query()
        
        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                        object_identifier=obj_inst.attr.name[0],
                                        qry=obj_inst.qry)

        



    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
