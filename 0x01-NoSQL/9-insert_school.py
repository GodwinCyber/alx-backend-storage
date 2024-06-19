#!/usr/bin/env python3
"""Module 9"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection based on kwargs
    Args:
        Return the new _id
    """
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
