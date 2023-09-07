#!/usr/bin/env python3
"""insertion module"""


def update_topics(mongo_collection, name, topics):
    '''update all topics'''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
