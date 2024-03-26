#!/usr/bin/env python3
'''Where to learn python'''


def schools_by_topic(mongo_collection, topic):
    '''show schools that teach python'''
    return mongo_collection.find({"topics": topic})
