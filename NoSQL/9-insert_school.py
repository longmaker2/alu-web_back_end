#!/usr/bin/env python3
"""python script"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in the collection"""
    new_document = mongo_collection.insert_one(kwargs)
    new_document.inserted_id
