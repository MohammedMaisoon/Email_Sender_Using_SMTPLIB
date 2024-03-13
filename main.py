import datetime as dt
import random
import smtplib

now = dt.datetime.now()
weekday = now.weekday()
my_email = "Your Gmail"
my_password = "Your Password"
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,msg=f"Subject: Daily Quotes\n\n{quote}")








