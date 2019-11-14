# DEPENDENCIES
from flask import Flask, render_template, jsonify
from flask_pymongo import pymongo
import pandas as pd
# FLASK SET UP
app = Flask(__name__)
# DATABASE CONNECTION-MONGO DB
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
mydb = client.liquid

alien_data = mydb.alien_data
csv_path = "assets/data/alien_data.csv"
df = pd.read_csv(csv_path)

abcd = df.to_dict(orient = 'records')
# money collection name
# var =>abcd df to dict
alien = mydb.db.money
alien.insert_many(abcd)

