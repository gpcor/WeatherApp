import json
import random
import requests
import datetime


def weather_lookup(city):
    with open("src/api.txt", "r") as get_key:
        api_key = get_key.read()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}"
    weather_json = requests.get(url.strip("\n")).json()
    return weather_json


def weather_format(weather_json):
    location = weather_json["name"]
    country = weather_json["sys"].get("country")
    current_temp = round(weather_json["main"].get("temp"))
    feels_like = round(weather_json["main"].get("feels_like"))
    weather_description = weather_json["weather"][0]["description"]
    wind_direction = weather_json["wind"].get("deg")
    wind_speed = round(weather_json["wind"].get("speed"))

    wind_direction_converstion = round((wind_direction / 22.5) + 0.5)
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
    wind_direction = cardinal_directions[(wind_direction_converstion % 16)]
    return (
        location,
        country,
        current_temp,
        feels_like,
        weather_description,
        wind_direction,
        wind_speed,
    )


def email_format():

    message_body = f"""
    Weather for {datetime.datetime.today} in {location}, {country}:
    - The current temperature is {current_temp}.
    - The temperature feel is {feels_like}.
    - It is {weather_description} out.
    - The wind is moving {wind_direction} at {wind_speed} MPH.
    You don't live here. Which means this weather doesn't do shit for you.
    But now you know something you really didn't need to, and I think that's
    just prime, mate.

    ~~Cheers~~
    Your Fucking Twin Brother
    """
    print(message_body)
    return message_body


if __name__ == "__main__":
    city_names = []
    with open("city.list.json", "r") as city_raw:
        city_list = json.loads(city_raw.read())
        for item in city_list:
            for k, v in item.items():
                if k == "name":
                    city_names.append(v)
    city = random.choice(city_names)
    weather_json = weather_lookup(city)
    weather_details = weather_format(weather_json)
    print(weather_details)
    email_format(weather_details)
