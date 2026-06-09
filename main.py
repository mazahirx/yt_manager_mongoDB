from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

db_url = os.getenv("DATABASE_URL")

client = MongoClient(db_url)
db = client["youtube_manager"]
video_collections = db["videos"]
