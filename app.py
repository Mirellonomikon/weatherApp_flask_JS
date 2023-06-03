from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import weather

app = Flask(__name__)
CORS(app)  # this line enables CORS
app.config['SECRET_KEY'] = 'your-secret-key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_location_key', methods=['POST'])
def get_location_key():
    location = request.json.get('location')
    location_key = weather.get_location_key(location)
    return jsonify({'location_key': location_key})


@app.route('/update_current_weather', methods=['POST'])
def update_current():
    location = request.json.get('location')
    location_key = request.json.get('location_key')
    weather_data = weather.get_current_weather(location_key, location)
    return jsonify(weather_data)


@app.route('/update_5day_weather', methods=['POST'])
def update_5day_weather():
    location = request.json.get('location')
    location_key = request.json.get('location_key')
    weather_data = weather.get_5day_weather(location_key, location)
    return jsonify(weather_data)


@app.route('/update_12hour_weather', methods=['POST'])
def update_12hour_weather():
    location = request.json.get('location')
    location_key = request.json.get('location_key')
    weather_data = weather.get_12hour_weather(location_key, location)
    return jsonify(weather_data)


if __name__ == '__main__':
    location = 'Constanta'
    app.run()
