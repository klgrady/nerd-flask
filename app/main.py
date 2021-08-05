from flask import Flask
import getnerdy

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>How We\'ll Die Today</h1>' + getnerdy.get_asteroid()