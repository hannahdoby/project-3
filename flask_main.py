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

### Flask Routes ###
## Set up API route to host NYC data from Yelp API call
@app.route("/api/v1.0/nyc")
def nyc():
    url = "https://api.yelp.com/v3/businesses/search?location="
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    location= ['NYC']
    term = ["hotels","restaurants"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=20", headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    business_name =data['businesses']
    return business_name


## Set up API route for Los Angeles data from Yelp API call
@app.route("/api/v1.0/la")
def la():
    url = "https://api.yelp.com/v3/businesses/search?location="
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    location= ['LosAngeles']
    term = ["hotels","restaurants"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=20", headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    business_name =data['businesses']
    return business_name


## Set up API route for Phoenix data from Yelp API call
@app.route("/api/v1.0/phx")
def phx():
    url = "https://api.yelp.com/v3/businesses/search?location="
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    location= ['Phoenix']
    term = ["hotels","restaurants"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=20", headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    business_name =data['businesses']
    return business_name


## Set up API route for Chicago data from Yelp API call
@app.route("/api/v1.0/cho")
def cho():
    url = "https://api.yelp.com/v3/businesses/search?location="
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    location= ['Chicago']
    term = ["hotels","restaurants"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=20", headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    business_name =data['businesses']
    return business_name

## Set up API route for San Antonio data from Yelp API call
@app.route("/api/v1.0/santo")
def santo():
    url = "https://api.yelp.com/v3/businesses/search?location="
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    location= ['SanAntonio']
    term = ["hotels","restaurants"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=20", headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    business_name =data['businesses']
    return business_name

## Set up API route for San Diego data from Yelp API call
@app.route("/api/v1.0/sandi")
def sandi():
    url = "https://api.yelp.com/v3/businesses/search?location="
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    location= ['San Diego']
    term = ["hotels","restaurants"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=20", headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    business_name =data['businesses']
    return business_name

## Set up API route for Dalas data from Yelp API call
@app.route("/api/v1.0/dalla")
def dalla():
    url = "https://api.yelp.com/v3/businesses/search?location="
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    location= ['Dallas']
    term = ["hotels","restaurants"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=20", headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    business_name =data['businesses']
    return business_name

## Set up API route for Philadelphia data from Yelp API call
@app.route("/api/v1.0/phila")
def phila():
    url = "https://api.yelp.com/v3/businesses/search?location="
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    location= ['Philadelphia']
    term = ["hotels","restaurants"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=20", headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    business_name =data['businesses']
    return business_name

## Set up API route for Houston data from Yelp API call
@app.route("/api/v1.0/houston")
def houston():
    url = "https://api.yelp.com/v3/businesses/search?location="
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    location= ['Houston']
    term = ["hotels","restaurants"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=20", headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    business_name =data['businesses']
    return business_name


## Set up API route for Austin data from Yelp API call
@app.route("/api/v1.0/austin")
def austin():
    url = "https://api.yelp.com/v3/businesses/search?location="
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    location= ['Austin']
    term = ["hotels","restaurants"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=20", headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    business_name =data['businesses']
    return business_name


### This is the home and the primary route hosting all the data from each API call
@app.route('/')
def home():
    return [nyc(),la(),phx(),cho(),santo(),sandi(),dalla(),phila(),houston(),austin()]

if __name__ == "__main__":
    app.run(debug = True)
