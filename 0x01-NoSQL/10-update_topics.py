#!/usr/bin/env python3
'''Updates school topics'''


def update_topics(mongo_collection, name, topics):
    '''changes all topics of a document school'''
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
