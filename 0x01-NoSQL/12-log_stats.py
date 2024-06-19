#!/usr/bin/env python3
"""module 12"""

from pymongo import MongoClient


def get_ngins_stats(nginx_collection):
    """function to get nginx stats"""
    total_logs = len(list(nginx_collection.find()))
    print("{} logs".format(total_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = len(list(nginx_collection.find({"method": method})))
        print("\tmethod {}: {}".format(method, count))

    status_check = len(list(nginx_collection.find({
        "method": "GET",
        "path": "/status"
    })))
    print("{} status check".format(status_check))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    get_ngins_stats(nginx_collection)
    client.close()
