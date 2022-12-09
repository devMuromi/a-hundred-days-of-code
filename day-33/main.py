import requests
import datetime as dt

# URL = "http://api.open-notify.org/iss-now.json"

# response = requests.get(url=URL)
# response.raise_for_status()

# data = response.json()
# print(data)

# Using API with parameters

parameters = {"let": 51.5, "lng": -0.1, "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = dt.datetime.now()

print(time_now)
