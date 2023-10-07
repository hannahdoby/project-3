// Store our API endpoint as queryUrl.
let queryUrl = "http://127.0.0.1:5000/";

// Perform a GET request to the query URL/
d3.json(queryUrl).then(function (data) {
  // Once we get a response, send the data.features object to the createFeatures function.
  console.log(data[0][0]);
});

// Set up dropdown menu
function init(){d3.json(queryUrl).then(function(data) {
  let dropdownMenu = d3.select("#selDataset");
  for (let j = 0; j < data.length; j++) {
    
      dropdownMenu.append("option").text(data[j][0].location.city).property("value", data[j][0].location.city)};
  
chart(data[0][0].location.city);
  
})}

function optionChanged(op){
  chart(op)
}
init();

function chart(cityID){d3.json(queryUrl).then(function (data){
  let cityData = data
  result = cityData.filter(cityID[0].location.city)
  console.log(result);
  //   let sample_values = result.sample_values
  //   let otu_ids = result.otu_ids
})}












