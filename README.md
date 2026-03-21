# Assessment 1 Software Critical Examination
# Name of Project: The EarthQUAKE Directory
This assessment explores the use of API'S and data reterival from external sources with proper data extraction from an API link.
By inputting the wanted information of an earthquake by choice. 
This directory uses the official USGS provided API. The fields in this project are location, date and location. 

# How to run the project:
first install depencies, and packages, by utilising the command pip install -r requirements.txt , which will automatically install all packages.
To actually activate the python file and tkinter, use python main.py 

# Features
For the 3 fields (location, date and location), only location is needed (But filling out all of the fields will make results more accurate), as it will search and filter for the most accurate information based off the information provided. After results are returned it is exported to a CSV by Panda Package

# API's Used
The offical USGS Earthquake API and OpenStreetMap Nominatim, are used for this project, OpenstreetMap turns the Users City into coordinates for USGS, as USGS only recognises coordinates not words for cities. 

# File's
The GUI for the project is built off main.py, where the user interacts and utilises the project. However some background processes also are handled there such as spell checking (textblob) and exporting the data to a CSV (pandas). 
The file where information and data is called, is earthquakedata.py. When information is submitted by the user, it calls the API and also reads how much information has been submitted, and returns data based off that factor.





