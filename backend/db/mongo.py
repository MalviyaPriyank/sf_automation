from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
from config import settings

client = MongoClient(settings.mongo_uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
db = client.frosty_db
 
collection_users = db["users"]
collection_conversations = db["conversations"]