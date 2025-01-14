class LoadType:
    def __get__(self,instance,owner):
        return instance._load_type
    
    def __set__(self,instance,value):
        instance._load_type = value
    
    def __delete__(self,instance):
        del instance._load_type

class LoadSequence:
    def __get__(self,instance,owner):
        return instance._load_sequence
    
    def __set__(self,instance,value):
        instance._load_sequence = value
    
    def __delete__(self,instance):
        del instance._load_sequence

class LoadAttr:
    load_type = LoadType()
    load_sequence = LoadSequence()

class Load:
    def __init__(self):
        self.table_name = "LOAD_CONTROL"
        self.attr = LoadAttr()

    def set_load_type(self,value):
        self.attr.load_type = value

    def set_load_sequence(self,value):
        self.attr.load_sequence = value


    def insert_record_into_load_control(self):
