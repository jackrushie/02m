import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Jack'
email['to'] = 'jack_rushforth@yahoo.co.uk'
email['subject'] = 'This is a test email from python'

email.set_content('Hello Jack, i have sent this automatically from python')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('jack.rushforth92@gmail.com', 'JRb1005258')
    smtp.send_message(email)
