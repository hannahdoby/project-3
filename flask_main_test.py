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
## Set up API route to host NYC hotels data from Yelp API call
@app.route("/api/v1.0/nyc_h")
def nyc_h():
    url = "https://api.yelp.com/v3/businesses/search?location="
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    location= ['NYC']
    term = ["hotels"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    business_name =data['businesses']
    return business_name


## Set up API route to host NYC food data from Yelp API call
@app.route("/api/v1.0/nyc_f")
def nyc_f():
    url = "https://api.yelp.com/v3/businesses/search?location="
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    location= ['NYC']
    term = ["food"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    business_name =data['businesses']
    return business_name



## Set up API route for Los Angeles hotel data from Yelp API call
@app.route("/api/v1.0/la_h")
def la_h():
    url = "https://api.yelp.com/v3/businesses/search?location="
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    location= ['LosAngeles']
    term = ["hotels"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    business_name =data['businesses']
    return business_name


## Set up API route for Los Angeles food data from Yelp API call
@app.route("/api/v1.0/la_f")
def la_f():
    url = "https://api.yelp.com/v3/businesses/search?location="
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    location= ['LosAngeles']
    term = ["food"]

    try: 
        uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    business_name =data['businesses']
    return business_name


# ## Set up API route for Phoenix hotel data from Yelp API call
# @app.route("/api/v1.0/phx_h")
# def phx_h():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['Phoenix']
#     term = ["hotels"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name


# ## Set up API route for Phoenix food data from Yelp API call
# @app.route("/api/v1.0/phx_f")
# def phx_f():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['Phoenix']
#     term = ["food"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name


# ## Set up API route for Chicago hotel data from Yelp API call
# @app.route("/api/v1.0/cho_h")
# def cho_h():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['Chicago']
#     term = ["hotels"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name

# ## Set up API route for Chicago food data from Yelp API call
# @app.route("/api/v1.0/cho_f")
# def cho_f():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['Chicago']
#     term = ["food"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name


# ## Set up API route for San Antonio hotel data from Yelp API call
# @app.route("/api/v1.0/santo_h")
# def santo_h():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['SanAntonio']
#     term = ["hotels"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name


# ## Set up API route for San Antonio food data from Yelp API call
# @app.route("/api/v1.0/santo_f")
# def santo_f():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['SanAntonio']
#     term = ["food"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name


# ## Set up API route for San Diego hotel data from Yelp API call
# @app.route("/api/v1.0/sandi_h")
# def sandi_h():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['San Diego']
#     term = ["hotel"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name

# ## Set up API route for San Diego food data from Yelp API call
# @app.route("/api/v1.0/sandi_f")
# def sandi_f():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['San Diego']
#     term = ["food"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name


# ## Set up API route for Dalas hotel data from Yelp API call
# @app.route("/api/v1.0/dalla_h")
# def dalla_h():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['Dallas']
#     term = ["hotels"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name


# ## Set up API route for Dalas food data from Yelp API call
# @app.route("/api/v1.0/dalla_f")
# def dalla_f():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['Dallas']
#     term = ["food"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name


# ## Set up API route for Philadelphia hotel data from Yelp API call
# @app.route("/api/v1.0/phila_h")
# def phila_h():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['Philadelphia']
#     term = ["hotels"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name


# ## Set up API route for Philadelphia food data from Yelp API call
# @app.route("/api/v1.0/phila_f")
# def phila_f():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['Philadelphia']
#     term = ["food"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name


# ## Set up API route for Houston hotel data from Yelp API call
# @app.route("/api/v1.0/houston_h")
# def houston_h():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['Houston']
#     term = ["hotels"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name


# ## Set up API route for Houston food data from Yelp API call
# @app.route("/api/v1.0/houston_f")
# def houston_f():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['Houston']
#     term = ["food"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name


# ## Set up API route for Austin hotel data from Yelp API call
# @app.route("/api/v1.0/austin_h")
# def austin_h():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['Austin']
#     term = ["hotels"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name


# ## Set up API route for Austin food data from Yelp API call
# @app.route("/api/v1.0/austin_f")
# def austin_f():
#     url = "https://api.yelp.com/v3/businesses/search?location="
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }
#     location= ['Austin']
#     term = ["food"]

#     try: 
#         uResponse = requests.get(f"{url}{location}&term={term}&sort_by=best_match&limit=15", headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     Jresponse = uResponse.text
#     data = json.loads(Jresponse)
#     business_name =data['businesses']
#     return business_name

### This is the home and the primary route hosting all the data from each API call
@app.route('/')
def hotel():
    return [nyc_h(),la_h()]

@app.route('/food')
def food():
    return [nyc_f(),la_f()]

if __name__ == "__main__":
    app.run(debug = True)
