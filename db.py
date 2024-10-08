import pymongo
import pandas as pd
import requests
import streamlit as st

# MongoDB connection
def get_mongo_data():
    # Connect to MongoDB instance
    client = pymongo.MongoClient("mongodb+srv://richadb:mongodb123@cluster0.2f8jo.mongodb.net")  # Replace with your MongoDB URI
    db = client['playlist-hack24']  # Replace with your database name
    songs_collection = db['Songs']  # Replace with your collection name

    # Fetch data from MongoDB and convert to a pandas DataFrame
    # songs_data = list(songs_collection.find())
    return songs_collection  # Return as a pandas DataFrame


# Base API URL
BASE_API_URL = "http://app.discofy.us"

# Function to fetch songs data from the updated API endpoint and return as DataFrame
def get_songs_data():
    try:
        response = requests.get(f"{BASE_API_URL}/songs/all_songs?limit=600")
        response.raise_for_status()  # Raise error for bad status
        songs_data = response.json()
        
        # Normalize and create a DataFrame
        #songs_df = pd.json_normalize(songs_data)
        songs_collection = songs_data
        return songs_collection
    
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching songs: {e}")
        return pd.DataFrame()
    
def get_job_postings_data():
    client = pymongo.MongoClient("mongodb+srv://richadb:mongodb123@cluster0.2f8jo.mongodb.net")
    db = client['playlist-hack24']
    job_postings = db['job_postings']

    return job_postings

def get_company_specialities_data():
    client = pymongo.MongoClient("mongodb+srv://richadb:mongodb123@cluster0.2f8jo.mongodb.net")
    db = client['playlist-hack24']
    company_specialities = db['company_specialities']

    return company_specialities