Project README
Data Entry and Visualization Project
Project Overview
This project involves creating a data entry system, processing data using a Django back-end, storing data in a MongoDB database, and generating interactive maps with location markers using Folium. The project also includes web UI templates to display location details, allow users to view more information, and update records in the database.

Components
Data Entry UI

URL: Data Entry UI
Description: This is the user interface where data will be input. Users can input location-related data here.
Django Back-end

Description: The Django back-end processes the data entered in the Data Entry UI.
MongoDB

Description: MongoDB is used to store the data that is processed by the Django back-end.
Python Script (Py Script)

Description: This Python script fetches data from MongoDB and generates a Folium map.
Folium Map

Description: The Folium map displays location coordinates with marker icons. When a user clicks on a marker icon, it opens a web UI pop-up template containing a summary of the location details.
URL: Folium Map
Location Details UI

Description: This UI template displays location details when a user clicks on a marker icon on the Folium map. It includes a hyperlink "View more details."
URL: Location Details UI
Navigation Pane UI

Description: This UI template is accessed by clicking the "View more details" hyperlink in the Location Details UI. It contains all location details.
URL: Navigation Pane UI
Status Update Template

Description: Accessed by clicking the "View more details" hyperlink in the Navigation Pane UI. This template allows users to update records in the database.
URL: Status Update Template
Project Workflow
Users input data through the Data Entry UI.

The Django back-end processes the entered data.

Processed data is stored in MongoDB.

The Python script fetches data from MongoDB and generates a Folium map with location markers.

When users click on a marker on the Folium map, they can view location details in the Location Details UI.

From the Location Details UI, users can navigate to the Navigation Pane UI to see all location details.

In the Navigation Pane UI, users can access the Status Update Template to update records in the database.

Project Setup
To set up this project locally, follow these steps:

Clone the project repository.

Install the required dependencies for Django, MongoDB, and Folium.

Configure the Django settings to connect to your MongoDB database.

Run the Django development server.

Access the Data Entry UI to start entering data.

Conclusion
This project combines data entry, processing, storage, and visualization to provide users with an interactive interface to view and update location details. It utilizes Django, MongoDB, Folium, and various UI templates to achieve these functionalities. Please refer to the respective URLs provided to access each part of the project.
