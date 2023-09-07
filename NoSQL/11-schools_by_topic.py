#!/usr/bin/env python3
"""insertion module"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school"""
    result = mongo_collection.find({'topics': {'$in': [topic]}})
    return result
