# Import Flask and dependencies
from flask import Flask,jsonify
import requests
import json
from jl_apiKey import api_key
from flask_cors import CORS

# Create App
app = Flask(__name__)
CORS(app)
# app.run(threaded=True)


# Define Route
@app.route("/")
# def index_js():
#     render_template("/js/index.js")

# Call out url
def hotels():
    urlHotels = "https://api.yelp.com/v3/businesses/search?location=NYC&categories=foods%2Chotels&sort_by=best_match&limit=10"
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_key}"
    }
    # params = {'categories':'hotels',
    #           'categories':'foods',
    #           'location':'NYC',
    #           'limit':20}

    try: 
        responseHotels = requests.get(urlHotels, headers=headers)
    except requests.ConnectionError:
        return "Connection Error"
    JresponseHotels = responseHotels.text
    dataHotels = json.loads(JresponseHotels)
    
    return dataHotels

# def foods():
#     urlFoods = "https://api.yelp.com/v3/businesses/search?location=NYC&categories=foods&sort_by=best_match&limit=20"
#     headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {api_key}"
#     }

#     try: 
#         responseFoods = requests.get(urlFoods, headers=headers)
#     except requests.ConnectionError:
#         return "Connection Error"
#     JresponseFoods = responseFoods.text
#     dataFoods = json.loads(JresponseFoods)
    
#     return dataFoods


if __name__ == "__main__":
    app.run(debug = True)

