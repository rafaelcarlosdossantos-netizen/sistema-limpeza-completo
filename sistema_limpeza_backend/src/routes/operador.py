from flask import Blueprint, request, jsonify
from src.main import db
from src.models.operador import Operador

operador_bp = Blueprint("operador_bp", __name__)

@operador_bp.route("/operadores", methods=["POST"])
def create_operador():
    data = request.get_json()
    new_operador = Operador(nome=data["nome"], email=data["email"], telefone=data["telefone"], nivel_acesso=data["nivel_acesso"])
    db.session.add(new_operador)
    db.session.commit()
    return jsonify({"message": "Operador criado com sucesso!"}), 201

@operador_bp.route("/operadores", methods=["GET"])
def get_operadores():
    operadores = Operador.query.all()
    result = []
    for operador in operadores:
        result.append({"id": operador.id, "nome": operador.nome, "email": operador.email, "telefone": operador.telefone, "nivel_acesso": operador.nivel_acesso, "ativo": operador.ativo})
    return jsonify(result), 200

@operador_bp.route("/operadores/<int:id>", methods=["GET"])
def get_operador(id):
    operador = Operador.query.get_or_404(id)
    return jsonify({"id": operador.id, "nome": operador.nome, "email": operador.email, "telefone": operador.telefone, "nivel_acesso": operador.nivel_acesso, "ativo": operador.ativo}), 200

@operador_bp.route("/operadores/<int:id>", methods=["PUT"])
def update_operador(id):
    operador = Operador.query.get_or_404(id)
    data = request.get_json()
    operador.nome = data["nome"]
    operador.email = data["email"]
    operador.telefone = data["telefone"]
    operador.nivel_acesso = data["nivel_acesso"]
    operador.ativo = data["ativo"]
    db.session.commit()
    return jsonify({"message": "Operador atualizado com sucesso!"}), 200

@operador_bp.route("/operadores/<int:id>", methods=["DELETE"])
def delete_operador(id):
    operador = Operador.query.get_or_404(id)
    db.session.delete(operador)
    db.session.commit()
    return jsonify({"message": "Operador deletado com sucesso!"}), 200


