document.addEventListener("DOMContentLoaded", function() {
    var locationSelector = document.getElementById("location-selector");
    var map = new google.maps.Map(d3.select("#map").node(), {
      zoom: 4,
      center: new google.maps.LatLng(38, 97),
      mapTypeId: google.maps.MapTypeId.TERRAIN
    });
  
    function loadData(selectedLocation) {
      d3.json(selectedLocation, function(error, data) {
        if (error) throw error;
  
        var overlay = new google.maps.OverlayView();
        overlay.onAdd = function() {
          var layer = d3.select(this.getPanes().overlayLayer).append("div")
              .attr("class", "stations");
  
          overlay.draw = function() {
            var projection = this.getProjection(),
                padding = 10;
  
            var marker = layer.selectAll("svg")
                .data(d3.entries(data))
                .each(transform)
              .enter().append("svg")
                .each(transform)
                .attr("class", "marker");
  
            marker.append("circle")
                .attr("r", 4.5)
                .attr("cx", padding)
                .attr("cy", padding);
  
            marker.append("text")
                .attr("x", padding + 7)
                .attr("y", padding)
                .attr("dy", ".31em")
                .text(function(d) { return d.key; });
  
            function transform(d) {
              d = new google.maps.LatLng(d.value[1], d.value[0]);
              d = projection.fromLatLngToDivPixel(d);
              return d3.select(this)
                  .style("left", (d.x - padding) + "px")
                  .style("top", (d.y - padding) + "px");
            }
          };
        };
        overlay.setMap(map);
      });
    }
  
    locationSelector.addEventListener("change", function() {
      var selectedLocation = locationSelector.value;
      loadData(selectedLocation);
    });
  
    // Initial load of data for the default location (stations.json)
    loadData("stations.json");
  });
  