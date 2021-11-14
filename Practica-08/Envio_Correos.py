# Practica-03 Ibrahim Zavala Hernandez
import ssl
import smtplib
import getpass
import argparse
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

parser = argparse.ArgumentParser()
parser.add_argument('--r', dest = 'emisor', default = '', help = 'Correo Electronico del remitente')
parser.add_argument('--c', dest = 'contraseña', default = '', help = 'Contraseña del remitente')
parser.add_argument('--d', dest = 'destino', default = '',  help = 'Destino del correo')
parser.add_argument('--a', dest = 'asunto', default= '', help = 'Asunto del Correo ')
parser.add_argument('--m', dest = 'mensaje', default = '', help = 'Mensaje del Correo')
params = parser.parse_args()


if __name__ == '__main__':
    try: 
        correo = MIMEMultipart()
        correo["From"] = params.emisor
        correo["Subject"] = params.asunto
        correo["To"] = params.destino
        correo["body"] = params.mensaje

        correo.attach(MIMEText(params.mensaje, "plain"))

        context = ssl.create_default_context()
        with smtplib.SMTP("outlook.office365.com", 587) as server:
            server.ehlo()
            server.starttls(context=context)
            server.login(params.emisor, params.contraseña)
            server.sendmail(
                params.emisor, params.destino, correo.as_string()
            )
        print("[+] Correo envido con éxito")
        
    except Exception as e:
        print("Error", e)