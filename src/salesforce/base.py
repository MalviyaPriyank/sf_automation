
from simple_salesforce import Salesforce
import pandas as pd
import logging

from validation.validatesalesforce import ValidateSalesforce as vsf

class ObjectType:
    def __get__(self,instance,owner):
        return instance._object_type
    
    def __set__(self,instance,value):
        instance._object_type = value
    
    def __delete__(self,instance):
        del instance._object_type

class ObjectName:
    def __get__(self,instance,owner):
        return instance._object_name
    
    def __set__(self,instance,value):
        instance._object_name=value
    
    def __delete__(self,instance):
        del instance._object_name

class AvailableColumns:
    def __get__(self,instance,owner):
        return instance._available_columns
    
    def __set__(self,instance,value):
        instance._available_columns = value
    
    def __delete__(self,instance):
        del instance._available_columns

class BaseSalesforceAttrs:
    object_type=ObjectType()
    object_name=ObjectName()
    available_columns=AvailableColumns()


class BaseSalesforce:
    def __init__(self):
        self.attr=BaseSalesforceAttrs()

    def set_object_type(self,val):
        self.attr.object_type=val
    
    def set_object_name(self):
        if self.attr.object_type=='ACCOUNT':
            self.attr.object_name=self.attr.object_type

    def set_available_columns(self,val):
        self.attr.available_columns=val

    def find_available_columns_for_object(self,conn):
        if self.attr.object_name=="ACCOUNT":
            metadata=conn.Account.describe()
            columns_list=[]
            for f in metadata['fields']:
                columns_list.append(f['name'])
        self.attr.available_columns=columns_list
        return columns_list


class SalesforceObject(BaseSalesforce):
    def __init__(self,logger,object_type):
        self.logger=logger
        self.set_object_type(object_type.upper())
        self.set_object_name()   
    
    @classmethod
    def generate_inner_select(cls,columns_list):
        cls.logger.info(" inside static method to generate inner select query")
        inner_select=""
        for i in range(0,len(columns_list)):
            if i != len(columns_list)-1:
                inner_select = inner_select + columns_list[i] + ","
                cls.logger.info(f"qry : {inner_select}")
            else:
                inner_select = inner_select + columns_list[i]
                cls.logger.info(f"qry : {inner_select}")
        
        return inner_select
    
    def get_records_from_salesforce(self,conn,columns_list,filter_column,object_identifier):
        col_lst=self.find_available_columns_for_object(conn=conn)
        vsf.is_valid_selection_for_columns_to_fetch(columns_list_available=self.attr.available_columns,
                                                    columns_to_pull=columns_list)
        self.logger.info(f"total columns to be fetched {len(columns_list)}")
        self.logger.info(f" fetching following: {columns_list}")
        qry = "SELECT "
        self.logger.info(f"generating inner select")
        inner_select=self.generate_inner_select()
        qry=qry+inner_select
        self.logger.info(f" select query : {qry}")
        qry=qry + f" FROM {self.attr.object_name} WHERE {filter_column} = {object_identifier}"
        self.logger.info(f" final query : {qry}")
        response=conn.query(qry)
        df=pd.DataFrame(response['records']).drop(columns='attributes')
        return df



    