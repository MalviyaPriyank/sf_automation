from fastapi import APIRouter
from models.conversation import Conversation
router = APIRouter()

from db.mongo import MongoService
mongo_service = MongoService()

@router.post("/conversation")
async def post_conversation(conversation: Conversation):
  saved = mongo_service.add_conversation(conversation)
  return saved

@router.get("/conversation")
async def get_conversations(user_id: str):
  conversations = mongo_service.get_conversations(user_id)
  return conversations

@router.get("/conversation/{id}")
async def get_conversation(id: str):
  conversation = mongo_service.get_conversation(id)
  return conversation

@router.delete("/conversation/{id}")
async def delete_conversation(id: str):
  return mongo_service.delete_conversation(id)