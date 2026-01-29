import smtplib
import ssl
import os
import random

# Configurações (Essas variaveis virão do GitHub depois)
email_origem = os.environ.get('EMAIL_USER')
senha_app = os.environ.get('EMAIL_SENHA')
email_destino = email_origem # Vai mandar para você mesmo

# Frases para testar
frases = [
    "Bom dia! O sistema está funcionando.",
    "Olá! Teste de automação com GitHub Actions bem sucedido.",
    "Aviso: O robô rodou as 07:00 com sucesso!",
    "Sucesso! Seu código Python está na nuvem."
]

mensagem_escolhida = random.choice(frases)

# Montando o e-mail
assunto = "Teste do Robo Diario"
corpo = f"Subject: {assunto}\n\n{mensagem_escolhida}"

# Enviando
contexto = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as servidor:
        servidor.login(email_origem, senha_app)
        servidor.sendmail(email_origem, email_destino, corpo.encode('utf-8'))
    print("E-mail de teste enviado!")
except Exception as e:
    print(f"Erro ao enviar: {e}")
