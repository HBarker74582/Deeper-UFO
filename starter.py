#Dependencies
from flask_pymongo import pymongo
import pandas as pd
<<<<<<< HEAD
import json
import os
=======
# DATABASE CONNECTION-MONGO DB
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
mongo = client.UFO
>>>>>>> f07cae5a8656ee56586cbd8a755c74fd2a7a72d5

# CREATING COLLECTIONS such as alien_data, military_bases, mj_legal, sightings_count IN DATABASE UFO
alien_collection = mongo.db.alien_data
military_basescollection = mongo.db.military_bases
sightings_collection = mongo.db.sightings_count
word_collection = mongo.db.word_cloud_usatotals

<<<<<<< HEAD
def import_csvfile(filepath):
    mongo_client = pymongo.MongoClient('localhost', 27017)
    mongo_db = mongo_client['UFO1']
    db_collection = mongo_db[sightings_count]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)
    data = pd.read_csv(file_res)
    data_json = json.load(data.to_json(orient='records'))
    db_collection.insert(data_json)
=======
# READING CSV FILES AND CONVERTING TO DATAFRAMES
alien_data_df = pd.read_csv("data/alien_data.csv")
military_bases_df = pd.read_csv("data/military_bases.csv")
sightings_count_df = pd.read_csv("data/sightings_count.csv")
word_cloud_df = pd.read_csv("data/word_cloud_usatotals.csv")
# DATAFRAMES TO DICTIONARIES
alien = alien_data_df.to_dict(orient = 'records')
military = military_bases_df.to_dict(orient = 'records')
sightings = sightings_count_df.to_dict(orient = 'records')
word = word_cloud_df.to_dict(orient ='records')
# LOAD DICTIONARIES TO COLLECTIONS
alien_collection.insert_many(alien)
military_basescollection.insert_many(military)
sightings_collection.insert_many(sightings)
word_collection.insert_many(word)
>>>>>>> f07cae5a8656ee56586cbd8a755c74fd2a7a72d5


    filepath = "data/sightings_count.csv"
    import_csvfile(filepath)
    print(filepath)

<<<<<<< HEAD
# connection = MongoClient()
# db = connection.UFO1

# sightings_count = db.sightings_count
# df = pd.read_csv("data/sightings_count.csv")
# records = df.to_dict(orient = 'state_long' )
# result = db.sightings_count.insert_many(records)
=======
>>>>>>> f07cae5a8656ee56586cbd8a755c74fd2a7a72d5
