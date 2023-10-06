# Import Flask and dependencies
from flask import Flask,jsonify, render_template
import requests
import json
from jl_apiKey import api_key
from flask_cors import CORS

# Create App
app = Flask(__name__)
CORS(app)

# Define Route
@app.route("/")
# def index_js():
#     render_template("/js/index.js")

# Call out url
def home():
    url = "https://api.yelp.com/v3/businesses/search?location=NYC&categories=hotels&sort_by=best_match&limit=20"
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    try: 
        uResponse = requests.get(url, headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    
    # # This is to display name
    # displayName = data['businesses'][0]['id']

    # # the reputation 
    # businessName = data['businesses'][0]['name']

    return data

if __name__ == "__main__":
    app.run(debug = True)