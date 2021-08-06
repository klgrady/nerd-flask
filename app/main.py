from flask import Flask, render_template
import requests
from datetime import datetime
import sys
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config.from_pyfile('config.py')
KEY = app.config["NASA_API_KEY"]

def get_asteroid():
    now = datetime.now()
    this_day = str(now.year) + '-' + str(now.month).zfill(2) + '-' + str(now.day).zfill(2)
    URL = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=' + this_day + '&api_key=' + KEY
    resp = requests.get(URL)

    death_dict = resp.json()
    todays_death = death_dict['near_earth_objects'][this_day]
    
    ret_string = "There are " + str(death_dict['element_count']) + " near-Earth objects right now! Lucky us!<p>Choose your favorite object of destruction:"

    for item in todays_death:
        ret_string += "<a href=\"" + item["nasa_jpl_url"] + "\">Near Earth Object " + item['name'] + "</a>: <BR>"

    return ret_string

def get_poem():
    URL= 'https://www.poemist.com/api/v1/randompoems'
    resp = requests.get(URL)
    poem_dict = resp.json()
    ret_string = "<h3>" + poem_dict[0]['title'] + " by " + poem_dict[0]['poet']['name'] + "</h3><p>" + poem_dict[0]['content'].replace('\n', '<br>')
    return ret_string

@app.route('/')
def index():
    #return '<h1>How We\'ll Die Today</h1>' + get_asteroid() + "<p>No worries, though. Here's a poem to calm your nerves.<p>" + get_poem()
    return render_template('main.html', death = get_asteroid(), poem = get_poem())