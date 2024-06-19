#!/usr/bin/env python3
"""Module 10"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Change all topic of school documents based on the name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    return mongo_collection.find({"name": name})
