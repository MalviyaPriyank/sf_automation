

class AccountUsageViews:
    _account_usage_view="SNOWFLAKE.ACCOUNT_USAGE"
    _copy_history_view=f"{_account_usage_view}.COPY_HISTORY"
    _query_history_view=f"{_account_usage_view}.QUERY_HISTORY"
    _query_insight_view=f"{_account_usage_view}.QUERY_INSIGHTS"