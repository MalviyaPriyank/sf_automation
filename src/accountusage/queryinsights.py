import sys 
import os

sys.path.append(os.path.join(os.path.dirname(__file__),'../vars'))

from vars.accountusage.queryinsightsview import QueryInsightsView


class QueryInsights:
    def __init__(self,session):
        self.attr=QueryInsightsView().attr
        self.session=session

    def get_insights_of_all_queries_in_past_x_days(self,x):
        qry=f""" SELECT {self.attr._query_id}, {self.attr._insight_type_id}, {self.attr._message}, {self.attr._message}
                FROM {self.attr._view} 
                WHERE 
                {self.attr._start_time} > TO_DATE(DATEADD(DAY, -{x}, CURRENT_DATE()));"""
        return qry
    
    def get_insights_of_all_queries_running_for_more_than_y_milliseconds_in_past_x_days_(self,x,y):
        qry=f"""
        SELECT {self.attr._query_id}, {self.attr._insight_type_id}, {self.attr._message}, {self.attr._message}
        FROM {self.attr._view}
        WHERE 
        {self.attr._start_time} > TO_DATE(DATEADD(DAY, -{x}, CURRENT_DATE()))
        AND {self.attr._total_elapsed_time} > {y};
        """
        return qry
    
    def get_col_definitions(self):
        return QueryInsightsView().get_col_and_definitions()