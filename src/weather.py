import json
import random
import requests


class WeatherApp:
    def __init__(self, city):
        self.city = city

    def weather_lookup(self):
        with open("src/api.txt", "r") as get_key:
            api_key = get_key.read()
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}"
        self.weather_json = requests.get(self.url.strip("\n")).json()

    def weather_format(self):
        self.location = self.weather_json["name"]
        self.country = self.weather_json["sys"].get("country")
        self.current_temp = round(self.weather_json["main"].get("temp"))
        self.feels_like = round(self.weather_json["main"].get("feels_like"))
        self.weather_description = self.weather_json["weather"][0]["description"]
        self.wind_direction = self.weather_json["wind"].get("deg")
        self.wind_speed = round(self.weather_json["wind"].get("speed"))

        wind_direction_converstion = round((self.wind_direction / 22.5) + 0.5)
        cardinal_directions = [
            "N",
            "NNE",
            "NE",
            "ENE",
            "E",
            "ESE",
            "SE",
            "SSE",
            "S",
            "SSW",
            "SW",
            "WSW",
            "W",
            "WNW",
            "NW",
            "NNW",
        ]
        self.wind_direction = cardinal_directions[(wind_direction_converstion % 16)]

        print(
            self.location,
            self.country,
            self.current_temp,
            self.feels_like,
            self.weather_description,
            self.wind_direction,
            self.wind_speed,
        )


if __name__ == "__main__":
    city_names = []
    with open("city.list.json", "r") as city_raw:
        city_list = json.loads(city_raw.read())
        for item in city_list:
            for k, v in item.items():
                if k == "name":
                    city_names.append(v)
    city = random.choice(city_names)
    w = WeatherApp(city)
    w.weather_lookup()
    w.weather_format()
