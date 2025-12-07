import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.tag.gvtag import TagTag as tags
from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo
from src.usr.user import ChatHistory


class Name:
    def __get__(self,instance,owner):
        return (instance._name,instance._rename_to)

    def __set__(self,instance,value):
        instance.parent.print_setter(self.__class__.__name__,value)
        if instance.parent.is_create=="TRUE":
            name=value["NAME"]
            vv.required_attribute_check(name,instance.parent.__class__.__name__,self.__class__.__name__)
            vo.is_new_object(
                session=instance.parent.session,
                object_type=instance.parent.__class__.__name__,
                object_name=name,
                **{'DATABASE': instance.parent.attr.database,
                   'SCHEMA':instance.parent.attr.schema}
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
                vv.required_attribute_check(old_name,instance.parent.__class__.__name__,self.__class__.__name__)
                vo.object_exist(
                    session=instance.parent.session,
                    object_type=instance.parent.__class__.__name__,
                    object_name=old_name,
                    **{'DATABASE':instance.parent.attr.database,
                       'SCHEMA':instance.parent.attr.schema}
                )
                vo.is_new_object(
                    session=instance.parent.session,
                    object_type=instance.parent.__class__.__name__,
                    object_name=new_name,
                    **{'DATABASE': instance.parent.attr.database,
                        'SCHEMA':instance.parent.attr.schema}
                )
                instance._name=old_name
                instance._rename_to=new_name
            else:
                instance._name=old_name
                instance._rename_to="NONE"

    def __delete__(self,instance):
        del instance._name
        del instance._rename_to

class AllowedValue:
    def __get__(self, instance, owner):
        return instance._allowed_values
    def __set__(self, instance, value):
        instance.parent.print_setter(self.__class__.__name__,value)
        vv.is_list(
            value=value,
            object_type=instance.parent.__class__.__name__,
            attr_name=self.__class__.__name__
        )
        val_str=""
        if len(value)==1:
            val_str=f"'{value[0]}'"
        else:
            for i in range(0,len(value)):
                if i != len(value)-1:
                    val_str=val_str+ f"'{value[i]}', "
                elif i == len(value)-1:
                    val_str=val_str + f"'{value[i]}'"
        instance._allowed_values=val_str


    def __delete__(self, instance):
        del instance._allowed_values

class TagAttrs:
    def __init__(self,parent):
        self.parent=parent
    name = Name()
    allowed_values = AllowedValue()

class Tag(BaseObject):
    def __init__(self, session, user_id, logger):
        super().__init__(
            session=session,
            user_id=user_id,
            logger=logger,
            database_required=True,
            schema_required=True
        )
        self.attr = TagAttrs(parent=self)
        self.logger = logger.getChild(self.__class__.__name__)

    # setter convenience methods
    def set_name(self, v): self.attr.name = v
    def set_allowed_values(self, v): self.attr.allowed_values = v

    def set_object_properties_flag(self):
        self.flag_dic = {}
        def set_flag(tag, attrname):
            self.flag_dic[tag] = 1 if getattr(self.attr, attrname, None) is not None else 0

        set_flag(tags.ALLOWED_VALUES, "allowed_values")
        set_flag(tags.COMMENT, "comment")

    def check_properties_to_set(self):
        self.property_lst = [p for p, flag in self.flag_dic.items() if flag == 1]

    def set_create_tag_qry(self):
        self.qry = f"""CREATE TAG 
        {self.attr.database}.{self.attr.schema}.{self.attr.name[0]} """

    def add_properties_to_query(self):
        for prop in self.property_lst:
            if prop == tags.ALLOWED_VALUES:
                self.qry += f"\n {tags.ALLOWED_VALUES} {self.attr.allowed_values}"
    '''
    def alter_object(self):
        for prop in self.property_lst:
            # SET some property
            self.qry = f"ALTER TAG {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()

        if tags.NAME in self.property_lst:
            self.qry = f"ALTER TAG {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming tag {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()
    '''

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_tag_qry()
            self.add_properties_to_query()
        #else:
        #    self.alter_object()

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=Tag(session=session,
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

        if tags.ALLOWED_VALUES in kwargs.keys():
            obj_inst.set_allowed_values(kwargs[tags.ALLOWED_VALUES])
        else:
            obj_inst.set_allowed_values('NONE')
        obj_inst.logger.info(f"set ALLOWED_VALUES {obj_inst.attr.allowed_values}")


        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        
        obj_inst.logger.info('execute query')
        obj_inst.execute_final_query()

        obj_inst.logger.info('create deployment entry')
        obj_inst.create_deployment_entry()

        obj_inst.logger.info('write to git')
        obj_inst.write_file_to_git()

        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                                object_identifier=obj_inst.attr.name[0],
                                                qry=obj_inst.qry)

    @staticmethod
    def show_object(session,user_id,kwargs,logger):
        obj_inst=Tag(session=session,
                     user_id=user_id,
                     logger=logger)
        
        obj_inst.logger.info(f"SHOW  {obj_inst.__class__.__name__}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.set_base_attributes(kwargs=kwargs,**{'SHOW_OBJECT':'TRUE'})
        return obj_inst.show_object()


    @classmethod
    def get_attributes(cls,**kwargs):
        if kwargs['SHOW_OBJECT']:
            return tags().get_show_attributes_with_description()
        else:
            return tags().get_attributes_with_description()


