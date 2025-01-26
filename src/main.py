import sys
import os 
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__),'./obj'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))


from obj.session import Session 
from processing.stage import Stage


if __name__ == '__main__':
    session_inst = Session()
    session_inst.set_user('rick')
    session_inst.set_password('mejzyg-pafpov-9noXmi')
    session_inst.set_account('TQNXPFG-BG28519')
    session = session_inst.get_session()
    root = session_inst.get_root_object()
    stg = Stage(root,"DB_CONFIG","SCH_CONFIG")
    sch_stg = stg.get_list_of_stages_in_schema()
    stg.set_stage('STG_INT_CONFIG')
    stg.set_stage_reference()
    file_lst = stg.get_list_of_files_from_stage()
    for files in file_lst:
        files = stg.remove_stage_name_from_file_path(files)
        stg.download_file_from_stage(files)
    stg.download_file_from_stage()
    tbl_file = pd.read_csv("./Snowchain_test_table.csv")
    os.remove("./Snowchain_test_table.csv")
    