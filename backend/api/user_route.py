from fastapi import APIRouter
from models.user import User
from db.mongo import MongoService
mongo_service = MongoService()

router = APIRouter()

@router.post("/user")
async def post_user(user: User): 
  saved = mongo_service.add_user(user)
  return saved

@router.get("/user")
async def get_user(user_id: str):
  user = mongo_service.get_user(user_id)
  return user
