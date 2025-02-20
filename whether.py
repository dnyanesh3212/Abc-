import streamlit as st
import requests

# OpenWeatherMap API Key
API_KEY = 'ca60b443558bec0e3c7638e5eb271309'

# Function to get weather data
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather
    else:
        return None

# Streamlit app
def main():
    st.title('Weather App')
    st.write('Enter a city name to get the current weather.')

    city = st.text_input('City Name')

    if city:
        weather = get_weather(city)
        if weather:
            st.write(f"### {weather['city']}")
            st.write(f"Temperature: {weather['temperature']}°C")
            st.write(f"Weather: {weather['description'].capitalize()}")
            icon_url = f"http://openweathermap.org/img/w/{weather['icon']}.png"
            st.image(icon_url)
        else:
            st.write("City not found. Please enter a valid city name.")

if __name__ == '__main__':
    main()
