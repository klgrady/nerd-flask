from datetime import date
import requests


def get_asteroid():
    API_KEY="Lf0UXoet5H9GvAIma6BqtR0sBNU7uVbbA4JIqVnE"
    DATE = date.today()
    URL = "https://api.nasa.gov/neo/rest/v1/feed?start_date={DATE}&api_key={API_KEY}"
    resp = requests.get(URL)

    return resp.json()


def main():
    get_asteroid()


if __name__ == "__main__":
    main()