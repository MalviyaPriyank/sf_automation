from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
from config import settings

from models.user import User
from bson import ObjectId
from schema.user import individual_serial


# client = MongoClient(settings.mongo_uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
# db = client.frosty_db

# collection_users = db["users"]
# collection_conversations = db["conversations"]

# create a class
# add methods 1 to add users 2nd add conversation for user
# chat.py logt should be in this classes message
# call insertuser through class instance

# mongo client should be in the constructor of the class

class MongoService():
  def __init__(self):
    self.client = MongoClient(settings.mongo_uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
    self.db = self.client.frosty_db
    self.collection_users = self.db["users"]
    self.collection_conversations = self.db["conversations"]

  def add_user(self, user: User):
    res = self.collection_users.insert_one(user.model_dump())
    return res.inserted_id
  
  def get_user(self, user_id: str):
    res = individual_serial(self.collection_users.find_one({"_id": ObjectId(user_id)}))
    return res
  

mongo_service = MongoService()