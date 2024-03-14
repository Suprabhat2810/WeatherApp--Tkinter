import requests

city = "London"  # Example city name, replace it with your desired city

api_key = "0b863b0ddda8ec337d93e20846986e50"  # Replace 'your_api_key' with your actual API key
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

json_data = requests.get(api).json()
condition = json_data['weather'][0]['main']
description = json_data['weather'][0]['description']
temp = int(json_data['main']['temp'] - 273.15)  # Convert temperature from Kelvin to Celsius
pressure = json_data['main']['pressure']
humidity = json_data['main']['humidity']
wind_speed = json_data['wind']['speed']

# Print the weather information
print(f"Condition: {condition}")
print(f"Description: {description}")
print(f"Temperature: {temp}°C")
print(f"Pressure: {pressure} hPa")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind_speed} m/s")
