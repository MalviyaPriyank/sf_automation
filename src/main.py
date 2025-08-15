from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'./dependency'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../validation'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../exception'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../setup'))
sys.path.append(os.path.join(os.path.dirname(__file__),'../conf'))
os.environ["OPENAI_API_KEY"] = "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"
llm = ChatOpenAI(model="gpt-4o",api_key = os.environ["OPENAI_API_KEY"])

#from obj.session import Session 
from dependency import basedependency
#from obj.table import Table
#from processing.stage import Stage
from setup.initial import InitialSetup

object_dependency_assistant = create_react_agent(
    model="openai:gpt-4o",
    tools=[basedependency.ObjectDependency().get_dependencies],
    prompt="You are snowflake object dependency specialist. You know all the prerquisite objects that should be setup before setting any object.",
    name="object_dependency_assistant"
)

supervisor = create_supervisor(
    agents=[object_dependency_assistant],
    model=ChatOpenAI(model="gpt-4o"),
    prompt=(
        "You manage object dependency assistant and assign work to it."
    )
).compile()

if __name__ == '__main__':
    tools = [basedependency.ObjectDependency().get_dependencies]
    for chunk in supervisor.stream(
    {
        "messages": [
            {
                "role": "user",
                "content": "I want to create Stage object"
            }
        ]
    }
    ):
        for agent_name, data in chunk.items():
            messages = data.get("messages", [])
            for msg in messages:
                content = getattr(msg, "content", None)
                if content:
                    print(f"[{agent_name}] {content}\n")