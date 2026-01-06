from pydantic import BaseModel

class Conversation(BaseModel):
  userId: str
  title: str