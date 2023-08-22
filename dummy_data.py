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
import base64

# Sample GeoDataFrame with data
# Assuming you already have 'gdf' DataFrame as shown in the dataset

# Define a dictionary to map each type to a color
type_colors = {
    'A': 'blue',
    'B': 'green',
    'C': 'red'
}

# Create a map object using the GeoDataFrame
m = folium.Map()

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
    </script>
'''

# Function to generate custom HTML for the navigation pane
def generate_navigation_ui(row):
    unique_id = row['unique_id']
    type_of_item = row['type_of_item']
    status = row['status']
    video_base64 = row['videos']

    # Specify the base64 encoded video source
    video_src = f'data:video/mp4;base64,{video_base64}'

    ui_html = f'''
        <div id="navigation-ui-{unique_id}" class="navigation-ui">
            <h2>Navigation UI</h2>
            <p><b>Unique ID:</b> {unique_id}</p>
            <p><b>Type of item:</b> {type_of_item}</p>
            <p><b>Status:</b> {status}</p>
            <div class="video-container">
                <video width="320" height="240" controls>
                    <source src="{video_src}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
        </div>
    '''

    return ui_html

# Create the navigation pane HTML content
selected_columns = ['unique_id', 'type_of_item', 'status', 'videos']
selected_gdf = gdf[selected_columns]

# Iterate over the rows of the GeoDataFrame
for index, row in gdf.iterrows():
    latitude = row['latitude']
    longitude = row['longitude']
    type_of_item = row['type_of_item']

    # Get the color for the marker based on the type
    marker_color = type_colors.get(type_of_item, 'gray')

    popup_html = create_popup_html(row)

    marker = folium.Marker(location=[latitude, longitude], popup=folium.Popup(popup_html),
                           icon=folium.Icon(color=marker_color), sticky=True)
    marker.add_to(m)

    navigation_ui_html = generate_navigation_ui(row)
    navigation_ui_element = folium.Element(navigation_ui_html)
    m.get_root().html.add_child(navigation_ui_element)

    # Add a script tag to hide the navigation pane initially
    m.get_root().html.add_child(folium.Element(f"<script>document.getElementById('navigation-ui-{row['unique_id']}').style.display = 'none';</script>"))

# Add the CSS and JavaScript code to the map
m.get_root().html.add_child(folium.Element(css_navigation_pane))
m.get_root().html.add_child(folium.Element(js_navigation_pane))

# Save the map to an HTML file
m.save('gis/templates/map.html')
