import requests
from dotenv import load_dotenv
import os

cities_RO = {"Iasi":{"lat": 47.151726, "lon": 27.587914}, 
             "Bucuresti":{"lat":44.439663, "lon":26.096306},
             "Brasov": {"lat": 45.657974, "lon":25.601198},
             "Cluj-Napoca": {"lat": 46.770439, "lon":23.591423}}
load_dotenv()
api_key = os.environ.get('API_KEY')
    
class WeatherAPI:
    def __init__(self, lat, lon, api):
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
            keys_i_want = ['temp', 'temp_min', 'temp_max', 'pressure', 'humidity']
            self.result = {key:self.response['main'][key] for key in keys_i_want}
            return self.result
        else:
            return None
    def show_result(self):
        self.result_list = self.json_parsing()
