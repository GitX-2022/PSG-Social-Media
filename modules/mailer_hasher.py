''' This code is Open Source Code for the GitX GitHub x PSG Tech Hackathon 2022.
    Team CodeHawk
    - Aaditya Rengarajan
    - Ajay Ramesh
    - S Karun Vikhash
    - Sanjay Kumaar Easwaran '''

import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl, smtplib, hashlib

def get_hash(clear:str):
    return hashlib.sha224(clear.encode("utf-8")).hexdigest()

def send(receiver,subject,text):
    mailid = 'ct.gms@psgtech.ac.in'
    mailps = os.environ['email_pass']
    sender_email = mailid
    receiver_email = receiver
    password = mailps
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email
    part1 = MIMEText(text, 'plain')
    message.attach(part1)
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(mailid,password)
    server.sendmail(mailid, receiver_email, message.as_string())
    server.quit()