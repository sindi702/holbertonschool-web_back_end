#!/usr/bin/env python3
'''list all doc in python'''


def list_all(mongo_collection):
    '''func that list all doc'''
    collec_list = []

    for data in mongo_collection.find():
        if data:
            collec_list.append(data)
    return collec_list
