from pymongo import MongoClient
from app.config import MONGO_URI

# Global MongoDB client
client = MongoClient(MONGO_URI)
db = client["calendar_db"]
tasks_collection = db["tasks"]