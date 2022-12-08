import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "example@example.com"
MY_PASSWORD = "example"
SMTP = "smtp.gmail.com"


def get_random_template():
    templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    template = random.choice(templates)
    f = open(f"./day-32/birthday-wisher/letter_templates/{template}", "r")
    text = ""
    while True:
        line = f.readline()
        if not line:
            break
        text += line
    return text


today = dt.datetime.today().date()
today_month = today.month
today_day = today.day

data = pandas.read_csv("./day-32/birthday-wisher/birthdays.csv")
data_filtered = data[data["month"] == today_month]
data_filtered = data_filtered[data_filtered["day"] == today_day]

print(data_filtered)

for info in data_filtered.itertuples():
    template = get_random_template()
    mail_content = template.replace("[NAME]", info.name)

    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=info.email,
            msg=f"Subject:Happy Birthday!!\n\n{mail_content}",
        )
