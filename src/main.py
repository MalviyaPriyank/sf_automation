from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import os
import sys

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, repo_root)


os.environ["OPENAI_API_KEY"] = "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"
llm = ChatOpenAI(model="gpt-4o",api_key = os.environ["OPENAI_API_KEY"])


#from obj.table import Table
from schema import DatabaseAttributes

'''
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
'''
def get_system_prompt():
    system_prompt = """
    You are database administrator. You assist user in creating objects.
    You return the output with values given by user or default values for each parameter. 
    If there is a required parameter for which user has not provided any value, ask user for it before returning the final output. 

    Example:
    User : I want to create schema.
    Answer: Can you specify the name for the schema since its a required parameter ?
    
    Do not use any other value.
    """
    return system_prompt
if __name__ == '__main__':
    '''
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
    '''
    import getpass
    import os

    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

    from langchain.chat_models import init_chat_model
    system_prompt = get_system_prompt()
    system_message = SystemMessage(content=system_prompt)
    human_message = HumanMessage(content="I want to create a database")
    prompt = [system_message,human_message]
    llm = init_chat_model("gpt-4o-mini", model_provider="openai")
    structured_llm = llm.with_structured_output(DatabaseAttributes)
    response = structured_llm.invoke(prompt)
    print(response)
