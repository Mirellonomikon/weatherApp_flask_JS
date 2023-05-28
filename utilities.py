import json

import json
import os


def save_accuweather_icons():
    icons = {}

    # Iterate over all possible WeatherIcon values
    for weather_icon in range(1, 50):
        icon_number = str(weather_icon).zfill(2)
        icon_url = f'http://developer.accuweather.com/sites/default/files/{icon_number}-s.png'
        icons[weather_icon] = icon_url

    # Get the static folder path in the Flask project
    static_folder = os.path.join(os.getcwd(), 'static')

    # Save the icons dictionary to a JSON file in the static folder
    with open(os.path.join(static_folder, 'accuweather_icons.json'), 'w') as file:
        json.dump(icons, file)


# Call the function to save the icons
# save_accuweather_icons()

def get_temperature_unit(unit_system):
    if unit_system == 'metric':
        return '°C'
    elif unit_system == 'imperial':
        return '°F'
    else:
        return ''


def get_wind_speed_unit(unit_system):
    if unit_system == 'metric':
        return 'km/h'
    elif unit_system == 'imperial':
        return 'mph'
    else:
        return ''


def get_rain_prob_unit():
    return '%'


def _celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def _kph_to_mph(kph):
    return round(kph * 0.6213712, 2)