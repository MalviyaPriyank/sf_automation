
import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))


from validation.validatevalue import ValidateValue as vv
from validation.validateobject import ValidateObject as vo


class Database:
    def __get__(self,instance,owner):
        return instance._database
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.database_exist(session=instance.parent.session, database_name=value)
        instance._database = value

    def __delete__(self,instance):
        del instance._database

class Schema:
    def __get__(self,instance,owner):
        return instance._schema
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        vo.database_exist(session=instance.parent.session, database_name=value)
        instance._schema = value

    def __delete__(self,instance):
        del instance._schema

class Name:
    def __get__(self,instance,owner):
        return instance._name
    
    def __set__(self,instance,value):
        vv.required_attribute_check(value,instance.parent.__class__.__name__,self.__class__.__name__)
        if ( vv.starts_with_alphabet(value,instance.parent.__class__.__name__,self.__class__.__name__) 
              and not vv.has_space(value,instance.parent.__class__.__name__,self.__class__.__name__)
              and not vv.has_special_characters_except_underscore(value,instance.parent.__class__.__name__,self.__class__.__name__)
            ):
            instance._name = value

    def __delete__(self,instance):
        del instance._name

class SourceTable:
    def __get__(self,instance,owner):
        return instance._source_table
    
    def __set__(self,instance,value):
        vo.table_exist(session=instance.parent.session, database_name=instance._database, schema_name=instance._schema, table_name=value)
        instance._source_table = value

    def __delete__(self,instance):
        del instance._source_table

class ReferencedTable:
    def __get__(self,instance,owner):
        return instance._referenced_table
    
    def __set__(self,instance,value):
        vo.table_exist(session=instance.parent.session, database_name=instance._database, schema_name=instance._schema, table_name=value)
        instance._referenced_table = value

    def __delete__(self,instance):
        del instance._referenced_table

class SourceColumn:
    def __get__(self,instance,owner):
        return instance._source_column
    
    def __set__(self,instance,value):
        vo.column_exist(session=instance.parent.session,database=instance._database,schema=instance._schema,table=instance._source_table,column=value)
        instance._source_column = value

    def __delete__(self,instance):
        del instance._source_column

class ReferencedColumn:
    def __get__(self,instance,owner):
        return instance._referenced_column
    
    def __set__(self,instance,value):
        vo.column_exist(session=instance.parent.session,database=instance._database,schema=instance._schema,table=instance._referenced_table,column=value)
        instance._referenced_column = value

    def __delete__(self,instance):
        del instance._referenced_column

class DataMetricFunctionAttrs:
    def __init__(self,parent):
        self.parent=parent
    
    database=Database()
    schema=Schema()
    name=Name()
    source_table=SourceTable()
    referenced_table=ReferencedTable()
    source_column=SourceColumn()
    referenced_column=ReferencedColumn()

class DataMetricFunction:
    def __init__(self,session,user_id):
        self.session=session
        self.user_id=user_id
        self.attr=DataMetricFunctionAttrs(self)

    def set_database(self,value):
        self.attr.database=value

    def set_schema(self,value):
        self.attr.schema=value

    def set_name(self,value):
        self.attr.name=value

    def set_source_table(self,value):
        self.attr.source_table=value
    
    def set_referenced_table(self,value):
        self.attr.referenced_table=value

    def set_source_column(self,value):
        self.attr.source_column=value
    
    def set_referenced_column(self,value):
        self.attr.referenced_column=value


    def create_dmf_for_referential_integrity(self,src_col_data_type,ref_col_data_type):
        dmf_sql=f"""
        CREATE OR REPLACE DATA METRIC FUNCTION {self.attr.database}.{self.attr.schema}.{self.attr.name}(
        arg_t1 TABLE (arg_c1 {src_col_data_type}), arg_t2 TABLE (arg_c2 {ref_col_data_type}))
        RETURNS NUMBER AS 
        'SELECT COUNT(*) FROM arg_t1 WHERE arg_c1 not in (SELECT arg_c2 from arg_t2)' ;
        """
        self.session.sql(dmf_sql).collect()

    def add_table_to_dmf(self,src_tbl,src_col,ref_tbl,ref_col):
        self.set_source_table(src_tbl)
        self.set_referenced_table(ref_tbl)
        self.set_source_column(src_col)
        self.set_referenced_column(ref_col)

        add_sql = f"""
        ALTER TABLE {self.attr.database}.{self.attr.schema}.{self.attr.source_table}
        ADD DATA METRIC FUNCTION {self.attr.database}.{self.attr.schema}.{self.attr.name}
        ON ({self.attr.source_column}, TABLE({self.attr.database}.{self.attr.schema}.{self.attr.referenced_table}({self.attr.referenced_column})));
        """
        self.session.sql(add_sql).collect()

