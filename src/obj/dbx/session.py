from databricks.connect import DatabricksSession
import os

class Host:
    def __get__(self, instance, owner):
        return instance._host

    def __set__(self, instance, value):
        instance._host = value

    def __delete__(self, instance):
        del instance._host

class Token:
    def __get__(self, instance, owner):
        return instance._token

    def __set__(self, instance, value):
        instance._token = value

    def __delete__(self, instance):
        del instance._token

class Http:
    def __get__(self, instance, owner):
        return instance._http

    def __set__(self, instance, value):
        instance._http = value

    def __delete__(self, instance):
        del instance._http

class Cluster:
    def __get__(self, instance, owner):
        return instance._cluster

    def __set__(self, instance, value):
        instance._cluster = value

    def __delete__(self, instance):
        del instance._cluster

class SessionAttr:
    def __init__(self, parent):
        self.parent = parent

    host = Host()
    token = Token()
    http_path = Http()
    cluster_id = Cluster()

class Session:
    def __init__(self):
        self.attr = SessionAttr(self)

    def set_host(self, value):
        self.attr.host = value

    def set_token(self, value):
        self.attr.token = value

    def set_http(self, value):
        self.attr.http_path = value

    def set_cluster(self, value):
        self.attr.cluster_id = value

    def get_session(self):
        self.set_host(self.attr.host)
        self.set_token(self.attr.token)
        self.set_http(self.attr.http_path)
        self.set_cluster(self.attr.cluster)

        #Bottom code would be translated here
        
        self.set_session(session)
        return self.attr.session
    
#Code that called db session, variables were inputed based on my db account
os.environ["DATABRICKS_HOST"] = f"https://{host}"
os.environ["DATABRICKS_TOKEN"] = token

if cluster_id!=None:
    os.environ["DATABRICKS_CLUSTER_ID"] = cluster_id
    session = DatabricksSession.builder.getOrCreate()
else:
    os.environ["DATABRICKS_HTTP_PATH"] = http_path
    session = DatabricksSession.builder.serverless(True).getOrCreate()
