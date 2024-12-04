# # importing important lib
# import smtplib

# # new Email id for Testing Purpose
# yahoo = "testingpythonsmtplib7@yahoo.com"
# gmail = "testingpythonsmtplib@gmail.com"
# g_password = ""
# y_password = ""

# # creating object
# connection = smtplib.SMTP("smtp.mail.yahoo.com")
# # tls = transport layer security - making connection secure
# connection.starttls()
# connection.login(user=yahoo,password=y_password)
# connection.sendmail(from_addr=yahoo, to_addrs=gmail, msg="Subject:hello\n\n Testing smtplib in python")
# connection.close()

# date Time module
# import datetime as dt

# now = dt.datetime.now()
# print(now)
# year = now.year
# print(year)

# #<class 'datetime.datetime'>
# print(type(now))

# day_of_week = now.weekday()
# # 0-based indexing
# print(day_of_week)

# date_of_birth = dt.datetime(day=1, month=1, year=2000)
# print(date_of_birth)

# Automated monday motivation mail sender
import smtplib
import datetime as dt
import random

yahoo = "*****"
gmail = "******"
g_password = "*******"
y_password = "*******"


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with open("quotes.txt",mode="r") as quotes_file:
        quotes_list = quotes_file.readlines()
        quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=gmail, password=g_password)
        connection.sendmail(from_addr=gmail, to_addrs=yahoo, msg=f"Subject: Monday Motivation \n\n{quote}".encode("utf-8"))



