# Formulário com Validação

<div allign: "left">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdc3f" alt="Python">
<img src="https://img.shields.io/badge/Flask-000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
</div>

## Sobre o Projeto

Este projeto consiste em um formulário de cadastro de usuários com validação de dados no frontend (JavaScript) e no backend (Python/Flask), reforçando práticas de segurança e integridade das informações fornecidas. Agora com autenticação segura usando **JWT** e login via **OAuth 2.0 (Google)**.

### 🔐 Funcionalidades de Segurança

- Validação de entrada (nome, e-mail, senha)
- Geração de token JWT para rotas protegidas
- Login via Google (OAuth 2.0) com `Flask-Dance`

---
### Estrutura do Projeto

```
formulario-validacao/ 
├── app.py 
├── requirements.txt 
├── README.md 
├── templates/ 
│ └── index.html 
├── static/ 
│ └── script.js

```
---

### Requisitos
- Python 3 instalado
- Flask
- Flask-Dance
- PyJWT

### Instalação

Clone o repositório e instale as dependências:

```bash
pip install -r requirements.txt
```

### Como Executar

Inicie o servidor Flask:

```bash
python app.py
```

Acesse no navegador:

```
http://127.0.0.1:5000
```
