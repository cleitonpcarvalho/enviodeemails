# Email Automation Script

Este repositório contém um script em Python para o envio automatizado de e-mails personalizados em massa, utilizando um servidor SMTP. O objetivo é facilitar campanhas de comunicação por e-mail, garantindo simplicidade e eficiência.

---

## Funcionalidades

- **Conexão Segura:** Conexão com o servidor de e-mail utilizando SMTP com SSL.
- **Leitura de Arquivo CSV:** Extração automática de endereços de e-mail de um arquivo CSV.
- **Cabeçalhos Personalizados:** Suporte a cabeçalhos adicionais, como `Reply-To` e `List-Unsubscribe`.
- **Mensagens Personalizadas:** Facilidade para editar o corpo do e-mail diretamente no script.
- **Tratamento de Erros:** Mensagens claras para identificar problemas durante o envio.

---

## Como Utilizar

### 1. Clone o Repositório

```bash
git clone https://github.com/seuusuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Instale as Dependências Necessárias

Certifique-se de que o Python 3.x está instalado e instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

### 3. Configure o Script

Atualize as configurações de e-mail no script principal:

```python
SMTP_SERVER = "smtp.doseuemail.com"
SMTP_PORT = 465  # Substitua pela porta do seu servidor SMTP
EMAIL_SENDER = "seuemail@seuemail.com"
EMAIL_PASSWORD = "senha_do_seu_email"
```

Substitua pelo seu servidor SMTP, porta e credenciais.

### 4. Prepare o Arquivo CSV

Certifique-se de que o arquivo `emails_webdesigner.csv` possui uma coluna chamada `e-mail`, onde estarão os endereços de e-mail para envio. Exemplo:

| Nome         | e-mail               |
|--------------|----------------------|
| João Silva   | joao@email.com       |
| Maria Souza  | maria@email.com      |

### 5. Execute o Script

Inicie o envio de e-mails:

```bash
python main.py
```

---

## Estrutura do Projeto

```
/
├── main.py              # Script principal
├── emails_webdesigner.csv  # Arquivo de exemplo para os contatos
├── requirements.txt     # Dependências do projeto (se houver)
└── README.md            # Documentação do projeto
```

---

## Personalização

- **Mensagem do E-mail:** Substitua o texto dentro de `body` no script para customizar a mensagem enviada.
- **Assunto do E-mail:** Altere o valor de `message["Subject"]` para definir o assunto desejado.

---

## Possíveis Problemas e Soluções

### Erro: "Arquivo CSV não encontrado"
Certifique-se de que o arquivo `emails_webdesigner.csv` está no mesmo diretório do script.

### Erro: "Cabeçalho 'e-mail' não encontrado"
Verifique se o arquivo CSV possui uma coluna nomeada exatamente como `e-mail`.

### Problemas com Credenciais
Confirme que as credenciais do seu servidor SMTP estão corretas. Caso use o Gmail, ative o acesso de aplicativos menos seguros ou configure uma senha de aplicativo.

---

## Contribuições

Sinta-se à vontade para abrir issues e enviar pull requests para melhorias no projeto. Todas as contribuições são bem-vindas!

---

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## Autor

Criado por **[Cleiton Carvalho](https://github.com/cleitonpcarvalho)**. Entre em contato em [cleiton.carvalho@automasoluct.com](mailto:cleiton.carvalho@automasoluct.com) para dúvidas ou sugestões.

---

**Divirta-se utilizando o script e otimize suas campanhas de e-mail!**
