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
    print("{} status check".format(nginx_collection.count_documents({})))
    print("IPs:")
    result = {}
    for item in nginx_collection.find():
        result[item["ip"]] = 0

    for item in nginx_collection.find():
        key = item["ip"]
        result[key] += 1

    count = 0
    for key, value in sorted(result.items(), key=lambda x: x[1], reverse=True):
        count += 1
        print(f"{key}: {value}")
        if count == 10:
            break
