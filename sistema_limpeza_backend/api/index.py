import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Inicialização com permissão total de acesso (CORS)
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/sistema_limpeza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev_key_123'

db = SQLAlchemy(app)

@app.route('/api')
def index():
    return jsonify({
        "status": "Sistema de Gestão de Limpeza Online",
        "version": "1.0.0",
        "database": "Conectado"
    })

@app.route('/')
def home():
    return jsonify({"message": "Backend Online! Use /api para testar."})

# Garante que o app seja exportado corretamente para a Vercel
app = app
