from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client["ns_master"]

songs = db["songs"]
users = db["users"]
