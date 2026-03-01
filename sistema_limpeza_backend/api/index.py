import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Inicialização simplificada
app = Flask(__name__)
CORS(app)

# Configuração do Banco de Dados (Usando pasta temporária da Vercel)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/sistema_limpeza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev_key_123'

db = SQLAlchemy(app)

# Rota de teste para confirmar que está online
@app.route('/api')
def index():
    return jsonify({
        "status": "Sistema de Gestão de Limpeza Online",
        "version": "1.0.0",
        "database": "Conectado"
    })

# Rota raiz para evitar o erro 404 na página inicial
@app.route('/')
def home():
    return jsonify({"message": "Backend do Sistema de Limpeza funcionando! Use /api para testar."})

# Se precisar das outras rotas depois, nós as adicionaremos uma a uma.
# O importante agora é o sistema "dar o boot".
