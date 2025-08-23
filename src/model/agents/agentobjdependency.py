from langgraph.prebuilt import create_react_agent
from model.prompts.promptobjectdependency import PromptObjectDependency
from model.tool import get_dependencies

class AgentObjectDependency:
    def __init__(self,model):
        self.prompt_inst = PromptObjectDependency()
        self.model = model

    def get_react_agent(self):
        return create_react_agent(
            model=self.model,
            tools=[get_dependencies],
            prompt=(
                self.prompt_inst.system_prompts
            ),
            name=self.__class__.__name__,
        )