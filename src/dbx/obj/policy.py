import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from src.dbx.vars.obj.gvpolicy import PolicyTags as tags
from src.validation.validatevalue import ValidateValue as vv
from src.validation.validateobject import ValidateObject as vo
from src.usr.user import ChatHistory


class DefinitionCustomTagsTestTagsType:
    def __get__(self, instance, owner):
        return instance._definition_custom_tags_test_tags_type
    
    def __set__(self, instance, value):
        instance._definition_custom_tags_test_tags_type=value

    def __delete__(self, instance):
        del instance._definition_custom_tags_test_tags_type


class DefinitionCustomTagsTestTagsValue:
    def __get__(self, instance, owner):
        return instance._definition_custom_tags_test_tags_value
    
    def __set__(self, instance, value):
        instance._definition_custom_tags_test_tags_value=value

    def __delete__(self, instance):
        del instance._definition_custom_tags_test_tags_value


class Description:
    def __get__(self, instance, owner):
        return instance._description
    
    def __set__(self, instance, value):
        instance._description=value

    def __delete__(self, instance):
        del instance._description


class LibrariesCranPackage:
    def __get__(self, instance, owner):
        return instance._libraries_cran_package
    
    def __set__(self, instance, value):
        instance._libraries_cran_package=value

    def __delete__(self, instance):
        del instance._libraries_cran_package


class LibrariesCranRepo:
    def __get__(self, instance, owner):
        return instance._libraries_cran_repo
    
    def __set__(self, instance, value):
        instance._libraries_cran_repo=value

    def __delete__(self, instance):
        del instance._libraries_cran_repo


class LibrariesEgg:
    def __get__(self, instance, owner):
        return instance._libraries_egg
    
    def __set__(self, instance, value):
        instance._libraries_egg=value

    def __delete__(self, instance):
        del instance._libraries_egg


class LibrariesJar:
    def __get__(self, instance, owner):
        return instance._libraries_jar
    
    def __set__(self, instance, value):
        instance._libraries_jar=value

    def __delete__(self, instance):
        del instance._libraries_jar


class LibrariesMavenCoordinates:
    def __get__(self, instance, owner):
        return instance._libraries_maven_coordinates
    
    def __set__(self, instance, value):
        instance._libraries_maven_coordinates=value

    def __delete__(self, instance):
        del instance._libraries_maven_coordinates


class LibrariesMavenExclusions:
    def __get__(self, instance, owner):
        return instance._libraries_maven_exclusions
    
    def __set__(self, instance, value):
        instance._libraries_maven_exclusions=value

    def __delete__(self, instance):
        del instance._libraries_maven_exclusions


class LibrariesMavenRepo:
    def __get__(self, instance, owner):
        return instance._libraries_maven_repo
    
    def __set__(self, instance, value):
        instance._libraries_maven_repo=value

    def __delete__(self, instance):
        del instance._libraries_maven_repo


class LibrariesPypiPackage:
    def __get__(self, instance, owner):
        return instance._libraries_pypi_package
    
    def __set__(self, instance, value):
        instance._libraries_pypi_package=value

    def __delete__(self, instance):
        del instance._libraries_pypi_package


class LibrariesPypiRepo:
    def __get__(self, instance, owner):
        return instance._libraries_pypi_repo
    
    def __set__(self, instance, value):
        instance._libraries_pypi_repo=value

    def __delete__(self, instance):
        del instance._libraries_pypi_repo


class Requirements:
    def __get__(self, instance, owner):
        return instance._requirements
    
    def __set__(self, instance, value):
        instance._requirements=value

    def __delete__(self, instance):
        del instance._requirements


class WHL:
    def __get__(self, instance, owner):
        return instance._whl
    
    def __set__(self, instance, value):
        instance._whl=value

    def __delete__(self, instance):
        del instance._whl


class MaxClustersPerUser:
    def __get__(self, instance, owner):
        return instance._max_clusters_per_user
    
    def __set__(self, instance, value):
        instance._max_clusters_per_user=value

    def __delete__(self, instance):
        del instance._max_clusters_per_user


