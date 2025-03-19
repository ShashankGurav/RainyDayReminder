import requests
from twilio.rest import Client

# OpenWeather API
Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "YOUR_OPENWEATHER_API_KEY"

# Twilio Credentials
account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"

# Weather parameters (Replace with actual coordinates)
weather_parameters = {
    "lat": YOUR_LATITUDE,  # Example: 19.0760 for Mumbai
    "lon": YOUR_LONGITUDE,  # Example: 72.8777 for Mumbai
    "appid": api_key,
    "cnt": 4
}

# Fetch weather data
response = requests.get(Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

# Check if it will rain
will_rain = False
for i in range(0, 4):
    weather_id = weather_data["list"][i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

# Send notification if it will rain
if will_rain:
    client = Client(account_sid, auth_token)

    # SMS (Commented out)
    # message = client.messages.create(
    #     body="It's going to rain today. Remember to bring an umbrella ☔",
    #     from_="+YOUR_TWILIO_PHONE_NUMBER",
    #     to="+YOUR_PHONE_NUMBER"
    # )

    # WhatsApp
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella ☔",
        to="whatsapp:+YOUR_PHONE_NUMBER"
    )

    print(message.status)
