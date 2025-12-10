from fastapi import APIRouter, HTTPException
from models.user import User
from db.mongo import collection_users
from schema.user import individual_serial
from bson import ObjectId

router = APIRouter()

@router.post("/user")
async def post_user(user: User):
  res = collection_users.insert_one(user.model_dump())
  return {"id": str(res.inserted_id), **user.model_dump()}

@router.get("/user")
async def get_user(user_id: str):
  user = individual_serial(collection_users.find_one({"_id": ObjectId(user_id)}))
  if not user:
    raise HTTPException(status_code=404, detail="No user found")
  return user