class Name:
    def __get__(self, instance, owner):
        return instance._name
    
    def __set__(self, instance, value):
        instance._name=value

    def __delete__(self, instance):
        del instance._name


class PolicyFamilyDefinitionOverridesCustomTagsTestTagType:
    def __get__(self, instance, owner):
        return instance._policy_family_definition_overrides_custom_tags_test_tag_type
    
    def __set__(self, instance, value):
        instance._policy_family_definition_overrides_custom_tags_test_tag_type=value

    def __delete__(self, instance):
        del instance._policy_family_definition_overrides_custom_tags_test_tag_type


class PolicyFamilyDefinitionOverridesCustomTagsTestTagValue:
    def __get__(self, instance, owner):
        return instance._policy_family_definition_overrides_custom_tags_test_tag_value
    
    def __set__(self, instance, value):
        instance._policy_family_definition_overrides_custom_tags_test_tag_value=value

    def __delete__(self, instance):
        del instance._policy_family_definition_overrides_custom_tags_test_tag_value


class PolicyAttrs:
    def __init__(self,parent):
        self.parent=parent

    definition_custom_tags_test_tags_type=DefinitionCustomTagsTestTagsType()
    definition_custom_tags_test_tags_value=DefinitionCustomTagsTestTagsValue()
    description=Description()
    libraries_cran_package=LibrariesCranPackage()
    libraries_cran_repo=LibrariesCranRepo()
    libraries_egg=LibrariesEgg()
    libraries_jar=LibrariesJar()
    libraries_maven_coordinates=LibrariesMavenCoordinates()
    libraries_maven_exclusions=LibrariesMavenExclusions()
    libraries_maven_repo=LibrariesMavenRepo()
    libraries_pypi_package=LibrariesPypiPackage()
    libraries_pypi_repo=LibrariesPypiRepo()
    requirements=Requirements()
    whl=WHL()
    max_clusters_per_user=MaxClustersPerUser()
    name=Name()
    policy_family_definition_overrides_custom_tags_test_tag_type=PolicyFamilyDefinitionOverridesCustomTagsTestTagType()
    policy_family_definition_overrides_custom_tags_test_tag_value=PolicyFamilyDefinitionOverridesCustomTagsTestTagValue()
    

