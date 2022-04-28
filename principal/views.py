from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from posix import environ
from pydoc import describe
import smtplib
from django.shortcuts import get_object_or_404, render
from principal.models import Form
from smtplib import SMTP
import os 
import environ

def index(request):

    if request.method == 'POST':
        name = request.POST['Nome']
        email = request.POST['Email']
        phone = request.POST['Telefone']
        site = request.POST['Site']
        description = request.POST['Mensagem']

        principal = Form.objects.create(name=name, email=email,
        phone=phone, site=site, description=description)

        principal.save()

        send_email(email, name)
    return render(request, 'index.html')

def send_email(to: str, name: str,):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        # DESATIVAR MODO DE SEGURANÇA DA CONTA
        server.ehlo()
        server.starttls() # start transport layer security
        server.login(os.environ.get('EMAIL_LOGIN'),os.environ.get('EMAIL_SENHA'))
        # ESTRUTURA DA ENVIO DE MSG
        msg_text = f"""<h3>Que incrivel!! Vejo que se interessou pelo meu trabalho!</h3>
        <p>Olá {name}, Tudo bem com você?</p>
        <p>Verificamos seu interesse, em meus trabalhos!</p>
        <p>Assim que possível lhe enviamos um orçamento desse íncrivel sistema!</p>
        <p>Caso queira entrar diretamente em contato comigo, Segue meu whatsapp +55 48 9 9935 6645</p>"""
        msg = MIMEMultipart()
        msg['From'] = 'frigottogiorgio@gmail.com'
        msg['To'] = to
        msg['Subject'] = 'Agradecimento!!'
        msg.attach(MIMEText(msg_text, 'html'))
        # FROM > TO > MSG
        server.sendmail('frigottogiorgio@gmail.com', to, msg.as_string())
        server.quit()

def portfolio(request):
    return render(request, 'pages/portfolio.html')

def sobre(request):
    return render(request, 'pages/sobre.html')
