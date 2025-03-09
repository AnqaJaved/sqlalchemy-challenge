from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")
session = Session(engine)

# Direct query to check the tables
result = session.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print("Tables in the database:", result)

# Check the columns in the 'measurement' and 'station' tables directly
if result:
    if ('measurement',) in result:
        columns_measurement = session.execute("PRAGMA table_info(measurement);").fetchall()
        print("Columns in 'measurement' table:", columns_measurement)

    if ('station',) in result:
        columns_station = session.execute("PRAGMA table_info(station);").fetchall()
        print("Columns in 'station' table:", columns_station)
else:
    print("No tables found in the database.")
