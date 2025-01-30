
class DevelopmentDatabase:
    def __get__(self,instance,owner):
        return instance._development_database
    
    def __set__(self,instance,value):
        instance._development_database = value

    def __delete__(self,instance):
        del instance._development_database

class TestDatabase:
    def __get__(self,instance,owner):
        return instance._test_database
    
    def __set__(self,instance,value):
        instance._test_database = value

    def __delete__(self,instance):
        del instance._test_database

class PreprodDatabase:
    def __get__(self,instance,owner):
        return instance._preprod_database
    
    def __set__(self,instance,value):
        instance._preprod_database = value

    def __delete__(self,instance):
        del instance._preprod_database

class ProdDatabase:
    def __get__(self,instance,owner):
        return instance._prod_database
    
    def __set__(self,instance,value):
        instance._prod_database = value

    def __delete__(self,instance):
        del instance._prod_database

class SetupAttr:
    development_database = DevelopmentDatabase()
    test_database = TestDatabase()
    preprod_database = PreprodDatabase()
    prod_database = ProdDatabase()

class Setup:
    def __init__(self):
        self.attr = SetupAttr()

    def set_development_database(self,value):
        self.attr.development_database = value

    def set_test_database(self,value):
        self.attr.test_database = value

    def set_preprod_database(self,value):
        self.attr.preprod_database = value

    def set_prod_database(self,value):
        self.attr.prod_database = value