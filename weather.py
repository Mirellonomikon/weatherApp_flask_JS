import requests

from utilities import _kph_to_mph, _celsius_to_fahrenheit, get_temperature_unit, get_rain_prob_unit, get_wind_speed_unit

API_KEY = 'kvZYgaZHLBVqI6XTqWQLa8Zqih7Ahvxa'  # rezerva XRlhSG2XcseQbpGXgICBqilMG56Adc7g ai 50 de calluri pe ZI iar daca schimbi locatia se pun 2 calluri
# daca mai ai nevoie de un api key iti faci cont pe accuweather api si generezi cheie
DEFAULT_UNIT_SYSTEM = 'metric'  # 'metric' for Celsius, 'imperial' for Fahrenheit


def get_location_key(location):
    url = f'http://dataservice.accuweather.com/locations/v1/search?q={location}&apikey={API_KEY}&language=en-us'

    response = requests.get(url)
    data = response.json()

    if data:
        location_key = data[0]['Key']
        return location_key

    return None


def get_5day_weather(location_key, location, unit_system=DEFAULT_UNIT_SYSTEM):
    if location_key is None:
        print('Location not found.')
        return []

    url = f'http://dataservice.accuweather.com/forecasts/v1/daily/5day/{location_key}?apikey={API_KEY}&language=en-us&details=true&metric=true'

    response = requests.get(url)
    data = response.json()

    if 'DailyForecasts' in data:
        daily_forecasts = data['DailyForecasts']
        weather_data = []
        for forecast in daily_forecasts:
            date = forecast['Date']
            min_temp_day = forecast['Temperature']['Minimum']['Value']
            max_temp_day = forecast['Temperature']['Maximum']['Value']
            moon_phase = forecast['Moon']['Phase']
            rain_probability_day = forecast['Day']['RainProbability']
            wind_speed_day = forecast['Day']['Wind']['Speed']['Value']
            wind_direction_day = forecast['Day']['Wind']['Direction']['Localized']
            weather_description_day = forecast['Day']['IconPhrase']
            weather_icon_day = forecast['Day']['Icon']
            rain_probability_night = forecast['Night']['RainProbability']
            wind_speed_night = forecast['Night']['Wind']['Speed']['Value']
            wind_direction_night = forecast['Night']['Wind']['Direction']['Localized']
            weather_description_night = forecast['Night']['IconPhrase']
            weather_icon_night = forecast['Night']['Icon']

            if unit_system == 'imperial':
                min_temp_day = _celsius_to_fahrenheit(min_temp_day)
                max_temp_day = _celsius_to_fahrenheit(max_temp_day)
                wind_speed_day = _kph_to_mph(wind_speed_day)
                wind_speed_night = _kph_to_mph(wind_speed_night)

            weather_data.append({
                'Date': date,
                'Location': location,
                'Max Temperature': max_temp_day,
                'Min Temperature': min_temp_day,
                'Rain Probability (Day)': rain_probability_day,
                'Wind Speed (Day)': wind_speed_day,
                'Wind Direction (Day)': wind_direction_day,
                'Weather Description (Day)': weather_description_day,
                'Weather Icon (Day)': weather_icon_day,
                'Moon Phase': moon_phase,
                'Rain Probability (Night)': rain_probability_night,
                'Wind Speed (Night)': wind_speed_night,
                'Wind Direction (Night)': wind_direction_night,
                'Weather Description (Night)': weather_description_night,
                'Weather Icon (Night)': weather_icon_night
            })

        return weather_data


def get_current_weather(location_key, location, unit_system=DEFAULT_UNIT_SYSTEM):
    if location_key is None:
        print('Location not found.')
        return None

    url = f'http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{location_key}?apikey={API_KEY}&language=en-us&details=true&metric=true'

    response = requests.get(url)
    data = response.json()

    if data:
        current_weather = data[0]
        temperature = current_weather['Temperature']['Value']
        feels_like = current_weather['RealFeelTemperature']['Value']
        rain_probability = current_weather['RainProbability']
        uv_index = current_weather['UVIndex']
        wind_speed = current_weather['Wind']['Speed']['Value']
        wind_direction = current_weather['Wind']['Direction']['Localized']
        weather_description = current_weather['IconPhrase']
        weather_icon = current_weather['WeatherIcon']
        is_daylight = current_weather['IsDaylight']

        if unit_system == 'imperial':
            temperature = _celsius_to_fahrenheit(temperature)
            feels_like = _celsius_to_fahrenheit(feels_like)
            wind_speed = _kph_to_mph(wind_speed)

        current_weather_data = {
            'Location': location,
            'Temperature': temperature,
            'Rain Probability': rain_probability,
            'UV Index': uv_index,
            'Wind Speed': round(wind_speed, 2),
            'Wind Direction': wind_direction,
            'Feels Like': round(feels_like, 2),
            'Weather Description': weather_description,
            'Weather Icon': weather_icon,
            'Is Daylight': is_daylight,
        }

        return current_weather_data


