from simple_salesforce import Salesforce
class SalesforceConnection:
    def __init__(self,user_name,password,security_token):
        self.user_name=user_name
        self.password=password
        self.security_token=security_token

        '''
        self.username="priyank-qztd@force.com"
        self.pwd="LaxmiValentina@0522"
        self.security_token="dzFwfjitJWW6T12IYo1PsGgfL"
        self.domain="login"
        '''

    def get_connection(self):
        sf=Salesforce(
            username=f"{self.user_name}",
            password=f"{self.password}",
            security_token=f"{self.security_token}",
            domain="login" 
        )
        return sf