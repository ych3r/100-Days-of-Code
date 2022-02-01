import smtplib
from datetime import datetime
import pandas
import random

SENDER = input("Name:")
EMAIL = input("Email:")
PASS = input("Password:")

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])
        contents = contents.replace("[SENDER]", SENDER)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASS)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthdays_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
# date_of_birth = dt.datetime(year=, month=, day=)