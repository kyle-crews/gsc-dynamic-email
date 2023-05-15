import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

# Fetching dynamic data from an API
def get_scorecard():
    response = requests.get('http://api.example.com/scorecard')  # replace with your API endpoint
    return response.json()  # assuming the response is in JSON format

# Preparing the email
def prepare_email(scorecard):
    # Email content with scorecard
    html = f"""
    <html>
    <head></head>
    <body>
        <h1>Golf Scorecard</h1>
        <table>
            <tr>
                <th>Hole</th>
                <th>Par</th>
                <th>Score</th>
            </tr>
    """

    for score in scorecard:
        html += f"""
        <tr>
            <td>{score['hole']}</td>
            <td>{score['par']}</td>
            <td>{score['score']}</td>
        </tr>
        """

    html += """
        </table>
    </body>
    </html>
    """

    return html

# Sending the email
def send_email(html_content):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Your Golf Scorecard"
    msg['From'] = "sender@example.com"
    msg['To'] = "receiver@example.com"

    # Attach HTML content
    msg.attach(MIMEText(html_content, 'html'))

    # Send the email (this example assumes SMTP settings are in environment variables)
    s = smtplib.SMTP('smtp.example.com')
    s.send_message(msg)
    s.quit()

# Fetch the scorecard
scorecard = get_scorecard()

# Prepare the email content
html_content = prepare_email(scorecard)

# Send the email
send_email(html_content)