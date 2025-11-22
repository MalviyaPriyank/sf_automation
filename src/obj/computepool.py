import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.computepool.gvcomputepool import ComputePoolTag as tags
from src.validation.validateobject import ValidateObject as vo
from src.validation.validatevalue import ValidateValue as vv
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
            vo.is_new_object(session=instance.parent.session,
                             object_type=instance.parent.__class__.__name__,
                             object_name=name)
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
                vo.object_exist(session=instance.parent.session,
                                object_type=instance.parent.__class__.__name__,
                                object_name=old_name)
                vo.is_new_object(session=instance.parent.session,
                             object_type=instance.parent.__class__.__name__,
                             object_name=new_name)
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to


class ForApplication:
    def __get__(self, instance, owner):
        return instance._for_application
    def __set__(self, instance, value):
        vo.object_exist(session=instance.parent.session,
                        object_type='APPLICATION',
                        object_name=value)
        instance._for_application = value
    def __delete__(self, instance):
        del instance._for_application

class MinNodes:
    def __get__(self, instance, owner):
        return instance._min_nodes
    def __set__(self, instance, value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vv.is_positive_number(value=value,
                              object_type=instance.parent.__class__.__name__,
                              attr_name=self.__class__.__name__)
        instance._min_nodes = value

    def __delete__(self, instance):
        del instance._min_nodes

class MaxNodes:
    def __get__(self, instance, owner):
        return instance._max_nodes
    def __set__(self, instance, value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        vv.is_positive_number(value=value,
                              object_type=instance.parent.__class__.__name__,
                              attr_name=self.__class__.__name__)
        vv.is_greater_than_or_equal_to(value_base=value,
                                       value_ref=instance._min_nodes,
                                       object_type=instance.parent.__class__.__name__,
                                       attr_name=self.__class__.__name__)
        instance._max_nodes = value
    def __delete__(self, instance):
        del instance._max_nodes


class InstanceFamily:
    def __get__(self, instance, owner):
        return instance._instance_family
    def __set__(self, instance, value):
        vv.required_attribute_check(value=value,
                                    object_type=instance.parent.__class__.__name__,
                                    attr_name=self.__class__.__name__)
        famli_list=vo.get_allowed_instance_families(session=instance.parent.session)
        vv.is_allowed_value(value=value,
                            allowed_list=famli_list,
                            object_type=instance.parent.__class__.__name__,
                            attr_name=self.__class__.__name__)
        instance._instance_family = value

    def __delete__(self, instance):
        del instance._instance_family

class AutoResume:
    def __get__(self, instance, owner):
        return instance._auto_resume
    def __set__(self, instance, value):
        vv.is_bool(value=value,
                   object_type=instance.parent.__class__.__name__,
                   attr_name=self.__class__.__name__)
        instance._auto_resume = value
    def __delete__(self, instance):
        del instance._auto_resume

class InitiallySuspended:
    def __get__(self, instance, owner):
        return instance._initially_suspended
    def __set__(self, instance, value):
        vv.is_bool(value=value,
                   object_type=instance.parent.__class__.__name__,
                   attr_name=self.__class__.__name__)
        instance._initially_suspended = value
    def __delete__(self, instance):
        del instance._initially_suspended

class AutoSuspendSecs:
    def __get__(self, instance, owner):
        return instance._auto_suspend_secs
    def __set__(self, instance, value):
        vv.is_positive_number(value=value,
                              object_type=instance.parent.__class__.__name__,
                              attr_name=self.__class__.__name__)
        instance._auto_suspend_secs = value
    def __delete__(self, instance):
        del instance._auto_suspend_secs



class ComputePoolAttrs:
    def __init__(self,parent):
        self.parent=parent
    name = Name()
    for_application=ForApplication()
    min_nodes = MinNodes()
    max_nodes = MaxNodes()
    instance_family = InstanceFamily()
    auto_resume = AutoResume()
    initially_suspended = InitiallySuspended()
    auto_suspend_secs = AutoSuspendSecs()

class ComputePool(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(session=session,user_id=user_id,logger=logger,database_required=False,schema_required=False)
        self.attr = ComputePoolAttrs(self)
        self.logger = logger.getChild(self.__class__.__name__)

    # setter methods
    def set_name(self, v): self.attr.name = v
    def set_for_application(self,v): self.attr.for_application=v
    def set_min_nodes(self, v): self.attr.min_nodes = v
    def set_max_nodes(self, v): self.attr.max_nodes = v
    def set_instance_family(self, v): self.attr.instance_family = v
    def set_auto_resume(self, v): self.attr.auto_resume = v
    def set_initially_suspended(self, v): self.attr.initially_suspended = v
    def set_auto_suspend_secs(self, v): self.attr.auto_suspend_secs = v
    def set_comment(self, v): self.attr.comment = v

    def set_object_properties_flag(self):
        self.flag_dic = {}
        def set_flag(tag, attrname):
            self.flag_dic[tag] = 1 if getattr(self.attr, attrname, None) is not None else 0

        set_flag(tags.FOR_APPLICATION,"for_application")
        set_flag(tags.AUTO_RESUME, "auto_resume")
        set_flag(tags.INITIALLY_SUSPENDED, "initially_suspended")
        set_flag(tags.AUTO_SUSPEND_SECS, "auto_suspend_secs")
        set_flag(tags.COMMENT, "comment")

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_computepool_qry(self):
        self.qry = f"CREATE COMPUTE POOL {self.attr.name[0]} "

    def add_properties_to_query(self):
        if tags.FOR_APPLICATION in self.property_lst:
            self.qry+= f"FOR APPLICATION {self.attr.for_application} "
            self.qry+= f"MIN_NODES = {self.attr.min_nodes} "
            self.qry+= f"MAX_NODES = {self.attr.max_nodes} "
            self.qry+= f"INSTANCE_FAMILY = {self.attr.instance_family} "
        else:
            self.qry+= f"MIN_NODES = {self.attr.min_nodes} "
            self.qry+= f"MAX_NODES = {self.attr.max_nodes} "
            self.qry+= f"INSTANCE_FAMILY = {self.attr.instance_family} "

        if tags.AUTO_RESUME in self.property_lst:
            self.qry += f"AUTO_RESUME = {self.attr.auto_resume} "
        if tags.INITIALLY_SUSPENDED in self.property_lst:
            self.qry += f"INITIALLY_SUSPENDED = {self.attr.initially_suspended} "
        if tags.AUTO_SUSPEND_SECS in self.property_lst:
            self.qry += f"AUTO_SUSPEND_SECS = {self.attr.auto_suspend_secs} "
        if tags.COMMENT in self.property_lst:
            self.qry += f"COMMENT = '{self.attr.comment}' "

    def alter_object(self):        
        for prop in self.property_lst:
            if prop == tags.MIN_NODES:
                self.qry = f"ALTER COMPUTE POOL {self.attr.name[0]} SET {tags.MIN_NODES} = {self.attr.min_nodes}"
                self.execute_final_query()
            if prop == tags.MAX_NODES:
                self.qry = f"ALTER COMPUTE POOL {self.attr.name[0]} SET {tags.MAX_NODES} = {self.attr.max_nodes}"
                self.execute_final_query()
            if prop == tags.INSTANCE_FAMILY:
                self.qry = f"ALTER COMPUTE POOL {self.attr.name[0]} SET {tags.INSTANCE_FAMILY} = {self.attr.instance_family}"
                self.execute_final_query()
            if prop == tags.AUTO_RESUME:
                self.qry = f"ALTER COMPUTE POOL {self.attr.name[0]} SET {tags.AUTO_RESUME} = {self.attr.auto_resume}"
                self.execute_final_query()
            if prop == tags.INITIALLY_SUSPENDED:
                self.qry = f"ALTER COMPUTE POOL {self.attr.name[0]} SET {tags.INITIALLY_SUSPENDED} = {self.attr.initially_suspended}"
                self.execute_final_query()
            if prop == tags.AUTO_SUSPEND_SECS:
                self.qry = f"ALTER COMPUTE POOL {self.attr.name[0]} SET {tags.AUTO_SUSPEND_SECS} = {self.attr.auto_suspend_secs}"
                self.execute_final_query()
            if prop == tags.COMMENT:
                self.qry = f"ALTER COMPUTE POOL {self.attr.name[0]} SET {tags.COMMENT} = {self.attr.comment}"
                self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER COMPUTE POOL {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming {self.__class__.__name__.upper()} {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()


    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_computepool_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=ComputePool(session=session,
                         user_id=user_id,
                         logger=logger)
        
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')

        obj_inst.set_base_attributes(kwargs=kwargs)

        obj_inst.logger.info(f"set name {kwargs[tags.NAME]}")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')
        obj_inst.logger.info(f"set name {obj_inst.attr.name}")

        obj_inst.logger.info(f"set min_nodes {kwargs[tags.MIN_NODES]}")
        if tags.MIN_NODES in kwargs.keys():
            obj_inst.set_min_nodes(kwargs[tags.MIN_NODES])
        else:
            obj_inst.set_min_nodes('NONE')

        obj_inst.logger.info(f"set max_nodes {kwargs[tags.MAX_NODES]}")
        if tags.MAX_NODES in kwargs.keys():
            obj_inst.set_max_nodes(kwargs[tags.MAX_NODES])
        else:
            obj_inst.set_max_nodes('NONE')

        obj_inst.logger.info(f"set instance_family {kwargs[tags.INSTANCE_FAMILY]}")
        if tags.INSTANCE_FAMILY in kwargs.keys():
            obj_inst.set_instance_family(kwargs[tags.INSTANCE_FAMILY])
        else:
            obj_inst.set_instance_family('NONE')

        obj_inst.logger.info(f"set auto_resume {kwargs[tags.AUTO_RESUME]}")
        if tags.AUTO_RESUME in kwargs.keys():
            obj_inst.set_auto_resume(kwargs[tags.AUTO_RESUME])
        else:
            obj_inst.set_auto_resume('NONE')

        obj_inst.logger.info(f"set initially_suspended {kwargs[tags.INITIALLY_SUSPENDED]}")
        if tags.INITIALLY_SUSPENDED in kwargs.keys():
            obj_inst.set_initially_suspended(kwargs[tags.INITIALLY_SUSPENDED])
        else:
            obj_inst.set_initially_suspended('NONE')

        obj_inst.logger.info(f"set auto_suspend_secs {kwargs[tags.AUTO_SUSPEND_SECS]}")
        if tags.AUTO_SUSPEND_SECS in kwargs.keys():
            obj_inst.set_auto_suspend_secs(kwargs[tags.AUTO_SUSPEND_SECS])
        else:
            obj_inst.set_auto_suspend_secs('NONE')

        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('write to git')
        obj_inst.write_file_to_git(object_name=obj_inst.attr.name[0],
                                   object_type=obj_inst.__class__.__name__,
                                   object_database='NA',
                                   object_schema='NA')
        
        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                           object_identifier=obj_inst.attr.name[0],
                                           qry=obj_inst.qry)


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()

