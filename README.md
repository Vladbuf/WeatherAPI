# Weather API Data Pipeline

A Python project that fetches live weather data for any city in the world and optionally stores it in a local SQLite database.

## What it does

- Takes a city name and optional country code as user input
- Converts the city name to coordinates using the OpenWeatherMap Geocoding API
- Fetches live weather data (temperature, pressure, humidity, weather description)
- Displays the results and optionally saves them to a SQLite database with a timestamp

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install requests python-dotenv
   ```
3. Create a `.env` file based on `.env.example`:
   ```
   API_KEY=your_openweathermap_api_key
   ```
4. Run:
   ```
   python main.py
   ```

## Project structure

```
main.py        — entry point
weather.py     — WeatherAPI class
geocoding.py   — GeoCoding class
weather_db.py  — database functions
```

## Notes

A free API key from [openweathermap.org](https://openweathermap.org) is required.