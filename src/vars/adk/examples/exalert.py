
instruction="""
Inside an alert action, you can’t reference the previous query’s result with RESULT_SCAN(LAST_QUERY_ID()).
LAST_QUERY_ID() returns the last executed statement, which in an alert context is undefined or may refer to the EXISTS query, not your intended dataset.

Snowflake’s CREATE ALERT syntax does not allow a plain SELECT statement after the IF (...) condition.
After IF, you must provide a THEN clause that performs an action (like CALL or INSERT), not just a SELECT.
"""

eg= """CREATE OR REPLACE ALERT db_config.sch_config.LONG_RUNNING_QUERIES_ALERT
  WAREHOUSE = 'QUERY_MONITOR_WH'
  SCHEDULE = 'USING CRON 0 * * * * America/Los_Angeles'
  IF (
    EXISTS (
      SELECT 1
      FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
      WHERE TOTAL_ELAPSED_TIME > 600000
        AND START_TIME > DATEADD(hour, -1, CURRENT_TIMESTAMP())
    )
  )
  THEN
    CALL SYSTEM$SEND_EMAIL(
      'ALERT.LONG_RUNNING_QUERIES@SNOWFLAKE.COM',
      'Long Running Query Alert',
      'The following queries have been running for more than 10 minutes: ' ||
      (
        SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))::STRING
        FROM (
          SELECT QUERY_ID, USER_NAME, WAREHOUSE_NAME, TOTAL_ELAPSED_TIME/60000 AS MINUTES_ELAPSED
          FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
          WHERE TOTAL_ELAPSED_TIME > 600000
            AND START_TIME > DATEADD(hour, -1, CURRENT_TIMESTAMP())
        )
      )
    );
"""
eg2="""
CREATE OR REPLACE ALERT db_config.sch_config.LONG_RUNNING_QUERIES_ALERT
  WAREHOUSE = 'QUERY_MONITOR_WH'
  SCHEDULE = 'USING CRON 0 * * * * America/Los_Angeles'
  IF (
    EXISTS (
      SELECT 1
      FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
      WHERE TOTAL_ELAPSED_TIME > 600000
        AND START_TIME > DATEADD(hour, -1, CURRENT_TIMESTAMP())
    )
  )
  THEN
    CALL SYSTEM$NOTIFY(
      'LONG_RUNNING_QUERIES_ALERT',
      'Queries running longer than 10 minutes detected',
      'The following queries have been running for more than 10 minutes: ' ||
      (
        SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))::STRING
        FROM (
          SELECT QUERY_ID, USER_NAME, WAREHOUSE_NAME, TOTAL_ELAPSED_TIME/60000 AS MINUTES_ELAPSED
          FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
          WHERE TOTAL_ELAPSED_TIME > 600000
            AND START_TIME > DATEADD(hour, -1, CURRENT_TIMESTAMP())
        )
      )
    );
"""
