import requests
import json

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


def parse_weather_data(data):
    if data is None:
        return

    weather = data["weather"][0]["description"]
    temperature_kelvin = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    temperature_celsius = round(temperature_kelvin - 273.15) 

    print("Weather Forecast:")
    print(f"Description: {weather}")
    print(f"Temperature: {temperature_celsius} °C")  
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")



def main():
    city = input("Enter the city name: ")
    weather_data = get_weather(city)

    if weather_data:
        parse_weather_data(weather_data)
    else:
        print("Failed to retrieve weather data.")


if __name__ == "__main__":
    main()
