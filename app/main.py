from flask import Flask
import requests
from datetime import datetime
import sys

app = Flask(__name__)
app.config.from_pyfile('config.py')
KEY = app.config["NASA_API_KEY"]

def get_asteroid():
    now = datetime.now()
    this_day = str(now.year) + '-' + str(now.month).zfill(2) + '-' + str(now.day).zfill(2)
    URL = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=' + this_day + '&api_key=' + KEY
    resp = requests.get(URL)

    death_dict = resp.json()
    todays_death = death_dict['near_earth_objects'][this_day]
    
    ret_string = "There are " + str(death_dict['element_count']) + " near-Earth objects right now!<p>"

    for item in todays_death:
        ret_string += "<a href=\"" + item["nasa_jpl_url"] + "\">Near Earth Object " + item['name'] + "</a><BR>"

    return ret_string

@app.route('/')
def index():
    return '<h1>How We\'ll Die Today</h1>' + get_asteroid()