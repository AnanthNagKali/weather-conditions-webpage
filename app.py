from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual OpenWeatherMap API key
API_KEY = '5340240693682acf2b44a219f44ed6f1'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    if city:
        weather_data = fetch_weather(city)
        return render_template('index.html', weather=weather_data, city=city)
    return render_template('index.html', error="Please enter a city name.")

def fetch_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)