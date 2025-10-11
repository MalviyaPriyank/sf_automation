import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.organizationprofile.gvorganizationprofile import OrganizationProfileTag as tags

class OrganizationProfileName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class OrganizationProfileBody:
    def __get__(self, instance, owner):
        return instance._body
    def __set__(self, instance, value):
        instance._body = value
    def __delete__(self, instance):
        del instance._body

class OrganizationProfileVersion:
    def __get__(self, instance, owner):
        return instance._version
    def __set__(self, instance, value):
        instance._version = value
    def __delete__(self, instance):
        del instance._version

class OrganizationProfilePublish:
    def __get__(self, instance, owner):
        return instance._publish
    def __set__(self, instance, value):
        instance._publish = value
    def __delete__(self, instance):
        del instance._publish

class OrganizationProfileAttrs:
    name = OrganizationProfileName()
    body = OrganizationProfileBody()
    version = OrganizationProfileVersion()
    publish = OrganizationProfilePublish()

class OrganizationProfile(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = OrganizationProfileAttrs()
        self.session = session
        self.user_id = user_id
        self.logger = logger

    # Setter methods
    def set_name(self, v): self.attr.name = v
    def set_body(self, v): self.attr.body = v
    def set_version(self, v): self.attr.version = v
    def set_publish(self, v): self.attr.publish = v

    # Object property flags
    def set_object_properties_flag(self):
        self.flag_dic = {}
        for attr, tag in [
            ("body", tags.BODY),
            ("version", tags.VERSION),
            ("publish", tags.PUBLISH),
        ]:
            self.flag_dic[tag] = 1 if getattr(self.attr, attr) is not None else 0

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_organization_profile_qry(self):
        self.qry = f"CREATE ORGANIZATION PROFILE {self.attr.name[0]} "

    def add_properties_to_query(self):
        if tags.BODY in self.property_lst:
            self.qry += f"AS $$ {self.attr.body} $$ "
        if tags.VERSION in self.property_lst:
            self.qry += f"VERSION {self.attr.version} "
        if tags.PUBLISH in self.property_lst:
            self.qry += f"PUBLISH = {self.attr.publish} "

    def alter_object(self):
        for prop in self.property_lst:
            self.qry = f"ALTER ORGANIZATION PROFILE {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()
        if tags.NAME in self.property_lst:
            self.qry = f"ALTER ORGANIZATION PROFILE {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming organization profile {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_organization_profile_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        self.is_create = kwargs.get(tags.IS_CREATE)
        self.set_name(kwargs.get(tags.NAME))
        self.set_body(kwargs.get(tags.BODY))
        self.set_version(kwargs.get(tags.VERSION))
        self.set_publish(kwargs.get(tags.PUBLISH))
        self.prepare_query()
        self.execute_final_query()


class Operation:
    @staticmethod
    def create_object(session,user_id,logger,kwargs,*largs):
        obj_inst=OrganizationProfile(session=session,
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

        logger.info("set body")
        if tags.BODY in kwargs.keys():
            obj_inst.set_body(kwargs[tags.BODY])
        else:
            obj_inst.set_body('NONE')

        logger.info("set version")
        if tags.VERSION in kwargs.keys():
            obj_inst.set_version(kwargs[tags.VERSION])
        else:
            obj_inst.set_version('NONE')

        logger.info("set publish")
        if tags.PUBLISH in kwargs.keys():
            obj_inst.set_publish(kwargs[tags.PUBLISH])
        else:
            obj_inst.set_publish('NONE')

        logger.info('prepare query')
        obj_inst.prepare_query()
        
        logger.info('execute query')
        obj_inst.execute_final_query()

        logger.info('create deployment entry')
        obj_inst.create_deployment_entry()


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()
