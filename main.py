import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = input("Masukkam Email Pengirim : ")
password = input("Masukkan Passwordmu     : ")
toaddr   = input("Masukkan Email Penerima : ")
subjec   = input("Masukkan Subject        : ")
body     = input("Masukkan Text           : ")
hingga   = int(input("Masukkan Total Pengiriman : "))

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subjec

msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
for i in range(hingga):
    server.sendmail(fromaddr, toaddr, text)
