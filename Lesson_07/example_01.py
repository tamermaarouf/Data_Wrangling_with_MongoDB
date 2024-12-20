#!/usr/bin/env python3
'''
Your task is to sucessfully run the exercise to see how pymongo works
and how easy it is to start using it.
You don't actually have to change anything in this exercise,
but you can change the city name in the add_city function if you like.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code on MongoDB outside of our classroom,
please see the Instructor comments at the bottom of this page for link.
'''


def add_city(db):
    # Changes to this function will be reflected in the output.
    # All other functions are for local use only.
    # Try changing the name of the city to be inserted
    db.cities.insert_one({"name": "Chicago"})


def get_city(db):
    return db.cities.find_one()


def get_db():
    # For local use
    from pymongo import MongoClient
    client = MongoClient('mongodb://127.0.0.1:27017')
    # here is the database name. It will be created if it does not exist.
    db = client.examples
    return db


if __name__ == "__main__":
    # For local use
    db = get_db()
    add_city(db)
    print(get_city(db))
