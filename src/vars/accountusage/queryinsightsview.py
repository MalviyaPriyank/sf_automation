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


class QueryInsightsView:
    def __init__(self):
        self.attr=QueryInsightsColumnList()