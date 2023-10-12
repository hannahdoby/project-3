document.addEventListener("DOMContentLoaded", function() {
const ctx1 = document.getElementById("location-selector");
const ctx2 = document.getElementById("category-selector");


  var apiUrl = 'http://localhost:5000/';

  async function fetchMarkerData(apiUrl) {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  }

  function createChart(data, ) {
    markers.clearCharts();
    for (let i=0; i < data.food.length; i++){
      let businesses = data.food[i].businesses;
      for (let j=0; j < businesses.length; j++){
        let location = businesses[j].coordinates
        let name = businesses[j].name
        let rating = businesses[j].rating
        let reviewCount = businesses[j].review_count
        let address= businesses[j].location.display_addresses
        new Chart(ctx1, {
            type: 'bar',
            data: {
              labels: [rating.slice(0,5).reverse().value],
              datasets: [{
                label: 'Hotels Ratings',
                data: [rating.slice(0,5).reverse()],
                borderWidth: 1
              }]
            },
            options: {
          
          
          
              scales: {
                y: {
                  beginAtZero: true
                }
              }
            }
          });
      }
    }
  }

  function updateChart() {
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
  updateChart();
});
