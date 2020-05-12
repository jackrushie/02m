import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Jack'
email['to'] = 'jack_rushforth@yahoo.co.uk'
email['subject'] = 'This is a test email from python'

email.set_content(html.substitute(name='Jack'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # ADD PASSWORD BACK IN
    smtp.login('jack.rushforth92@gmail.com', '#############')
    smtp.send_message(email)
