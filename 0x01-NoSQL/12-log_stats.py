#!/usr/bin/env python3

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods")
    for item in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\t method {}: {}".format(item,
              nginx_collection.count_documents({"method": item})))
