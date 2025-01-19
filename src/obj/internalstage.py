import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))


from global_vars import InternalStage as gv
from validatevalue import ValidateValue as vv

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        if value == "NONE" :
            raise KeyError
        elif not vv.starts_with_alphabet(value):
            raise ValueError
        elif not vv.is_enclosed_in_double_quotes(value):
            if vv.has_space(value):
                raise ValueError
            if vv.has_special_characters(value):
                raise ValueError
            else:
                instance._name = value

    def __del__(self,instance):
        del instance._name

class NameTag:
    def __get__(self,instance,owner):
        return instance._name_tag
    
    def __set__(self,instance,value):
        instance._name_tag = value

    def __del__(self,instance):
        del instance._name_tag



class FileFormat:   
    def __get__(self,instance,owner):
        return instance._file_format
    
    def __set__(self,instance,value):
        instance._file_format = value

    def __del__(self,instance):
        del instance._file_format


class FileFormatTag:   
    def __get__(self,instance,owner):
        return instance._file_format_tag
    
    def __set__(self,instance,value):
        instance._file_format_tag = value

    def __del__(self,instance):
        del instance._file_format_tag

class Comment:
    def __get__(self,instance,owner):
        return instance._comment
    
    def __set__(self,instance,value):
        instance._comment = value


    def __del__(self,instance):
        del instance._comment

class CommentTag:
    def __get__(self,instance,owner):
        return instance._comment_tag
    
    def __set__(self,instance,value):
        instance._comment_tag = value

    def __del__(self,instance):
        del instance._comment_tag

class Tag:
    def __get__(self,instance,owner):
        return instance._tag
    
    def __set__(self,instance,value):
        instance._tag = value


    def __del__(self,instance):
        del instance._tag

class TagTag:
    def __get__(self,instance,owner):
        return instance._tag_tag
    
    def __set__(self,instance,value):
        instance._tag_tag = value

    def __del__(self,instance):
        del instance._tag_tag

class Encryption:
    def __get__(self,instance,owner):
        return instance._encryption
    
    def __set__(self,instance,value):
        if value not in gv._allowed_values_encryption:
            raise ValueError
        else:
            instance._encryption = value

    def __del__(self,instance):
        del instance._encryption

class EncryptionTag:
    def __get__(self,instance,owner):
        return instance._encryption_tag
    
    def __set__(self,instance,value):
        instance._encryption_tag = value

    def __del__(self,instance):
        del instance._encryption_tag

class Directory:
    def __get__(self,instance,owner):
        return instance._directory
    
    def __set__(self,instance,value):
        if vv.is_bool(value):
            instance._directory = value
        else:
            raise ValueError

    def __del__(self,instance):
        del instance._directory

class DirectoryTag:
    def __get__(self,instance,owner):
        return instance._directory_tag
    
    def __set__(self,instance,value):
        instance._directory_tag = value


    def __del__(self,instance):
        del instance._directory_tag

class RefreshOnCreate:
    def __get__(self,instance,owner):
        return instance._refresh_on_create
    
    def __set__(self,instance,value):
        if vv.is_bool(value):
            instance._refresh_on_create = value
        else:
            raise ValueError


    def __del__(self,instance):
        del instance._refresh_on_create

class RefreshOnCreateTag:
    def __get__(self,instance,owner):
        return instance._refresh_on_create_tag
    
    def __set__(self,instance,value):
        instance._refresh_on_create_tag = value


    def __del__(self,instance):
        del instance._refresh_on_create_tag




class InternalStageAttrs:
    name = Name()
    name_tag = NameTag()

    file_format = FileFormat()
    file_format_tag = FileFormatTag()

    comment = Comment()
    comment_tag = CommentTag()
    
    tag = Tag()
    tag_tag = TagTag()
    
    encryption = Encryption()
    encryption_tag = EncryptionTag()

    directory = Directory()
    directory_tag = DirectoryTag()

    refresh_on_create = RefreshOnCreate()
    refresh_on_create_tag = RefreshOnCreateTag()
    


