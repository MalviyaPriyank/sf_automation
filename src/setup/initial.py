import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'../obj/global'))


from role import Role
 
def create_role_for_privileges(session,role_name,comment):
    role = Role()
    qry = role.get_create_qry({"NAME":role_name,"COMMENT":comment})
    session.sql(qry)


def main(session):
    create_role_for_privileges(session,"RL_PRIV_OWNER","Role to have ownerhip")
    create_role_for_privileges(session,"RL_PRIV_ALL","Role to have all privileges except ownership")
    
    