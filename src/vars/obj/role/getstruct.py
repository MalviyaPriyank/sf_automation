
from pydantic import BaseModel,Field

class StructRole(BaseModel):
    NAME: str=Field(
        description="User provided value for NAME"
    )
    COMMENT: str=Field(
        description="Comment for the role. If not provided by user, use a comment that best describes the object."
    )