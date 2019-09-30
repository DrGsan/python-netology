import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

HOST_SMTP = "smtp.gmail.com"
HOST_IMAP = "imap.gmail.com"


class MailBox:  # Работа с почтой
    def __init__(self, login, password, smtp=HOST_SMTP, imap=HOST_IMAP, port=SMTP_PORT):
        self.login = login
        self.password = password
        self.smtp = smtp
        self.imap = imap
        self.port = port

    def send_mail(self, subject, recipients, message):  # Отправка почты

        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.smtp, self.port)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, recipients, msg.as_string())
        ms.quit()

    def recieve_email(self, folder='inbox', header=None):  # Приём почты

        mail = imaplib.IMAP4_SSL(self.imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select(folder)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        mail.logout()
        return email_message


if __name__ == '__main__':
    work_email = Email('login@gmail.com', 'qwerty')
    work_email.send_email('Subject', ['vasya@email.com', 'petya@email.com'], 'Message')
    print(work_email.receive_message())
