# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Hjp5n4EBV4u6OB74i_gPSa5_62r8FcwL
"""

#http://api.weatherapi.com/v1/current.json?key=6ecaf03f630b43c39fe44435250801&q=Tokyo&lang=ja
import requests
import ipywidgets as widgets
from IPython.display import display


API_KEY = '6ecaf03f630b43c39fe44435250801'


def get_weather(city_name):
    base_url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city_name}&lang=ja"


    response = requests.get(base_url)
    data = response.json()


    print(data)


    if "error" in data:
        return f"エラー: {data['error']['message']}"


    city = data["location"]["name"]
    region = data["location"]["region"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    weather_desc = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    wind_kph = data["current"]["wind_kph"]


    weather_info = f"都市: {city}, {region}, {country}\n" \
                   f"気温: {temp_c}°C\n" \
                   f"天気: {weather_desc}\n" \
                   f"湿度: {humidity}%\n" \
                   f"風速: {wind_kph} km/h"

    return weather_info


def on_button_click(b):
    city_name = text.value
    result = get_weather(city_name)
    output_area.value = result


text = widgets.Text(placeholder="都市名を入力してください")
button = widgets.Button(description="天気を取得")
output_area = widgets.Textarea(layout={'width': '400px', 'height': '200px'})


button.on_click(on_button_click)


display(text, button, output_area)