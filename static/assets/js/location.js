// This function will be called when the search button is clicked
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
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Attach fetchLocation function to the search button's click event
document.getElementById("search_button").addEventListener("click", fetchLocation);
