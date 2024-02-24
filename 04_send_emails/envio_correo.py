import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()
remitente = os.getenv('USER')
destinatario = 'abelgebel@gmail.com'
asunto = 'test'

msg = MIMEMultipart()
msg['Subject'] = asunto
msg['From'] = remitente
msg['To'] = destinatario

with open('email.html') as archivo:
    html = archivo.read()




# Adjuntar contenido HTML
msg.attach(MIMEText(html, 'html'))

# representa una conexion con un servidor de correo saliente (SMPT server)
server = smtplib.SMTP('smtp.gmail.com', 587)
# conexion segura
server.starttls()
server.login(remitente, os.getenv('PASS'))

# enviar correo electronico
server.sendmail(remitente,
                destinatario,
                msg.as_string())

server.quit()