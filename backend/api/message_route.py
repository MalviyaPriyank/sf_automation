import asyncio
from fastapi import APIRouter, BackgroundTasks
from models.message import Message
from db.mongo import MongoService
mongo_service = MongoService()
router = APIRouter()

async def enque_fake_reply(user_id: str):
  await asyncio.sleep(5)
  mongo_service.add_message(Message(userId=user_id, role="assistant", content="This is a delayed reply"))

@router.post("/message")
async def post_message(message: Message, bg: BackgroundTasks):
  saved = mongo_service.add_message(message)
  bg.add_task(enque_fake_reply, message.userId)
  return saved

@router.get("/message")
async def get(user_id: str):
  messages = mongo_service.get_message(user_id)
  return messages