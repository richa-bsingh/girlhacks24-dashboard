import pymongo
import pandas as pd

# MongoDB connection
def get_mongo_data():
    # Connect to MongoDB instance
    client = pymongo.MongoClient("mongodb+srv://richadb:mongodb123@cluster0.2f8jo.mongodb.net")  # Replace with your MongoDB URI
    db = client['playlist-hack24']  # Replace with your database name
    songs_collection = db['Songs']  # Replace with your collection name

    # Fetch data from MongoDB and convert to a pandas DataFrame
    songs_data = list(songs_collection.find())
    return pd.DataFrame(songs_data)  # Return as a pandas DataFrame