class InternalStage:
    def __init__(self,session):
        self.attr = InternalStageAttrs()
        self.session = session
        self.qry = ""

    def set_name(self,val):
        self.attr.name = val
    
    def set_name_tag(self,val):
        self.attr.name_tag = val

    def set_file_format(self,val):
        self.attr.file_format = val
    
    def set_file_format_tag(self,val):
        self.attr.file_format_tag = val
    
    def set_comment(self,val):
        self.attr.comment = val
    
    def set_comment_tag(self,val):
        self.attr.comment_tag = val

    def set_tag(self,val):
        self.attr.tag = val
    
    def set_tag_tag(self,val):
        self.attr.tag_tag = val

    def set_encryption(self,val):
        self.attr.encryption = val
    
    def set_encryption_tag(self,val):
        self.attr.encryption_tag = val

    def set_directory(self,val):
        self.attr.directory = val
    
    def set_directory_tag(self,val):
        self.attr.directory_tag = val

    def set_refresh_on_create(self,val):
        self.attr.refresh_on_create = val
    
    def set_refresh_on_create_tag(self,val):
        self.attr.refresh_on_create_tag = val

    def set_object_properties_flag(self):
        self.flag_dic = {}

        def set_flag(attribute_tag,attribute_name):
            self.flag_dic[attribute_tag] = 1 if getattr(self.attr, attribute_name) != "NONE" else 0

        set_flag(gv._name_tag,"_name")
        set_flag(gv._file_format_tag,"_file_format")
        set_flag(gv._comment_tag,"_comment")
        set_flag(gv._tag_tag,"_tag")
        set_flag(gv._encryption_tag,"_encryption")
        set_flag(gv._directory_tag,"_directory")
        set_flag(gv._refresh_on_create_tag,"_refresh_on_create")

    def check_properties_to_set(self): 
        self.property_lst = []
        for prop in self.flag_dic.keys():
            if self.flag_dic[prop] == 1:
                self.property_lst.append(prop)

    def set_create_qry(self):
        self.qry = f"CREATE STAGE  {self.attr.name} "

    def add_properties_to_query(self):
        if len(self.property_lst) != 0 :
            for prop in self.property_lst:
                if prop == gv._file_format_tag:
                    self.qry = f" {self.qry} {self.attr.file_format_tag} = {self.attr.file_format} "
                if prop == gv._comment_tag:
                    self.qry = f" {self.qry} {self.attr.comment_tag} = {self.attr.comment} "
                if prop == gv._tag_tag:
                    self.qry = f" {self.qry} {self.attr.tag_tag} = {self.attr.tag} "
                if prop == gv._encryption_tag:
                    self.qry = f" {self.qry} {self.attr.encryption_tag} = {self.attr.encryption} "
                if prop == gv._directory_tag:
                    self.qry = f" {self.qry} {self.attr.directory_tag} = {self.attr.directory} "
                if prop == gv._refresh_on_create_tag:
                    self.qry = f" {self.qry} {self.attr.refresh_on_create_tag} = {self.attr.refresh_on_create} "

    def prepare_query(self):
        self.set_object_properties_flag()
        self.check_properties_to_set()
        self.set_create_qry()
        self.add_properties_to_query()

    def create_internal_stage(self):
        self.session.sql(self.qry)

    def create_object(session,**kwargs):
        internal_stage = InternalStage(session)

        internal_stage.set_name(kwargs[gv._name_tag])
        internal_stage.set_name_tag(gv._name_tag)

        internal_stage.set_file_format(kwargs[gv._file_format_tag])
        internal_stage.set_file_format_tag(gv._file_format_tag)

        internal_stage.set_comment(kwargs[gv._comment_tag])
        internal_stage.set_comment_tag(gv._comment_tag)

        internal_stage.set_tag(kwargs[gv._tag_tag])
        internal_stage.set_tag_tag(gv._tag_tag)

        internal_stage.set_encryption(kwargs[gv._encryption_tag])
        internal_stage.set_encryption_tag(gv._encryption_tag)

        internal_stage.set_directory(kwargs[gv._directory_tag])
        internal_stage.set_directory_tag(gv._directory_tag)

        internal_stage.set_refresh_on_create(kwargs[gv._refresh_on_create_tag])
        internal_stage.set_refresh_on_create_tag(gv._refresh_on_create_tag)

        internal_stage.prepare_query()
        internal_stage.create_internal_stage()


        



