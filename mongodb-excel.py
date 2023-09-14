import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://dummy:code@cluster0.nqhzqof.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Access the 'dummy' database and 'dummy' collection
db = client['dummy']
collection = db['navigation_entry']

def read_all_records_to_xlsx(file_name='dummy_data.xlsx'):
    # Retrieve all records from the collection
    cursor = collection.find()

    # Convert the cursor to a pandas DataFrame
    df = pd.DataFrame(list(cursor))

    if not df.empty:
        # Write the DataFrame to a .xlsx file
        df.to_excel(file_name, index=False)
        print(f'Data saved to {file_name} successfully.')
    else:
        print('No records found in the collection.')

if __name__ == '__main__':
    read_all_records_to_xlsx()
