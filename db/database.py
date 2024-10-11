import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_URI")  # Load the MongoDB URI from .env

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# Define database and collections
database = client['your_database']
items_collection = database.get_collection('items')
clock_in_collection = database.get_collection('clock_in_records')
