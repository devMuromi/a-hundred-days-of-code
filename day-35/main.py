import requests
from twillo.rest import Client

API_KEY = "openweatherapikeycomeshere"
LAT = 44.43
LON = 10.99


def get_12hours_weather_data(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()

    rawdata = response.json()
    rawdata = rawdata["list"][:4]
    data = []
    for i in rawdata:
        data.append(i["weather"][0])
    return data


def get_will_rain_in_12hours(lat, lon):
    data = get_12hours_weather_data(lat, lon)
    for i in data:
        if i["id"] < 700:
            return True
    return False


# I didn't use the code below, but I left it here for reference
OWN_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""
account_sid = "ACe8f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f"
auth_token = "f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f1f"

if get_will_rain_in_12hours(LAT, LON):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+15017122661",
        to="+15558675310",
    )
    print(message.status)
