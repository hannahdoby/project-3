// Make Ajax request
$.ajax({
    url: {{ url_for('endpoint_to_resource') }},
    method: "GET",
    success: call_back()
  })