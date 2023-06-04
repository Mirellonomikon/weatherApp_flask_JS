function fetchLocation() {
    var location = document.getElementById("search_bar").value;
    localStorage.setItem("location", location);

    fetch('/get_location_key', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ location: location }),
    })
    .then(response => response.json())
    .then(data => {
        localStorage.setItem("location_key", data.location_key);
        fetchWeatherDataCurrent();
        fetchWeatherData5Day();
        fetchWeatherData12Hour();

        // Show the weather tabs after fetching data
        document.getElementById("weather_tabs").style.display = "block";
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Attach fetchLocation function to the search button's click event
document.getElementById("search_button").addEventListener("click", fetchLocation);
