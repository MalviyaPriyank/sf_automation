
from sqlserverconnection import SqlServerOperations 
def database_exist(operations : SqlServerOperations,db_name):
    qry=f"""
    SELECT 
    database_id
    FROM
    sys.databases
    WHERE
    name = ?
    """
    res=operations.execute_query_and_get_result_count(qry=qry,**{'DATABASE':db_name})
    if res:
        return True
    else:
        return False
