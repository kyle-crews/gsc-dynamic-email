<script>
function getAPIData() {
  // Get the API data.
  var data = {
    // Your API request parameters here.
  };

  // Make the API request.
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/api/v1/data", true);
  xhr.send(JSON.stringify(data));

  // Handle the response.
  xhr.onload = function() {
    if (xhr.status === 200) {
      var responseData = JSON.parse(xhr.responseText);

      // Update the text box with the dynamic data.
      document.getElementById("dynamic-data").innerHTML = responseData.data;
    } else {
      console.log("Error fetching API data: " + xhr.status);
    }
  };
}
</script>
