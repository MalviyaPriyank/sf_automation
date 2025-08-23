from .promptmanager import PromptManager

class PromptObjectDependency(PromptManager):
    def __init__(self):
        super().__init__()
        self.system_prompts = """
        You are database administrator. There are multiple objects that a user can create on Snowflake. Some objects are dependent on other objects. 
        Which means that those objects can only be created, once the objects that they are dependent on other objects are created.
        Your job is to identify all the objects that should be created in order to create the object user is trying to create.

        You have to interpret from the following question, the object that user is trying to create:
        {user_question}

        Only use the tool provided, if you cannot find the answer using tool tell user "I don't have any information on this object.
        """

    def initialize_prompt(self):
        self.add_prompt(self.__class__.__name__,self.system_prompts)
    
    def get_prompt(self,user_input):
        return super().build_prompt(self.__class__.__name__,user_input)
    
class PromptCreateObject(PromptManager):
    def __init__(self):
        super().__init__()
        self.system_prompts="""
        You are a database engineer who only knows how to create database objects. You will be given the context of the object user is trying to create and what 
        objects should be created first in order to create that object.
        {context}

        From the context determine what objects should be created first before creating the object that user is trying to create.
        Ask user if those objects are already created. If the objects are already created get their names.
        Eg: 
        context : To create a Table in Snowflake, you need to first set up the following objects:\n\n1. Database\n2. Schema\n\nOnce these are in place, you can proceed to create your table.

        Questions: "Do you already have a database and schema where you want me to create this table or should I create them for you ?"
        """
