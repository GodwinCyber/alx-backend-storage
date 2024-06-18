#!/usr/bin/env python3
"""Moudle"""

import pymongo

def list_all(mongo_collection):
    """List all documents in a collection
    Args:
        Return an empty list if no document in the collection
        mongo_collection will be pymongo collection object
    """
    
    
    if mongo_collection is None:
        return []
    
    docs = [doc for doc in mongo_collection.find()]
    return docs