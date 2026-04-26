from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from threading import Lock

from app.config import MONGO_URI

# Global MongoDB client
client = MongoClient(MONGO_URI)