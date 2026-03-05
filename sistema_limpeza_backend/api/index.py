import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Banco de Dados SQLite (Salvo na pasta temporária da Vercel)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/sistema_limpeza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev_key_123'

db = SQLAlchemy(app)

# Modelo do Cliente no Banco de Dados
class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(20), nullable=False)
    valor = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='Agendado')

# Criar o banco de dados se não existir
with app.app_context():
    db.create_all()

@app.route('/api/servicos', methods=['GET'])
def listar_servicos():
    servicos = Servico.query.all()
    return jsonify([{
        "id": s.id,
        "cliente": s.cliente,
        "data": s.data,
        "valor": s.valor,
        "status": s.status
    } for s in servicos])

@app.route('/api/servicos', methods=['POST'])
def adicionar_servico():
    dados = request.json
    novo = Servico(
        cliente=dados['cliente'],
        data=dados['data'],
        valor=dados['valor'],
        status='Agendado'
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify({"message": "Salvo com sucesso!", "id": novo.id}), 201

@app.route('/api')
def index():
    return jsonify({"status": "Sistema Online", "database": "Conectado"})

@app.route('/')
def home():
    return jsonify({"message": "Backend Online!"})

app = app
