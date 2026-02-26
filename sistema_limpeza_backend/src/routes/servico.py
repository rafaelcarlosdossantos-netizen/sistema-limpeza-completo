from flask import Blueprint, request, jsonify
from src.main import db
from src.models.servico import Servico

servico_bp = Blueprint("servico_bp", __name__)

@servico_bp.route("/servicos", methods=["POST"])
def create_servico():
    data = request.get_json()
    new_servico = Servico(nome=data["nome"], descricao=data.get("descricao"), preco=data["preco"], duracao_estimada_horas=data.get("duracao_estimada_horas"))
    db.session.add(new_servico)
    db.session.commit()
    return jsonify({"message": "Serviço criado com sucesso!"}), 201

@servico_bp.route("/servicos", methods=["GET"])
def get_servicos():
    servicos = Servico.query.all()
    result = []
    for servico in servicos:
        result.append({"id": servico.id, "nome": servico.nome, "descricao": servico.descricao, "preco": servico.preco, "duracao_estimada_horas": servico.duracao_estimada_horas, "ativo": servico.ativo})
    return jsonify(result), 200

@servico_bp.route("/servicos/<int:id>", methods=["GET"])
def get_servico(id):
    servico = Servico.query.get_or_404(id)
    return jsonify({"id": servico.id, "nome": servico.nome, "descricao": servico.descricao, "preco": servico.preco, "duracao_estimada_horas": servico.duracao_estimada_horas, "ativo": servico.ativo}), 200

@servico_bp.route("/servicos/<int:id>", methods=["PUT"])
def update_servico(id):
    servico = Servico.query.get_or_404(id)
    data = request.get_json()
    servico.nome = data["nome"]
    servico.descricao = data.get("descricao")
    servico.preco = data["preco"]
    servico.duracao_estimada_horas = data.get("duracao_estimada_horas")
    servico.ativo = data["ativo"]
    db.session.commit()
    return jsonify({"message": "Serviço atualizado com sucesso!"}), 200

@servico_bp.route("/servicos/<int:id>", methods=["DELETE"])
def delete_servico(id):
    servico = Servico.query.get_or_404(id)
    db.session.delete(servico)
    db.session.commit()
    return jsonify({"message": "Serviço deletado com sucesso!"}), 200


