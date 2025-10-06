import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.baseaccountusage import AccountUsageViews

class QueryInsightsColumnList:
    _view=AccountUsageViews._query_insight_view
    _start_time="START_TIME"
    _end_time="END_TIME"
    _total_elapsed_time="TOTAL_ELAPSED_TIME"
    _query_id="QUERY_ID"
    _query_hash="QUERY_HASH"
    _query_parameterized_hash="QUERY_PARAMETERIZED_HASH"
    _warehouse_id="WAREHOUSE_ID"
    _warehouse_name="WAREHOUSE_NAME"
    _insight_instance_id="INSIGHT_INSTANCE_ID"
    _insight_type_id="INSIGHT_TYPE_ID"
    _message="MESSAGE"
    _suggestions="SUGGESTIONS"
    _is_opportunity="IS_OPPORTUNITY"
    _insight_topic="INSIGHT_TOPIC"


class QueryInsightsView:
    def __init__(self):
        self.attr=QueryInsightsColumnList()

    @classmethod
    def build(cls):
        inst=cls()
        return inst 

    def get_col_and_definitions(self):
        semantic_dic={
            self.attr._start_time : "Start time of the query.",
            self.attr._end_time:"End time of the query.",
            self.attr._total_elapsed_time:"Total elapsed time of the query (in milliseconds).",
            self.attr._query_id:"Internal/system-generated identifier for the SQL statement.",
            self.attr._query_hash:"The hash value computed based on the canonicalized SQL text.",
            self.attr._query_parameterized_hash:"The hash value computed based on the parameterized query.",
            self.attr._warehouse_id:"Internal/system-generated identifier for the warehouse that was used.",
            self.attr._warehouse_name:"Warehouse that the query executed on, if any.",
            self.attr._insight_instance_id:"Internal/system-generated identifier for the insight.",
            self.attr._insight_type_id:"Identifier of the insight type.",
            self.attr._message:"Structured information and details about the insight.",
            self.attr._suggestions:"Array of strings, each containing a recommended action for the insight.",
            self.attr._is_opportunity:"""If true, the insight includes suggestions to improve query performance. For example:
                                    For an insight with the type ID QUERY_INSIGHT_NO_FILTER_ON_TOP_OF_TABLE_SCAN, this column contains true because the insight includes suggestions for improving performance.
                                    For an insight with the type ID QUERY_INSIGHT_FILTER_WITH_CLUSTERING_KEY, this column contains false because the insight does not include suggestions for improving performance.""",
            self.attr._insight_topic:"Label that identifies the type of performance impact detected by this insight. For the list of labels"
        }
        return semantic_dic