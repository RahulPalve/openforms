from pymongo import MongoClient

client = MongoClient("mongodb://admin:rahpal399@localhost:27017/?authSource=admin")
db = client["oforms"]
db.user.insert_one({"name": "Test User", "email": "rahulpalve91@gmail.com", "password": "testword"})
client.close()
