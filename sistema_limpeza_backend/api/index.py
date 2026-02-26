import os
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
    app.config['SQLALCHEMY_DATABASE_URL'] = database_url or 'sqlite:///sistema_limpeza.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)
    db.init_app(app)

    with app.app_context():
        # Importação das rotas dentro do contexto para evitar erro circular
        from .routes.cliente import cliente_bp
        from .routes.operador import operador_bp
        from .routes.servico import servico_bp
        from .routes.ordem_servico import os_bp
        from .routes.orcamento import orcamento_bp

        app.register_blueprint(cliente_bp, url_prefix='/api/clientes')
        app.register_blueprint(operador_bp, url_prefix='/api/operadores')
        app.register_blueprint(servico_bp, url_prefix='/api/servicos')
        app.register_blueprint(os_bp, url_prefix='/api/ordens-servico')
        app.register_blueprint(orcamento_bp, url_prefix='/api/orcamentos')

        db.create_all()

    @app.route('/')
    def index():
        return {"status": "Sistema de Gestão de Limpeza Online", "version": "1.0.0"}

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0', port=port)