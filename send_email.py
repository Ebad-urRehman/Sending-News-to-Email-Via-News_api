import os
import ssl
import smtplib

def send_email(message_arg):
    port = 465
    host = "smtp.gmail.com"
    password = os.getenv("PASSWORD")
    sender_email = "ebadinfalltraders@gmail.com"
    receiver_email = "ifallswitft@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message_arg)


if __name__ == "__main__":
    send_email("Hi there")