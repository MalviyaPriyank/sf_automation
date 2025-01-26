import sys
import os 
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__),'./obj'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))


from obj.session import Session 
from obj.table import Table
from processing.stage import Stage


if __name__ == '__main__':
    session_inst = Session()
    session_inst.set_user('rick')
    session_inst.set_password('mejzyg-pafpov-9noXmi')
    session_inst.set_account('TQNXPFG-BG28519')
    session = session_inst.get_session()
    root = session_inst.get_root_object()
    tbl = Table(session,root)
    tbl.create_table_using_files_from_stage("DEV_SNOWCHAIN","CUSTOMER")
    print("DONE")
    os.remove("./Snowchain_test_table.csv")
    