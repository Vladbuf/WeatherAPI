# Weather API Data Pipeline

A Python project that fetches live weather data for some Romanian cities, stores it in a local SQLite database, and displays current conditions.

## What it does

- Fetches live weather data (temperature, pressure, humidity) from the OpenWeatherMap API for a list of cities
- Parses and cleans the JSON response
- Stores the results in a local SQLite database with a timestamp for each reading
- Designed to run daily to build up historical weather data over time (still WIP)

## Technologies used

- Python 3
- `requests` — API calls
- `sqlite3` — local database storage
- `python-dotenv` — secure API key management

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install requests python-dotenv
   ```
3. Create a `.env` file in the project root based on `.env.example`:
   ```
   API_KEY=your_openweathermap_api_key
   ```
4. Run the script:
   ```
   python main.py
   ```

## Database

Data is stored in `weatherapi_database.db` with the following fields: city, country, weather_desc, temperature, min/max temperature, pressure, humidity, and recorded timestamp.

## Notes

A free OpenWeatherMap API key is required. Sign up at [openweathermap.org](https://openweathermap.org).