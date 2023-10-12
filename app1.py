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
    LosAngeles_Food = json.load(open('JSON/LosAngeles_food.json'))
    LosAngeles_Hotels = json.load(open('JSON/LosAngeles_hotels.json'))
    NewYorkCity_Food = json.load(open('JSON/NYC_food.json'))
    NewYorkCity_Hotels = json.load(open('JSON/NYC_hotels.json'))
    Chicago_Food = json.load(open('JSON/Chicago_food.json'))
    Chicago_Hotels = json.load(open('JSON/Chicago_hotels.json'))
    SanAntonio_Food = json.load(open('JSON/SanAntonio_food.json'))
    SanAntonio_Hotels = json.load(open('JSON/SanAntonio_hotels.json'))
    SanDiego_Food = json.load(open('JSON/SanDiego_food.json'))
    SanDiego_Hotels = json.load(open('JSON/SanDiego_hotels.json'))
    Dallas_Food = json.load(open('JSON/Dallas_food.json'))
    Dallas_Hotels = json.load(open('JSON/Dallas_hotels.json'))
    Austin_Food = json.load(open('JSON/Austin_food.json'))
    Austin_Hotels = json.load(open('JSON/Austin_hotels.json'))
    Phoenix_Food = json.load(open('JSON/Phoenix_food.json'))
    Phoenix_Hotels = json.load(open('JSON/Phoenix_hotels.json'))
    Philadelphia_Food = json.load(open('JSON/Philadelphia_food.json'))
    Philadelphia_Hotels = json.load(open('JSON/Philadelphia_hotels.json'))
    Houston_Food = json.load(open('JSON/Houston_food.json'))
    Houston_Hotels = json.load(open('JSON/Houston_hotels.json'))

    return jsonify({
        'food':[LosAngeles_Food,NewYorkCity_Food,Chicago_Food,SanAntonio_Food,SanDiego_Food,Dallas_Food,Austin_Food,Phoenix_Food,Philadelphia_Food,Houston_Food],
        'hotels':[LosAngeles_Hotels, NewYorkCity_Hotels, Chicago_Hotels,SanAntonio_Hotels,SanDiego_Hotels,Dallas_Hotels,Austin_Hotels,Phoenix_Hotels,Philadelphia_Hotels,Houston_Hotels]
    })



if __name__ == '__main__':
    app.run(debug=True)
