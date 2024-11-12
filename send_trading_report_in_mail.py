import smtplib
from email.mime.text import MIMEText
from config import FROM_MAIL, TO_MAIL, MAIL_PASSWORD

class EmailWrapper:
    def __init__(self) -> None:
        pass

    def send_email(self, msg, subject):
        msg = MIMEText()
        msg['Subject'] = subject
        msg['From'] = FROM_MAIL
        msg['To'] = TO_MAIL
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.ehlo()
        server.login(FROM_MAIL, MAIL_PASSWORD)
        server.sendmail(FROM_MAIL, TO_MAIL, msg.as_string())
        server.quit()
