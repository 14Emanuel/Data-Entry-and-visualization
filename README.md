
Data Entry and Visualization Project
Project Overview
This project creates a data entry system, processes data with a Django back-end, stores data in MongoDB, and generates interactive maps using Folium. It includes web UI templates for location details, user information, and database updates.

Tech Stack
Frontend:

Data Entry UI: HTML, CSS, JavaScript
Location Details UI, Navigation Pane UI, Status Update Template: HTML, CSS, JavaScript
Backend:

Django: Python web framework
MongoDB: NoSQL database for data storage
Python Script: Fetches data from MongoDB
Mapping:

Folium: Generates interactive maps
Deployment and Automation:

Deployment: PythonAnywhere
Automation: Cron jobs for scheduled tasks
Project Workflow
Users input data through the Data Entry UI.
The Django back-end processes the data.
Processed data is stored in MongoDB.
A Python script fetches data from MongoDB and generates a Folium map with location markers.
Clicking a marker on the Folium map opens the Location Details UI.
Users navigate to the Navigation Pane UI from the Location Details UI.
In the Navigation Pane UI, users can access the Status Update Template to update records in the database.
Project Setup
Clone the project repository.
Install required dependencies for Django, MongoDB, and Folium.
Configure Django settings to connect to your MongoDB database.
Deploy the app on PythonAnywhere.
Set up cron jobs for automation.
Conclusion
This project integrates data entry, processing, storage, and visualization, providing an interactive interface for location data management. Utilizing Django, MongoDB, Folium, and PythonAnywhere for deployment and automation, it streamlines the entire process. Please refer to the respective URLs for accessing different parts of the project.
