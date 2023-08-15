import os
import ssl
import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender="sender@gmail.com"
password="password"
receiver=["receiver1@gmail.com", "receiver2@gmail.com"]

subject="subject"
body="body"

context=ssl.create_default_context()

def sendEmails(receiver):
    for p in receiver:
        # body of the email
        email_body=f"""
        line1
        line2
        line3
        """
        #parts of the email are created in a MIME object
        em=MIMEMultipart()
        em['From']=sender
        em['To']=p
        em['Subject']=subject
        #attach body of message
        em.attach(MIMEText(email_body, 'plain'))

        filename="demofile.txt"
        attachment=open(filename, "rb")

        #encode as base 64
        attachment_package=MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= "+filename)
        em.attach(attachment_package)

        text=em.as_string()

        print("Connecting to server...")
        TIE_server=smtplib.SMTP("smtp.gmail.com", 587)
        TIE_server.starttls()
        TIE_server.login(sender, password)
        print("successfully connected to server")

        print(f"Sending email to: {p}...")
        TIE_server.sendmail(sender, p, text)
        print(f"Email sent to {p}")
    
    TIE_server.quit()

schedule.every().day.at("22:46").do(sendEmails, receiver)

while True:
    schedule.run_pending()
    time.sleep(1)