class Policy():
    def __init__(self, session, user_id, logger):
        super().__init__(session=session,user_id=user_id,logger=logger)
        self.attr = PolicyAttrs(self)
        self.logger = logger.getChild(self.__class__.__name__)


    def set_definition_custom_tags_test_tags_type(self, v): self.attr.definition_custom_tags_test_tags_type = v
    def set_definition_custom_tags_test_tags_value(self, v): self.attr.definition_custom_tags_test_tags_value = v
    def set_description(self, v): self.attr.description = v
    def set_libraries_cran_package(self, v): self.attr.libraries_cran_package = v
    def set_libraries_cran_repo(self, v): self.attr.libraries_cran_repo = v
    def set_libraries_egg(self, v): self.attr.libraries_egg = v
    def set_libraries_jar(self, v): self.attr.libraries_jar = v
    def set_libraries_maven_coordinates(self, v): self.attr.libraries_maven_coordinates = v
    def set_libraries_maven_exclusions(self, v): self.attr.libraries_maven_exclusions = v
    def set_libraries_maven_repo(self, v): self.attr.libraries_maven_repo = v
    def set_libraries_pypi_package(self, v): self.attr.libraries_pypi_package = v
    def set_libraries_pypi_repo(self, v): self.attr.libraries_pypi_repo = v
    def set_requirements(self, v): self.attr.requirements = v
    def set_whl(self, v): self.attr.whl = v
    def set_max_clusters_per_user(self, v): self.attr.max_clusters_per_user = v
    def set_name(self, v): self.attr.name = v
    def set_policy_family_definition_overrides_custom_tags_test_tag_type(self, v): self.attr.policy_family_definition_overrides_custom_tags_test_tag_type = v
    def set_policy_family_definition_overrides_custom_tags_test_tag_value(self, v): self.attr.policy_family_definition_overrides_custom_tags_test_tag_value = v

    # Object property flags
    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(tags.DEFINITION_CUSTOM_TAGS_TEST_TAGS_TYPE,"definition_custom_tags_test_tags_type")
        set_flag(tags.DEFINITION_CUSTOM_TAGS_TEST_TAGS_VALUE,"definition_custom_tags_test_tags_value")
        set_flag(tags.DESCRIPTION,"description")
        set_flag(tags.LIBRARIES_CRAN_PACKAGE,"libraries_cran_package")
        set_flag(tags.LIBRARIES_CRAN_REPO,"libraries_cran_repo")
        set_flag(tags.LIBRARIES_EGG,"libraries_egg")
        set_flag(tags.LIBRARIES_JAR,"libraries_jar")
        set_flag(tags.LIBRARIES_MAVEN_COORDINATES,"libraries_maven_coordinates")
        set_flag(tags.LIBRARIES_MAVEN_EXCLUSIONS,"libraries_maven_exclusions")
        set_flag(tags.LIBRARIES_MAVEN_REPO,"libraries_maven_repo")
        set_flag(tags.LIBRARIES_PYPI_PACKAGE,"libraries_pypi_package")
        set_flag(tags.LIBRARIES_PYPI_REPO,"libraries_pypi_repo")
        set_flag(tags.REQUIREMENTS,"requirements")
        set_flag(tags.WHL,"whl")
        set_flag(tags.MAX_CLUSTERS_PER_USER,"max_clusters_per_user")
        set_flag(tags.NAME,"name")
        set_flag(tags.POLICY_FAMILY_DEFINITION_OVERRIDES_CUSTOM_TAGS_TEST_TAG_TYPE,"policy_family_definition_overrides_custom_tags_test_tag_type")
        set_flag(tags.POLICY_FAMILY_DEFINITION_OVERRIDES_CUSTOM_TAGS_TEST_TAG_VALUE,"policy_family_definition_overrides_custom_tags_test_tag_value")
        

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

