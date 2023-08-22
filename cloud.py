# Mongo DB to excel code start:
import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://dummy:code@cluster0.nqhzqof.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Access the 'dummy' database and 'dummy' collection
db = client['dummy']
collection = db['dummy']

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


import folium
import pandas as pd
#import base64

# Define a dictionary to map each type to a color
type_colors = {
    'A': 'blue',
    'B': 'green',
    'C': 'red',
    'default': 'gray'  # Default color for unknown types
}

# Create the navigation pane HTML content
selected_columns = ['unique_id', 'coordinates', 'gis', 'plus_code',
       'nearby_railway_address', 'nearby_railway_station', 'photos', 'videos',
       'type_of_item', 'status', 'verified_scrap', 'pending_department',
       'lot_no_engineering', 'lot_no_stores', 'auction_date_given', 'fdp_date',
       'phone_no', 'custodian', 'approx_weight', 'approx_rate', 'latitude',
       'longitude', 'geometry']
selected_gdf = gdf[selected_columns]

# Create a map object using the GeoDataFrame
m = folium.Map(location=[selected_gdf['latitude'].mean(), selected_gdf['longitude'].mean()], zoom_start=10)

# Create FeatureGroups for each type of item
type_feature_groups = {type_item: folium.FeatureGroup(name=f'Type {type_item}') for type_item in type_colors}

# Define a function to create the HTML content for the pop-up pane
def create_popup_html(row):
    unique_id = row['unique_id']
    coordinates = row['coordinates']
    gis = row['gis']
    plus_code = row['plus_code']
    image_base64 = row['photos']

    # Specify the base64 encoded image source
    image_src = f'data:image/jpeg;base64,{image_base64}'

    popup_html = f'''
        <img src="{image_src}" alt="Image" width="200"><br>
        <b>Unique ID:</b> {unique_id}<br>
        <b>Coordinates:</b> {coordinates}<br>
        <b>GIS:</b> {gis}<br>
        <b>PLUS CODE:</b> {plus_code}<br>

        <a href="#" onclick="toggleNavigationPane('{unique_id}', event)">View More Details</a>
    '''

    return popup_html

# Define the CSS and JavaScript code for the navigation pane
css_navigation_pane = '''
    <style>
    /* Custom CSS for the navigation pane */
    .navigation-ui {
        display: none;
        position: absolute;
        top: 80px; /* Adjust the top position as needed */
        left: 10px;
        padding: 10px;
        background-color: white;
        z-index: 1000;
    }
    .video-container {
        margin-bottom: 10px;
    }
    </style>
'''

js_navigation_pane = '''
    <script>
    // JavaScript code for the navigation pane
    function toggleNavigationPane(uniqueId, event) {
        event.preventDefault();
        var navigationPane = document.getElementById('navigation-ui-' + uniqueId);
        if (navigationPane.style.display === 'none') {
            navigationPane.style.display = 'block';
        } else {
            navigationPane.style.display = 'none';
        }
    }

    // JavaScript code for the navigation pane
    function editDataFieldsStatus(uniqueId, event) {
    event.preventDefault();

    // Open the status_update.html file in a new tab, passing the uniqueId as a query parameter
    var url = `/status_update/${uniqueId}/`; // Modify the URL to include the uniqueId as a parameter
    //var url = `/status_update/`; // Modify the URL to include the uniqueId as a parameter
    window.open(url, '_blank');
    }

    </script>
'''


