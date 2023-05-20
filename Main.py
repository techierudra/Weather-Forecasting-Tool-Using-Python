import requests
import json
import datetime

API_KEY = "fe4feefa8543e06d4f3c66d92c61b69c"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

def get_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/onecall?lat={city['coord']['lat']}&lon={city['coord']['lon']}&exclude=current,minutely,hourly&appid={API_KEY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

def parse_weather_data(data):
    if data is None:
        return

    weather = data["weather"][0]["description"]
    temperature_kelvin = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    temperature_celsius = round(temperature_kelvin - 273.15)

    print("Current Weather:")
    print(f"Description: {weather}")
    print(f"Temperature: {temperature_celsius} °C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

def parse_forecast_data(data):
    if data is None:
        return

    print("Upcoming 4-days Forecast:")
    for day in data["daily"][:4]:
        weather = day["weather"][0]["description"]
        temperature_day = round(day["temp"]["day"] - 273.15)
        temperature_night = round(day["temp"]["night"] - 273.15)
        humidity = day["humidity"]
        wind_speed = day["wind_speed"]

        date = datetime.datetime.fromtimestamp(day["dt"])
        formatted_date = date.strftime("%d/%m/%Y")

        print("----------------------------")
        print(f"Date: {formatted_date}")
        print(f"Weather: {weather}")
        print(f"Temperature (Day): {temperature_day} °C")
        print(f"Temperature (Night): {temperature_night} °C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

def main():
    city = input("Enter the city name: ")
    weather_data = get_weather(city)

    if weather_data:
        parse_weather_data(weather_data)
        forecast_data = get_forecast(weather_data)
        if forecast_data:
            parse_forecast_data(forecast_data)
        else:
            print("Failed to retrieve forecast data.")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()
