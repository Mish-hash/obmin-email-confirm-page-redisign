import smtplib, ssl, email, sys

from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

args = sys.argv[1:]

if len(args) < 1 :
    receiver_email = "m_poluektov@ukr.net"
else :
    receiver_email = args[0]

print("Send email to => " + receiver_email )

sender_email = "m_poluektov@ukr.net"
password = "sBG4lDzYHRcjKuDs"

#Create MIMEMultipart object
msg = MIMEMultipart("alternative")
msg["Subject"] = "Obminyashka confirm"
msg["From"] = sender_email
msg["To"] = receiver_email

report_file = open('email.html')

#HTML Message Part

html = report_file.read()
part = MIMEText(html, "html")
msg.attach(part)

# Create secure SMTP connection and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.ukr.net", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, msg.as_string()
    )