// This function will be called when the search button is clicked
function fetchLocation() {
    // Fetch the location from the search bar
    var location = document.getElementById("search_bar").value;

    // Save the location in localStorage to be used by other scripts
    localStorage.setItem("location", location);

    // Fetch the new weather data
    fetchWeatherDataCurrent();
}

// Attach fetchLocation function to the search button's click event
document.getElementById("search_button").addEventListener("click", fetchLocation);
