from dotenv import load_dotenv
import os
from weather_db import create_db, insert_db
from geocoding import GeoCoding
from weather import WeatherAPI

load_dotenv()
api_key = os.environ.get('API_KEY')

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
db_response = input('Do you want the weather data stored in SQL database? Y/N: ').lower()
print(data)
if db_response in ('y', 'yes', 'yeah'):
    create_db()
    insert_db(upload_data)
else:
    print("Thank you for using my WeatherAPI!")