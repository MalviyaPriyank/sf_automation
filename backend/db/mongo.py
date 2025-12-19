from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
from config import settings

from models.user import User
from models.conversation import Conversation
from bson import ObjectId
from schema.user import individual_serial as user_serial
from schema.conversation import individual_serial as convo_serial
from schema.conversation import list_serial

class MongoService():
  def __init__(self):
    self.client = MongoClient(settings.mongo_uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
    self.db = self.client.gyrus_db

  def add_user(self, user: User):
    res = self.db["users"].insert_one(user.model_dump())
    return res.inserted_id
  
  def get_user(self, user_id: str):
    res = user_serial(self.db["users"].find_one({"_id": ObjectId(user_id)}))
    return res
  
  def add_conversation(self, conversation: Conversation):
    # convert userId to ObjectId
    payload = conversation.model_dump()
    payload["userId"] = ObjectId(payload["userId"])
    res = self.db["conversations"].insert_one(payload)
    saved = self.db["conversations"].find_one({"_id": res.inserted_id})
    return convo_serial(saved)

  def get_conversations(self, user_id: str):
    return list_serial(self.db["conversations"].find({"userId" : ObjectId(user_id)}))
  
  def get_conversation(self, id: str):
    conversation = self.db["conversations"].find_one({"_id" : ObjectId(id)})
    return convo_serial(conversation)
  
  def delete_conversation(self, id: str):
    self.db["conversations"].find_one_and_delete({"_id" : ObjectId(id)})
    return { "message" : "conversation deleted"}
  

mongo_service = MongoService()