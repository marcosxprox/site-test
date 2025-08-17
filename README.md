# Cadastro de Usuário com reCAPTCHA v3

## Descrição
Este projeto é um sistema de cadastro de usuários com **FastAPI** no backend e **HTML/JS** no frontend.  
Possui integração com **Google reCAPTCHA v3** para validação anti-bot e armazena os dados em um banco de dados **MySQL**.

O projeto foi feito totalmente do zero, incluindo frontend, backend e conexão com o banco.

---

## Funcionalidades
- Cadastro de usuário com:
  - Nome de usuário
  - E-mail
  - Senha
- Validação com Google reCAPTCHA v3
- Armazenamento seguro de senha com hash (`bcrypt`)
- Inserção dos dados no banco MySQL via **SQLAlchemy**
- Deploy online funcional

---

## Tecnologias Utilizadas
- **Backend:** Python, FastAPI, SQLAlchemy
- **Banco de Dados:** MySQL
- **Frontend:** HTML, JavaScript
- **Segurança:** Google reCAPTCHA v3, hash de senhas com bcrypt
- **Deploy:** Railway (ou outra plataforma que você utilizou)

---

## Como Rodar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio/backend
