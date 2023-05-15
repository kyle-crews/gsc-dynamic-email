# fetch data from API

import requests

response = requests.get('https://api.example.com/data-endpoint')

data = response.json()  # Assuming the API returns JSON

# Send an email with dynamic content

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define the SMTP server details
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_username = "username"
smtp_password = "password"

# Create the email
msg = MIMEMultipart('alternative')
msg['Subject'] = "Here's your dynamic data"
msg['From'] = smtp_username
msg['To'] = "recipient@example.com"

# Create the HTML version of your message
html = f"""
<html>
<body>
    <p>Here's the dynamic data you requested:</p>
    <p>{data}</p>
</body>
</html>
"""
msg.attach(MIMEText(html, 'html'))

# Send the email
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)
server.sendmail(smtp_username, msg['To'], msg.as_string())
server.quit()
