// Set up first chart
const ctx1 = document.getElementById('myChart1');
      
        new Chart(ctx1, {
          type: 'bar',
          data: {
            labels: ['New York City', 'Los Angeles', 'Phoenix', 'Chicago', 'San Antonio', 'San Diego', 'Dallas', 'Philadelphia' , 'Houston' ,'Austin'],
            datasets: [{
              label: 'Hotels Ratings',
              data: [12, 19, 3, 5, 2, 3],
              borderWidth: 1
            }]
          },
          options: {
            maintainAspectRatio :false,
            responsive : true,
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
              data: [12, 19, 3, 5, 2, 3],
              borderWidth: 1
            }]
          },
          options: {
            maintainAspectRatio : false ,
            responsive: true,
            scales: {
              y: {
                beginAtZero: true
              }
            }
          }
        });