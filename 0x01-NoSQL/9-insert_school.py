#!/usr/bin/env python3
'''inserts a new document in a collection based on kwargs'''


def insert_school(mongo_collection, **kwargs):
    '''Adds docs into a collection'''
    new_docs = mongo_collection.insert_one(kwargs)
    return new_docs.inserted_id
