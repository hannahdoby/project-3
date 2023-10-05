document.addEventListener("DOMContentLoaded", function() {
  var locationSelector = document.getElementById("location-selector");
  var categorySelector = document.getElementById("category-selector");
  var map = L.map('map').setView([38, -97], 4);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
  var markers = L.layerGroup().addTo(map);

  function updateMap() {
    var selectedLocation = locationSelector.value;
    var selectedCategory = categorySelector.value;
    var fileName = selectedLocation.toLowerCase() + "_" + selectedCategory.toLowerCase() + ".json";

    d3.json(fileName, function(error, data) {
      if (error) {
        console.error("Error loading data:", error);
        return; // Exit the function early if there's an error
      }

      markers.clearLayers();

      if (data && data.length > 0) {
        data.forEach(function(d) {
          var marker = L.circleMarker([d.coordinates[0], d.coordinates[1]], {
            radius: 5,
            fillColor: "brown",
            color: "black",
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
          }).bindPopup(d.key + "<br>Address: " + d.address + "<br>Rating: " + d.review + "<br>Review Count: " + d.reviewCount);
          markers.addLayer(marker);
        });

        map.fitBounds(markers.getBounds());
      } else {
        console.log("No data available for the selected location and category.");
      }
    });
  }

  locationSelector.addEventListener("change", updateMap);
  categorySelector.addEventListener("change", updateMap);

  // Initial load of data for the default location and category
  updateMap();
});
