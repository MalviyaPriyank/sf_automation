
import json

class ObjectType:
    def __get__(self,instance,owner):
        return instance._object_type
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
        elif value not in ['account','connection','database','databaserole','fileformat','resourcemonitor','role','schema','share','stage','table','user','warehouse']:
            raise TypeError
        else:
            instance._object_type = value

    def __delete__(self,instance):
        del instance._object_type


class ConfFileToRead:
    def __get__(self,instance,owner):
        return instance._conf_file_to_read
    
    def __set__(self,instance,value):
        instance._conf_file_to_read = value

    def __delete__(self,instance):
        del instance._conf_file_to_read

class ReadConfigAttrs:

    object_type = ObjectType()

    conf_file_to_read = ConfFileToRead()


class ReadConfig:
    def __init__(self):
        self.attr = ReadConfigAttrs()

    def set_object_type(self,object_type):
        self.attr.object_type = object_type

    def set_conf_file_to_read(self):
        self.attr.conf_file_to_read = f"{self.attr.object_type}.json"

    def read_conf_file(self):
        with open(self.attr.conf_file_to_read,'r') as conf:
            data = json.load(conf)
        return data

    
    read_cfg = ReadConfig()

    read_cfg.set_object_type(object_type= object_type)
    read_cfg.set_conf_file_to_read()
    config_dict = read_cfg.read_conf_file()
    return config_dict

    


    

    
