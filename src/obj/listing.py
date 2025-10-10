import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.listing.gvlisting import ListingTag as tags

class ListingName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class ListingShare:
    def __get__(self, instance, owner):
        return instance._share
    def __set__(self, instance, value):
        instance._share = value
    def __delete__(self, instance):
        del instance._share

class ListingApplicationPackage:
    def __get__(self, instance, owner):
        return instance._application_package
    def __set__(self, instance, value):
        instance._application_package = value
    def __delete__(self, instance):
        del instance._application_package

class ListingYamlManifest:
    def __get__(self, instance, owner):
        return instance._yaml_manifest
    def __set__(self, instance, value):
        instance._yaml_manifest = value
    def __delete__(self, instance):
        del instance._yaml_manifest

class ListingPublish:
    def __get__(self, instance, owner):
        return instance._publish
    def __set__(self, instance, value):
        instance._publish = value
    def __delete__(self, instance):
        del instance._publish

class ListingReview:
    def __get__(self, instance, owner):
        return instance._review
    def __set__(self, instance, value):
        instance._review = value
    def __delete__(self, instance):
        del instance._review

class ListingComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = value
    def __delete__(self, instance):
        del instance._comment

class ListingAttrs:
    name = ListingName()
    share = ListingShare()
    application_package = ListingApplicationPackage()
    yaml_manifest = ListingYamlManifest()
    publish = ListingPublish()
    review = ListingReview()
    comment = ListingComment()

class Listing(BaseObject):
    def __init__(self, session, user_id):
        super().__init__(session=session,user_id=user_id)
        self.attr = ListingAttrs()

    # Setter methods
    def set_name(self, v): self.attr.name = v
    def set_share(self, v): self.attr.share = v
    def set_application_package(self, v): self.attr.application_package = v
    def set_yaml_manifest(self, v): self.attr.yaml_manifest = v
    def set_publish(self, v): self.attr.publish = v
    def set_review(self, v): self.attr.review = v
    def set_comment(self, v): self.attr.comment = v

    # Object property flags
    def set_object_properties_flag(self):
        self.flag_dic = {}
        for attr, tag in [
            ("share", tags.SHARE),
            ("application_package", tags.APPLICATION_PACKAGE),
            ("yaml_manifest", tags.YAML_MANIFEST),
            ("publish", tags.PUBLISH),
            ("review", tags.REVIEW),
            ("comment", tags.COMMENT),
        ]:
            self.flag_dic[tag] = 1 if getattr(self.attr, attr) is not None else 0

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_listing_qry(self):
        self.qry = f"CREATE EXTERNAL LISTING {self.attr.name[0]} "

    def add_properties_to_query(self):
        if tags.SHARE in self.property_lst:
            self.qry += f"SHARE {self.attr.share} "
        if tags.APPLICATION_PACKAGE in self.property_lst:
            self.qry += f"APPLICATION PACKAGE {self.attr.application_package} "
        if tags.YAML_MANIFEST in self.property_lst:
            self.qry += f"AS $$ {self.attr.yaml_manifest} $$ "
        if tags.PUBLISH in self.property_lst:
            self.qry += f"PUBLISH = {self.attr.publish} "
        if tags.REVIEW in self.property_lst:
            self.qry += f"REVIEW = {self.attr.review} "
        if tags.COMMENT in self.property_lst:
            self.qry += f"COMMENT = '{self.attr.comment}' "

    def alter_object(self):
        for prop in self.property_lst:
            self.qry = f"ALTER LISTING {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()
        if tags.NAME in self.property_lst:
            self.qry = f"ALTER LISTING {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming listing {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_listing_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        self.is_create = kwargs.get(tags.IS_CREATE)
        self.set_name(kwargs.get(tags.NAME))
        self.set_share(kwargs.get(tags.SHARE))
        self.set_application_package(kwargs.get(tags.APPLICATION_PACKAGE))
        self.set_yaml_manifest(kwargs.get(tags.YAML_MANIFEST))
        self.set_publish(kwargs.get(tags.PUBLISH))
        self.set_review(kwargs.get(tags.REVIEW))
        self.set_comment(kwargs.get(tags.COMMENT))
        self.prepare_query()
        self.execute_final_query()

class Operation:
    @staticmethod
    def create_object(session,user_id,kwargs,*largs):
        obj_inst=Listing(session=session,
                         user_id=user_id
                        )
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')
        obj_inst.is_create=kwargs[tags.IS_CREATE]

        obj_inst.logger.info("set name")
        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')

        obj_inst.logger.info("set share")
        if tags.SHARE in kwargs.keys():
            obj_inst.set_share(kwargs[tags.SHARE])
        else:
            obj_inst.set_share('NONE')

        obj_inst.logger.info("set application_package")
        if tags.APPLICATION_PACKAGE in kwargs.keys():
            obj_inst.set_application_package(kwargs[tags.APPLICATION_PACKAGE])
        else:
            obj_inst.set_application_package('NONE')

        obj_inst.logger.info("set yaml_manifest")
        if tags.YAML_MANIFEST in kwargs.keys():
            obj_inst.set_yaml_manifest(kwargs[tags.YAML_MANIFEST])
        else:
            obj_inst.set_yaml_manifest('NONE')

        obj_inst.logger.info("set publish")
        if tags.PUBLISH in kwargs.keys():
            obj_inst.set_publish(kwargs[tags.PUBLISH])
        else:
            obj_inst.set_publish('NONE')

        obj_inst.logger.info("set review")
        if tags.REVIEW in kwargs.keys():
            obj_inst.set_review(kwargs[tags.REVIEW])
        else:
            obj_inst.set_review('NONE')

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

