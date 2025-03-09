import datetime as dt
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Setup Flask and the database connection
app = Flask(__name__)

# Database setup
engine = create_engine('sqlite:///Resources/hawaii.sqlite')  # Adjust path if necessary
Base = automap_base()
Base.prepare(autoload_with=engine)  # Reflect tables into SQLAlchemy ORM

# Reflect the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Date handling for the last year
most_recent_date = session.query(func.max(Measurement.date)).scalar()
one_year_ago = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)

# Home route
@app.route("/")
def home():
    return (
        f"Welcome to the Climate App API!<br>"
        f"Available Routes:<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/temp/<start><br>"
        f"/api/v1.0/temp/<start>/<end>"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Query the last 12 months of precipitation data
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).all()

    # Check if data is found
    if not results:
        return jsonify({"error": "No precipitation data found for the last year."})

    # Create a dictionary from the query results
    precipitation_data = {date: prcp for date, prcp in results}

    return jsonify(precipitation_data)

# Temperature Observations (TOBS) route
@app.route("/api/v1.0/tobs")
def tobs():
    # Query the database to get the temperature observations (TOBS) for the most active station
    active_station = 'USC00519281'  # You can adjust this to get the most active station dynamically if needed
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == active_station).\
        filter(Measurement.date >= one_year_ago).all()

    # Check if data is found
    if not results:
        return jsonify({"error": "No temperature data found for the last year."})

    # Create a dictionary from the query results
    temperature_data = {date: tobs for date, tobs in results}

    return jsonify(temperature_data)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    # Query the stations data
    results = session.query(Station.station, Station.name).all()

    # Check if data is found
    if not results:
        return jsonify({"error": "No stations data found."})

    # Create a dictionary from the query results
    stations_data = {station: name for station, name in results}

    return jsonify(stations_data)

# Start date route
@app.route("/api/v1.0/<start>")
def start(start):
    # Try to query the min, max, and average temperatures from the start date onwards
    try:
        results = session.query(
            func.min(Measurement.tobs),
            func.max(Measurement.tobs),
            func.avg(Measurement.tobs)
        ).filter(Measurement.date >= start).all()

        # Check if data is found
        if not results:
            return jsonify({"error": f"No temperature data found for the start date {start}."})

        # Return data as a JSON response
        return jsonify({
            "Start Date": start,
            "Min Temp": results[0][0],
            "Max Temp": results[0][1],
            "Avg Temp": results[0][2]
        })
    except Exception as e:
        return jsonify({"error": str(e)})

# Start/end date route
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Try to query the min, max, and average temperatures between the start and end dates
    try:
        results = session.query(
            func.min(Measurement.tobs),
            func.max(Measurement.tobs),
            func.avg(Measurement.tobs)
        ).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

        # Check if data is found
        if not results:
            return jsonify({"error": f"No temperature data found for the date range {start} to {end}."})

        # Return data as a JSON response
        return jsonify({
            "Start Date": start,
            "End Date": end,
            "Min Temp": results[0][0],
            "Max Temp": results[0][1],
            "Avg Temp": results[0][2]
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
