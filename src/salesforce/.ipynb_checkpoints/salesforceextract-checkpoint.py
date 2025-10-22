
from base import SalesforceObject 
class SalesforceExtract:
    def __init__(self,logger,object_type,conn):
        self.sf_object=SalesforceObject(logger=logger,object_type=object_type)
        self.conn=conn

    def get_available_columns_to_pull_from_salesforce(self):
        return self.sf_object.find_available_columns_for_object(conn=self.conn)

    def get_data_from_salesforce(self,columns_list,filter_column,object_identifier):
        self.sf_object.set_available_columns(conn=self.conn)
        self.sf_object.get_records_from_salesforce(conn=self.conn,
                                                   columns_list=columns_list,
                                                   filter_column=filter_column,
                                                   object_identifier=object_identifier)