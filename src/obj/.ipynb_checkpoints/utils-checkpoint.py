
from simple_salesforce import Salesforce
import pandas as pd

def write_pandas_df_to_snowflake(session,df,database,schema,table):
    session.sql(f"USE DATABASE {database}").collect()
    session.sql(f"USE SCHEMA {schema}").collect()
    session.write_pandas(
        df,
        table_name=f"{table}",
        auto_create_table=True,   # creates the table automatically if it doesn't exist
        overwrite=True            # replaces data if table already exists
    )
    return f"Table {table} created successfully in snowflake."