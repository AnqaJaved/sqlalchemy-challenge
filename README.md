###Module 10
By #Anqa Javed

Overview
This project involves creating a Flask API to analyze and serve climate data from Honolulu, Hawaii. The analysis and API development are divided into two main parts:

Data Analysis with Jupyter Notebook: Utilizing Python, SQLAlchemy, Pandas, and Matplotlib to explore climate data.
Flask API Development: Designing a web API to provide access to the analyzed climate data.

##Part 1: Data Analysis with Jupyter Notebook
In the climate_starter.ipynb notebook, the following steps were performed:

Data Loading: Connected to the SQLite database using SQLAlchemy and loaded the measurement and station tables.
Precipitation Analysis:
Retrieved the last 12 months of precipitation data.
Visualized precipitation trends using Matplotlib.
Station Analysis:
Identified the most active weather stations.
Analyzed temperature observations for the most active station.
Part 2: Flask API Development
The Flask API provides several routes to access climate data:

Home Route (/):

Displays a list of all available API routes.
Precipitation Route (/api/v1.0/precipitation):

Returns the last 12 months of precipitation data in JSON format.
Stations Route (/api/v1.0/stations):

Provides a JSON list of all weather stations.
Temperature Observations Route (/api/v1.0/tobs):

Returns temperature observations for the most active station over the last year.
Start Date Route (/api/v1.0/<start>):

Accepts a start date in YYYY-MM-DD format.
Returns min, avg, and max temperatures from the start date to the most recent data.
Start and End Date Route (/api/v1.0/<start>/<end>):

Accepts start and end dates in YYYY-MM-DD format.
Returns min, avg, and max temperatures for the specified date range.
How to Run the Flask API
Clone the Repository:

bash
Copy
git clone https://github.com/AnqaJaved/sqlalchemy-challenge.git
cd sqlalchemy-challenge/SurfsUp
Install Dependencies: Ensure you have Python installed, then install the required packages:

bash
Copy
pip install Flask SQLAlchemy
Run the Flask App: Start the Flask development server:

bash
Copy
python app.py
The API will be accessible at http://127.0.0.1:5000/.

Testing the API Routes
With the Flask app running, you can test the API routes by visiting the following URLs in your browser or using a tool like Postman:

Home Route: http://127.0.0.1:5000/
Precipitation Route: http://127.0.0.1:5000/api/v1.0/precipitation
Stations Route: http://127.0.0.1:5000/api/v1.0/stations
Temperature Observations Route: http://127.0.0.1:5000/api/v1.0/tobs
Start Date Route (e.g., August 1, 2016): http://127.0.0.1:5000/api/v1.0/2016-08-01
Start and End Date Route (e.g., August 1–23, 2016): http://127.0.0.1:5000/api/v1.0/2016-08-01/2016-08-23
Requirements
Python 3.x
Flask
SQLAlchemy
SQLite
Acknowledgments
Data Source: Climate data sourced from the hawaii.sqlite database.
Flask: Used for creating the web API.
SQLAlchemy: Used for database interactions.
Conclusion
This project demonstrates how to analyze climate data using Python and create a Flask API to serve the data. The API allows users to access precipitation, station, and temperature data, as well as perform date-based temperature analyses.

