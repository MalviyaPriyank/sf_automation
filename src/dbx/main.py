from session import DbxSession as dbx

if __name__=='__main__':
    dbx_inst=dbx()
    session=dbx_inst.connect(connection_type='SERVERLESS')
    print(type(session))