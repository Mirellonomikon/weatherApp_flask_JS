from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import weather

app = Flask(__name__)
CORS(app)  # this line enables CORS
app.config['SECRET_KEY'] = 'your-secret-key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update_weather', methods=['POST'])
def update_weather():
    location = request.json.get('location')
    location_key = weather.get_location_key(location)
    weather_data = weather.get_current_weather(location_key, location)
    return jsonify(weather_data)


if __name__ == '__main__':
    location = 'London'
    app.run()
