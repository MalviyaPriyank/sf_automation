# class message struct 
from pydantic import BaseModel

class Message(BaseModel):
  userId: str
  role: str
  content: str