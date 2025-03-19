# RainAlertBot 🌧️

## Overview
RainAlertBot is a Python script that fetches weather data from OpenWeatherMap and notifies users via **WhatsApp** and **SMS** (Twilio) if rain is expected.

## Features
- Fetches weather forecast for a specified location.
- Detects rain based on weather conditions.
- Sends alerts via **WhatsApp** and optionally **SMS**.

## Technologies Used
- **Python**, **Requests**, **Twilio API**, **OpenWeatherMap API**

## Setup Instructions
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/RainAlertBot.git
cd RainAlertBot
```

### 2️⃣ Install Dependencies
```sh
pip install requests twilio
```

### 3️⃣ Configure API Keys & Location
Replace placeholders in `weather_alert.py`:
```python
api_key = "YOUR_OPENWEATHER_API_KEY"
account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"
weather_parameters = { "lat": YOUR_LAT, "lon": YOUR_LON, "appid": api_key, "cnt": 4 }
```

### 4️⃣ Run the Script
```sh
python weather_alert.py
```

## Future Improvements
- Support multiple locations.
- Add email notifications.
- Web UI for configuration.



