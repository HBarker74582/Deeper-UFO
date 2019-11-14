##############################################################################################################################
# DEPENDENCIES
from flask import Flask, render_template, jsonify
from flask_pymongo import pymongo
import pandas as pd
# FLASK SET UP
app = Flask(__name__)
# DATABASE CONNECTION-MONGO DB
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
mongo = client.CAT


# CREATING COLLECTIONS such as alien_data, military_bases, mj_legal, sightings_count IN DATABASE UFO
alien_collection = mongo.db.alien_data
military_collection = mongo.db.military_bases
sightings_collection = mongo.db.sightings_count


# READING CSV FILES AND CONVERTING TO DATAFRAMES
alien_data_df = pd.read_csv("assets/data/alien_data.csv")
military_bases_df = pd.read_csv("assets/data/military_bases.csv")
sightings_count_df = pd.read_csv("assets/data/sightings_count.csv")
# DATAFRAMES TO DICTIONARIES
alien = alien_data_df.to_dict(orient = 'records')
military = military_bases_df.to_dict(orient = 'records')
sightings = sightings_count_df.to_dict(orient = 'records')
# LOAD DICTIONARIES TO COLLECTIONS
alien_collection.insert_many(alien)
military_collection.insert_many(military)
sightings_collection.insert_many(sightings)

#############################################################################################################################

sightings_count_df = pd.DataFrame(list(sightings_collection.find()))
sightings_count_df_new = sightings_count_df[['state_long','state_short','sightings_total']]
print(sightings_count_df_new)       

mj_legal_df = pd.DataFrame(list(mj_collection.find()))
mj_legal_df_new = mj_legal_df[['State','Marijuana Legal']]
mj_legal_df_rename = mj_legal_df_new.rename(columns={'State': 'state_long','Marijuana Legal': 'marijuana_legal'})
print(mj_legal_df_rename)   

combined_sightings_and_mj_legal_df = pd.merge(sightings_count_df_new, mj_legal_df_rename, on='state_long')
combined_sightings_and_mj_legal_sort_df = combined_sightings_and_mj_legal_df.sort_values(by='state_long')
print(combined_sightings_and_mj_legal_sort_df)               
#combined_df_to_dict = combined_sightings_and_mj_legal_df.to_dict(orient = 'records')
#creating a new database 'sightings_Vs_mj'
#sightings_Vs_mj_collection = mongo.db.sightings_Vs_mj
#sightings_Vs_mj_collection.insert_many(combined_df_to_dict)



# FLASK ROUTES
