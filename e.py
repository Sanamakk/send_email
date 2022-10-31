import email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# My Config
login = ''
password = ''
# Host and Port is a pattern of google
host = 'smtp.gmail.com'
port = '587'

# Email Config
recipients = ['', '']
message = input("A message for sending: ")


def init():
    # Init the server
    server = smtplib.SMTP(host,port)
    print('Conectado ao servidor!')

    # The google require a start TLS
    # Using two functions for start TLS
    server.ehlo()
    server.starttls()

    # Login
    server.login(login,password)
    print('Logado!')

    # Sendig email for all recipients
    for recipient in recipients:
        # Codifing the email in MIMEmultipart
        email_msg = MIMEMultipart()
        # My login email
        email_msg['From'] = login
        # Recipient of email
        email_msg['To'] = recipient
        # Title of email
        email_msg['Subject'] = "Meu email de teste automático"
        # Attaching in email one text type PLAIN
        email_msg.attach(MIMEText(message,'Plain'))
        # Sending email in string
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())


    # Close server
    server.quit()

# Call the function
init()
