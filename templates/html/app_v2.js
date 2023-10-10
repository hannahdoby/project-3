// Store our API endpoint as queryUrl.
let queryUrl = "http://127.0.0.1:5000/";

// Perform a GET request to the query URL/
d3.json(queryUrl).then(function (data) {
  // Once we get a response, send the data.features object to the createFeatures function.
  console.log(data);
  let names = data[0].map(function (row){

  }

  )
});




// Initializes the page with a default plot
function init(){d3.json(queryUrl).then(function(data){

  // Plot initital plot 
  let data1 = {
    x: data[0]
    y:
    type:'bar'

  };
  let data2 ={
    x:
    y:
    type:'bar'
  }

     Plotly.newPlot('myChart1', data1);
     Plotly.newPlot('myChart2', data2)
})}
  // Call updatePlotly() when a change takes place to the DOM
  d3.selectAll("#location-selector").on("change", updatePlot);

  function updatePlot(){d3.json(queryUrl).then(function(data){
  let dropdownCity = d3.select('#location-selector');
  let dataset = dropdownCity.property('value')

    // Initialize x and y arrays
    let x = [];
    let y = [];

    if (dataset === 'Dallas') {
      x = [1, 2, 3, 4, 5];
      y = [a,b,c,d,e],
      type: 'bar'
    }

    else if (dataset === 'SanAntonio') {
      x = [10, 20, 30, 40, 50];
      y = [1, 10, 100, 1000, 10000];
    }

    else if (dataset === 'SanDiego') {
      x = [10, 20, 30, 40, 50];
      y = [1, 10, 100, 1000, 10000];
    }

    else if (dataset === 'LosAngeles') {
      x = [10, 20, 30, 40, 50];
      y = [1, 10, 100, 1000, 10000];
    }

    else if (dataset === 'Chicago') {
      x = [10, 20, 30, 40, 50];
      y = [1, 10, 100, 1000, 10000];
    }

    else if (dataset === 'NewYorkCity') {
      x = [10, 20, 30, 40, 50];
      y = [1, 10, 100, 1000, 10000];
    }

    else if (dataset === 'Phoenix') {
      x = [10, 20, 30, 40, 50];
      y = [1, 10, 100, 1000, 10000];
    }

    else if (dataset === 'Philadelphia') {
      x = [10, 20, 30, 40, 50];
      y = [1, 10, 100, 1000, 10000];
    }

    else if (dataset === 'Houston') {
      x = [10, 20, 30, 40, 50];
      y = [1, 10, 100, 1000, 10000];
    }

    else if (dataset === 'Austin') {
      x = [10, 20, 30, 40, 50];
      y = [1, 10, 100, 1000, 10000];
    }
}
  
  )
}

init();
