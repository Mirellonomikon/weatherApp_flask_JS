function fetchWeatherDataCurrent() {
    let location = localStorage.getItem('location');
    let locationKey = localStorage.getItem('location_key');


    if (location && locationKey) {
        fetch('/update_current_weather', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                location: location,
                location_key: locationKey
            })
        })
        .then(response => response.json())
        .then(data => {
            // Update the fields in your HTML here
            document.getElementById('weather_location').textContent = data['Location'];
            document.getElementById('temp_cur').textContent = data['Temperature'] + "°C";
            document.getElementById('weather_description').textContent = data['Weather Description'];
            document.getElementById('feels_like').textContent = "Feels like " + data['Feels Like'] + "°C";
            document.getElementById('rain_probability').textContent = "Rain: " + data['Rain Probability'] + "%";
            document.getElementById('uv').textContent = "UV: " + data['UV Index'];
            document.getElementById('wind_speed').textContent = "Wind speed: " + data['Wind Speed'] + " km/h";
            document.getElementById('wind_direction').textContent = "Wind direction: " + data['Wind Direction'];
            // Fetch the AccuWeather icons JSON data
        fetch('accuweather_icons.json')
        .then(response => response.json())
        .then(iconData => {
            // Assuming your data includes a 'Weather Icon' field with a number that corresponds to the keys in your icons JSON
            let weatherIconCode = data['Weather Icon'];
            let iconUrl = iconData[weatherIconCode];
            document.getElementById('weather_icon').src = iconUrl;
    });

            // Select the card
            let weather_card = document.getElementById('current_weather_card');

            // Check if daylight is 1 or 0 and apply the corresponding class
            if (data['Is Daylight'] === true) {
                weather_card.classList.remove('card-night');
                weather_card.classList.add('card-day');
            } else {
                weather_card.classList.remove('card-day');
                weather_card.classList.add('card-night');
            }
        });
    }
}

// Call the function once when the script loads
fetchWeatherDataCurrent();

// Then set it to call the function every 5 minutes
setInterval(fetchWeatherDataCurrent, 5 * 60 * 1000);
