# set up Flask weather app
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# set up the database
engine = create_engine('sqlite:///hawaii.sqlite')

Base = automap_base()
Base.prepare(engine, reflect = True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

# set up Flask
app = Flask(__name__)

# create welcome route
@app.route('/')

# add routing information for each of the other routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs 
    /api/v1.0/temp/start/end  
    '''
    )

# precipitation route and function
@app.route('/api/v1.0/precipitation')

def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365) # calculate the given date 1 year ago
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all() # get the date and precipitation for the given year
    precip = {date: prcp for date, prcp in precipitation} # 
    return jsonify(precip) # format results into a JSON structured file 

# stations route and function
@app.route('/api/v1.0/stations')

def stations(): 
    results = session.query(Station.station).all()  # get all of the stations in our database
    stations = list(np.ravel(results)) # unravel results and convert results into a list
    return jsonify(stations = stations) # return the list as a JSON

# monthly temperature route
@app.route('/api/v1.0/tobs')

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365) # calculate the given date 1 year ago
    results = session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= prev_year).all() # query the primary station for all the temperature observations from the given year
    temps = list(np.ravel(results)) # unravel the results into a one-dimensional array and convert array into a list
    return jsonify(temps = temps) # return the list as a JSON

# statistics route and function
@app.route('/api/v1.0/temp/<start>') # starting date 
@app.route('/api/v1.0/temp/<start>/<end>') # ending date

def stats(start = None, end = None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)] 

    if not end:
        results = session.query(*sel).\
        filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
    filter(Measurement.date >= start).\
    filter(Measurement.date <= end).all() # get our statistics data
    temps = list(np.ravel(results))
    return jsonify(temps)

    