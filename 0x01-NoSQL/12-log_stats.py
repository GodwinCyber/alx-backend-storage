#!/usr/bin/env python3
"""module 12"""

from pymongo import MongoClient


def get_ngins_stats(nginx_collection):
    """function to get nginx stats"""
    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("    method {}: {}".format(method, count))

    status_check = nginx_collection.count_documents({
        "method": "GET",
        "path": "/status"
        })
    print("{} status check".format(status_check))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    get_ngins_stats(nginx_collection)
    client.close()
