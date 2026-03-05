import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/sistema_limpeza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'chave_mestra_789'

db = SQLAlchemy(app)

class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(20), nullable=False)
    valor = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='Agendado')

with app.app_context():
    db.create_all()

# --- NOVA ROTA DE LOGIN ---
@app.route('/api/login', methods=['POST'])
def login():
    dados = request.json
    # Usuário e Senha definidos por você (Pode mudar aqui!)
    USUARIO_CORRETO = "admin"
    SENHA_CORRETA = "123456"
    
    if dados.get('usuario') == USUARIO_CORRETO and dados.get('senha') == SENHA_CORRETA:
        return jsonify({"success": True, "message": "Login realizado!"})
    else:
        return jsonify({"success": False, "message": "Usuário ou senha incorretos"}), 401

@app.route('/api/servicos', methods=['GET'])
def listar_servicos():
    servicos = Servico.query.all()
    return jsonify([{"id": s.id, "cliente": s.cliente, "data": s.data, "valor": s.valor, "status": s.status} for s in servicos])

@app.route('/api/servicos', methods=['POST'])
def adicionar_servico():
    dados = request.json
    novo = Servico(cliente=dados['cliente'], data=dados['data'], valor=dados['valor'])
    db.session.add(novo)
    db.session.commit()
    return jsonify({"message": "Salvo!", "id": novo.id}), 201

@app.route('/api')
def index():
    return jsonify({"status": "Sistema Online", "auth": "Habilitada"})

app = app
