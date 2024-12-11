import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

# Configurações de e-mail
SMTP_SERVER = "smtp.doseuemail.com"
SMTP_PORT = 0000 # Número da porta SMTP do seu servidor de email
EMAIL_SENDER = "seuemail@seuemail.com"
EMAIL_PASSWORD = "senha_do_seu_email"

# Função para enviar e-mail
def send_email(to_email):
    try:
        # Configura a mensagem do e-mail
        message = MIMEMultipart()
        message["From"] = "Seu Nome <seuemail@seuemail.com>"
        message["To"] = to_email
        message["Subject"] = "Assunto do seu email"
        message["Reply-To"] = "seuemail@seuemail.com"  # Adicionando cabeçalho de resposta
        message["List-Unsubscribe"] = "<mailto:descadastro@seuemail.com>"  # Cabeçalho de descadastro

        body = """
        
            ESCREVA AQUI A SUA MENSAGEM
        
        """
        message.attach(MIMEText(body, "plain"))

        # Conecta ao servidor SMTP e envia o e-mail
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, to_email, message.as_string())
        print(f"E-mail enviado para: {to_email}")
    except smtplib.SMTPException as e:
        print(f"Erro SMTP ao enviar para {to_email}: {e}")
    except Exception as e:
        print(f"Erro desconhecido ao enviar para {to_email}: {e}")

# Função principal
def main():
    try:
        print("Abrindo o arquivo CSV...")
        with open("emails_webdesigner.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Imprimir os cabeçalhos para verificar os nomes das colunas
            print("Cabeçalhos encontrados:", reader.fieldnames)

            # Verifica se o cabeçalho "email" existe no arquivo CSV
            if "e-mail" not in reader.fieldnames:
                print("Erro: O cabeçalho 'e-mail' não foi encontrado no arquivo CSV.")
                return

            print("Arquivo CSV lido com sucesso. Iniciando envio de e-mails...")
            for row in reader:
                email = row.get("e-mail", "").strip()  # Usa "e-mail" como chave
                if email:
                    print(f"Iniciando envio para {email}...")
                    send_email(email)
                else:
                    print("E-mail não encontrado ou linha vazia no CSV.")
    except FileNotFoundError:
        print("Erro: O arquivo 'planilha_de_contatos.csv' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
