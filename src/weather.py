import json
import requests


class WeatherApp:
    def __init__(self, lat, long, units):
        self.lat = lat
        self.long = long
        self.units = units
        with open("api.txt", "r") as get_key:
            api_key = get_key.read()
        self.url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&units={units}&appid={api_key}"

    def weather_lookup(self):
        weather_json = requests.get(self.url.strip("\n")).json()
        with open("weather.json", "a") as weather_to_file:
            json.dump(weather_json, weather_to_file, indent=4, sort_keys=True)

    def weather_format(self):
        with open("weather.json", "r+") as weather_from_file:
            weather_from_file.truncate(0)
            weather_from_file.close()


if __name__ == "__main__":
    lat = input("Enter lattitude: ")
    long = input("Enter longitude: ")
    units = input("Enter units (imperial or metric): ")

    w = WeatherApp(lat, long, units)
    w.weather_lookup()
