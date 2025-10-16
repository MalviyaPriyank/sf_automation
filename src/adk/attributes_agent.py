from config import Config as cfg
from google.adk.agents import Agent
import asyncio
from google.adk.tools import FunctionTool

# Define a Tool that takes an object type as input
def get_attributes(object_type: str):
    # Here you can fetch attributes from metadata or a dictionary
    print(f"Fetching attributes for object type: {object_type}")
    return f"Attributes for {object_type}: [...]"  # placeholder

# Wrap the function as a Tool so the agent can call it dynamically
attributes_tool = FunctionTool(get_attributes)

# Create the agent
attributes_agent = Agent(
    name="attributes_agent",
    model=cfg.MODEL_GPT_4O,
    description="Provides attributes required to configure an object on the data warehouse.",
    instruction=(
        "You are an expert database engineer. "
        "When a user asks about an object, figure out which object they mean "
        "and use the get_attributes tool to retrieve its configurations."
    ),
    tools=[attributes_tool]
)

# Define an async function to execute the agent
async def execute_agent():
    user_input = "What attributes are needed for a TABLE?"
    
    # Use 'await' with the agent's asynchronous execution method (try 'run' first)
    try:
        # Most likely correct method
        response = await attributes_agent.run(user_input) 
    except AttributeError:
        # If 'run' isn't defined, try 'invoke'
        response = await attributes_agent.invoke(user_input)
    
    # Access the text attribute of the response object
    print(response.text)

# Run the async function
if __name__ == "__main__":
    asyncio.run(execute_agent())
