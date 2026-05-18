import requests

cities_RO = {"Iasi":{"lat": 47.151726, "lon": 27.587914}, 
             "Bucuresti":{"lat":44.439663, "lon":26.096306},
             "Brasov": {"lat": 45.657974, "lon":25.601198},
             "Cluj-Napoca": {"lat": 46.770439, "lon":23.591423}}
keys_i_want = ['temp', 'temp_min', 'temp_max', 'pressure', 'humidity']
temp_list = []
API_KEY = 'a5cffaaedbb28fbb1a85272783cf7a5f'

r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=47.151726&lon=27.587914&appid={API_KEY}&units=metric", timeout=10)
response = r.json()
print(response)