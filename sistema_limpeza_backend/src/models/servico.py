from src.main import db

class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    preco = db.Column(db.Float, nullable=False)
    duracao_estimada_horas = db.Column(db.Float, nullable=True)
    ativo = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Servico {self.nome}>'


