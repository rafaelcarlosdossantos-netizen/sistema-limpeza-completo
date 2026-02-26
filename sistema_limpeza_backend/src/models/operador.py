from src.main import db

class Operador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    nivel_acesso = db.Column(db.String(50), nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Operador {self.nome}>'


