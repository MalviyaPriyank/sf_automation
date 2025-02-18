def undrop_database(session,db_name):
    session.sql(f"UNDROP DATABASE {db_name}").collect()