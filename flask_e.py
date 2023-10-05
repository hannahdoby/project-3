# Import Flask and dependencies
from flask import Flask, jsonify, request
import requests

# Create App
app = Flask(__name__)

# Define Route to fetch Yelp data based on location
@app.route("/api/data", methods=["GET"])
def get_data():
    location = request.args.get("location")
    category = request.args.get("category")
    filename = f"{location}_{category}.json"
    url = f"https://api.yelp.com/v3/businesses/search?location={location}&categories=hotels&sort_by=best_match&limit=20"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer iYZnRBxpQmvIqH_Fc2NYor7h1BWUjfFLBk8-uj__-Hhkb8CZfTbmh3cNx4tNW17fxAhu4EFlQZkckYGMd5xPNm-4uTUD-HJ-FBRjupJTYYVEU9hnz4m9jA1fJ2ITZXYx"
    }

    try:
        uResponse = requests.get(url, headers=headers)
        data = uResponse.json()
        formatted_data = format_data_for_selected_location(data)
        return jsonify(formatted_data)
    except requests.ConnectionError:
        return jsonify({"error": "Connection Error"})

# Function to format Yelp data for display on the map
def format_data_for_selected_location(data):
    businesses = data.get("businesses", [])
    formatted_data = []
    for business in businesses:
        formatted_data.append({
            "key": business.get("name"),
            "id": business.get("id"),
            "address": business.get("location", {}).get("address1"),
            "review": business.get("rating"),
            "reviewCount": business.get("review_count"),
            "coordinates": [business.get("coordinates", {}).get("latitude"), business.get("coordinates", {}).get("longitude")]
        })
    return formatted_data

if __name__ == "__main__":
    app.run(debug=True)
