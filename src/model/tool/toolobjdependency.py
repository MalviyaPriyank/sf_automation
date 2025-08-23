import os
import sys

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, repo_root)
from dependency import ObjectDependency
from obj import *
from langchain.tools import tool

obj_dep = ObjectDependency()

@tool
def get_dependencies(object_type: str):
    """Find all the objects that should be set up before creating the given Snowflake object."""
    return obj_dep.get_dependencies(object_type)

@tool
def create_object(object_name:str):
    """Create objects."""
    if object_name.upper() == 'DATABASE':
        return Database.create_object()
    elif object_name.upper() == 'SCHEMA':
        return Schema.create_object()
    elif object_name.upper() == 'INTERNALSTAGE':
        return InternalStage.create_object()  

