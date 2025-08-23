from langchain_core.messages import SystemMessage, HumanMessage

class PromptManager:
    def __init__(self):
        self.prompts={}
    
    def add_prompt(self,key,value):
        self.prompts[key] = value

    def get_system_prompt(self,name:str)-> SystemMessage:
        if name not in self.prompts:
            raise ValueError(f"No prompt found for {name}")
        else:
            return SystemMessage(content=self.prompts[name])
        
    def build_prompt(self, name: str, user_input: str):
        return [
            self.get_system_prompt(name),
            HumanMessage(content=user_input)
        ]