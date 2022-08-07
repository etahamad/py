from importlib.resources import path
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Omar Hamad'
email['to'] = ''
email['subject'] = 'This is a test'
email.set_content(html.substitute({'name': 'Omar'}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('', '')
    smtp.send_message(email)
    print('Email sent')
