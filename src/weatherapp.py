import json
import random
import requests
import datetime


class WeatherApp:
    def __init__(self):
        self.city = ""
        self.city_names = []
        self.weather_json = ""
        self.location = ""
        self.country = ""
        self.current_temp = ""
        self.feels_like = ""
        self.weather_description = ""
        self.wind_direction = ""
        self.wind_speed = ""
        self.today = datetime.date.today()
        self.recipient = "andrewcameron.corsini@gmail.com"
        self.sender = "gabriel.corsini@gmail.com"
        self.subject = "Your Fucking Weather"

        with open("city.list.json", "r") as city_raw:
            city_list = json.loads(city_raw.read())
            for item in city_list:
                for k, v in item.items():
                    if k == "name":
                        self.city_names.append(v)
        self.city = random.choice(self.city_names)

    def weather_lookup(self):
        with open("src/api.txt", "r") as get_key:
            api_key = get_key.read()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&units=imperial&appid={api_key}"
        self.weather_json = requests.get(url.strip("\n")).json()

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

    def email_format(self):
        message_body = f"""
            Weather for {self.today} in {self.location}, {self.country}:
            - The current temperature is {self.current_temp}.
            - The temperature feel is {self.feels_like}.
            - It is {self.weather_description} out.
            - The wind is moving {self.wind_direction} at {self.wind_speed} MPH.
            You don't live here. Which means this weather doesn't do shit for you.
            But now you know something you really didn't need to, and I think that's
            just prime, mate.

            ~~Cheers~~
            Your Fucking Twin Brother
            """
        print(message_body)
        message = MIMEText(message_body)
        message["to"] = self.recipient
        message["from"] = self.sender
        message["subject"] = self.subject


if __name__ == "__main__":
    weather = WeatherApp()
    weather.weather_lookup()
    weather.weather_format()
    weather.email_format()
