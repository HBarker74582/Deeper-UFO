from flask import Flask, render_template, redirect
from pymongo import MongoClient
import csv
import pandas as pd
import os

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import pymongo

connection = MongoClient("mongodb://localhost:27017/UFO")
db = connection.UFO.alien_data



sightings = "/data/sightings_count.csv"
df = pd.read_csv(sightings)
df = df.to_dict(orient = 'state_long' )
app_data = mongo.db.UFO
app_data.insert_many(df)
