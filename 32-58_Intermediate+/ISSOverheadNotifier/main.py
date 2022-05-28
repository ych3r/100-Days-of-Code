import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 42.361145
MY_LONG = -71.057083
MY_EMAIL = input("email:")
MY_PASSWORD = input("password:")


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    print("iss location:", iss_longitude, iss_latitude)
    # Compare my position - within 5 degrees
    if (MY_LONG - 5 < iss_longitude < MY_LONG + 5) and (MY_LAT - 5 < iss_latitude < MY_LAT + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Summer in Boston -4 , Winter would be -5
    sunrise = (24 + sunrise - 4) % 24
    sunset = (24 + sunset - 4) % 24
    # print(sunrise, sunset)
    # print(sunrise.split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )

# If the ISS is close to my current position
# and it is dark outside
# then send me an email to tell me to look up
# run the code every 60 sec
