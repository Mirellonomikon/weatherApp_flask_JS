function fetchWeatherData5Day() {
    let location = localStorage.getItem('location');
    let locationKey = localStorage.getItem('location_key');

    if (location && locationKey) {
        fetch('/update_5day_weather', {
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
            let weatherPane = document.getElementById('day_weather');

            // Clear previous cards
            weatherPane.innerHTML = '';
            let locationCard = document.createElement('div');
            locationCard.classList.add('card');
            locationCard.style.marginBottom = "10px";
            locationCard.innerHTML = `<div class="card-body" style="height: 66.3906px;margin-top: -5px;"><h2 id="weather_location-2">${location}</h2></div>`;
            weatherPane.appendChild(locationCard);

            data.forEach((forecast, index) => {
                // Create a new day card
                let dayCard = document.createElement('div');
                dayCard.classList.add('card', 'card-day');
                dayCard.style.marginBottom = "10px";
                dayCard.innerHTML = `
                    <div class="card-body">
                        <div class="container">
                            <div class="row">
                                <div class="col">
                                    <h3 id="day_index-${index}">${forecast['Date']}</h3>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-12">
                                    <h2 id="max_temp-${index}">
                                        <picture><img id="weather_icon-2-${index}" style="height: 55px;width: 70px;margin-left: 0px;margin-right: 22px;" src="icon_url/${forecast['Weather Icon (Day)']}"></picture>${forecast['Max Temperature']}°C
                                    </h2>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-4">
                                    <h6 class="text-muted" id="weather_description_day-${index}" style="width: 174px;">${forecast['Weather Description (Day)']}</h6>
                                    <p id="min_weather-${index}">Min ${forecast['Min Temperature']}°C</p>
                                </div>
                                <div class="col-md-4">
                                    <p id="rain_probability_day-${index}">Rain: ${forecast['Rain Probability (Day)']}%</p>
                                </div>
                                <div class="col-md-4">
                                    <p id="wind_speed_day-${index}">Wind speed: ${forecast['Wind Speed (Day)']} km/h</p>
                                    <p id="wind_direction_day-${index}">Wind direction: ${forecast['Wind Direction (Day)']}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
                weatherPane.appendChild(dayCard);

                // Create a new night card
                let nightCard = document.createElement('div');
                nightCard.classList.add('card', 'card-night');
                nightCard.style.marginBottom = "10px";
                nightCard.innerHTML = `
                    <div class="card-body">
                        <div class="container">
                            <div class="row">
                                <div class="col-md-12">
                                    <h5 id="moon_phase-${index}">
                                        <picture><img id="weather_icon-3-${index}" style="height: 55px;width: 70px;margin-left: 0px;margin-right: 22px;" src="icon_url/${forecast['Weather Icon (Night)']}"></picture>${forecast['Moon Phase']}
                                    </h5>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-md-4">
                                    <h6 class="text-muted mb-2" id="weather_description_night-${index}" style="width: 174px;">${forecast['Weather Description (Night)']}</h6>
                                </div>
                                <div class="col-md-4">
                                    <p id="rain_probability_day_night-${index}">Rain: ${forecast['Rain Probability (Night)']}%</p>
                                </div>
                                <div class="col-md-4">
                                    <p id="wind_speed_night-${index}">Wind speed: ${forecast['Wind Speed (Night)']} km/h</p>
                                    <p id="wind_direction_night-${index}">Wind direction: ${forecast['Wind Direction (Night)']}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
                weatherPane.appendChild(nightCard);
            });
        });
    }
}

// // Call the function once when the script loads
// fetchWeatherData5Day();

// Then set it to call the function every 60 minutes
setInterval(fetchWeatherData5Day, 60 * 60 * 1000);
