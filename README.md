Can I play badminton outside right now based on weather data?
===============================

This repository contains the backend and frontend code for an application that can tell you if you can play badminton at your location based on weather data:

1.  `train_classifier.py`: This script is responsible for training a decision tree model on a custom dataset. The dataset contains a CSV file, which contains weather data and the target variable.

2.  `main_page.py`: This is a Streamlit code to display an user interface. It shows the current weather data based on your location, and weather you can play badminton or not. It loads the serialized decision tree model and make predictions based on your weather data.

3.  `get_weather_data.py`: Load the weather data using the `OPENWEATHERMAP API` and converts them to the desired format.

4.  `get_location.py`: Get the geolocation with this [package](https://github.com/aghasemi/streamlit_js_eval)


Demo
-----

You can find a working demo [here](https://can-i-play-badmiinton-right-now.streamlit.app/).

Dataset
-------

You can find the training dataset [here](https://www.kaggle.com/datasets/aditya0kumar0tiwari/play-badminton/data).

Requirements
-------------

stramlit

You can find the others in the `requirements.txt` file
