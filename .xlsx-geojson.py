import pandas as pd
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
