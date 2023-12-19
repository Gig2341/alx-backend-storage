#!/usr/bin/python3


'''
this module inserts a new document in a collection based on kwargs
returns new _id
'''


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    '''
    this function inserts a new document in a collection based on kwargs
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
