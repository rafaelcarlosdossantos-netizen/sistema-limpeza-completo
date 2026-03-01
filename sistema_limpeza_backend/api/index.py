import os
import sys

# Adiciona a pasta raiz ao caminho para que as importações funcionem
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Inicialização do Banco de Dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configurações
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_key_123')
    database_url = os.environ.get('DATABASE_URL')
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'sqlite:////tmp/sistema_limpeza.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)
    db.init_app(app)

    with app.app_context():
        # Importações internas
        from src.routes.cliente import cliente_bp
        from src.routes.operador import operador_bp
        from src.routes.servico import servico_bp
        from src.routes.ordem_servico import os_bp
        from src.routes.orcamento import orcamento_bp

        app.register_blueprint(cliente_bp, url_prefix='/api/clientes')
        app.register_blueprint(operador_bp, url_prefix='/api/operadores')
        app.register_blueprint(servico_bp, url_prefix='/api/servicos')
        app.register_blueprint(os_bp, url_prefix='/api/ordens-servico')
        app.register_blueprint(orcamento_bp, url_prefix='/api/orcamentos')

        db.create_all()

    @app.route('/api')
    def index():
        return {"status": "Sistema de Gestão de Limpeza Online", "version": "1.0.0"}

    return app

# A Vercel precisa que o objeto se chame 'app' na raiz do arquivo
app = create_app()
