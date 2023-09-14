#run python manage.py collecstatic to collect static files: 'images'
import subprocess

# Define the command to run
command = "python manage.py collectstatic"

# Use subprocess to run the command and automatically answer 'yes'
try:
    subprocess.run(command, shell=True, input='yes\n', text=True, check=True)
    print("Static files collected successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error while collecting static files: {e}")
#stop

# Mongo DB to excel code start:
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

##Mongodb-excel.py stop

##Start .xlsx-geojson.py

#import pandas as pd
import geopandas as gpd

# Step 1: Read the Excel file
df = pd.read_excel("dummy_data.xlsx")

# Step 2: Process the data - Extract latitude and longitude from the "coordinates" column
df['latitude'] = df['coordinates'].str.split(',').str[0].astype(float)
df['longitude'] = df['coordinates'].str.split(',').str[1].astype(float)

# Step 3: Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))

# Step 4: Save as GeoJSON
gdf.to_file("dummy_data.geojson", driver="GeoJSON")


##Stop .xlsx-geojson.py

##Start dummy_data.py

import warnings
warnings.filterwarnings('ignore')

import geopandas as gpd
#from folium import Markup

import geopandas as gpd

# Read the GeoJSON file and load its contents into a GeoDataFrame
gdf = gpd.read_file("dummy_data.geojson")

# Display the first few rows of the GeoDataFrame
gdf.tail()

import pandas as pd
import folium
import requests

# Define a dictionary to map each type to a color
type_colors = {
    'A': 'blue',
    'B': 'green',
    'C': 'red',
    'default': 'gray'  # Default color for unknown types
}

# Create the navigation pane HTML content
selected_columns = ['_id', 'unique_id', 'surveyor_id', 'coordinates', 'nearby_station',
       'scrap_location', 'scrap_category', 'sub_category', 'scrap_status',
       'verified_scrap', 'pending_department', 'custodian',
       'custodian_contact', 'approx_weight', 'approx_rate', 'remarks',
       'latitude', 'longitude', 'geometry']
selected_gdf = gdf[selected_columns]

# Extract the first latitude and longitude values from the selected_gdf DataFrame
latitude = selected_gdf['latitude'].iloc[0]
longitude = selected_gdf['longitude'].iloc[0]

# Create a map object
m = folium.Map(location=[latitude, longitude], zoom_start=10)


# Define a function to fetch the HTML content for the pop-up pane from a URL
def fetch_popup_html(unique_id):
    try:
        url = f'https://dinudashilua.pythonanywhere.com/popup/{unique_id}/'  # Replace with your actual URL
        #print(url)
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f'<p>Unable to fetch pop-up content for unique_id={unique_id}</p>'
    except Exception as e:
        return f'<p>Error fetching pop-up content for unique_id={unique_id}: {str(e)}</p>'

def fetch_navigation_pane_html(unique_id):
    try:
        url = f'https://dinudashilua.pythonanywhere.com/navigation-pane/{unique_id}/'  # Replace with your actual URL
        #print(url)
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f'<p>Unable to fetch navigation pane content for unique_id={unique_id}</p>'
    except Exception as e:
        return f'<p>Error fetching navigation pane content for unique_id={unique_id}: {str(e)}</p>'

# Loop through the entries to add markers
for index, row in selected_gdf.iterrows():
    latitude = row['latitude']
    longitude = row['longitude']
    type_of_item = row['scrap_category']

    # Get the color for the marker based on the type
    marker_color = type_colors.get(type_of_item, type_colors['default'])

    # Fetch the pop-up HTML content for the popup template
    popup_template_html = fetch_popup_html(row['unique_id'])  # Use your function to fetch popup content

    # Fetch the pop-up HTML content for the navigation pane
    navigation_pane_html = fetch_navigation_pane_html(row['unique_id'])  # Use your function to fetch navigation pane content

    # Create a new marker for the current point
    marker = folium.Marker(
        location=[latitude, longitude],
        popup=folium.Popup(popup_template_html, max_width=500),  # Use the iframe HTML string to embed the content
        icon=folium.Icon(color=marker_color)
    )

    marker.add_to(m)

# Save the map to an HTML file in the "gis/templates/" directory
m.save('/home/dinudashilua/django-app/gis/templates/map.html')

##Stop dummy_data.py