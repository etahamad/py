import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Omar Hamad'
email['to'] = ''
email['subject'] = 'This is a test'
email.set_content('This is a test')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('', '')
    smtp.send_message(email)
    print('Email sent')
