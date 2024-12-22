from conf.readconf import ReadConfig as rcfg
import subprocess

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

class SrcToExecute:
    def __get__(self,instance,owner):
        return instance._src_to_execute
    
    def __set__(self,instance,value):
        instance._src_to_execute = value

    def __delete__(self,instance):
        del instance._src_to_execute

class SFSetupAttrs:

    object_type = ObjectType()

    src_to_execute = SrcToExecute()


class SFSetup:
    def __init__(self):
        self.attr = SFSetupAttrs()

    def set_object_type(self,object_type):
        self.attr.object_type = object_type

    def set_src_to_execute(self):
        self.attr.src_to_execute = f"{self.attr.object_type}.py"

def main(object_type):
    sf_setup = SFSetup()

    sf_setup.set_object_type(object_type)
    sf_setup.set_src_to_execute()

    read_cfg = rcfg()
    read_cfg.set_object_type()
    read_cfg.set_conf_file_to_read()
    config_dict = read_cfg.read_conf_file()


    subprocess.run(["python", sf_setup.attr.src_to_execute])

