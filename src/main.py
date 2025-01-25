import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__),'./obj'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))


from obj.session import Session 


if __name__ == '__main__':
    session_inst = Session()
    session_inst.set_user('rick')
    session_inst.set_password('mejzyg-pafpov-9noXmi')
    session_inst.set_account('TQNXPFG-BG28519')
    print("SESSION DONE")