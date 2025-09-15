import smtplib
import os

my_email = os.getenv("MY_EMAIL")  # Store credentials in environment variables
password = os.getenv("EMAIL_PASSWORD")
receive_email = "example@email.com"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=receive_email,
        msg="Subject:Your subject\n\nMessage"
    )