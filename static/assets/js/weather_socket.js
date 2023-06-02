var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
socket.on('connect', function() {
    console.log('Connected to server');
});

socket.on('new-weather', function(msg) {
  // update HTML elements with new data
  document.getElementById("weather_location").textContent = msg.data["Location"];
  document.getElementById("temp_cur").textContent = msg.data["Temperature"] + "°C";
  document.getElementById("weather_description").textContent = msg.data["Weather Description"];
  document.getElementById("feels_like").textContent = "Feels like " + msg.data["Feels Like"] + "°C";
  document.getElementById("rain_probability").textContent = "Rain: " + msg.data["Rain Probability"] + "%";
  document.getElementById("wind_speed").textContent = "Wind speed: " + msg.data["Wind Speed"] + " km/h";
  document.getElementById("wind_direction").textContent = "Wind direction: " + msg.data["Wind Direction"];
  document.getElementById("uv").textContent = "UV: " + msg.data["UV Index"];
  // add more as needed
});