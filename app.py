from flask import Flask, render_template, jsonify, request
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

FRED_API_KEY = os.getenv("FRED_API_KEY")

SERIES = {
    "Median Home Price": "MSPUS",
    "30-Year Mortgage Rate": "MORTGAGE30US",
    "Housing Starts": "HOUST",
    "Home Ownership Rate": "RHORUSQ156N"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fetch-data")
def fetch_data():
    series_id = request.args.get("series_id")
    start = request.args.get("start", "2000-01-01")
    end = request.args.get("end", "2099-01-01")
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "sort_order": "desc",
        "observation_start": start,
        "observation_end": end
    }
    response = requests.get(url, params=params)
    data = response.json()
    observations = data.get("observations", [])
    return jsonify(observations)

@app.route("/get-series")
def get_series():
    return jsonify(SERIES)

if __name__ == "__main__":
    app.run(debug=True)