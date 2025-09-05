# 🚀 CRUD Flask - Usuários e Produtos

Um projeto simples de **CRUD** desenvolvido em **Flask + SQLAlchemy**, com interface em **Bootstrap 5**.  
Permite gerenciar **Usuários** e **Produtos**: cadastrar, listar, editar e excluir.

---

## 📌 Tecnologias

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Bootstrap 5](https://getbootstrap.com/)

---

## 📂 Estrutura

meu_crud_flask/
│── app.py
│── meubanco.db
│── requirements.txt
│── .gitignore
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── usuarios/
│ │ ├── listar.html
│ │ ├── add.html
│ │ └── edit.html
│ └── produtos/
│ ├── listar.html
│ ├── add.html
│ └── edit.html
└── static/
└── css/
└── style.css


---

## ⚙️ Instalação e Execução

Clone o repositório e rode o projeto:

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio

# 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o servidor
python app.py

Acesse no navegador:
👉 http://127.0.0.1:5000/
🛠 Funcionalidades

✅ Usuários

    Criar

    Listar

    Editar

    Excluir

✅ Produtos

    Criar

    Listar

    Editar

    Excluir

✨ Autor
👤 Victor Hugo 
🔗 https://github.com/VIctorHugo216
