document.addEventListener("DOMContentLoaded", function() {
  var locationSelector = document.getElementById("location-selector");
  var categorySelector = document.getElementById("category-selector");
  var map = L.map('map').setView([38, -97], 4);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
  var markers = L.layerGroup().addTo(map);

  // Coordinates of cities
  var cityCoordinates = {
    "Dallas": [32.7767, -96.7970],
    "SanAntonio": [29.4241, -98.4936],
    "SanDiego": [32.7157, -117.1611],
    "Chicago": [41.8781, -87.6298],
    "LosAngeles": [34.0522, -118.2437],
    "NewYorkCity": [40.7128, -74.0060],
    "Phoenix": [33.4484, -112.0740],
    "Austin": [30.2500, -97.7500],
    "Houston": [29.7604, -95.3698],
    "Philadelphia": [39.9526, -75.1652]
  };

  // Map category names to marker colors
  var categoryColors = {
    "Hotels": "brown",
    "Food": "green"
  };

  var apiUrl = 'http://localhost:5000/';

  async function fetchMarkerData(apiUrl) {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  }

  function createMarkers(data, markerColor) {
    markers.clearLayers();
    for (let i=0; i < data.food.length; i++){
      let businesses = data.food[i].businesses;
      for (let j=0; j < businesses.length; j++){
        let location = businesses[j].coordinates
        let name = businesses[j].name
        let rating = businesses[j].rating
        let reviewCount = businesses[j].review_count
        let address= businesses[j].location.display_addresses
        if (location) {
          let marker = L.circleMarker([location.latitude, location.longitude],{
            radius: 5,
          fillColor: markerColor,
          // markerColor: "black",
           weight: 1,
           opacity: 1,
          fillOpacity: 0.8
          }).bindPopup(name+"<br>Address: " + address + "<br>Rating: " + rating + "<br>Review Count: " + reviewCount);
          markers.addLayer(marker);

        }
      }
    }

    for (let i=0; i < data.hotels.length; i++){
      let businessesHotels = data.hotels[i].businesses;
      for (let j=0; j < businessesHotels.length; j++){
        let locationHotels = businessesHotels[j].coordinates
        let nameHotels = businessesHotels[j].name
        let ratingHotels = businessesHotels[j].rating
        let reviewCountHotels = businessesHotels[j].review_count
        let addressHotels= businessesHotels[j].location.display_addresses
        if (locationHotels) {
          let markerHotels = L.circleMarker([locationHotels.latitude, locationHotels.longitude],{
            radius: 5,
          fillColor: markerColor,
          // markerColor: "black",
           weight: 1,
           opacity: 1,
          fillOpacity: 0.8
          }).bindPopup(nameHotels+"<br>Address: " + addressHotels + "<br>Rating: " + ratingHotels + "<br>Review Count: " + reviewCountHotels);
          markers.addLayer(markerHotels);

        }
      }
    }


  }

  function updateMap() {
    var selectedLocation = locationSelector.value;
    var selectedCategory = categorySelector.value;
    var markerColor = categoryColors[selectedCategory];

    map.setView(cityCoordinates[selectedLocation], 10);
    
    // Fetch data from the Flask API
    fetchMarkerData(apiUrl)
    .then(data => {
      createMarkers(data, markerColor);
    })
    .catch(error => {
      console.error('Error fetching marker data:', error);
    });
  }

  locationSelector.addEventListener("change", updateMap);
  categorySelector.addEventListener("change", updateMap);

  // Initial load of data for the default location and category
  updateMap();
});
