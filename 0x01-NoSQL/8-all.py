#!/usr/bin/env python3


'''
this module lists all documents in a collection
returns an empty list if no document in the collection
'''


from pymongo import MongoClient


def list_all(mongo_collection):
    '''a function that lists all documents in a collection'''
    for document in mongo_collection.find():
        return document