def get_12hour_weather(location_key, location, unit_system=DEFAULT_UNIT_SYSTEM):
    if location_key is None:
        print('Location not found.')
        return []

    url = f'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{location_key}?apikey={API_KEY}&language=en-us&details=true&metric=true'

    response = requests.get(url)
    data = response.json()

    if data:
        hourly_forecasts = data
        weather_data = []
        for forecast in hourly_forecasts:
            timestamp = forecast['DateTime']
            temperature = forecast['Temperature']['Value']
            rain_probability = forecast['RainProbability']
            wind_speed = forecast['Wind']['Speed']['Value']
            wind_direction = forecast['Wind']['Direction']['Localized']
            weather_description = forecast['IconPhrase']
            weather_icon = forecast['WeatherIcon']
            is_daylight = forecast['IsDaylight']

            if unit_system == 'imperial':
                temperature = _celsius_to_fahrenheit(temperature)
                wind_speed = _kph_to_mph(wind_speed)

            weather_data.append({
                'Timestamp': timestamp,
                'Location': location,
                'Temperature': temperature,
                'Rain Probability': rain_probability,
                'Wind Speed': round(wind_speed, 2),
                'Wind Direction': wind_direction,
                'Weather Description': weather_description,
                'Weather Icon': weather_icon,
                'Is Daylight': is_daylight,
            })

        return weather_data


# This is for previewing the data
def print_current_weather_data(current_weather_data, unit_system=DEFAULT_UNIT_SYSTEM):
    if current_weather_data:
        print('Temperature:', current_weather_data['Temperature'], get_temperature_unit(unit_system))
        print('Rain Probability:', current_weather_data['Rain Probability'], get_rain_prob_unit())
        print('UV Index:', current_weather_data['UV Index'])
        print('Wind Speed:', current_weather_data['Wind Speed'], get_wind_speed_unit(unit_system))
        print('Wind Direction:', current_weather_data['Wind Direction'])
        print('Feels Like:', current_weather_data['Feels Like'], get_temperature_unit(unit_system))
        print('Weather Description:', current_weather_data['Weather Description'])
        print('Is Daylight:', current_weather_data['Is Daylight'])
        print()
    else:
        print('No current weather data available.')


def print_five_weather_data(weather_data, unit_system=DEFAULT_UNIT_SYSTEM):
    for forecast in weather_data:
        print('Date:', forecast['Date'])
        print('Max Temperature:', forecast['Max Temperature'], get_temperature_unit(unit_system))
        print('Min Temperature:', forecast['Min Temperature'], get_temperature_unit(unit_system))
        print('Day:')
        print('Rain Probability:', forecast['Rain Probability (Day)'], get_rain_prob_unit())
        print('Wind Speed:', forecast['Wind Speed (Day)'], get_wind_speed_unit(unit_system))
        print('Wind Direction:', forecast['Wind Direction (Day)'])
        print('Weather Description:', forecast['Weather Description (Day)'])
        print('Night:')
        print('Moon Phase:', forecast['Moon Phase'])
        print('Rain Probability:', forecast['Rain Probability (Night)'], get_rain_prob_unit())
        print('Wind Speed:', forecast['Wind Speed (Night)'], get_wind_speed_unit(unit_system))
        print('Wind Direction:', forecast['Wind Direction (Night)'])
        print('Weather Description:', forecast['Weather Description (Night)'])
        print()


def print_12hour_weather_data(weather_data, unit_system=DEFAULT_UNIT_SYSTEM):
    for forecast in weather_data:
        print('Timestamp:', forecast['Timestamp'])
        print('Temperature:', forecast['Temperature'], get_temperature_unit(unit_system))
        print('Rain Probability:', forecast['Rain Probability'], get_rain_prob_unit())
        print('Wind Speed:', forecast['Wind Speed'], get_wind_speed_unit(unit_system))
        print('Wind Direction:', forecast['Wind Direction'])
        print('Weather Description:', forecast['Weather Description'])
        print('Is Daylight:', forecast['Is Daylight'])
        print()

# Example usage
# location = 'Cluj-Napoca'
# location_key = get_location_key(location)
# unit_system = 'metric'  # 'metric' or 'imperial' to switch between Celsius and Fahrenheit

# current_data = get_current_weather(location_key, location, unit_system)
# print_current_weather_data(current_data, unit_system)

# five_day_data = get_5day_weather(location_key,location, unit_system)
# print_five_weather_data(five_day_data, unit_system)

# twelve_hour_data = get_12hour_weather(location_key, location, unit_system)
# print_12hour_weather_data(twelve_hour_data, unit_system)
