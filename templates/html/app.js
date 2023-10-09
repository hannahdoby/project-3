// Store our API endpoint as queryUrl.
let queryUrl = "http://127.0.0.1:5000/";

// Perform a GET request to the query URL/
d3.json(queryUrl).then(function (data) {
  // Once we get a response, send the data.features object to the createFeatures function.
  console.log(data);
});

// Set up dropdown menu
function init(){d3.json(queryUrl).then(function(data) {
  let dropdownMenu = d3.select("#selDataset");
  for (let j = 0; j < data.length; j++) {
         dropdownMenu.append("option").text(data[j][2].location.city).property("value", data[j][2].location.city)};
  
chart(data[0][0].location.city);
  
})}

function optionChanged(op){
  chart(op)
}
init();  

// Sort and select top 5 hotels
function chart(sort){d3.json(queryUrl).then(function (data){
  for (let i = 0; i < data[i].length; i++){
    let sortByRating = data[i].sort((a,b) => b.rating - a.rating);
    let sliceHotel = topFiveHotels.slice(0,5);
    
    // Set Trace to plot hotel sorted hotel data
    let trace = {
      x: sliceHotel.map(object => object.i.categories[0].title),
      y: sliceHotel.map(object => object.i.rating),
      text: sliceHotel.map(object => object.i.name),
      name: "Hotels",
      type: "bar",
      orientation: 'h',
    };

    // Data array for the trace
    let data = [trace];

    // Apply layout to trace 
    let layout = {
      title: "Hotel Ratings vs. Cities",
      l: 100,
      r: 100,
      t: 100,
      b: 100
    };
    
    Plotly.newPlot('plot',data,layout)
    

  }
  

})}












