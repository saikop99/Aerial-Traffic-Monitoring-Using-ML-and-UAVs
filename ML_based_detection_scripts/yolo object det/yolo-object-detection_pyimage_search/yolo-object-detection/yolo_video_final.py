# Python code to illustrate
# inserting data in MongoDB
from pymongo import MongoClient
import urllib.parse

try:
    conn = MongoClient('cluster0-9bp5w.mongodb.net',username='user01',password='user@123',authSource='Traffic_Monitoring',authMechanism='SCRAM-SHA-1')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# database
db = conn.Traffic_Monitoring
# Created or Switched to collection names: my_gfg_collection
collection = db.Density

data1 = {
        "val":24,
        "location":"Calicut"
        }
data2 = {
        "val":14,
        "location":"Calicut"
        }

# Insert Data
rec_id1 = collection.insert_one(data1)
rec_id2 = collection.insert_one(data2)

print("Data inserted with record ids",data1," ",data2)

# Printing the data inserted
cursor = collection.find()
for record in cursor:
    print(record)
