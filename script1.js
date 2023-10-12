document.addEventListener("DOMContentLoaded", function() {
  const locationSelector = document.getElementById("location-selector");
  const categorySelector = document.getElementById("category-selector");
  const map = L.map('map').setView([38, -97], 4);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
  const markers = L.layerGroup().addTo(map);

  // Coordinates of cities
  const cityCoordinates = {
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
  const categoryColors = {
    "Hotels": "brown",
    "Food": "green"
  };

  const apiUrl = 'http://localhost:5000/';

  const fetchMarkerData = async (apiUrl) => {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  };

  const createDropdownOptions = (data, selector) => {
    const options = selector.options;
    options.length = 0;
  
    if (selector.id === "category-selector") {
      for (const category of Object.keys(categoryColors)) {
        const option = document.createElement("option");
        option.value = category;
        option.text = category;
        options.add(option);
      }
    } else if (selector.id === "location-selector") {
      const locations = selector.value === "All" ? Object.keys(cityCoordinates) : [selector.value];
      for (const location of locations) {
        const option = document.createElement("option");
        option.value = location;
        option.text = location;
        options.add(option);
      }
    } else if (selector.id === "food-selector") {
      for (const { category } of data.food) {
        const option = document.createElement("option");
        option.value = category;
        option.text = category;
        options.add(option);
      }
    } else if (selector.id === "hotels-selector") {
      for (const { category } of data.hotels) {
        const option = document.createElement("option");
        option.value = category;
        option.text = category;
        options.add(option);
      }
    }
  };

  function updateMap() {
    const selectedLocation = locationSelector.value;
    const selectedCategory = categorySelector.value;
    const markerColor = categoryColors[selectedCategory];
  
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

  const createMarkers = (data, markerColor) => {
    markers.clearLayers();
    for (const { businesses } of data.food){
      for (const { coordinates, name, rating, review_count, location: { display_addresses } } of businesses){
        if (coordinates) {
          const marker = L.circleMarker([coordinates.latitude, coordinates.longitude],{
            radius: 5,
            fillColor: markerColor,
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
          }).bindPopup(`${name}<br>Address: ${display_addresses}<br>Rating: ${rating}<br>Review Count: ${review_count}`);
          markers.addLayer(marker);
        }
      }
    }

    for (const { businesses } of data.hotels){
      for (const { coordinates, name, rating, review_count, location: { display_addresses } } of businesses){
        if (coordinates) {
          const marker = L.circleMarker([coordinates.latitude, coordinates.longitude],{
            radius: 5,
            fillColor: markerColor,
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
          }).bindPopup(`${name}<br>Address: ${display_addresses}<br>Rating: ${rating}<br>Review Count: ${review_count}`);
          markers.addLayer(marker);
        }
      }
    }
  };

  locationSelector.addEventListener("change", () => updateMap());
  categorySelector.addEventListener("change", () => updateMap());

  const updateMap = () => {
    const selectedLocation = locationSelector.value;
    const selectedCategory = categorySelector.value;
    const markerColor = categoryColors[selectedCategory];

    map.setView(cityCoordinates[selectedLocation], 10);

    const updateDropdowns = (data) => {
      createDropdownOptions(data, locationSelector);
      createDropdownOptions(data, categorySelector);
      createDropdownOptions(data, foodSelector);
      createDropdownOptions(data, hotelsSelector);
    };

    // Fetch data from the Flask API
    fetchMarkerData(apiUrl)
    .then(data => {
      createMarkers(data, markerColor);
    })
    .catch(error => {
      console.error('Error fetching marker data:', error);
    });
  };

  // Initial load of data for the default location and category
  updateMap();
});



const locationSelector = document.getElementById("location-selector");
const categorySelector = document.getElementById("category-selector");
const map = L.map('map').setView([38, -97], 4);
const markers = L.layerGroup().addTo(map);

// Coordinates of cities
const cityCoordinates = {
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
const categoryColors = {
  "Hotels": "brown",
  "Food": "green"
};

const apiUrl = 'http://localhost:5000/';

const fetchMarkerData = async (apiUrl) => {
  const response = await fetch(apiUrl);
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
};

const createMarkers = (data, markerColor) => {
  markers.clearLayers();
  for (const { businesses } of data.food){
    for (const { coordinates, name, rating, review_count, location: { display_addresses } } of businesses){
      if (coordinates) {
        const marker = L.circleMarker([coordinates.latitude, coordinates.longitude],{
          radius: 5,
          fillColor: markerColor,
          weight: 1,
          opacity: 1,
          fillOpacity: 0.8
        }).bindPopup(`${name}<br>Address: ${display_addresses}<br>Rating: ${rating}<br>Review Count: ${review_count}`);
        markers.addLayer(marker);
      }
    }
  }

  for (const { businesses } of data.hotels){
    for (const { coordinates, name, rating, review_count, location: { display_addresses } } of businesses){
      if (coordinates) {
        const marker = L.circleMarker([coordinates.latitude, coordinates.longitude],{
          radius: 5,
          fillColor: markerColor,
          weight: 1,
          opacity: 1,
          fillOpacity: 0.8
        }).bindPopup(`${name}<br>Address: ${display_addresses}<br>Rating: ${rating}<br>Review Count: ${review_count}`);
        markers.addLayer(marker);
      }
    }
  }
};

locationSelector.addEventListener("change", updateMap);
categorySelector.addEventListener("change", updateMap);

// Initial load of data for the default location and category
updateMap();

async function updateChart() {
  const selectedCategory = categorySelector.value;
  try {
    const data = await fetchCityData(selectedCategory);
    const cityRatings = {};
    for (const business of data.businesses) {
      const city = business.location.city;
      const rating = business.rating;
      if (cityRatings[city] === undefined) {
        cityRatings[city] = [rating];
      } else {
        cityRatings[city].push(rating);
      }
    }
    const cityAverages = {};
    for (const city in cityRatings) {
      const ratings = cityRatings[city];
      const average = ratings.reduce((a, b) => a + b, 0) / ratings.length;
      cityAverages[city] = average;
    }
    createBarChart(Object.entries(cityAverages));
  } catch (error) {
    console.error('Error fetching city data:', error);
  }
}