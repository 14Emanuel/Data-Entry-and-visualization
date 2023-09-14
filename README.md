Data Entry and Visualization Project
Project Overview
This project encompasses a comprehensive data management system, featuring a web-based data entry system, a Django back-end for data processing, MongoDB for data storage, and Folium for interactive map generation. Additionally, an Android application has been developed to enhance data entry and provide users with more versatile update options. The project also includes various web UI templates for location details, user information, and database updates.

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
Android Application:

Java or Kotlin (Android SDK)
Deployment and Automation:

Deployment: PythonAnywhere
Automation: Cron jobs for scheduled tasks
Project Workflow
Users input data through the Data Entry UI, accessible via web browsers.
The Django back-end processes the entered data.
Processed data is stored in MongoDB.
A Python script fetches data from MongoDB and generates a Folium map with location markers.
Clicking a marker on the Folium map opens the Location Details UI.
Users navigate to the Navigation Pane UI from the Location Details UI.
In the Navigation Pane UI, users can access the Status Update Template to update records in the database.
An Android application provides additional data entry and update options for users on mobile devices.
Project Setup
Clone the project repository.
Install required dependencies for Django, MongoDB, and Folium.
Configure Django settings to connect to your MongoDB database.
Deploy the web application on PythonAnywhere.
Set up cron jobs for automation.
Build and deploy the Android application on mobile devices.
Conclusion
This project offers a comprehensive data management solution, combining web-based and mobile data entry options. By integrating Django, MongoDB, Folium, PythonAnywhere, and Android development, it provides users with versatile tools for managing location data. Please refer to the respective URLs for accessing different parts of the web application and the Android application for mobile data entry and updates.
