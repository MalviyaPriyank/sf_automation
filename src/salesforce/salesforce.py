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

    def get_records_from_salesforce(self,object_type,object_identifier,columns_list):
        sf=Salesforce(
            username=self.username,
            password=self.pwd,
            security_token=self.security_token,
            domain="login" 
        )
        if object_type.upper()=="ACCOUNT":
            qry = "SELECT "
            for i in range(0,len(columns_list)):
                if i != len(columns_list)-1:
                    qry = qry + columns_list[i] + ","
                else:
                    qry = qry + columns_list[i]
            qry = qry + f" FROM ACCOUNT WHERE NAME = '{object_identifier}'"

        response = sf.query(qry)
        df = pd.DataFrame(response['records']).drop(columns='attributes')
        return df