import sqlite3

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