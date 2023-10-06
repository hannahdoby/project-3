// Store our API endpoint as queryUrl.
let queryUrl = "http://127.0.0.1:5000/";

// Perform a GET request to the query URL/
d3.json(queryUrl).then(function (data) {
  // Once we get a response, send the data.features object to the createFeatures function.
  console.log(data);
});

