import randomimage as rd
l=rd.k
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib
from playsound import playsound
import time

message = MIMEMultipart()
message["from"]="0201csai107@niet.co.in"
message["to"]="ag075261@gmail.com"
message["subject"] = "Hey bro"
message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path(l).read_bytes()))
with smtplib.SMTP(host="smtp.outlook.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("0201csai107@niet.co.in", "niet@1234")
    smtp.send_message(message)

    print("sent...................................100%")
    playsound('D:\email_sender\danger-alarm-23793.mp3')
    # else:
    #     print("message not sent")
