from src.main import db

class Orcamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=False)
    servico_id = db.Column(db.Integer, db.ForeignKey("servico.id"), nullable=False)
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())
    data_validade = db.Column(db.Date, nullable=False)
    valor_total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default="pendente") # pendente, aprovado, rejeitado, expirado
    descricao = db.Column(db.Text, nullable=True)


    cliente = db.relationship("Cliente", backref="orcamentos")
    servico = db.relationship("Servico", backref="orcamentos")

    def __repr__(self):
        return f'<Orcamento {self.id} - {self.status}>'


