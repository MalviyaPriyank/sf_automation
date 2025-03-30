def execute_qry(session,qry):
    df = session.sql(qry).collect()
    return df