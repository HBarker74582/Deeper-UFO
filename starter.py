# DATABASE CONNECTION-MONGO DB
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
mongo = client.UFO

# CREATING COLLECTIONS such as alien_data, military_bases, mj_legal, sightings_count IN DATABASE UFO
alien_collection = mongo.db.alien_data
military_basescollection = mongo.db.military_bases
sightings_collection = mongo.db.sightings_count
word_collection = mongo.db.word_count

# READING CSV FILES AND CONVERTING TO DATAFRAMES
alien_data_df = pd.read_csv("data/alien_data.csv")
military_bases_df = pd.read_csv("data/military_bases.csv")
sightings_count_df = pd.read_csv("data/sightings_count.csv")
word_count_df = pd.read_csv("data/word_count.csv")
# DATAFRAMES TO DICTIONARIES
alien = alien_data_df.to_dict(orient = 'records')
military = military_bases_df.to_dict(orient = 'records')
sightings = sightings_count_df.to_dict(orient = 'records')
word = word_count_df.to_dict(orient ='records')
# LOAD DICTIONARIES TO COLLECTIONS
alien_collection.insert_many(alien)
military_basescollection.insert_many(military)
sightings_collection.insert_many(sightings)
word_collection.insert_many(word)



