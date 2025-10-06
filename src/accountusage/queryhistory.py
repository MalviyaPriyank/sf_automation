import sys 
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from vars.accountusage.queryhistoryview import QueryHistoryView


class QueryHistory:
    def __init__(self,session):
        self.attr=QueryHistoryView().attr
        self.session=session


    def get_queries_running_longer_than_x_milliseconds(self,x,**kwargs):
        if kwargs[f"{self.attr._database_name}"]!="NONE":
            qry=f""" SELECT 
            FROM {self.attr._view} 
            WHERE 
            {self.attr._database_name} = {kwargs[f"{self.attr._database_name}"]}
            AND
            {self.attr._total_elapsed_time} > {x};"""
            return qry

        qry=f""" SELECT 
        FROM {self.attr._view} 
        WHERE 
        {self.attr._total_elapsed_time} > {x};"""
        return qry

    
