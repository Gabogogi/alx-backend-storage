#!/usr/bin/env python3
'''A script to list all docs in a collection'''


def list_all(mongo_collection):
    '''lists all documents'''
    return mongo_collection.find()
