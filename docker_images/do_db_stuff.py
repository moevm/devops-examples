#!/bin/python3.7
from pymongo import MongoClient

HOST = "mongo"
client = MongoClient(HOST, 27017)


print(client.example.list_collection_names())
