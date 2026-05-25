import requests
from dotenv import load_dotenv
import os
import datetime
from weather_db import create_db, insert_db
from geocoding import GeoCoding

load_dotenv()
api_key = os.environ.get('API_KEY')

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
                Country: {self.result_list['country']}
                Temperature: {self.result_list['temp']} celsius
                Minimum temp: {self.result_list['temp_min']} celsius
                Maximum temp: {self.result_list['temp_max']}
                Pressure: {self.result_list['pressure']}
                Humidity: {self.result_list['humidity']}
                Date Recorded: {self.result_list['recorded_at']}""")
            return self.result_list

data = []
input_city = input("Please type the city: ")
input_country = input("Please type the country code (eg. US, RO, FR, TR). This is optional, please press Enter to skip: ")
input_country = input_country if input_country else None
temp_coords = GeoCoding(input_city, input_country)
coords = temp_coords.parsing()
result = WeatherAPI(**coords, api= api_key)
weather_data = result.show_result()
if weather_data is not None:
    data.append(weather_data)
upload_data = [tuple(element.values()) for element in data]
db_response = input('Do you want the weather data stored in a SQL database? Y/N: ').lower()
if db_response in ('y', 'yes', 'yeah'):
    create_db()
    insert_db(upload_data)
else:
    print("Thank you for using my WeatherAPI!")