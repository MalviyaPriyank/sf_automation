import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'../base'))

from base.baseaccountusage import AccountUsageViews

class QueryHistoryColumnList:
    _view=AccountUsageViews._query_history_view


class QueryHistoryView:
    def __init__(self):
        self.attr=QueryHistoryColumnList()