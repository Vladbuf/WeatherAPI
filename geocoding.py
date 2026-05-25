import requests
from dotenv import load_dotenv
import os
import sys
sys.stdout.reconfigure(encoding='utf-8') # type: ignore

load_dotenv()
api_key = os.environ.get('API_KEY')
city_list = ['Iasi', 'Bucharest', 'Brasov', 'Cluj', "Roman"]

class GeoCoding:
    def __init__(self, city, country):
        self.city = city
        self.country = country
    def get_result(self):
        try:
            r = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={self.city}, {self.country}&limit=1&appid={api_key}', timeout=10)
            r.raise_for_status()
            return r.json()
        except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as e:
            print(f"Error: {e}")
    def parsing(self):
        self.result = self.get_result()
        if self.result:
            self.lat = self.result[0]['lat']
            self.lon = self.result[0]['lon']
            return {'lat':self.lat, 'lon':self.lon}
        else:
            return None