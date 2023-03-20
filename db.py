from motor.motor_asyncio import AsyncIOMotorClient
from config import settings 
client = AsyncIOMotorClient(settings.db_uri)
db = client.hncar
