from snowflake.snowpark.functions import col

class Databases:
    def __init__(self,session):
        self.view = "INFORMATION_SCHEMA.DATABASES"
        self.session = session

    def db_exist(self,db_name):
        df = self.session.table(self.view).filter(col("database_name") == '{db_name}')
        res = df.collect()
        if len(res) == 0:
            return False
        elif len(res) > 0:
            return True
        
    def get_owner_of_db(self,db_name):
        df = self.session.table(self.view).filter(col("database_name") == f'{db_name}').select(col("database_owner"))
        res = df.collect()
        return res[0][0]
    
    def get_type_of_db(self,db_name):
        df = self.session.table(self.view).filter(col("database_name") == f'{db_name}').select(col("type"))
        res = df.collect()
        return res[0][0]
    
    def get_retention_time_of_db(self,db_name):
        df = self.session.table(self.view).filter(col("database_name") == f'{db_name}').select(col("retention_time"))
        res = df.collect()
        return res[0][0]
    
    def get_information_on_db(self,db_name,col_name):
        df = self.session.table(self.view).filter(col("database_name") == f'{db_name}').select(col(f'{col_name}'))
        res = df.collect()
        return res[0][0]