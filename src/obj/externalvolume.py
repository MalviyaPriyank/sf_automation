import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.externalvolume.gvexternalvolume import ExternalVolumeTag as tags

class EVName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class EVStorageLocations:
    def __get__(self, instance, owner):
        return instance._storage_locations
    def __set__(self, instance, value):
        instance._storage_locations = value
    def __delete__(self, instance):
        del instance._storage_locations

class EVAllowWrites:
    def __get__(self, instance, owner):
        return instance._allow_writes
    def __set__(self, instance, value):
        instance._allow_writes = value
    def __delete__(self, instance):
        del instance._allow_writes

class EVComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = value
    def __delete__(self, instance):
        del instance._comment

class EVTagClause:
    def __get__(self, instance, owner):
        return instance._tag_clause
    def __set__(self, instance, value):
        if isinstance(value, dict):
            clause = ", ".join(f"{k} = '{v}'" for k, v in value.items())
        else:
            k, v = next(iter(value.items()))
            clause = f"{k} = '{v}'"
        instance._tag_clause = f"TAG {clause}"
    def __delete__(self, instance):
        del instance._tag_clause

class ExternalVolumeAttrs:
    name = EVName()
    storage_locations = EVStorageLocations()
    allow_writes = EVAllowWrites()
    comment = EVComment()
    tag_clause = EVTagClause()

class ExternalVolume(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = ExternalVolumeAttrs()
        self.session = session
        self.user_id = user_id
        self.logger = logger

    # setter methods
    def set_name(self, v): self.attr.name = v
    def set_storage_locations(self, v): self.attr.storage_locations = v
    def set_allow_writes(self, v): self.attr.allow_writes = v
    def set_comment(self, v): self.attr.comment = v
    def set_tag_clause(self, v): self.attr.tag_clause = v

    def set_object_properties_flag(self):
        self.flag_dic = {}
        def set_flag(tag, attrname):
            self.flag_dic[tag] = 1 if getattr(self.attr, attrname, None) is not None else 0

        set_flag(tags.STORAGE_LOCATIONS, "storage_locations")
        set_flag(tags.ALLOW_WRITES, "allow_writes")
        set_flag(tags.COMMENT, "comment")
        set_flag(tags.TAG_CLAUSE, "tag_clause")

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_externalvolume_qry(self):
        self.qry = f"CREATE EXTERNAL VOLUME {self.attr.name[0]} "

    def add_properties_to_query(self):
        if tags.STORAGE_LOCATIONS in self.property_lst:
            self.qry += f"STORAGE_LOCATIONS = {self.attr.storage_locations} "
        if tags.ALLOW_WRITES in self.property_lst:
            self.qry += f"ALLOW_WRITES = {self.attr.allow_writes} "
        if tags.COMMENT in self.property_lst:
            self.qry += f"COMMENT = '{self.attr.comment}' "
        if tags.TAG_CLAUSE in self.property_lst:
            self.qry += f"{self.attr.tag_clause} "

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
        if self.is_create == "TRUE":
            self.set_create_externalvolume_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        self.is_create = kwargs.get(tags.IS_CREATE)
        self.set_name(kwargs.get(tags.NAME))
        self.set_storage_locations(kwargs.get(tags.STORAGE_LOCATIONS))
        self.set_allow_writes(kwargs.get(tags.ALLOW_WRITES))
        self.set_comment(kwargs.get(tags.COMMENT))
        self.set_tag_clause(kwargs.get(tags.TAG_CLAUSE))

        self.prepare_query()
        self.execute_final_query()

class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        obj_inst=DatabaseRole(session=session,
                         user_id=user_id,
                         logger=logger)
        logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        logger.info("set database")
        if tags.DATABASE in kwargs.keys():
            obj_inst.set_database(kwargs[tags.DATABASE])
        else:
            obj_inst.set_database(kwargs[tags.DATABASE])

        logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name(kwargs[tags.NAME])

        logger.info("set comment")
        if tags.COMMENT in kwargs.keys():
            obj_inst.set_comment(kwargs[tags.COMMENT])
        else:
            obj_inst.set_comment(kwargs[tags.COMMENT])


        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()

