import streamlit as st
from utils.get_weather_data import get_weather_data, classify_weather_data
from utils.get_location import get_my_location
import pandas as pd
import pickle

st.title('Can I play badminton right now?')

lat, lon = get_my_location()
# city = 'Budapest'
# lat = '47.4979'
# lon = '19.0402'

description, temperature, humidity, wind_speed = get_weather_data(lat, lon)

st.caption('Weather data based :blue[on your location]:')

col1, col2, col3, col4 = st.columns(4)
col1.metric("Description", f'{str(description)} ')
col2.metric("Temperature", f'{str(temperature)} K')
col3.metric("Humidity", f'{str(humidity)} %')
col4.metric("Wind Speed", f'{str(wind_speed)} m/s')

classification_result = classify_weather_data(description, temperature, humidity, wind_speed)
current_weather = pd.DataFrame(classification_result)

dtree_model = pickle.load(open('./backend/trained_classifier_model/dt_model.sav', 'rb'))
play_badminton_prediction = dtree_model.predict(current_weather)

if play_badminton_prediction == 1:
    st.success('Yes, you can play badminton!')
else:
    st.error('No, unfortunately the weather conditions are not suitable for badminton!')