# Function to generate custom HTML for the navigation pane
def generate_navigation_ui(row):
    unique_id = row['unique_id']
    nearby_location = row['nearby_railway_address']
    nearby_railway_station = row['nearby_railway_station']
    videos_base64 = row['videos']
    type_of_item = row['type_of_item']
    status = row['status']
    verified_scrap = row['verified_scrap']
    pending_department = row['pending_department']
    lot_no_engineering = row['lot_no_engineering']
    lot_no_stores = row['lot_no_stores']
    auction_date_given = row['auction_date_given']
    fdp_date = row['fdp_date']
    phone_no = row['phone_no']
    custodian = row['custodian']
    approx_weight = row['approx_weight']
    approx_rate = row['approx_rate']

    # Specify the base64 encoded video source
    video_src = f'data:video/mp4;base64,{videos_base64}'

    # Add the hyperlink "Edit Data Fields Status" with an anchor tag
    edit_data_fields_link = f'<a href="#" onclick="editDataFieldsStatus(\'{unique_id}\', event)">Edit Data Fields Status</a>'




    ui_html = f'''
        <div id="navigation-ui-{unique_id}" class="navigation-ui">
            <h2>Navigation UI</h2>
            <p><b>Unique ID:</b> {unique_id}</p>
            <p><b>Nearby Railway Address:</b> {nearby_location}</p>
            <p><b>Nearby Railway Station:</b> {nearby_railway_station}</p>
            <p><b>Type of item:</b> {type_of_item}</p>
            <p><b>Status:</b> {status}</p>
            <p><b>Verified as Scrap:</b> {verified_scrap}</p>
            <p><b>Pending with Department:</b> {pending_department}</p>
            <p><b>Lot no Engineering:</b> {lot_no_engineering}</p>
            <p><b>Lot no Stores:</b> {lot_no_stores}</p>
            <p><b>Auction Date Given:</b> {auction_date_given}</p>
            <p><b>FDP ends:</b> {fdp_date}</p>
            <p><b>Phone no:</b> {phone_no}</p>
            <p><b>Custodian:</b> {custodian}</p>
            <p><b>Approximate Weight:</b> {approx_weight}</p>
            <p><b>Approximate Rate:</b> {approx_rate}</p>
            <div class="video-container">
                <video width="320" height="240" controls>
                    <source src="{video_src}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            <div>
            {edit_data_fields_link}
            </div>
        </div>
    '''

    return ui_html



# Iterate over the rows of the selected GeoDataFrame (selected_gdf)
for index, row in selected_gdf.iterrows():
    unique_id = row['unique_id']
    coordinates = row['coordinates']
    gis = row['gis']
    plus_code = row['plus_code']
    nearby_location = row['nearby_railway_address']
    nearby_railway_station = row['nearby_railway_station']
    image_base64 = row['photos']
    videos_base64 = row['videos']
    type_of_item = row['type_of_item']
    status = row['status']
    verified_scrap = row['verified_scrap']
    pending_department = row['pending_department']
    lot_no_engineering = row['lot_no_engineering']
    lot_no_stores = row['lot_no_stores']
    auction_date_given = row['auction_date_given']
    fdp_date = row['fdp_date']
    phone_no = row['phone_no']
    custodian = row['custodian']
    approx_weight = row['approx_weight']
    approx_rate = row['approx_rate']
    latitude = row['latitude']
    longitude = row['longitude']

    # Get the color for the marker based on the type
    marker_color = type_colors.get(type_of_item, type_colors['default'])

    # Create the HTML content for the pop-up pane
    popup_html = create_popup_html(row)

    # Create a new marker for the current point
    marker = folium.Marker(
        location=[latitude, longitude],
        popup=folium.Popup(popup_html, max_width=250),
        icon=folium.Icon(color=marker_color)
    )

    # Add the marker to the respective FeatureGroup based on the type of item
    type_feature_group = type_feature_groups.get(type_of_item, type_feature_groups['default'])
    marker.add_to(type_feature_group)

    # Generate the navigation pane HTML content and add it to the map
    navigation_ui_html = generate_navigation_ui(row)
    navigation_ui_element = folium.Element(navigation_ui_html)
    m.get_root().html.add_child(navigation_ui_element)

    # Add a script tag to hide the navigation pane initially
    m.get_root().html.add_child(folium.Element(f"<script>document.getElementById('navigation-ui-{unique_id}').style.display = 'none';</script>"))


# Add the CSS and JavaScript code to the map
m.get_root().html.add_child(folium.Element(css_navigation_pane))
m.get_root().html.add_child(folium.Element(js_navigation_pane))

# Add each FeatureGroup to the map
for feature_group in type_feature_groups.values():
    feature_group.add_to(m)

# Add a LayerControl to the map to toggle the visibility of the feature groups
folium.LayerControl().add_to(m)

# Save the map to an HTML file in the "gis/templates/" directory
m.save('/home/dinudashilua/django-app/gis/templates/map.html')

##Stop dummy_data.py