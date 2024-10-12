import os
import urllib.parse

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

USERNAME_DB = os.getenv('USERNAME_DB')
USERPASSWORD = os.getenv('USERPASSWORD')
HOST = os.getenv('HOST')
DATABASE= os.getenv('DATABASE')
COLLECTION1=os.getenv('COLLECTION1')
COLLECTION2=os.getenv('COLLECTION2')

# URL encode the username and password
USERNAME = urllib.parse.quote_plus(USERNAME_DB)
USERPASSWORD = urllib.parse.quote_plus(USERPASSWORD)
# breakpoint()
uri = f"mongodb+srv://{USERNAME_DB}:{USERPASSWORD}@{HOST}"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# Use motor's AsyncIOMotorClient for asynchronous MongoDB operations
client = AsyncIOMotorClient(uri)

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
    
# Define database and collections
database = client[f'{DATABASE}']
items_collection = database.get_collection(f'{COLLECTION1}')
clock_in_collection = database.get_collection(f'{COLLECTION2}')
    # Define a function to insert a document into the collection