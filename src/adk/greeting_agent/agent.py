
import sys
import os

# Add the src folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from vars import StructRole

from google.adk.agents import Agent

def get_attributes():
    """Get the attributes required"""
    return {"NAME":"NONE"}
root_agent=Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="Data Engineer agent",
    instruction="""You are an expert data engineer. You have to figure out all the configurations that user is trying to setup
    for the object. You can use the tool to get the list of all attributes required to create the object.
    """,
    output_schema=StructRole,
    output_key="struct_role"
)
