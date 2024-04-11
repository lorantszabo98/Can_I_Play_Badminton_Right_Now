import requests
# from utils.API_KEYS import OPEN_WEATHER_API_KEY
import pickle
import pandas as pd
import streamlit as st


def get_weather_data(lat, lon):

    # Construct the API URL
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={st.secrets["OPEN_WEATHER_API_KEY"]}'

    try:
        # Send a GET request to the API
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()
            # Extract relevant weather information
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Print the weather information
            # print(f'Weather in {city}:')
            print(f'Description: {weather_description}')
            print(f'Temperature: {temperature} K')
            print(f'Humidity: {humidity}%')
            print(f'Wind Speed: {wind_speed} m/s')

            return weather_description, temperature, humidity, wind_speed

        else:

            print(f'Failed to retrieve weather data. Status code: {response.status_code}')
            return None, None, None, None

    except requests.RequestException as e:

        print(f'Error occurred while retrieving weather data: {e}')
        return None, None, None, None


def classify_weather_data(description, temperature, humidity, wind_speed):
    # Initialize the dictionary to store the classified weather parameters
    weather_classification = {
        'Outlook_Overcast': [0],
        'Outlook_Rain': [0],
        'Outlook_Sunny': [0],
        'Temperature_Cool': [0],
        'Temperature_Hot': [0],
        'Temperature_Mild': [0],
        'Humidity_High': [0],
        'Humidity_Normal': [0],
        'Wind_Strong': [0],
        'Wind_Weak': [0]

    }
    # Classify based on weather description
    if 'haze' in description.lower():
        weather_classification['Outlook_Overcast'] = [1]
    elif 'rain' in description.lower():
        weather_classification['Outlook_Rain'] = [1]
    else:
        weather_classification['Outlook_Sunny'] = [1]

    # Classify based on temperature
    if temperature < 290:
        weather_classification['Temperature_Cool'] = [1]
    elif temperature > 303:
        weather_classification['Temperature_Hot'] = [1]
    else:
        weather_classification['Temperature_Mild'] = [1]

        # Classify based on humidity
    if humidity > 50:
        weather_classification['Humidity_High'] = [1]
    else:
        weather_classification['Humidity_Normal'] = [1]

        # Classify based on wind speed
    if wind_speed > 3.3:
        weather_classification['Wind_Strong'] = [1]
    else:
        weather_classification['Wind_Weak'] = [1]

    return weather_classification

