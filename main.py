import requests
from dotenv import load_dotenv
import os
import sqlite3
import datetime

cities_RO = {"Iasi":{"lat": 47.151726, "lon": 27.587914}, 
             "Bucuresti":{"lat":44.439663, "lon":26.096306},
             "Brasov": {"lat": 45.657974, "lon":25.601198},
             "Cluj-Napoca": {"lat": 46.770439, "lon":23.591423}}
load_dotenv()
api_key = os.environ.get('API_KEY')

def create_db():
    try:
        conn = sqlite3.connect('weatherapi_database.db')
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_api(
                    ID INTEGER PRIMARY KEY NOT NULL,
                    city TEXT,
                    country TEXT,
                    weather_desc TEXT,
                    temperature REAL,
                    min_temperature REAL,
                    max_temperature REAL,
                    pressure INTEGER,
                    humidity INTEGER,
                    recorded_at TEXT)''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)

def insert_db(data_list):
    try:
        conn = sqlite3.connect('weatherapi_database.db')
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO weather_api (city, country, weather_desc, temperature, min_temperature, max_temperature, pressure, humidity, recorded_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", data_list)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(e)

class WeatherAPI:
    def __init__(self, city, lat, lon, api):
        self.city = city
        self.lat = lat
        self.lon = lon
        self.api = api
    def get_result(self):
        try:
            r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.api}&units=metric", timeout=10)
            r.raise_for_status()
            return r.json()
        except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as e:
            print(f"Error: {e}")
    def json_parsing(self):
        self.response = self.get_result()
        if self.response:
            keys = ['temp', 'temp_min', 'temp_max', 'pressure', 'humidity']
            self.result = {'city': self.city}
            self.result['country'] = self.response['sys']['country']
            self.result['weather_desc'] = self.response['weather'][0]['description']
            self.result.update({key:self.response['main'][key] for key in keys})
            time = datetime.datetime.now()
            self.date_today = time.strftime("%Y-%m-%d %H:%M:%S")
            self.result['recorded_at'] = self.date_today
            return self.result
        else:
            return None
    def show_result(self):
        self.result_list = self.json_parsing()
        if self.result_list:
            print(f"""
                City: {self.result_list['city']}
                Temperature: {self.result_list['temp']} celsius
                Minimum temp: {self.result_list['temp_min']} celsius
                Maximum temp: {self.result_list['temp_max']}
                Pressure: {self.result_list['pressure']}
                Humidity: {self.result_list['humidity']}
                Date Recorded: {self.result_list['recorded_at']}""")
            return self.result_list

data = []
for city in cities_RO:
    result = WeatherAPI(city, cities_RO[city]['lat'], cities_RO[city]['lon'], api_key)
    city_data = result.show_result()
    if city_data is not None:
        data.append(city_data)
upload_data = [tuple(element.values()) for element in data]
create_db()
insert_db(upload_data)