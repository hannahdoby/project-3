# Import Flask and dependencies
from flask import Flask,jsonify
import requests
import json

# Create App
app = Flask(__name__)

# Define Route
@app.route("/")

# Call out url
def home():
    url = "https://api.yelp.com/v3/businesses/search?location=NYC&categories=hotels&sort_by=best_match&limit=20"
    headers = {
    "accept": "application/json",
    "Authorization": "Bearer CHjD6kmFOME90In-E5XCPX4j-bRFI8XTrhXpC4mSkiUPM5rEYHz0Ny_NDkuBFvliTm2yaGMLW-h4NUsjLtyakj8wgZMT48_vJQP8_RccUQ3jgR2mt6pUW9QwYmQTZXYx"}

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

    return Jresponse

if __name__ == "__main__":
    app.run(debug = True)