from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meubanco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Modelos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

# --- Usuários ---
@app.route("/usuarios")
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template("usuarios/listar.html", usuarios=usuarios)

@app.route("/usuarios/add", methods=["GET","POST"])
def add_usuarios():
    if request.method == "POST":
        nome = request.form["nome"]
        u = Usuario(nome=nome)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for("listar_usuarios"))
    return render_template("usuarios/add.html")

@app.route("/usuarios/edit/<int:id>", methods=["GET","POST"])
def edit_usuarios(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == "POST":
        usuario.nome = request.form["nome"]
        db.session.commit()
        return redirect(url_for("listar_usuarios"))
    return render_template("usuarios/edit.html", usuario=usuario)

@app.route("/usuarios/delete/<int:id>")
def delete_usuarios(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for("listar_usuarios"))

# --- Produtos ---
@app.route("/produtos")
def listar_produtos():
    produtos = Produto.query.all()
    return render_template("produtos/listar.html", produtos=produtos)

@app.route("/produtos/add", methods=["GET","POST"])
def add_produtos():
    if request.method == "POST":
        nome = request.form["nome"]
        preco = float(request.form["preco"])
        p = Produto(nome=nome, preco=preco)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("listar_produtos"))
    return render_template("produtos/add.html")

@app.route("/produtos/edit/<int:id>", methods=["GET","POST"])
def edit_produtos(id):
    produto = Produto.query.get_or_404(id)
    if request.method == "POST":
        produto.nome = request.form["nome"]
        produto.preco = float(request.form["preco"])
        db.session.commit()
        return redirect(url_for("listar_produtos"))
    return render_template("produtos/edit.html", produto=produto)

@app.route("/produtos/delete/<int:id>")
def delete_produtos(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for("listar_produtos"))

# Página inicial
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
