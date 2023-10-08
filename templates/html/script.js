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

  function updateMap() {
    var selectedLocation = locationSelector.value;
    var selectedCategory = categorySelector.value;
    var markerColor = categoryColors[selectedCategory];

    var apiUrl = 'http://localhost:5000/'; // Define API endpoint URL
    var fileName = selectedLocation.toLowerCase() + "_" + selectedCategory.toLowerCase() + ".json"; // Generate file name based on selected location and category

    map.setView(cityCoordinates[selectedLocation], 10);
    
    // Fetch data from the Flask API
    fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      markers.clearLayers();
      
      data.forEach(function(d) {
        var marker = L.circleMarker([d.coordinates[0], d.coordinates[1]], {
          radius: 5,
          fillColor: markerColor,
          color: "black",
          weight: 1,
          opacity: 1,
          fillOpacity: 0.8
        }).bindPopup(d.key + "<br>Address: " + d.address + "<br>Rating: " + d.review + "<br>Review Count: " + d.reviewCount);
        
        markers.addLayer(marker);
      });

      map.fitBounds(markers.getBounds());
    });
  }

  locationSelector.addEventListener("change", updateMap);
  categorySelector.addEventListener("change", updateMap);

  // Initial load of data for the default location and category
  updateMap();
});
