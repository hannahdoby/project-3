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
    LosAngeles_food = json.load(open('JSON/LosAngeles_food.json'))
    LosAngeles_hotels = json.load(open('JSON/LosAngeles_hotels.json'))
    NYC_food = json.load(open('JSON/NYC_food.json'))
    NYC_hotels = json.load(open('JSON/NYC_hotels.json'))
    Chicago_food = json.load(open('JSON/Chicago_food.json'))
    Chicago_hotels = json.load(open('JSON/Chicago_hotels.json'))
    SanAntonio_food = json.load(open('JSON/SanAntonio_food.json'))
    SanAntonio_hotels = json.load(open('JSON/SanAntonio_hotels.json'))
    SanDiego_food = json.load(open('JSON/SanDiego_food.json'))
    SanDiego_hotels = json.load(open('JSON/SanDiego_hotels.json'))
    Dallas_food = json.load(open('JSON/Dallas_food.json'))
    Dallas_hotels = json.load(open('JSON/Dallas_hotels.json'))
    Austin_food = json.load(open('JSON/Austin_food.json'))
    Austin_hotels = json.load(open('JSON/Austin_hotels.json'))
    Phoenix_food = json.load(open('JSON/Phoenix_food.json'))
    Phoenix_hotels = json.load(open('JSON/Phoenix_hotels.json'))
    Philadelphia_food = json.load(open('JSON/Philadelphia_food.json'))
    Philadelphia_hotels = json.load(open('JSON/Philadelphia_hotels.json'))
    Houston_food = json.load(open('JSON/Houston_food.json'))
    Houston_hotels = json.load(open('JSON/Houston_hotels.json'))

    return jsonify({
        "LosAngeles_food": LosAngeles_food,
        "LosAngeles_hotels": LosAngeles_hotels,
        "NYC_food": NYC_food,
        "NYC_hotels": NYC_hotels,
        "Chicago_food": Chicago_food,
        "Chicago_hotels": Chicago_hotels,
        "SanAntonio_food": SanAntonio_food,
        "SanAntonio_hotels": SanAntonio_hotels,
        "SanDiego_food": SanDiego_food,
        "SanDiego_hotels": SanDiego_hotels,
        "Dallas_hotels": Dallas_hotels,
        "Dallas_food": Dallas_food,
        "Austin_food": Austin_food,
        "Austin_hotels": Austin_hotels,
        "Phoenix_food": Phoenix_food,
        "Phoenix_hotels": Phoenix_hotels,
        "Philadelphia_food": Philadelphia_food,
        "Philadelphia_hotels": Philadelphia_hotels,
        "Houston_food": Houston_food,
        "Houston_hotels": Houston_hotels
    })

if __name__ == '__main__':
    app.run(debug=True)
