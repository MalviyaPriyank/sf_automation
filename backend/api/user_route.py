from fastapi import APIRouter
from models.user import User
from db.mongo import MongoService
mongo_service = MongoService()

router = APIRouter()

@router.post("/user")
async def post_user(user: User): 
  inserted_id = mongo_service.add_user(user)
  return { "id": str(inserted_id), **user.model_dump()}

@router.get("/user")
async def get_user(user_id: str):
  user = mongo_service.get_user(user_id)
  return user