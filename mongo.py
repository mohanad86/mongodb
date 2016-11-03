import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 54321)
print (client)
db = client.clients
db.clients.count()
clients = db.clients
clients.find()



for k in range(6000):
    clients = db.clients.insert({"birthdate":"1970-01-01"});
print (k)

for l in range(6000):
    clients = db.clients.insert({"birthdate":"1995-01-01"});
print(l)

for i in range(100):
   clients = db.clients.insert({"name":"Tom"});
print(i)

for j in range(100):
   clients = db.clients.insert({"name":"Tom hanks"});
print(j)



print(db.clients.count())

