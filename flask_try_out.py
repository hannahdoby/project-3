# Import Flask and dependencies
from flask import Flask,jsonify
import requests
import json
from jl_apiKey import api_key
from flask_cors import CORS

### Set up Flask ###
# Create App
app = Flask(__name__)
CORS(app)


# Define Route
@app.route("/")

# Call out url
def home():
    url = "https://api.yelp.com/v3/businesses/search?location=NYC&term=food&sort_by=best_match&limit=20"
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"}

    location= ['NYC']
    term = ["hotels"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=20", headers=headers)
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