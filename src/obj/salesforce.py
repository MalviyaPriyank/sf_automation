from simple_salesforce import Salesforce
import pandas as pd

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

response = sf.query(query)
df = pd.DataFrame(response['records']).drop(columns='attributes')
print(df)


def get_columns_of_object(object_type,sf):
    if object_type.upper()=="ACCOUNT":
        metadata=sf.Account.describe()