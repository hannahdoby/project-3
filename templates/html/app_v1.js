// Perform url call to local host
let url = 'http://localhost:5000/';

// d3 json read data from localhost
d3.json(url).then(function(data){

// Set up first chart
const ctx1 = document.getElementById("category-selector");
      
        new Chart(ctx1, {
          type: 'bar',
          data: {
            labels: [cityCoordinates.key],
            datasets: [{
              label: 'Hotels Ratings',
              data: [5,4,4.5,4,4,4,4,4,4,4,4],
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

    const ctx2 = document.getElementById('myChart2');
      
        new Chart(ctx2, {
          type: 'line',
          data: {
            labels: ['New York City', 'Los Angeles', 'Phoenix', 'Chicago', 'San Antonio', 'San Diego', 'Dallas', 'Philadelphia' , 'Houston' ,'Austin'],
            datasets: [{
              label: 'Foods Ratings',
              data: [5,4,4.5,4,4,4,4,4,4,4,4],
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

})
    