#3 different payloads required
    def prepare_payload(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.payload={}
        for prop in self.property_lst:
            if prop == tags.AUTO_STOP_MINS:
                self.payload[tags.AUTO_STOP_MINS] = self.attr.auto_stop_mins
            if prop==tags.CLUSTER_SIZE:
                self.payload[tags.CLUSTER_SIZE]=self.attr.cluster_size
            if prop == tags.CREATOR_NAME:
                self.payload[tags.CREATOR_NAME] = self.attr.creator_name
            if prop==tags.ENABLE_PHOTON:
                self.payload[tags.ENABLE_PHOTON]=self.attr.enable_photon
            if prop == tags.ENABLE_SERVERLESS_COMPUTE:
                self.payload[tags.ENABLE_SERVERLESS_COMPUTE] = self.attr.enable_serverless_compute
            if prop==tags.INSTANCE_PROFILE_ARN:
                self.payload[tags.INSTANCE_PROFILE_ARN]=self.attr.instance_profile_arn
            if prop == tags.MAX_NUM_CLUSTERS:
                self.payload[tags.MAX_NUM_CLUSTERS] = self.attr.max_num_clusters
            if prop==tags.MIN_NUM_CLUSTERS:
                self.payload[tags.MIN_NUM_CLUSTERS]=self.attr.min_num_clusters
            if prop == tags.NAME:
                self.payload[tags.NAME] = self.attr.name
            if prop==tags.SPOT_INSTANCE_POLICY:
                self.payload[tags.SPOT_INSTANCE_POLICY]=self.attr.spot_instance_policy
            if prop==tags.WAREHOUSE_TYPE:
                self.payload[tags.WAREHOUSE_TYPE] = self.attr.warehouse_type

class Operation:
    @staticmethod
    def create_object(session,user_chat_inst:ChatHistory,user_id,logger,kwargs,*largs):
        obj_inst=Policy(session=session,
                         user_id=user_id,
                         logger=logger)
        obj_inst.logger.info(f"Operating on {obj_inst.__class__.__name__}, create flag : {kwargs[tags.IS_CREATE]}")
        obj_inst.logger.info(f'dictionary passed {kwargs}')

        if tags.DEFINITION_CUSTOM_TAGS_TEST_TAGS_TYPE in kwargs.keys():
            obj_inst.set_definition_custom_tags_test_tags_type(kwargs[tags.DEFINITION_CUSTOM_TAGS_TEST_TAGS_TYPE])
        else:
            obj_inst.set_definition_custom_tags_test_tags_type('NONE')
        obj_inst.logger.info(f"set definition_custom_tags_test_tags_type {obj_inst.attr.definition_custom_tags_test_tags_type}")

        
        if tags.DEFINITION_CUSTOM_TAGS_TEST_TAGS_VALUE in kwargs.keys():
            obj_inst.set_definition_custom_tags_test_tags_value(kwargs[tags.DEFINITION_CUSTOM_TAGS_TEST_TAGS_VALUE])
        else:
            obj_inst.set_definition_custom_tags_test_tags_value('NONE')
        obj_inst.logger.info(f"set definition_custom_tags_test_tags_value {obj_inst.attr.definition_custom_tags_test_tags_value}")

        
        if tags.DESCRIPTION in kwargs.keys():
            obj_inst.set_description(kwargs[tags.DESCRIPTION])
        else:
            obj_inst.set_description('NONE')
        obj_inst.logger.info(f"set description {obj_inst.attr.description}")

        
        if tags.LIBRARIES_CRAN_PACKAGE in kwargs.keys():
            obj_inst.set_libraries_cran_package(kwargs[tags.LIBRARIES_CRAN_PACKAGE])
        else:
            obj_inst.set_libraries_cran_package('NONE')
        obj_inst.logger.info(f"set libraries_cran_package {obj_inst.attr.libraries_cran_package}")


        if tags.LIBRARIES_CRAN_REPO in kwargs.keys():
            obj_inst.set_libraries_cran_repo(kwargs[tags.LIBRARIES_CRAN_REPO])
        else:
            obj_inst.set_libraries_cran_repo('NONE')
        obj_inst.logger.info(f"set libraries_cran_repo {obj_inst.attr.libraries_cran_repo}")


        if tags.LIBRARIES_EGG in kwargs.keys():
            obj_inst.set_libraries_egg(kwargs[tags.LIBRARIES_EGG])
        else:
            obj_inst.set_libraries_egg('NONE')
        obj_inst.logger.info(f"set libraries_egg {obj_inst.attr.libraries_egg}")

        
        if tags.LIBRARIES_JAR in kwargs.keys():
            obj_inst.set_libraries_jar(kwargs[tags.LIBRARIES_JAR])
        else:
            obj_inst.set_libraries_jar('NONE')
        obj_inst.logger.info(f"set libraries_jar {obj_inst.attr.libraries_jar}")

        
        if tags.LIBRARIES_MAVEN_COORDINATES in kwargs.keys():
            obj_inst.set_libraries_maven_coordinates(kwargs[tags.LIBRARIES_MAVEN_COORDINATES])
        else:
            obj_inst.set_libraries_maven_coordinates('NONE')
        obj_inst.logger.info(f"set libraries_maven_coordinates {obj_inst.attr.libraries_maven_coordinates}")


        if tags.LIBRARIES_MAVEN_EXCLUSIONS in kwargs.keys():
            obj_inst.set_libraries_maven_exclusions(kwargs[tags.LIBRARIES_MAVEN_EXCLUSIONS])
        else:
            obj_inst.set_libraries_maven_exclusions('NONE')
        obj_inst.logger.info(f"set libraries_maven_exclusions {obj_inst.attr.libraries_maven_exclusions}")

        
        if tags.LIBRARIES_MAVEN_REPO in kwargs.keys():
            obj_inst.set_libraries_maven_repo(kwargs[tags.LIBRARIES_MAVEN_REPO])
        else:
            obj_inst.set_libraries_maven_repo('NONE')
        obj_inst.logger.info(f"set libraries_maven_repo {obj_inst.attr.libraries_maven_repo}")

        
        if tags.LIBRARIES_PYPI_PACKAGE in kwargs.keys():
            obj_inst.set_libraries_pypi_package(kwargs[tags.LIBRARIES_PYPI_PACKAGE])
        else:
            obj_inst.set_libraries_pypi_package('NONE')
        obj_inst.logger.info(f"set libraries_pypi_package {obj_inst.attr.libraries_pypi_package}")


        if tags.LIBRARIES_PYPI_REPO in kwargs.keys():
            obj_inst.set_libraries_pypi_repo(kwargs[tags.LIBRARIES_PYPI_REPO])
        else:
            obj_inst.set_libraries_pypi_repo('NONE')
        obj_inst.logger.info(f"set libraries_pypi_repo {obj_inst.attr.libraries_pypi_repo}")


        if tags.REQUIREMENTS in kwargs.keys():
            obj_inst.set_requirements(kwargs[tags.REQUIREMENTS])
        else:
            obj_inst.set_requirements('NONE')
        obj_inst.logger.info(f"set requirements {obj_inst.attr.requirements}")

        
        if tags.WHL in kwargs.keys():
            obj_inst.set_whl(kwargs[tags.WHL])
        else:
            obj_inst.set_whl('NONE')
        obj_inst.logger.info(f"set whl {obj_inst.attr.whl}")

        
        if tags.MAX_CLUSTERS_PER_USER in kwargs.keys():
            obj_inst.set_max_clusters_per_user(kwargs[tags.MAX_CLUSTERS_PER_USER])
        else:
            obj_inst.set_max_clusters_per_user('NONE')
        obj_inst.logger.info(f"set max_clusters_per_user {obj_inst.attr.max_clusters_per_user}")


        if tags.NAME in kwargs.keys():
            obj_inst.set_name(kwargs[tags.NAME])
        else:
            obj_inst.set_name('NONE')
        obj_inst.logger.info(f"set name {obj_inst.attr.name}")


        if tags.POLICY_FAMILY_DEFINITION_OVERRIDES_CUSTOM_TAGS_TEST_TAG_TYPE in kwargs.keys():
            obj_inst.set_policy_family_definition_overrides_custom_tags_test_tag_type(kwargs[tags.POLICY_FAMILY_DEFINITION_OVERRIDES_CUSTOM_TAGS_TEST_TAG_TYPE])
        else:
            obj_inst.set_policy_family_definition_overrides_custom_tags_test_tag_type('NONE')
        obj_inst.logger.info(f"set policy_family_definition_overrides_custom_tags_test_tag_type {obj_inst.attr.policy_family_definition_overrides_custom_tags_test_tag_type}")


        if tags.POLICY_FAMILY_DEFINITION_OVERRIDES_CUSTOM_TAGS_TEST_TAG_VALUE in kwargs.keys():
            obj_inst.set_policy_family_definition_overrides_custom_tags_test_tag_value(kwargs[tags.POLICY_FAMILY_DEFINITION_OVERRIDES_CUSTOM_TAGS_TEST_TAG_VALUE])
        else:
            obj_inst.set_policy_family_definition_overrides_custom_tags_test_tag_value('NONE')
        obj_inst.logger.info(f"set policy_family_definition_overrides_custom_tags_test_tag_value {obj_inst.attr.policy_family_definition_overrides_custom_tags_test_tag_value}")


        obj_inst.logger.info('prepare query')
        obj_inst.prepare_query()
        obj_inst.print_query()
        
        obj_inst.logger.info('execute query')
        obj_inst.execute_final_query()

        obj_inst.logger.info('create deployment entry')
        obj_inst.create_deployment_entry()
        
        obj_inst.write_file_to_git()

        user_chat_inst.add_to_chat_history(object_type=obj_inst.__class__.__name__,
                                           object_identifier=obj_inst.attr.name[0],
                                           qry=obj_inst.qry)


    @classmethod
    def get_attributes(cls):
        return tags().get_attributes_with_description()


