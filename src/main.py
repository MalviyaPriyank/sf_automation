import sys
import os 


sys.path.append(os.path.join(os.path.dirname(__file__),'./obj'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../setup'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../conf'))



#from obj.session import Session 
from obj.snowpipe import Snowpipe
#from obj.table import Table
#from processing.stage import Stage
#from setup.initial import InitialSetup

if __name__ == '__main__':
    #session_inst = Session()
    snowpipe_inst = Snowpipe('abc','abc','abc','abc','abc')
    snowpipe_inst.set_name('PIPE_CRM_ACCOUNTS')
    print('DONE')
    input()
    session_inst.set_user('rick')
    session_inst.set_password('mejzyg-pafpov-9noXmi')
    session_inst.set_account('TQNXPFG-BG28519')
    session = session_inst.get_session()
    ####### PATCH FOR CREATE TABLE ################
    '''
    root = session_inst.get_root_object()
    tbl = Table(session,root)
    tbl.create_table_using_files_from_stage("MY_DB","SCH_TEST")
    '''
    ###### PATCH FOR CREATE TABLE ################
    init_setup = InitialSetup(session)  
    init_setup.perform_initial_setup()
    print("DONE")