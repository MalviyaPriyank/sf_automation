
from accountglobalvars import *
from snowpipe import Snowpipe

class ExternalStage:
    def __get__(self,instance,owner):
        return instance._external_stage
    
    def __set__(self,instance,value):
        if value == None :
            raise KeyError
        else:
            instance._external_stage = value

    def __delete__(self,instance):
        del instance._external_stage

class LoadType:
    def __get__(self,instance,owner):
        return instance._load_type
    
    def __set__(self,instance,value):
        if value == None:
            raise KeyError
        else:
            instance._load_type = value

    def __delete__(self,instance):
        del instance._load_type

class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        if value == None:
            raise KeyError
        else:
            instance._database = value

    def __delete__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        if value not in ADMT._allowed_schema_values: # ['PERSON','SERVICE','LEGACY_SERVICE','NULL']
            raise ValueError
        else:
            instance._schema = value

    def __delete__(self,instance):
        del instance._schema

class Table:
    def __get__(self,instance,owner):
        return instance._table
    
    def __set__(self,instance,value):
        instance._table = value

    def __delete__(self,instance):
        del instance._table


class Misc:
    def __get__(self,instance,owner):
        return instance._misc
    
    def __set__(self,instance,value):
        instance._misc = value
    
    def __delete__(self,instance):
        del instance._misc


class IngestAttrs:
    external_stage = ExternalStage()
    load_type = LoadType()
    database = Database()
    schema = Schema()
    table = Table()
    misc = Misc()

class Ingest:
    def __init__(self,session):
        self.attr = IngestAttrs()
        self.session = session

    def set_external_stage(self,external_stage):
        self.attr.external_stage = external_stage

    def set_load_type(self,load_type):
        self.attr.load_type = load_type 

    def set_database(self,database):
        self.attr.database = database

    def set_schema(self,schema):
        self.attr.schema = schema

    def set_table(self,table):
        self.attr.table = table

    def set_misc(self,misc):
        self.attr.misc = misc


def main(session,**kwargs):
    ingest = Ingest()

    ingest.set_external_stage(kwargs['external_stage'])

    ingest.set_load_type(kwargs['load_type'])

    ingest.set_database(kwargs['database'])

    ingest.set_schema(kwargs['schema'])

    ingest.set_table(kwargs['table'])

    ingest.set_misc(kwargs['misc'])
    
    if ingest.attr.load_type == 'SNOWPIPE':
        sp = Snowpipe()
        sp.set_auto_ingest(ingest.attr.misc['auto_ingest'])
        sp.set_aws_sns_topic(ingest.attr.misc['aws_sns_topic'])
        sp.set_error_integration(ingest.attr.misc['error_integration'])
        sp.set_integration(ingest.attr.misc['integration'])
        sp.set_comment(ingest.attr.misc['comment'])
        sp.get_create_snowpipe_qry(ingest)