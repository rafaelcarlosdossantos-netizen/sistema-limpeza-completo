from src.main import db

class OrdemServico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=False)
    operador_id = db.Column(db.Integer, db.ForeignKey("operador.id"), nullable=True)
    servico_id = db.Column(db.Integer, db.ForeignKey("servico.id"), nullable=False)
    data_agendada = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(50), default="pendente") # pendente, agendada, em_andamento, concluida, cancelada
    endereco_servico = db.Column(db.String(200), nullable=False)
    observacoes = db.Column(db.Text, nullable=True)
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())
    data_atualizacao = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    cliente = db.relationship("Cliente", backref="ordens_servico")
    operador = db.relationship("Operador", backref="ordens_servico")
    servico = db.relationship("Servico", backref="ordens_servico")

    def __repr__(self):
        return f'<OrdemServico {self.id} - {self.status}>'


