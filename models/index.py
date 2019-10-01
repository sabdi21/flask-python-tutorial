from pymongo import MongoClient
import os

# os is how you access environment variables
mongo_client = os.environ.get('MONGOD_URI', default='mongodb://localhost:27017')

client = MongoClient(mongo_client)
db = client['py-tutorials']