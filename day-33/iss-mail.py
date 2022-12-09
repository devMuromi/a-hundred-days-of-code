# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

import requests
import datetime as dt
import smtplib
import time

MY_LAT = 51.5
MY_LONG = -0.1
ERROR_MARGIN = 5

MY_EMAIL = "example@gmail.com"
MY_PASSWORD = "abcd1234()"
SMTP_SERVER = "smtp.gmail.com"


def is_iss_above_head(lat, long):
    URL = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url=URL)
    response.raise_for_status()

    data = response.json()
    print(data)
    ISS_LAT = float(data["iss_position"]["longitude"])
    ISS_LONG = float(data["iss_position"]["latitude"])

    if abs(ISS_LAT - lat) <= 5 and abs(ISS_LONG - long) <= 5:
        return True
    return False


def is_dark(lat, long):
    URL = "https://api.sunrise-sunset.org/json"
    parameters = {"let": lat, "lng": long, "formatted": 0}
    response = requests.get(URL, params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    hour_now = dt.datetime.now().hour

    if sunrise <= hour_now and hour_now <= sunset:
        return False
    return True


def is_iss_observable(lat, long):
    if is_iss_above_head(lat, long):
        if is_dark(lat, long):
            return True
    return False


def send_iss_email(email, password, smtp):
    with smtplib.SMTP(smtp) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:You can see ISS right now!!\n\ntitle",
        )


while True:
    if is_iss_observable(MY_LAT, MY_LONG):
        send_iss_email(MY_EMAIL, MY_PASSWORD, SMTP_SERVER)
    time.sleep(60)
