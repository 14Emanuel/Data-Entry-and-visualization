from pymongo import MongoClient
from pymongo.errors import CursorNotFound

# Replace the placeholder with your actual MongoDB connection string
mongo_client = MongoClient('mongodb+srv://dummy:code@cluster0.nqhzqof.mongodb.net/?retryWrites=true&w=majority')

# Use the 'dummy' database and collection
database = mongo_client['dummy']
collection = database['dummy']

# Define the pipeline for the change stream
pipeline = [{'$match': {'operationType': 'insert'}}]

# Open a change stream cursor
try:
    with collection.watch(pipeline) as stream:
        print("Listening for new data...")
        for change in stream:
            # Process the new document
            print("New data detected:")
            print(change['fullDocument'])
except CursorNotFound:
    print("The change stream cursor was closed.")
except Exception as e:
    print(f"An error occurred: {e}")
