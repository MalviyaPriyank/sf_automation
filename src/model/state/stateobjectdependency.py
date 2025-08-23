from typing import TypedDict,Dict
from .basestate import GraphState


class AgentDependencyOutputState(TypedDict):
    dependency_dict: Dict[int, str]
    