class Streamlit:
    _required_privileges_dict={
        "SCHEMA":"USAGE",
        "SCHEMA":"CREATE STREAMLIT",
        "SCHEMA":"CREATE STAGE",
        "DATABASE":"USAGE",
        "WAREHOUSE":"USAGE"
    }
    _schema_tag = "SCHEMA"
    _database_tag = "DATABASE"
    _role_tag="ROLE"
    _warehouse_tag="WAREHOUSE"