
import os 
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../../obj'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.dirname(__file__))
from crewai import Agent
from mytool import CreateDatabase

if __name__=='__main__':
    agent=Agent(role="Database Administrator",
                goal= "create objects",
                backstory="You are an expert with years of experience in database.",
                tools=[CreateDatabase()],
                verbose=True)
    agent.kickoff("Create database with name MY_DB")