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
from setup.initial import InitialSetup

if __name__ == '__main__':
    ###### PATCH FOR CREATE TABLE ################
    init_setup = InitialSetup(session)  
    init_setup.perform_initial_setup()
    print("DONE")