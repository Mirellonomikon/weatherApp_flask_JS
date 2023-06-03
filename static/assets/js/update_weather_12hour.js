function fetchWeatherData12Hour() {
    let location = localStorage.getItem('location');
    let locationKey = localStorage.getItem('location_key');

    if (location && locationKey) {
        fetch('/update_12hour_weather', {
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
            let weatherPane = document.getElementById('hour_weather');

            // Clear previous cards
            weatherPane.innerHTML = '';
            let locationCard = document.createElement('div');
            locationCard.classList.add('card');
            locationCard.style.marginBottom = "10px";
            locationCard.innerHTML = `<div class="card-body" style="height: 66.3906px;margin-top: -5px;"><h2 id="weather_location-2">${location}</h2></div>`;
            weatherPane.appendChild(locationCard);

            data.forEach((forecast, index) => {
                // Create a new hourly card
                let hourlyCard = document.createElement('div');
                hourlyCard.classList.add('card');
                hourlyCard.classList.add(forecast['Is Daylight'] ? 'card-day' : 'card-night');
                hourlyCard.innerHTML = `
                    <div class="card-body" style="border-style: none;">
                        <div class="container">
                            <div class="row">
                                <div class="col">
                                    <h2 id="hour_index-${index}">${forecast['Timestamp']}</h2>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-12">
                                    <h2 id="temp_cur-${index}" style="width: 185px;">
                                        <picture><img id="weather_icon-${index}" style="height: 55px;width: 70px;margin-left: 0px;margin-right: 22px;"></picture>${forecast['Temperature']}°C
                                    </h2>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-4">
                                    <h6 class="text-muted mb-2" id="weather_description-${index}" style="width: 174px;">${forecast['Weather Description']}</h6>
                                </div>
                                <div class="col-md-4">
                                    <p id="rain_probability-${index}">Rain: ${forecast['Rain Probability']}%</p>
                                </div>
                                <div class="col-md-4">
                                    <p id="wind_speed-${index}">Wind speed: ${forecast['Wind Speed']} km/h</p>
                                    <p id="wind_direction-${index}">Wind direction: ${forecast['Wind Direction']}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
                weatherPane.appendChild(hourlyCard);
            });
        })
        .finally(() => {
            // Calculate minutes until next hour and schedule next fetch
            let now = new Date();
            let minutesUntilNextHour = 60 - now.getMinutes();
            setTimeout(fetchWeatherData12Hour, minutesUntilNextHour * 60 * 1000);
        });
    }
}

// Call the function once when the script loads
fetchWeatherData12Hour();
