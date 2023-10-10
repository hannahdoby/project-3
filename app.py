# Import Flask and dependencies
from flask import Flask, jsonify
import json
from flask_cors import CORS

### Set up Flask ###
# Create App
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    la_food = json.load(open('JSON/LosAngeles_food.json'))
    la_hotels = json.load(open('JSON/LosAngeles_hotels.json'))
    nyc_food = json.load(open('JSON/NYC_food.json'))
    nyc_hotels = json.load(open('JSON/NYC_hotels.json'))
    cho_food = json.load(open('JSON/Chicago_food.json'))
    cho_hotels = json.load(open('JSON/Chicago_hotels.json'))
    santo_food = json.load(open('JSON/SanAntonio_food.json'))
    santo_hotels = json.load(open('JSON/SanAntonio_hotels.json'))
    sandi_food = json.load(open('JSON/SanDiego_food.json'))
    sandi_hotels = json.load(open('JSON/SanDiego_hotels.json'))
    dalla_food = json.load(open('JSON/Dallas_food.json'))
    dalla_hotels = json.load(open('JSON/Dallas_hotels.json'))
    austin_food = json.load(open('JSON/Austin_food.json'))
    austin_hotels = json.load(open('JSON/Austin_hotels.json'))
    phx_food = json.load(open('JSON/Phoenix_food.json'))
    phx_hotels = json.load(open('JSON/Phoenix_hotels.json'))
    phila_food = json.load(open('JSON/Philadelphia_food.json'))
    phila_hotels = json.load(open('JSON/Philadelphia_hotels.json'))
    houston_food = json.load(open('JSON/Houston_food.json'))
    houston_hotels = json.load(open('JSON/Houston_hotels.json'))

    return jsonify({
        "la_food": la_food,
        "la_hotels": la_hotels,
        "nyc_food": nyc_food,
        "nyc_hotels": nyc_hotels,
        "cho_food": cho_food,
        "cho_hotels": cho_hotels,
        "santo_food": santo_food,
        "santo_hotels": santo_hotels,
        "sandi_food": sandi_food,
        "sandi_hotels": sandi_hotels,
        "dalla_food": dalla_food,
        "dalla_hotels": dalla_hotels,
        "austin_food": austin_food,
        "austin_hotels": austin_hotels,
        "phx_food": phx_food,
        "phx_hotels": phx_hotels,
        "phila_food": phila_food,
        "phila_hotels": phila_hotels,
        "houston_food": houston_food,
        "houston_hotels": houston_hotels
    })

if __name__ == '__main__':
    app.run(debug=True)
