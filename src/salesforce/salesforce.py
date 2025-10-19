from simple_salesforce import Salesforce
import pandas as pd

'''
sf = Salesforce(
    username="priyank-qztd@force.com",
    password="LaxmiValentina@0522",
    security_token="dzFwfjitJWW6T12IYo1PsGgfL",
    domain="login"  # 'test' if sandbox
)

# Replace with the actual Account Id of the record
ACCOUNT_NAME = "ProvingGround"

# Query for a single account
query = f"""
SELECT Id, Name, Industry, BillingCity, BillingCountry, Phone
FROM Account
WHERE Name = '{ACCOUNT_NAME}'
"""


metadata=sf.Account.describe()
#print(metadata['fields'])
for f in metadata['fields']:
    print(f['name'], f['type'], f.get('length'), f.get('nillable'))
'''

class SForce:
    def __init__(self):
        self.username="priyank-qztd@force.com"
        self.pwd="LaxmiValentina@0522"
        self.security_token="dzFwfjitJWW6T12IYo1PsGgfL"
        self.domain="login"

    def get_columns_of_object(self,object_type):
        sf=Salesforce(
            username=f"{self.username}",
            password=f"{self.pwd}",
            security_token=f"{self.security_token}",
            domain="login" 
        )
        if object_type.upper()=="ACCOUNT":
            metadata=sf.Account.describe()
            columns_list=[]
            for f in metadata['fields']:
                columns_list.append(f['name'])
            return columns_list

    def get_records_from_salesforce(self,logger,object_type,object_identifier,columns_list):
        sf=Salesforce(
            username=self.username,
            password=self.pwd,
            security_token=self.security_token,
            domain="login" 
        )
        
        if object_type.upper()=="ACCOUNT":
            logger.info("create select query for ACCOUNT object")
            logger.info(f"colummns list {columns_list}")
            logger.info(f"type of colummns list {type(columns_list)}")
            qry = "SELECT "
            for i in range(0,len(columns_list)):
                logger.info(f"total number of columns {len(columns_list)}")
                logger.info(f"for column {columns_list[i]}")
                if i != len(columns_list)-1:
                    qry = qry + columns_list[i] + ","
                    logger.info(f"qry : {qry}")
                else:
                    qry = qry + columns_list[i]
                    logger.info(f"qry : {qry}")
            qry = qry + f" FROM ACCOUNT WHERE NAME = '{object_identifier}'"
            logger.info(f"final qry : {qry}")
        response = sf.query(qry)
        df = pd.DataFrame(response['records']).drop(columns='attributes')
        return df

    def write_pandas_df_to_snowflake(session, df, database, schema, table):
        session.sql(f"USE DATABASE {database}").collect()
        session.sql(f"USE SCHEMA {schema}").collect()
        session.write_pandas(
            df,
            table_name=f"{table}",
            auto_create_table=True,   # creates the table automatically if it doesn't exist
            overwrite=True            # replaces data if table already exists
        )
        return f"Table {table} created successfully in snowflake."