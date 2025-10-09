import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../vars'))

from .baseobj import BaseObject
from vars.obj.gitrepository.gvgitrepository import GitRepositoryTag as tags

class GitRepositoryName:
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        del instance._name

class GitRepositoryOrigin:
    def __get__(self, instance, owner):
        return instance._origin
    def __set__(self, instance, value):
        instance._origin = value
    def __delete__(self, instance):
        del instance._origin

class GitRepositoryApiIntegration:
    def __get__(self, instance, owner):
        return instance._api_integration
    def __set__(self, instance, value):
        instance._api_integration = value
    def __delete__(self, instance):
        del instance._api_integration

class GitRepositoryCredentials:
    def __get__(self, instance, owner):
        return instance._credentials
    def __set__(self, instance, value):
        instance._credentials = value
    def __delete__(self, instance):
        del instance._credentials

class GitRepositoryComment:
    def __get__(self, instance, owner):
        return instance._comment
    def __set__(self, instance, value):
        instance._comment = value
    def __delete__(self, instance):
        del instance._comment

class GitRepositoryTags:
    def __get__(self, instance, owner):
        return instance._tags
    def __set__(self, instance, value):
        instance._tags = value
    def __delete__(self, instance):
        del instance._tags

class GitRepositoryAttrs:
    name = GitRepositoryName()
    origin = GitRepositoryOrigin()
    api_integration = GitRepositoryApiIntegration()
    credentials = GitRepositoryCredentials()
    comment = GitRepositoryComment()
    tags = GitRepositoryTags()

class GitRepository(BaseObject):
    def __init__(self, session, user_id, logger):
        self.attr = GitRepositoryAttrs()
        self.session = session
        self.user_id = user_id
        self.logger = logger

    # Setter methods
    def set_name(self, v): self.attr.name = v
    def set_origin(self, v): self.attr.origin = v
    def set_api_integration(self, v): self.attr.api_integration = v
    def set_credentials(self, v): self.attr.credentials = v
    def set_comment(self, v): self.attr.comment = v
    def set_tags(self, v): self.attr.tags = v

    # Object property flags
    def set_object_properties_flag(self):
        self.flag_dic = {}
        for attr, tag in [
            ("origin", tags.ORIGIN),
            ("api_integration", tags.API_INTEGRATION),
            ("credentials", tags.CREDENTIALS),
            ("comment", tags.COMMENT),
            ("tags", tags.TAGS),
        ]:
            self.flag_dic[tag] = 1 if getattr(self.attr, attr) is not None else 0

    def check_properties_to_set(self):
        self.property_lst = [prop for prop, flag in self.flag_dic.items() if flag == 1]

    def set_create_git_repository_qry(self):
        self.qry = f"CREATE GIT REPOSITORY {self.attr.name[0]} "

    def add_properties_to_query(self):
        self.qry += f"ORIGIN = '{self.attr.origin}' "
        self.qry += f"API_INTEGRATION = {self.attr.api_integration} "
        if tags.CREDENTIALS in self.property_lst:
            self.qry += f"GIT_CREDENTIALS = {self.attr.credentials} "
        if tags.COMMENT in self.property_lst:
            self.qry += f"COMMENT = '{self.attr.comment}' "
        if tags.TAGS in self.property_lst:
            tags_str = ', '.join([f"{k} = '{v}'" for k, v in self.attr.tags.items()])
            self.qry += f"WITH TAG ({tags_str}) "

    def alter_object(self):
        for prop in self.property_lst:
            self.qry = f"ALTER GIT REPOSITORY {self.attr.name[0]} SET {getattr(self.attr, prop.lower())}"
            self.execute_final_query()
        if tags.NAME in self.property_lst:
            self.qry = f"ALTER GIT REPOSITORY {self.attr.name[0]} RENAME TO {self.attr.name[1]}"
            self.logger.info(f"Renaming git repository {self.attr.name[0]} to {self.attr.name[1]}")
            self.execute_final_query()

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        if self.is_create == "TRUE":
            self.set_create_git_repository_qry()
            self.add_properties_to_query()
        else:
            self.alter_object()

    def create_object(self, *largs, **kwargs):
        self.is_create = kwargs.get(tags.IS_CREATE)
        self.set_name(kwargs.get(tags.NAME))
        self.set_origin(kwargs.get(tags.ORIGIN))
        self.set_api_integration(kwargs.get(tags.API_INTEGRATION))
        self.set_credentials(kwargs.get(tags.CREDENTIALS))
        self.set_comment(kwargs.get(tags.COMMENT))
        self.set_tags(kwargs.get(tags.TAGS))
        self.prepare_query()
        self.execute_final_query()
