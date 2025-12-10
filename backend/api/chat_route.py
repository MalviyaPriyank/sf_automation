from fastapi import APIRouter, HTTPException
from schema.conversation import individual_serial, list_serial
from models.conversation import Conversation
from db.mongo import collection_conversations
from bson import ObjectId

router = APIRouter()


@router.post("/conversation")
async def post_conversation(conversation: Conversation):
    payload = conversation.model_dump()
    payload["userId"] = ObjectId(payload["userId"])
    res = collection_conversations.insert_one(payload)
    saved = collection_conversations.find_one({"_id": res.inserted_id})
    if not saved:
        raise HTTPException(status_code=500, detail="Failed to save conversation")
    return individual_serial(saved)


@router.get("/conversation")
async def get_conversations(user_id: str):
    return list_serial(collection_conversations.find({"userId": ObjectId(user_id)}))


@router.get("/conversation/{id}")
async def get_conversation(id: str):
    conversation = collection_conversations.find_one({"_id": ObjectId(id)})
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return individual_serial(conversation)

@router.delete("/conversation/{id}")
async def delete_conversation(id: str):
    collection_conversations.find_one_and_delete({"_id": ObjectId(id)})
    return { "message" : "conversation deleted" }
