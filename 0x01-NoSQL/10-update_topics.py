#!/usr/bin/env python3


'''
 a Python function that changes all topics of a school document based
 on the name.
'''


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    '''
    Update documents that match the specified criteria
    '''
    result = mongo_collection.update_many(
        {'name': name},  # Filter criteria:Update documents with the givenname
        {'$set': {'topics': topics}}  # Update operation:Set the'topics'field
    )
    # Return the number of modified documents
    return result.modified_count
