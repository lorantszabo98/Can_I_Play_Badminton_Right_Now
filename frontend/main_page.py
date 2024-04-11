import streamlit as st
from utils.get_weather_data import get_weather_data, classify_weather_data
from utils.get_location import get_my_location
import pandas as pd
import pickle


st.title('Can I play badminton right now?')

lat, lon = get_my_location()

if lat is not None:

    description, temperature, humidity, wind_speed = get_weather_data(lat, lon)

    if description is not None:

        metrics_toogle = st.toggle('Switch to metric')
        st.caption('Weather data based :blue[on your location]:')

        if metrics_toogle:
            # temperature, wind_speed = convert_metrics(temperature, wind_speed)
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Description", f'{str(description)} ')
            col2.metric("Temperature", f'{str(round(temperature-273.15, 2))} °C')
            col3.metric("Humidity", f'{str(humidity)} %')
            col4.metric("Wind Speed", f'{str(round(wind_speed*3.6, 1))} km/h')
        else:
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
    else:
        st.error('Failed to retrieve weather data. Please try again later.')
else:
    st.error('Failed to retrieve GPS data, please enable location permission in your browser!')