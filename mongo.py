import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 54321)
db = client.clients
collection = db.clients
db.clients.count()
clients = db.clients
clients.find()


print(db.clients.count())

for i in range(5):
    clients = db.clients.insert({'date': 'name'})
    
print(clients)



