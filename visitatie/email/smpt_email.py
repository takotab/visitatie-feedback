import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

from .email_config import gmail_password

gmail_user = "visitatiecommissiealkmaar@gmail.com"


def send_mail(
    send_from="visitatiecommissiealkmaar@gmail.com",
    send_to: list = ["takotabak@gmail.com"],
    subject="test",
    text="text_test",
    files=None,
):
    assert isinstance(send_to, list)

    sent_from = gmail_user

    msg = MIMEMultipart()
    msg["From"] = send_from
    msg["To"] = COMMASPACE.join(send_to)
    msg["Date"] = formatdate(localtime=True)
    msg["Subject"] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(fil.read(), Name=basename(f))
        # After the file is closed
        part["Content-Disposition"] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, send_to, msg.as_string())
    server.close()

    print("Email sent!")
